"""GraphQL operation errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class NetworkUserError(BaseError):
    def __init__(self) -> None:
        super().__init__("A network error occured")


class OperationUserError(BaseError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class NoDataUserError(BaseError):
    def __init__(self) -> None:
        super().__init__("The operation did not return any data")
