"""Auth client implementation for OAuth2 device code flow."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any, cast
from urllib.parse import urlparse

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport

from .approvers.types import AuthApprover
from .errors import InstanceError
from .queries import (
    CREATED_AUTHENTICATION_TOKEN,
    REFRESH_AUTHENTICATION_TOKEN,
    START_AUTHENTICATION_FLOW,
)
from .types import (
    AuthenticationRequest,
    AuthenticationToken,
    CreatedAuthenticationTokenError,
    CreatedAuthenticationTokenResponse,
    RefreshAuthenticationTokenError,
    RefreshAuthenticationTokenResponse,
    StartAuthenticationFlowError,
    StartAuthenticationFlowResponse,
)


@dataclass(frozen=True, slots=True)
class AuthClientOptions:
    """Options used to configure AuthClient."""

    instance_url: str
    approver: AuthApprover
    timeout_ms: int | None = None


@dataclass(frozen=True, slots=True)
class ErrorDetails:
    """Structured error details extracted from GraphQL user errors."""

    reason: str | None = None
    message: str | None = None


class AuthClient:
    """Client for authenticating with a Caido instance."""

    def __init__(self, options: AuthClientOptions) -> None:
        self._instance_url = options.instance_url.rstrip("/")
        self._graphql_url = f"{self._instance_url}/graphql"
        self._websocket_url = self._get_websocket_url()
        self._approver = options.approver
        self._timeout_seconds = (
            options.timeout_ms / 1000 if options.timeout_ms is not None else None
        )
        self._graphql_client = Client(
            transport=AIOHTTPTransport(
                url=self._graphql_url,
                timeout=self._timeout_seconds,
            ),
            fetch_schema_from_transport=False,
        )

    def _get_websocket_url(self) -> str:
        """Convert GraphQL HTTP URL to the websocket subscription URL."""
        parsed = urlparse(self._graphql_url)
        scheme = "wss" if parsed.scheme == "https" else "ws"
        return f"{scheme}://{parsed.netloc}/ws/graphql"

    @staticmethod
    def _extract_error_details(
        error: StartAuthenticationFlowError
        | CreatedAuthenticationTokenError
        | RefreshAuthenticationTokenError,
    ) -> ErrorDetails:
        """Extract optional reason/message from a typed GraphQL user error."""
        return ErrorDetails(
            reason=error["reason"] if "reason" in error else None,
            message=error["message"] if "message" in error else None,
        )

    async def start_authentication_flow(self) -> AuthenticationToken:
        """Start the device code flow and wait for the token."""
        # Step 1: Start the authentication flow via GraphQL mutation.
        async with self._graphql_client as session:
            try:
                result: dict[str, Any] = await session.execute(START_AUTHENTICATION_FLOW)
            except Exception as exc:
                raise InstanceError("GRAPHQL_ERROR", message=str(exc)) from exc

        response = cast(StartAuthenticationFlowResponse, result)
        payload = response.get("startAuthenticationFlow")
        if payload is None:
            raise InstanceError(
                "NO_RESPONSE", message="No response from startAuthenticationFlow"
            )

        if payload.get("error") is not None:
            error = payload["error"]
            details = self._extract_error_details(error)
            raise InstanceError(
                error["code"], reason=details.reason, message=details.message
            )

        if payload.get("request") is None:
            raise InstanceError("NO_REQUEST", message="No authentication request returned")

        # Step 2: Delegate approval to the configured approver strategy.
        auth_request = AuthenticationRequest.from_wire(payload["request"])
        await self._approver.approve(auth_request)

        # Step 3: Wait for the token through the websocket subscription.
        return await self._wait_for_token(auth_request.id)

    async def _wait_for_token(self, request_id: str) -> AuthenticationToken:
        """Subscribe to token creation events until a token is received."""
        transport = WebsocketsTransport(url=self._websocket_url)

        try:
            async with Client(
                transport=transport,
                fetch_schema_from_transport=False,
            ) as session:
                subscription = session.subscribe(
                    CREATED_AUTHENTICATION_TOKEN,
                    variable_values={"requestId": request_id},
                )
                if self._timeout_seconds is None:
                    async for result in subscription:
                        token = self._process_subscription_result(result)
                        if token is not None:
                            return token
                else:
                    async with asyncio.timeout(self._timeout_seconds):
                        async for result in subscription:
                            token = self._process_subscription_result(result)
                            if token is not None:
                                return token
        except InstanceError:
            raise
        except TimeoutError as exc:
            raise InstanceError(
                "SUBSCRIPTION_ERROR", message="Subscription timed out while waiting for token"
            ) from exc
        except Exception as exc:
            raise InstanceError("SUBSCRIPTION_ERROR", message=str(exc)) from exc

        raise InstanceError(
            "SUBSCRIPTION_COMPLETE",
            message="Subscription ended without receiving token",
        )

    def _process_subscription_result(
        self, result: dict[str, Any]
    ) -> AuthenticationToken | None:
        """Validate subscription payload and convert token payload when present."""
        response = cast(CreatedAuthenticationTokenResponse, result)
        payload = response.get("createdAuthenticationToken")
        if payload is None:
            raise InstanceError("NO_RESPONSE", message="No subscription payload received")

        if payload.get("error") is not None:
            error = payload["error"]
            details = self._extract_error_details(error)
            raise InstanceError(
                error["code"], reason=details.reason, message=details.message
            )

        if payload.get("token") is not None:
            return AuthenticationToken.from_wire(payload["token"])

        return None

    async def refresh_token(self, refresh_token: str) -> AuthenticationToken:
        """Refresh an access token using a refresh token."""
        async with self._graphql_client as session:
            try:
                variable_values = {"refreshToken": refresh_token}
                result: dict[str, Any] = await session.execute(
                    REFRESH_AUTHENTICATION_TOKEN, variable_values=variable_values
                )
            except Exception as exc:
                raise InstanceError("GRAPHQL_ERROR", message=str(exc)) from exc

        response = cast(RefreshAuthenticationTokenResponse, result)
        payload = response.get("refreshAuthenticationToken")
        if payload is None:
            raise InstanceError(
                "NO_RESPONSE", message="No response from refreshAuthenticationToken"
            )

        if payload.get("error") is not None:
            error = payload["error"]
            details = self._extract_error_details(error)
            raise InstanceError(
                error["code"], reason=details.reason, message=details.message
            )

        if payload.get("token") is None:
            raise InstanceError("NO_TOKEN", message="No token returned from refresh")

        return AuthenticationToken.from_wire(payload["token"])
