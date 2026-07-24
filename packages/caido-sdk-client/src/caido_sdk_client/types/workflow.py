"""Workflow-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Literal

from caido_sdk_client.graphql.__generated__.schema import WorkflowKind
from caido_sdk_client.types.network import ConnectionInfoInput
from caido_sdk_client.types.strings import Id, IdLike


@dataclass(frozen=True)
class Workflow:
    """Workflow information."""

    id: Id
    name: str
    kind: WorkflowKind
    definition: dict[str, Any]
    enabled: bool
    global_: bool
    read_only: bool
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateWorkflowOptions:
    """Options for creating a workflow."""

    definition: dict[str, Any]
    """The workflow definition payload."""

    global_: bool
    """Whether the workflow is global."""


@dataclass(frozen=True)
class UpdateWorkflowOptions:
    """Options for updating a workflow."""

    definition: dict[str, Any]
    """The workflow definition payload."""


@dataclass(frozen=True)
class TestWorkflowConvertOptions:
    """Options for testing a convert workflow."""

    kind: Literal["convert"]
    definition: dict[str, Any]
    data: str | bytes


@dataclass(frozen=True)
class TestWorkflowRequest:
    """Request input for testing an HTTP workflow."""

    connection: ConnectionInfoInput
    raw: str | bytes


@dataclass(frozen=True)
class TestWorkflowResponse:
    """Response input for testing an HTTP workflow."""

    raw: str | bytes


@dataclass(frozen=True)
class TestWorkflowPassiveOptions:
    """Options for testing a passive workflow."""

    kind: Literal["passive"]
    definition: dict[str, Any]
    request: TestWorkflowRequest
    response: TestWorkflowResponse | None = None


@dataclass(frozen=True)
class TestWorkflowActiveOptions:
    """Options for testing an active workflow."""

    kind: Literal["active"]
    definition: dict[str, Any]
    request: TestWorkflowRequest
    response: TestWorkflowResponse | None = None


@dataclass(frozen=True)
class TestWorkflowConvertResult:
    """Result of testing a convert workflow."""

    output: bytes | None = None
    run_state: dict[str, Any] | None = None


@dataclass(frozen=True)
class TestWorkflowHttpResult:
    """Result of testing a passive or active workflow."""

    run_state: dict[str, Any] | None = None


@dataclass(frozen=True)
class RunConvertWorkflowOptions:
    """Options for running a convert workflow."""

    kind: Literal["convert"]
    id: IdLike
    data: str | bytes


@dataclass(frozen=True)
class RunActiveWorkflowOptions:
    """Options for running an active workflow."""

    kind: Literal["active"]
    id: IdLike
    request_id: IdLike


@dataclass(frozen=True)
class RunConvertWorkflowResult:
    """Result of running a convert workflow."""

    output: bytes | None = None
