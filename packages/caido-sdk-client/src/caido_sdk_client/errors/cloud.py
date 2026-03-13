"""Cloud-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import (
    CloudErrorReason,
    CloudUserErrorFull,
)


class CloudUserError(BaseError):
    reason: CloudErrorReason

    def __init__(self, error: CloudUserErrorFull) -> None:
        match error.cloudReason:
            case CloudErrorReason.UNAVAILABLE:
                super().__init__("Could not communicate with Caido cloud")
                self.reason = error.cloudReason
            case CloudErrorReason.UNEXPECTED:
                super().__init__(
                    "An unknown error occured while communicating with Caido cloud"
                )
                self.reason = error.cloudReason
