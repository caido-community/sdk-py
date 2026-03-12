"""Server authentication SDK for OAuth2 device code authentication."""

from .approvers import (
    AuthApprover,
    BrowserApprover,
    OnRequestCallback,
    PATApprover,
    PATApproverOptions,
)
from .client import AuthClient, AuthClientOptions
from .errors import AuthenticationError, CloudError, InstanceError
from .types import (
    AuthenticationRequest,
    AuthenticationToken,
    DeviceInformation,
    DeviceScope,
)

__all__ = [
    "AuthApprover",
    "AuthClient",
    "AuthClientOptions",
    "AuthenticationError",
    "AuthenticationRequest",
    "AuthenticationToken",
    "BrowserApprover",
    "CloudError",
    "DeviceInformation",
    "DeviceScope",
    "InstanceError",
    "OnRequestCallback",
    "PATApprover",
    "PATApproverOptions",
]
