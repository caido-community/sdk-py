"""Conversion helpers for project-related GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.graphql.__generated__.schema import ProjectFull
from caido_sdk_client.types import Project
from caido_sdk_client.types.strings import Id


def map_to_project(node: ProjectFull) -> Project:
    """Convert a ProjectFull fragment into the public Project type."""
    return Project(
        id=Id(node.id),
        name=node.name,
        path=node.path,
        status=node.status,
        temporary=node.temporary,
        created_at=datetime.fromisoformat(node.createdAt),
        updated_at=datetime.fromisoformat(node.updatedAt),
        version=node.version,
        size=node.size,
        read_only=node.readOnly,
    )
