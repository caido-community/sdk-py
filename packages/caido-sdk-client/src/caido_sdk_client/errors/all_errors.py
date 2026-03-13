"""Union type for all GraphQL user errors."""

from __future__ import annotations

from typing import Union

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

AllErrors = Union[
    UnknownIdUserErrorFull,
    AliasTakenUserErrorFull,
    InvalidGlobTermsUserErrorFull,
    PermissionDeniedUserErrorFull,
    NameTakenUserErrorFull,
    ProjectUserErrorFull,
    ReadOnlyUserErrorFull,
    OtherUserErrorFull,
    NewerVersionUserErrorFull,
    CloudUserErrorFull,
    PluginUserErrorFull,
    StoreUserErrorFull,
    TaskInProgressUserErrorFull,
    WorkflowUserErrorFull,
]
