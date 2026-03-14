"""Tests for the Workflow SDK."""

from __future__ import annotations

import pytest
from caido_sdk_client import Client
from caido_sdk_client.types import CreateWorkflowOptions, UpdateWorkflowOptions


@pytest.mark.usefixtures("test_project")
async def test_workflow_crud(caido: Client) -> None:
    """Perform workflow CRUD: list, create from existing, get, update, list again."""
    existing = await caido.workflow.list()
    assert len(existing) > 0, "test requires at least one existing workflow"

    source = existing[0]
    created = await caido.workflow.create(
        CreateWorkflowOptions(
            definition=source.definition,
            global_=False,
        )
    )

    fetched = await caido.workflow.get(created.id)
    assert fetched is not None
    assert fetched.id == created.id

    updated = await caido.workflow.update(
        created.id,
        UpdateWorkflowOptions(definition=created.definition),
    )
    assert updated.id == created.id

    listed = await caido.workflow.list()
    assert any(w.id == created.id for w in listed)
