"""Error types for server authentication."""

from __future__ import annotations


class AuthenticationError(Exception):
    """Base error class for authentication-related failures."""


class CloudError(AuthenticationError):
    """Error for failures coming from the Caido cloud API."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        code: str | None = None,
        reason: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.reason = reason


class InstanceError(AuthenticationError):
    """Error for failures coming from a Caido instance."""

    def __init__(
        self,
        code: str,
        *,
        reason: str | None = None,
        message: str | None = None,
    ) -> None:
        super().__init__(reason or message or code)
        self.code = code
        self.reason = reason
        self.error_message = message
