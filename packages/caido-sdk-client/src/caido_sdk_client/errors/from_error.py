"""Convert a GraphQL error fragment into the appropriate error class."""

from __future__ import annotations

from caido_sdk_client.errors.authorization import PermissionDeniedUserError
from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.errors.cloud import CloudUserError
from caido_sdk_client.errors.form import (
    AliasTakenUserError,
    InvalidGlobTermsUserError,
    NameTakenUserError,
)
from caido_sdk_client.errors.misc import (
    NotFoundUserError,
    OtherUserError,
    ReadOnlyUserError,
)
from caido_sdk_client.errors.plugin import PluginUserError, StoreUserError
from caido_sdk_client.errors.project import ProjectUserError
from caido_sdk_client.errors.tasks import TaskInProgressUserError
from caido_sdk_client.errors.version import NewerVersionUserError
from caido_sdk_client.errors.workflow import WorkflowUserError


def from_error(error: object) -> BaseError:
    """Map a GraphQL error fragment to the corresponding SDK error class."""
    # We intentionally dispatch on the GraphQL typename string here instead of
    # matching on specific pydantic model classes. This keeps the function
    # compatible with both fragment `...Full` models and operation-specific
    # inline fragment models, as long as they expose the required attributes.
    typename = getattr(error, "typename", None)

    match typename:
        case "UnknownIdUserError":
            return NotFoundUserError()

        case "PermissionDeniedUserError":
            return PermissionDeniedUserError()

        case "OtherUserError":
            return OtherUserError(getattr(error, "code"))

        case "NameTakenUserError":
            return NameTakenUserError(getattr(error, "name"))

        case "AliasTakenUserError":
            return AliasTakenUserError(error)  # type: ignore[arg-type]

        case "InvalidGlobTermsUserError":
            return InvalidGlobTermsUserError(getattr(error, "terms"))

        case "ProjectUserError":
            reason = getattr(error, "projectReason")
            return ProjectUserError(reason)

        case "NewerVersionUserError":
            return NewerVersionUserError(error)  # type: ignore[arg-type]

        case "CloudUserError":
            return CloudUserError(error)  # type: ignore[arg-type]

        case "PluginUserError":
            return PluginUserError(error)  # type: ignore[arg-type]

        case "StoreUserError":
            return StoreUserError(error)  # type: ignore[arg-type]

        case "TaskInProgressUserError":
            return TaskInProgressUserError(getattr(error, "taskId", ""))

        case "ReadOnlyUserError":
            return ReadOnlyUserError()

        case "WorkflowUserError":
            code = getattr(error, "code")
            reason = getattr(error, "reason")
            message = getattr(error, "message")
            node = getattr(error, "node")
            return WorkflowUserError(code, reason, message, node)

        case _:
            raise ValueError(f"Unknown error typename: {typename}")
