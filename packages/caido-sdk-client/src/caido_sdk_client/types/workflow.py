"""Workflow-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from caido_sdk_client.graphql.__generated__.schema import WorkflowKind
from caido_sdk_client.types.strings import Id


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
