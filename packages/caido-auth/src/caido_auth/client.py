"""Caido authentication client for OAuth2 device code flow."""

import asyncio
from typing import Callable, Optional
from urllib.parse import urljoin, urlparse

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport

from .models import (
    AuthenticationError,
    AuthenticationFlowError,
    AuthenticationRequest,
    AuthenticationToken,
    TokenRefreshError,
)
from .queries import (
    CREATED_AUTHENTICATION_TOKEN_SUBSCRIPTION,
    REFRESH_AUTHENTICATION_TOKEN,
    START_AUTHENTICATION_FLOW,
)


class CaidoAuth:
    """Client for authenticating with a Caido instance"""

    def __init__(self, instance_url: str):
        """
        Initialize the authentication client.

        Args:
            instance_url: Base URL of the Caido instance (e.g., "http://localhost:8080")
        """
        self.instance_url = instance_url.rstrip("/")
        self._graphql_url = urljoin(self.instance_url, "/graphql")
        self._websocket_url = self._get_websocket_url()

    def _get_websocket_url(self) -> str:
        """Convert HTTP(S) URL to WS(S) URL for subscriptions."""
        parsed = urlparse(self._graphql_url)
        scheme = "wss" if parsed.scheme == "https" else "ws"
        return f"{scheme}://{parsed.netloc}/ws/graphql"

    async def start_authentication_flow(
        self,
        on_request: Optional[Callable[[AuthenticationRequest], None]] = None,
    ) -> AuthenticationToken:
        """
        Start the device code authentication flow.

        This method:
        1. Initiates the authentication flow
        2. Starts a subscription to wait for user authorization
        3. Calls the callback with the authentication request details
        4. Waits for the user to authorize in their browser
        5. Returns the authentication token once approved

        Args:
            on_request: Optional callback function called with AuthenticationRequest
                       when the user needs to visit the verification URL

        Returns:
            AuthenticationToken with access token, refresh token, and expiration

        Raises:
            AuthenticationFlowError: If the flow fails to start
            AuthenticationError: If token retrieval fails
        """
        # Step 1: Start the authentication flow
        transport = AIOHTTPTransport(url=self._graphql_url)
        async with Client(
            transport=transport,
            fetch_schema_from_transport=False,
        ) as session:
            result = await session.execute(START_AUTHENTICATION_FLOW)
            payload = result["startAuthenticationFlow"]

            if payload.get("error"):
                error = payload["error"]
                reason = error.get("reason", error.get("code", "UNKNOWN"))
                message = error.get("message", "Authentication flow failed")
                raise AuthenticationFlowError(reason, message)

            if not payload.get("request"):
                raise AuthenticationFlowError(
                    "NO_REQUEST", "No authentication request returned"
                )

            auth_request = AuthenticationRequest.from_graphql(payload["request"])

        # Step 2: Call the user callback with the request details
        if on_request:
            on_request(auth_request)

        # Step 3: Subscribe to wait for token
        token = await self._wait_for_token(auth_request.id)
        return token

    async def _wait_for_token(self, request_id: str) -> AuthenticationToken:
        """
        Subscribe and wait for the authentication token.

        Args:
            request_id: The authentication request ID

        Returns:
            AuthenticationToken once the user authorizes

        Raises:
            AuthenticationError: If subscription fails or returns an error
        """
        transport = WebsocketsTransport(url=self._websocket_url)

        async with Client(
            transport=transport,
            fetch_schema_from_transport=False,
        ) as session:
            async for result in session.subscribe(
                CREATED_AUTHENTICATION_TOKEN_SUBSCRIPTION,
                variable_values={"requestId": request_id},
            ):
                payload = result["createdAuthenticationToken"]

                if payload.get("error"):
                    error = payload["error"]
                    reason = error.get("reason", error.get("code", "UNKNOWN"))
                    message = error.get("message", "Token retrieval failed")
                    raise AuthenticationError(f"{reason}: {message}")

                if payload.get("token"):
                    return AuthenticationToken.from_graphql(payload["token"])

        raise AuthenticationError("Subscription ended without receiving token")

    async def refresh_token(self, refresh_token: str) -> AuthenticationToken:
        """
        Refresh an access token using a refresh token.

        Args:
            refresh_token: The refresh token from a previous authentication

        Returns:
            New AuthenticationToken with updated access and refresh tokens

        Raises:
            TokenRefreshError: If the refresh fails
        """
        transport = AIOHTTPTransport(url=self._graphql_url)

        async with Client(
            transport=transport,
            fetch_schema_from_transport=False,
        ) as session:
            result = await session.execute(
                REFRESH_AUTHENTICATION_TOKEN,
                variable_values={"refreshToken": refresh_token},
            )
            payload = result["refreshAuthenticationToken"]

            if payload.get("error"):
                error = payload["error"]
                reason = error.get("reason", error.get("code", "UNKNOWN"))
                message = error.get("message", "Token refresh failed")
                raise TokenRefreshError(reason, message)

            if not payload.get("token"):
                raise TokenRefreshError("NO_TOKEN", "No token returned from refresh")

            return AuthenticationToken.from_graphql(payload["token"])

    def authenticate(
        self,
        on_request: Callable[[AuthenticationRequest], None],
    ) -> AuthenticationToken:
        """
        Synchronous wrapper for start_authentication_flow.

        Args:
            on_request: Optional callback function called with AuthenticationRequest

        Returns:
            AuthenticationToken with access token, refresh token, and expiration
        """
        return asyncio.run(self.start_authentication_flow(on_request))

    def refresh(self, refresh_token: str) -> AuthenticationToken:
        """
        Synchronous wrapper for refresh_token.

        Args:
            refresh_token: The refresh token from a previous authentication

        Returns:
            New AuthenticationToken with updated access and refresh tokens
        """
        return asyncio.run(self.refresh_token(refresh_token))
