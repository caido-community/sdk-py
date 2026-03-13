"""Authentication-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class TokenRefreshError(BaseError):
    """Error thrown when attempting to refresh a token but no refresh token is available."""

    def __init__(self) -> None:
        super().__init__(
            "Cannot refresh token: no refresh token available. "
            "Provide a token pair with a refresh token, or use PAT/browser authentication."
        )
