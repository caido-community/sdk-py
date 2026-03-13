"""Authentication manager."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from caido_sdk_client.auth.cache.types import CachedToken, TokenCache
from caido_sdk_client.auth.types import (
    AuthOptions,
    BrowserAuthOptions,
    TokenAuthOptions,
)
from caido_sdk_client.auth.utils import is_pat_auth, resolve_cache
from caido_sdk_client.errors.auth import TokenRefreshError
from caido_sdk_client.logger import Logger


@dataclass(slots=True)
class _TokenState:
    access_token: str
    refresh_token: str | None = None
    expires_at: datetime | None = None


class AuthManager:
    def __init__(
        self,
        instance_url: str,
        logger: Logger,
        auth_options: AuthOptions | None = None,
    ) -> None:
        self._instance_url = instance_url
        self._logger = logger
        self._auth_options = auth_options
        self._cache: TokenCache | None = (
            resolve_cache(auth_options.cache, logger)
            if auth_options is not None and auth_options.cache is not None
            else None
        )

        self._token_state: _TokenState | None = None
        self._auth_client: Any = None
        self._on_token_refresh_callbacks: set[Callable[[], None]] = set()

    def get_access_token(self) -> str | None:
        if self._token_state is None:
            return None
        return self._token_state.access_token

    def can_refresh(self) -> bool:
        return (
            self._token_state is not None
            and self._token_state.refresh_token is not None
        )

    def on_token_refresh(self, callback: Callable[[], None]) -> Callable[[], None]:
        """Subscribe to token refresh events.

        Returns an unsubscribe function.
        """
        self._on_token_refresh_callbacks.add(callback)

        def unsubscribe() -> None:
            self._on_token_refresh_callbacks.discard(callback)

        return unsubscribe

    def _notify_token_refresh(self) -> None:
        for callback in self._on_token_refresh_callbacks:
            try:
                callback()
            except Exception:
                self._logger.warn("Error in token refresh callback")

    async def authenticate(self) -> None:
        auth = self._auth_options

        cache = self._cache
        if cache is not None:
            self._logger.debug("Attempting to load cached token")
            cached = await cache.load()
            if cached is not None:
                self._logger.info("Loaded token from cache")
                self._token_state = _from_cached_token(cached)
                self._notify_token_refresh()
                return

        if auth is not None and isinstance(auth, TokenAuthOptions):
            self._logger.debug("Using provided token")
            if isinstance(auth.token, str):
                self._token_state = _TokenState(access_token=auth.token)
            else:
                self._token_state = _TokenState(
                    access_token=auth.token.access_token,
                    refresh_token=auth.token.refresh_token,
                )
            self._notify_token_refresh()
            await self._maybe_cache_token()
            return

        self._logger.info("Starting authentication flow")
        auth_client = self._get_or_create_auth_client()
        token = await auth_client.start_authentication_flow()
        self._apply_auth_token(token)
        self._logger.info("Authentication flow completed")
        await self._maybe_cache_token()

    async def refresh(self) -> None:
        refresh_token = self._token_state.refresh_token if self._token_state else None
        if refresh_token is None:
            raise TokenRefreshError()

        self._logger.debug("Refreshing access token")
        auth_client = self._get_or_create_auth_client()
        token = await auth_client.refresh_token(refresh_token)
        self._apply_auth_token(token)
        self._logger.info("Access token refreshed")
        await self._maybe_cache_token()
        self._notify_token_refresh()

    def _get_or_create_auth_client(self) -> Any:
        if self._auth_client is None:
            try:
                from caido_server_auth import (
                    AuthClient,
                    AuthClientOptions,
                )
            except ImportError as exc:
                raise ImportError(
                    "caido-server-auth is required for PAT/browser authentication "
                    "and token refresh. Install it with: pip install caido-server-auth"
                ) from exc

            approver = self._create_approver()
            self._auth_client = AuthClient(
                AuthClientOptions(
                    instance_url=self._instance_url,
                    approver=approver,
                )
            )
        return self._auth_client

    def _create_approver(self) -> Any:
        auth = self._auth_options

        if auth is not None and is_pat_auth(auth):
            try:
                from caido_server_auth import (
                    PATApprover,
                    PATApproverOptions,
                )
            except ImportError as exc:
                raise ImportError(
                    "caido-server-auth is required for PAT authentication."
                ) from exc
            return PATApprover(PATApproverOptions(pat=auth.pat))  # type: ignore[union-attr]

        try:
            from caido_server_auth import BrowserApprover  # noqa: F811
        except ImportError as exc:
            raise ImportError(
                "caido-server-auth is required for browser authentication."
            ) from exc

        logger = self._logger
        browser_auth = auth if isinstance(auth, BrowserAuthOptions) else None
        on_request = (
            browser_auth.on_request
            if browser_auth is not None and browser_auth.on_request is not None
            else lambda request: logger.info(
                f"Please visit the following URL to authenticate: {request.verification_url}"
            )
        )
        return BrowserApprover(on_request)

    def _apply_auth_token(self, token: Any) -> None:
        self._token_state = _TokenState(
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            expires_at=token.expires_at,
        )
        self._notify_token_refresh()

    async def _maybe_cache_token(self) -> None:
        cache = self._cache
        token_state = self._token_state
        if cache is None or token_state is None:
            return
        self._logger.debug("Saving token to cache")
        await cache.save(_to_cached_token(token_state))


def _to_cached_token(state: _TokenState) -> CachedToken:
    return CachedToken(
        access_token=state.access_token,
        refresh_token=state.refresh_token,
        expires_at=state.expires_at.isoformat()
        if state.expires_at is not None
        else None,
    )


def _from_cached_token(cached: CachedToken) -> _TokenState:
    return _TokenState(
        access_token=cached.access_token,
        refresh_token=cached.refresh_token,
        expires_at=(
            datetime.fromisoformat(cached.expires_at)
            if cached.expires_at is not None
            else None
        ),
    )
