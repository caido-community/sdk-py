"""Project-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from caido_sdk_client.graphql.__generated__.schema import ProjectStatus
from caido_sdk_client.types.strings import Id


@dataclass(frozen=True)
class Project:
    """Project information."""

    id: Id
    name: str
    path: str
    status: ProjectStatus
    temporary: bool
    created_at: datetime
    updated_at: datetime
    version: str
    size: int
    read_only: bool


@dataclass(frozen=True)
class CreateProjectOptions:
    """Options for creating a project."""

    name: str
    temporary: bool
