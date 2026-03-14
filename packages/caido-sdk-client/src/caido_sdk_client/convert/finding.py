"""Conversion helpers for finding-related GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.graphql.__generated__.schema import FindingFull
from caido_sdk_client.types.finding import Finding


def map_to_finding(node: FindingFull) -> Finding:
    """Convert a FindingFull fragment into the public Finding type."""
    return Finding(
        id=node.id,
        request_id=node.request.id,
        title=node.title,
        reporter=node.reporter,
        description=node.description,
        dedupe_key=node.dedupeKey,
        host=node.host,
        path=node.path,
        hidden=node.hidden,
        created_at=datetime.fromtimestamp(node.createdAt / 1000.0),
    )
