"""Miscellaneous errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class NotFoundUserError(BaseError):
    def __init__(self) -> None:
        super().__init__("This resource does not exist")


class ReadOnlyUserError(BaseError):
    def __init__(self) -> None:
        super().__init__("This resource is read-only")


class OtherUserError(BaseError):
    def __init__(self, code: str, message: str | None = None) -> None:
        if message is not None:
            super().__init__(message)
        else:
            super().__init__(f"An unknown user error occured: {code!r}")
