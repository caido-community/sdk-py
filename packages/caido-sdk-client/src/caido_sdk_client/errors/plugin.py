"""Plugin-related errors."""

from __future__ import annotations

from typing import Any

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import (
    PluginErrorReason,
    PluginUserErrorFull,
    StoreErrorReason,
    StoreUserErrorFull,
)


class PluginFunctionCallError(BaseError):
    """Error from calling a plugin function via REST."""

    kind: str

    def __init__(self, name: str, error: Any) -> None:
        kind = (
            error.get("kind")
            if isinstance(error, dict)
            else getattr(error, "kind", None)
        )
        match kind:
            case "invalid_procedure":
                fn_name = (
                    error.get("name")
                    if isinstance(error, dict)
                    else getattr(error, "name", None)
                )
                super().__init__(
                    f"Could not call plugin function with name '{fn_name}'."
                )
                self.kind = kind
            case "invalid_output":
                expected = (
                    error.get("expected")
                    if isinstance(error, dict)
                    else getattr(error, "expected", None)
                )
                found = (
                    error.get("found")
                    if isinstance(error, dict)
                    else getattr(error, "found", None)
                )
                super().__init__(
                    f"Invalid output type for plugin function. Expected {expected} but got {found}."
                )
                self.kind = kind
            case "thrown":
                message = (
                    error.get("message")
                    if isinstance(error, dict)
                    else getattr(error, "message", None)
                ) or "Unknown error"
                stack = (
                    error.get("stack")
                    if isinstance(error, dict)
                    else getattr(error, "stack", None)
                ) or ""
                stack_text = f"\n\n{stack}" if stack else ""
                super().__init__(
                    f"Plugin function '{name}' threw an error: {message}{stack_text}"
                )
                self.kind = kind
            case _:
                super().__init__(f"Plugin function call error: {kind}")
                self.kind = str(kind)


class PluginUserError(BaseError):
    reason: PluginErrorReason

    def __init__(self, error: PluginUserErrorFull) -> None:
        match error.reason:
            case PluginErrorReason.INVALID_MANIFEST:
                super().__init__("The plugin manifest is invalid")
                self.reason = error.reason
            case PluginErrorReason.INVALID_PACKAGE:
                super().__init__("The plugin package is invalid")
                self.reason = error.reason
            case PluginErrorReason.MISSING_FILE:
                super().__init__("The plugin package is missing a file")
                self.reason = error.reason
            case PluginErrorReason.ALREADY_INSTALLED:
                super().__init__("The plugin is already installed")
                self.reason = error.reason
            case PluginErrorReason.INVALID_OPERATION:
                super().__init__(
                    "This operation cannot be performed on this type of plugin"
                )
                self.reason = error.reason


class StoreUserError(BaseError):
    def __init__(self, error: StoreUserErrorFull) -> None:
        match error.storeReason:
            case StoreErrorReason.FILE_UNAVAILABLE:
                super().__init__("The plugin package files are unavailable")
            case StoreErrorReason.INVALID_PUBLIC_KEY:
                super().__init__("The plugin package public key is invalid")
            case StoreErrorReason.INVALID_SIGNATURE:
                super().__init__("The plugin package signature is invalid")
            case StoreErrorReason.PACKAGE_TOO_LARGE:
                super().__init__("The plugin package is too large")
            case StoreErrorReason.PACKAGE_UNKNOWN:
                super().__init__(
                    "An unknown error occured while installing the plugin package"
                )
