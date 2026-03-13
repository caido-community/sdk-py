"""Error handling utilities."""

from __future__ import annotations

from typing import NoReturn

from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.from_error import from_error


def handle_graphql_error(error: AllErrors) -> NoReturn:
    """Handle a GraphQL error by throwing the appropriate error class."""
    error_instance = from_error(error)
    raise error_instance
