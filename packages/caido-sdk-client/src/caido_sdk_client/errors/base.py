"""Base error class for all Caido client errors."""

from __future__ import annotations


class BaseError(Exception):
    """Base error class for all Caido client errors."""

    source: Exception | None

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.source = None

    def with_source(self, source: Exception) -> BaseError:
        self.source = source
        return self

    def __str__(self) -> str:
        message = super().__str__()

        source = self.source
        if source is not None:
            message += f"\n  Source: {source}"
        return message
