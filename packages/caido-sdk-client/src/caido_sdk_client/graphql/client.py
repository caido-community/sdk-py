"""Low-level GraphQL client for queries, mutations, and subscriptions."""

from __future__ import annotations

from collections.abc import AsyncIterator, Mapping
from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse

from gql import Client
from gql.graphql_request import GraphQLRequest
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import (
    TransportError,
    TransportQueryError,
)
from gql.transport.websockets import WebsocketsTransport
from graphql import DocumentNode

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.errors.graphql import (
    NetworkUserError,
    NoDataUserError,
    OperationUserError,
)
from caido_sdk_client.graphql.utils import to_user_error

if TYPE_CHECKING:
    from caido_sdk_client.auth.manager import AuthManager


class GraphQLClient:
    """Low-level GraphQL client for query/mutation/subscription operations."""

    def __init__(
        self,
        base_url: str,
        auth: AuthManager,
        *,
        headers: Mapping[str, str] | None = None,
        timeout_ms: int | None = None,
    ) -> None:
        normalized_url = base_url.rstrip("/")
        self._graphql_url = f"{normalized_url}/graphql"
        self._websocket_url = self._to_websocket_url(normalized_url)
        self._static_headers = dict(headers) if headers is not None else {}
        self._timeout_seconds = (
            int(timeout_ms / 1000) if timeout_ms is not None else None
        )
        self._auth = auth

        self._http_transport, self._http_client = self._create_http_client()
        self._ws_transport, self._ws_client = self._create_ws_client()

        # Keep transports in sync with auth token changes.
        self._auth.on_token_refresh(self._on_token_refresh)

    def _create_http_client(self) -> tuple[AIOHTTPTransport, Client]:
        access_token = self._auth.get_access_token()
        headers: dict[str, str] = dict(self._static_headers)
        if access_token is not None:
            headers["Authorization"] = f"Bearer {access_token}"
        transport = AIOHTTPTransport(
            url=self._graphql_url,
            headers=headers,
            timeout=self._timeout_seconds,
        )
        client = Client(
            transport=transport,
            fetch_schema_from_transport=False,
        )
        return transport, client

    def _create_ws_client(self) -> tuple[WebsocketsTransport, Client]:
        access_token = self._auth.get_access_token()
        init_payload: dict[str, str] = {}
        if access_token is not None:
            init_payload["Authorization"] = f"Bearer {access_token}"
        transport = WebsocketsTransport(
            url=self._websocket_url,
            init_payload=init_payload,
            close_timeout=2,
        )
        client = Client(
            transport=transport,
            fetch_schema_from_transport=False,
        )
        return transport, client

    def _on_token_refresh(self) -> None:
        """Recreate transports when the auth token changes."""
        self._http_transport, self._http_client = self._create_http_client()
        self._ws_transport, self._ws_client = self._create_ws_client()

    @staticmethod
    def _to_websocket_url(base_url: str) -> str:
        parsed = urlparse(base_url)
        scheme = "wss" if parsed.scheme == "https" else "ws"
        return f"{scheme}://{parsed.netloc}/ws/graphql"

    @staticmethod
    def _request(
        document: str | DocumentNode,
        variable_values: dict[str, Any] | None = None,
        operation_name: str | None = None,
    ) -> GraphQLRequest:
        return GraphQLRequest(
            document,
            variable_values=variable_values,
            operation_name=operation_name,
        )

    async def query(
        self,
        document: str | DocumentNode,
        variables: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a GraphQL query and return raw data payload."""
        return await self._execute(document, variables)

    async def mutation(
        self,
        document: str | DocumentNode,
        variables: Mapping[str, Any] | None = None,
        *,
        upload_files: bool = False,
    ) -> dict[str, Any]:
        """Execute a GraphQL mutation and return raw data payload.

        Set upload_files=True when variables contain gql FileVar values
        (e.g. for uploadHostedFile).
        """
        return await self._execute(document, variables, upload_files=upload_files)

    async def _execute(
        self,
        document: str | DocumentNode,
        variables: Mapping[str, Any] | None,
        *,
        upload_files: bool = False,
    ) -> dict[str, Any]:
        try:
            request = self._request(
                document,
                variable_values=dict(variables) if variables is not None else None,
            )
            result = await self._http_client.execute_async(
                request,
                upload_files=upload_files,
            )
        except TransportQueryError as exc:
            self._raise_from_query_error(exc)
        except TransportError as exc:
            raise NetworkUserError().with_source(exc) from exc
        except BaseError:
            raise
        except Exception as exc:
            raise OperationUserError(str(exc)).with_source(exc) from exc

        if not isinstance(result, dict):
            raise NoDataUserError()
        return result

    async def subscribe(
        self,
        document: str | DocumentNode,
        variables: Mapping[str, Any] | None = None,
    ) -> AsyncIterator[dict[str, Any]]:
        """Subscribe to a GraphQL subscription and yield payloads."""
        try:
            request = self._request(
                document,
                variable_values=dict(variables) if variables is not None else None,
            )
            async with self._ws_client as session:
                subscription = session.subscribe(request)
                async for result in subscription:
                    if not isinstance(result, dict):
                        raise NoDataUserError()
                    yield result
        except TransportQueryError as exc:
            self._raise_from_query_error(exc)
        except TransportError as exc:
            raise NetworkUserError().with_source(exc) from exc
        except BaseError:
            raise
        except Exception as exc:
            raise OperationUserError(str(exc)).with_source(exc) from exc

    @staticmethod
    def _raise_from_query_error(exc: TransportQueryError) -> None:
        """Inspect a TransportQueryError for CAIDO extensions and raise the appropriate error."""
        if exc.errors:
            for error in exc.errors:
                if isinstance(error, dict):
                    caido_error = to_user_error(error)
                    if caido_error is not None:
                        raise caido_error from exc

        raise OperationUserError(str(exc)).with_source(exc) from exc
