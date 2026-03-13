"""Public package exports."""

from caido_sdk_client.auth import (
    AuthCacheFile,
    AuthManager,
    AuthOptions,
    BrowserAuthOptions,
    CachedToken,
    FileTokenCache,
    PATAuthOptions,
    TokenAuthOptions,
    TokenCache,
    TokenPair,
)
from caido_sdk_client.client import Client, ConnectOptions, Health, ReadyOptions
from caido_sdk_client.errors import (
    BaseError,
    InstanceNotReadyError,
    NoViewerInResponseError,
    UnsupportedViewerTypeError,
    from_error,
)
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.logger import ConsoleLogger, Logger
from caido_sdk_client.sdks import UserSDK
from caido_sdk_client.types import (
    CloudUser,
    GuestUser,
    ScriptUser,
    SubscriptionEntitlement,
    SubscriptionPlan,
    User,
    UserIdentity,
    UserProfile,
    UserSubscription,
)

__all__ = [
    "AuthCacheFile",
    "AuthManager",
    "AuthOptions",
    "BaseError",
    "BrowserAuthOptions",
    "CachedToken",
    "Client",
    "CloudUser",
    "ConnectOptions",
    "ConsoleLogger",
    "FileTokenCache",
    "GraphQLClient",
    "GuestUser",
    "Health",
    "InstanceNotReadyError",
    "Logger",
    "NoViewerInResponseError",
    "PATAuthOptions",
    "ReadyOptions",
    "ScriptUser",
    "SubscriptionEntitlement",
    "SubscriptionPlan",
    "TokenAuthOptions",
    "TokenCache",
    "TokenPair",
    "UnsupportedViewerTypeError",
    "User",
    "UserIdentity",
    "UserProfile",
    "UserSDK",
    "UserSubscription",
    "from_error",
]
