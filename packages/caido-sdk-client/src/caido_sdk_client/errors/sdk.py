"""SDK-specific errors that don't map directly to GraphQL error types."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class NoViewerInResponseError(BaseError):
    """Raised when the GraphQL response does not include a viewer object."""

    def __init__(self) -> None:
        super().__init__("No viewer found in GraphQL response")


class UnsupportedViewerTypeError(BaseError):
    """Raised when the viewer type is not supported by UserSDK."""

    def __init__(self, typename: object) -> None:
        super().__init__(f"Unsupported viewer type: {typename!r}")


class MissingExpectedValueError(BaseError):
    """Raised when a GraphQL payload is missing an expected non-null value."""

    def __init__(self, path: str) -> None:
        super().__init__(f"Missing expected value at {path}")
