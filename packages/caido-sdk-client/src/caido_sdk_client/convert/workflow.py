"""Conversion helpers for workflow-related GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.graphql.__generated__.schema import WorkflowFull
from caido_sdk_client.types.strings import Id
from caido_sdk_client.types.workflow import Workflow


def map_to_workflow(node: WorkflowFull) -> Workflow:
    """Convert a WorkflowFull fragment into the public Workflow type."""
    return Workflow(
        id=Id(node.id),
        name=node.name,
        kind=node.kind,
        definition=node.definition,
        enabled=node.enabled,
        global_=node.global_,
        read_only=node.readOnly,
        created_at=datetime.fromisoformat(node.createdAt),
        updated_at=datetime.fromisoformat(node.updatedAt),
    )
