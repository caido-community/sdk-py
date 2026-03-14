"""Task-related types."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from caido_sdk_client.graphql.__generated__.schema import (
    TaskStatus as GraphQLTaskStatus,
)

if TYPE_CHECKING:
    from caido_sdk_client.sdks.task import Task


# Re-export generated enum for public API
TaskStatus = GraphQLTaskStatus


@dataclass(frozen=True, slots=True)
class TaskResult:
    """Result of a finished task from the FinishedTask subscription."""

    task: Task
    status: GraphQLTaskStatus
    error: dict[str, str] | None = None
    """Error payload when status is ERROR; typically has a 'code' key."""
