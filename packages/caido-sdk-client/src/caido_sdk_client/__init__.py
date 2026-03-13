"""Public package exports."""

from caido_sdk_client.client import Client, ConnectOptions, Health, ReadyOptions
from caido_sdk_client.errors import (
    BaseError,
    InstanceNotReadyError,
    NoViewerInResponseError,
    UnsupportedViewerTypeError,
    from_error,
)
from caido_sdk_client.graphql import GraphQLClient, GraphQLClientOptions
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
    "BaseError",
    "Client",
    "CloudUser",
    "ConnectOptions",
    "GraphQLClient",
    "GraphQLClientOptions",
    "GuestUser",
    "Health",
    "InstanceNotReadyError",
    "NoViewerInResponseError",
    "ReadyOptions",
    "ScriptUser",
    "SubscriptionEntitlement",
    "SubscriptionPlan",
    "UnsupportedViewerTypeError",
    "User",
    "UserIdentity",
    "UserProfile",
    "UserSDK",
    "UserSubscription",
    "from_error",
]
