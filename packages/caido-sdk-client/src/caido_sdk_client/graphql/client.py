"""Low-level GraphQL client for queries, mutations, and subscriptions."""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable, Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportError
from gql.transport.websockets import WebsocketsTransport
from graphql import DocumentNode

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.errors.graphql import (
    NetworkUserError,
    NoDataUserError,
    OperationUserError,
)


@dataclass(frozen=True, slots=True)
class GraphQLClientOptions:
    """Options used to configure GraphQLClient."""

    base_url: str
    headers: Mapping[str, str] | None = None
    timeout_ms: int | None = None
    access_token_provider: Callable[[], str | None] | None = None


class GraphQLClient:
    """Low-level GraphQL client for query/mutation/subscription operations."""

    def __init__(self, options: GraphQLClientOptions) -> None:
        normalized_url = options.base_url.rstrip("/")
        self._graphql_url = f"{normalized_url}/graphql"
        self._websocket_url = self._to_websocket_url(normalized_url)
        self._static_headers = (
            dict(options.headers) if options.headers is not None else {}
        )
        self._timeout_seconds = (
            int(options.timeout_ms / 1000) if options.timeout_ms is not None else None
        )
        self._access_token_provider = options.access_token_provider

    @staticmethod
    def _to_websocket_url(base_url: str) -> str:
        parsed = urlparse(base_url)
        scheme = "wss" if parsed.scheme == "https" else "ws"
        return f"{scheme}://{parsed.netloc}/ws/graphql"

    def _headers(self) -> dict[str, str]:
        headers = dict(self._static_headers)
        if self._access_token_provider is not None:
            access_token = self._access_token_provider()
            if access_token is not None:
                headers["Authorization"] = f"Bearer {access_token}"
        return headers

    @staticmethod
    def _document(document: str | DocumentNode) -> DocumentNode:
        if isinstance(document, str):
            return gql(document)
        return document

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
    ) -> dict[str, Any]:
        """Execute a GraphQL mutation and return raw data payload."""
        return await self._execute(document, variables)

    async def _execute(
        self,
        document: str | DocumentNode,
        variables: Mapping[str, Any] | None,
    ) -> dict[str, Any]:
        transport = AIOHTTPTransport(
            url=self._graphql_url,
            headers=self._headers(),
            timeout=self._timeout_seconds,
        )
        gql_client = Client(transport=transport, fetch_schema_from_transport=False)
        try:
            async with gql_client as session:
                result = await session.execute(
                    self._document(document),
                    variable_values=dict(variables) if variables is not None else None,
                )
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
        transport = WebsocketsTransport(
            url=self._websocket_url,
            headers=self._headers(),
            close_timeout=2,
        )
        gql_client = Client(transport=transport, fetch_schema_from_transport=False)
        try:
            async with gql_client as session:
                subscription = session.subscribe(
                    self._document(document),
                    variable_values=dict(variables) if variables is not None else None,
                )
                async for result in subscription:
                    if not isinstance(result, dict):
                        raise NoDataUserError()
                    yield result
        except TransportError as exc:
            raise NetworkUserError().with_source(exc) from exc
        except BaseError:
            raise
        except Exception as exc:
            raise OperationUserError(str(exc)).with_source(exc) from exc
