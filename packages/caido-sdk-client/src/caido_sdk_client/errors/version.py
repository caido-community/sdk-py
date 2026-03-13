"""Version-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import NewerVersionUserErrorFull


class NewerVersionUserError(BaseError):
    version: int

    def __init__(self, error: NewerVersionUserErrorFull) -> None:
        super().__init__("Stale data, please refresh")
        self.version = error.version
