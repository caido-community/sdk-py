"""Convert a GraphQL error fragment into the appropriate error class."""

from __future__ import annotations

from caido_sdk_client.errors.all_errors import AllErrors
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
from caido_sdk_client.graphql.__generated__.schema import (
    AliasTakenUserErrorFull,
    CloudUserErrorFull,
    InvalidGlobTermsUserErrorFull,
    NameTakenUserErrorFull,
    NewerVersionUserErrorFull,
    OtherUserErrorFull,
    PermissionDeniedUserErrorFull,
    PluginUserErrorFull,
    ProjectUserErrorFull,
    ReadOnlyUserErrorFull,
    StoreUserErrorFull,
    TaskInProgressUserErrorFull,
    UnknownIdUserErrorFull,
    WorkflowUserErrorFull,
)


def from_error(error: AllErrors) -> BaseError:
    """Map a GraphQL error fragment to the corresponding SDK error class."""
    match error:
        case UnknownIdUserErrorFull():
            return NotFoundUserError()
        case PermissionDeniedUserErrorFull():
            return PermissionDeniedUserError()
        case OtherUserErrorFull():
            return OtherUserError(error.code)
        case NameTakenUserErrorFull():
            return NameTakenUserError(error.name)
        case AliasTakenUserErrorFull():
            return AliasTakenUserError(error)
        case InvalidGlobTermsUserErrorFull():
            return InvalidGlobTermsUserError(error.terms)
        case ProjectUserErrorFull():
            return ProjectUserError(error)
        case NewerVersionUserErrorFull():
            return NewerVersionUserError(error)
        case CloudUserErrorFull():
            return CloudUserError(error)
        case PluginUserErrorFull():
            return PluginUserError(error)
        case StoreUserErrorFull():
            return StoreUserError(error)
        case TaskInProgressUserErrorFull():
            return TaskInProgressUserError(error.taskId)
        case ReadOnlyUserErrorFull():
            return ReadOnlyUserError()
        case WorkflowUserErrorFull():
            return WorkflowUserError(
                error.code,
                error.reason,
                error.message,
                error.node,
            )
        case _:
            typename = getattr(error, "typename", None)
            raise ValueError(f"Unknown error typename: {typename}")
