"""Conversion helpers for hosted-file GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.graphql.__generated__.schema import HostedFileFull
from caido_sdk_client.types import HostedFile
from caido_sdk_client.types.strings import Id


def map_to_hosted_file(node: HostedFileFull) -> HostedFile:
    """Convert a HostedFileFull fragment into the public HostedFile type."""
    return HostedFile(
        id=Id(node.id),
        name=node.name,
        path=node.path,
        size=node.size,
        status=node.status,
        created_at=datetime.fromisoformat(node.createdAt),
        updated_at=datetime.fromisoformat(node.updatedAt),
    )
