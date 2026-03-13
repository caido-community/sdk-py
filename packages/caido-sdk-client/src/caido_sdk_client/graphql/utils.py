"""Utilities for parsing GraphQL error extensions into typed SDK errors."""

from __future__ import annotations

from typing import Any

from caido_sdk_client.errors.authorization import AuthorizationUserError
from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.errors.cloud import CloudUserError
from caido_sdk_client.errors.misc import OtherUserError
from caido_sdk_client.graphql.__generated__.schema import (
    CloudErrorReason,
    CloudUserErrorFull,
)

_ERROR_CODE_AUTHORIZATION = "AUTHORIZATION"
_ERROR_CODE_CLOUD = "CLOUD"
_ERROR_CODE_INTERNAL = "INTERNAL"

_VALID_AUTHORIZATION_REASONS = {"FORBIDDEN", "INVALID_TOKEN", "MISSING_SCOPE"}
_VALID_CLOUD_REASONS = {r.value for r in CloudErrorReason}


def to_user_error(
    error: dict[str, Any],
) -> AuthorizationUserError | CloudUserError | OtherUserError | None:
    """Parse a GraphQL error's CAIDO extension into a typed user error.

    Returns None if the error doesn't have a recognized CAIDO extension.
    """
    extensions = error.get("extensions")
    if not isinstance(extensions, dict):
        return None

    caido_extension = extensions.get("CAIDO")
    if not isinstance(caido_extension, dict):
        return None

    code = caido_extension.get("code")

    if code == _ERROR_CODE_AUTHORIZATION:
        reason = caido_extension.get("reason")
        if isinstance(reason, str) and reason in _VALID_AUTHORIZATION_REASONS:
            return AuthorizationUserError({"reason": reason})
        return None

    if code == _ERROR_CODE_CLOUD:
        reason = caido_extension.get("reason")
        if isinstance(reason, str) and reason in _VALID_CLOUD_REASONS:
            fragment = CloudUserErrorFull(
                cloudReason=CloudErrorReason(reason),
                code=code,
            )
            return CloudUserError(fragment)
        return None

    if code == _ERROR_CODE_INTERNAL:
        message = caido_extension.get("message")
        if isinstance(message, str):
            return OtherUserError(code, message)
        return None

    return None


def has_authorization_error(errors: list[dict[str, Any]]) -> bool:
    """Check if a list of GraphQL errors contains an authorization error."""
    for e in errors:
        user_error = to_user_error(e)
        if user_error is not None and isinstance(user_error, AuthorizationUserError):
            return True
    return False
