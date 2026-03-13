"""REST request errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class RestRequestError(BaseError):
    """Error thrown when a REST request fails."""

    method: str
    path: str
    status: int
    error_text: str

    def __init__(
        self, method: str, path: str, status: int, error_text: str
    ) -> None:
        super().__init__(
            f"REST request failed: {method} {path} - {status}: {error_text}"
        )
        self.method = method
        self.path = path
        self.status = status
        self.error_text = error_text
