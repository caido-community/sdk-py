"""Form validation errors."""

from __future__ import annotations

import json

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import AliasTakenUserErrorFull


class NameTakenUserError(BaseError):
    def __init__(self, name: str) -> None:
        super().__init__(f"The name {name} is already in use.")


class InvalidGlobTermsUserError(BaseError):
    def __init__(self, terms: list[str]) -> None:
        super().__init__(f"Invalid glob terms: {json.dumps(terms)}")


class AliasTakenUserError(BaseError):
    def __init__(self, error: AliasTakenUserErrorFull) -> None:
        super().__init__(f"Alias already exists: {error.alias}")
