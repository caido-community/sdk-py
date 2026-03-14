"""Conversion helpers for scope-related GraphQL fragments."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import ScopeFull
from caido_sdk_client.types import Scope
from caido_sdk_client.types.strings import Id


def map_to_scope(node: ScopeFull) -> Scope:
    """Convert a ScopeFull fragment into the public Scope type."""
    return Scope(
        id=Id(node.id),
        name=node.name,
        allowlist=node.allowlist,
        denylist=node.denylist,
        indexed=node.indexed,
    )
