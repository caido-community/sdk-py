"""Error types for the Caido SDK client."""

from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.auth import TokenRefreshError
from caido_sdk_client.errors.authorization import (
    AuthorizationUserError,
    PermissionDeniedUserError,
)
from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.errors.cloud import CloudUserError
from caido_sdk_client.errors.form import (
    AliasTakenUserError,
    InvalidGlobTermsUserError,
    NameTakenUserError,
)
from caido_sdk_client.errors.from_error import from_error
from caido_sdk_client.errors.graphql import (
    NetworkUserError,
    NoDataUserError,
    OperationUserError,
)
from caido_sdk_client.errors.health import InstanceNotReadyError
from caido_sdk_client.errors.misc import (
    NotFoundUserError,
    OtherUserError,
    ReadOnlyUserError,
)
from caido_sdk_client.errors.plugin import (
    PluginFunctionCallError,
    PluginUserError,
    StoreUserError,
)
from caido_sdk_client.errors.project import ProjectUserError
from caido_sdk_client.errors.rest import RestRequestError
from caido_sdk_client.errors.sdk import NoViewerInResponseError, UnsupportedViewerTypeError
from caido_sdk_client.errors.tasks import TaskInProgressUserError
from caido_sdk_client.errors.version import NewerVersionUserError
from caido_sdk_client.errors.workflow import WorkflowUserError

__all__ = [
    "AllErrors",
    "AliasTakenUserError",
    "AuthorizationUserError",
    "BaseError",
    "CloudUserError",
    "InstanceNotReadyError",
    "InvalidGlobTermsUserError",
    "NameTakenUserError",
    "NetworkUserError",
    "NoDataUserError",
    "NotFoundUserError",
    "OperationUserError",
    "OtherUserError",
    "PermissionDeniedUserError",
    "PluginFunctionCallError",
    "PluginUserError",
    "ProjectUserError",
    "ReadOnlyUserError",
    "RestRequestError",
    "StoreUserError",
    "TaskInProgressUserError",
    "TokenRefreshError",
    "WorkflowUserError",
    "NewerVersionUserError",
    "NoViewerInResponseError",
    "UnsupportedViewerTypeError",
    "from_error",
]
