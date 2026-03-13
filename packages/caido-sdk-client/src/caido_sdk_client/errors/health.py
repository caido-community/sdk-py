"""Health check errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class InstanceNotReadyError(BaseError):
    """Error thrown when the instance is not ready after exhausting all retry attempts."""

    attempts: int

    def __init__(self, attempts: int) -> None:
        super().__init__(f"Instance not ready after {attempts} attempts")
        self.attempts = attempts
