"""Authorization-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class PermissionDeniedUserError(BaseError):

    def __init__(self) -> None:
        super().__init__("You don't have the required permissions for this action.")

    @staticmethod
    def is_permission_denied_user_error(error: BaseError) -> bool:
        return isinstance(error, PermissionDeniedUserError)


class AuthorizationUserError(BaseError):
    reason: str

    def __init__(self, error: object) -> None:
        reason = getattr(error, "reason", None) or (
            error["reason"] if isinstance(error, dict) else None
        )
        match reason:
            case "FORBIDDEN":
                super().__init__(
                    "You don't have the required permissions for this action."
                )
                self.reason = "FORBIDDEN"
            case "INVALID_TOKEN":
                super().__init__(
                    "Your session has expired or is invalid. Please try signing in again."
                )
                self.reason = "INVALID_TOKEN"
            case "MISSING_SCOPE":
                super().__init__(
                    "Your account is missing the required permissions for this action."
                )
                self.reason = "MISSING_SCOPE"
            case _:
                super().__init__(f"Authorization error: {reason}")
                self.reason = str(reason)
