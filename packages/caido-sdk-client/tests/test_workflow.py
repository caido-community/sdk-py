"""Tests for the Workflow SDK."""

from __future__ import annotations

import json
from typing import Any

import pytest
from caido_sdk_client import Client
from caido_sdk_client.types import (
    ConnectionInfoInput,
    CreateWorkflowOptions,
    RunActiveWorkflowOptions,
    RunConvertWorkflowOptions,
    TestWorkflowActiveOptions,
    TestWorkflowConvertOptions,
    TestWorkflowPassiveOptions,
    TestWorkflowRequest,
    TestWorkflowResponse,
    UpdateWorkflowOptions,
)

from tests.utils import create_mock_request

CONVERT_HEX_ENCODE_DEFINITION: dict[str, Any] = {
    "edition": 2,
    "id": "convert-1",
    "name": "Convert 1",
    "description": "",
    "kind": "convert",
    "graph": {
        "nodes": [
            {
                "id": 1,
                "alias": "convert_start_1",
                "name": "Convert Start",
                "definition_id": "caido/convert-start",
                "version": "*",
                "inputs": [],
                "display": None,
            },
            {
                "id": 2,
                "alias": "hex_encode_2",
                "name": "Hex Encode",
                "definition_id": "caido/hex-encode",
                "version": "*",
                "inputs": [
                    {"alias": "delimiter", "value": {"kind": "string", "data": ","}},
                    {"alias": "format", "value": {"kind": "string", "data": "UPPER"}},
                    {"alias": "prefix", "value": {"kind": "string", "data": "0x"}},
                    {
                        "alias": "data",
                        "value": {
                            "kind": "ref",
                            "data": "$convert_start_1.data",
                        },
                    },
                ],
                "display": None,
            },
            {
                "id": 3,
                "alias": "convert_end_3",
                "name": "Convert End",
                "definition_id": "caido/convert-end",
                "version": "*",
                "inputs": [
                    {
                        "alias": "data",
                        "value": {"kind": "ref", "data": "$hex_encode_2.data"},
                    },
                ],
                "display": None,
            },
        ],
        "edges": [
            {
                "source": {"node_id": 1, "exec_alias": "exec"},
                "target": {"node_id": 2, "exec_alias": "exec"},
            },
            {
                "source": {"node_id": 2, "exec_alias": "exec"},
                "target": {"node_id": 3, "exec_alias": "exec"},
            },
        ],
    },
}

PASSIVE_SET_COLOR_DEFINITION: dict[str, Any] = {
    "edition": 2,
    "id": "passive-1",
    "name": "Passive 1",
    "description": "",
    "kind": "passive",
    "graph": {
        "nodes": [
            {
                "id": 1,
                "alias": "on_intercept_request",
                "name": "On Intercept Request",
                "definition_id": "caido/on-intercept-request",
                "version": "*",
                "inputs": [],
                "display": None,
            },
            {
                "id": 2,
                "alias": "set_color",
                "name": "Set Color",
                "definition_id": "caido/color-set",
                "version": "*",
                "inputs": [
                    {"alias": "color", "value": {"kind": "string", "data": "red"}},
                    {
                        "alias": "request",
                        "value": {
                            "kind": "ref",
                            "data": "$on_intercept_request.request",
                        },
                    },
                ],
                "display": None,
            },
        ],
        "edges": [
            {
                "source": {"node_id": 1, "exec_alias": "exec"},
                "target": {"node_id": 2, "exec_alias": "exec"},
            },
        ],
    },
}

ACTIVE_SET_COLOR_DEFINITION: dict[str, Any] = {
    "edition": 2,
    "id": "active-1",
    "name": "Active 1",
    "description": "",
    "kind": "active",
    "graph": {
        "nodes": [
            {
                "id": 1,
                "alias": "active_start",
                "name": "Active Start",
                "definition_id": "caido/active-start",
                "version": "*",
                "inputs": [],
                "display": None,
            },
            {
                "id": 2,
                "alias": "set_color",
                "name": "Set Color",
                "definition_id": "caido/color-set",
                "version": "*",
                "inputs": [
                    {"alias": "color", "value": {"kind": "string", "data": "red"}},
                    {
                        "alias": "request",
                        "value": {
                            "kind": "ref",
                            "data": "$active_start.request",
                        },
                    },
                ],
                "display": None,
            },
        ],
        "edges": [
            {
                "source": {"node_id": 1, "exec_alias": "exec"},
                "target": {"node_id": 2, "exec_alias": "exec"},
            },
        ],
    },
}

TEST_CONNECTION = ConnectionInfoInput(
    host="localhost",
    port=5956,
    is_tls=False,
)

TEST_REQUEST_RAW = "GET /health/other HTTP/1.1\r\nHost: localhost:5956\r\n\r\n"

TEST_RESPONSE_RAW = "HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"


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


@pytest.mark.usefixtures("test_project")
async def test_convert_workflow_against_input_data(caido: Client) -> None:
    """Test a convert workflow against input data."""
    result = await caido.workflow.test(
        TestWorkflowConvertOptions(
            kind="convert",
            definition=CONVERT_HEX_ENCODE_DEFINITION,
            data="TEST",
        )
    )

    assert result.output is not None
    assert result.output.decode() == "0x54,0x45,0x53,0x54"


@pytest.mark.usefixtures("test_project")
async def test_passive_workflow_against_request(caido: Client) -> None:
    """Test a passive workflow against a request."""
    result = await caido.workflow.test(
        TestWorkflowPassiveOptions(
            kind="passive",
            definition=PASSIVE_SET_COLOR_DEFINITION,
            request=TestWorkflowRequest(
                connection=TEST_CONNECTION,
                raw=TEST_REQUEST_RAW,
            ),
        )
    )

    assert result.run_state is not None
    assert "set_color" in json.dumps(result.run_state)


@pytest.mark.usefixtures("test_project")
async def test_active_workflow_against_request_and_response(caido: Client) -> None:
    """Test an active workflow against a request and response."""
    result = await caido.workflow.test(
        TestWorkflowActiveOptions(
            kind="active",
            definition=ACTIVE_SET_COLOR_DEFINITION,
            request=TestWorkflowRequest(
                connection=TEST_CONNECTION,
                raw=TEST_REQUEST_RAW,
            ),
            response=TestWorkflowResponse(raw=TEST_RESPONSE_RAW),
        )
    )

    assert result.run_state is not None
    assert "set_color" in json.dumps(result.run_state)


@pytest.mark.usefixtures("test_project")
async def test_toggle_workflow_enabled_state(caido: Client) -> None:
    """Toggle a workflow's enabled state."""
    existing = await caido.workflow.list()
    assert len(existing) > 0, "test requires at least one existing workflow"

    created = await caido.workflow.create(
        CreateWorkflowOptions(
            definition=existing[0].definition,
            global_=False,
        )
    )

    disabled = await caido.workflow.toggle(created.id, False)
    assert disabled.enabled is False

    enabled = await caido.workflow.toggle(created.id, True)
    assert enabled.enabled is True


@pytest.mark.usefixtures("test_project")
async def test_run_convert_workflow_against_input_data(caido: Client) -> None:
    """Run a convert workflow against input data."""
    created = await caido.workflow.create(
        CreateWorkflowOptions(
            definition=CONVERT_HEX_ENCODE_DEFINITION,
            global_=False,
        )
    )

    result = await caido.workflow.run(
        RunConvertWorkflowOptions(
            kind="convert",
            id=created.id,
            data="TEST",
        )
    )

    assert result.output is not None
    assert result.output.decode() == "0x54,0x45,0x53,0x54"


@pytest.mark.usefixtures("test_project")
async def test_run_active_workflow_against_request(caido: Client) -> None:
    """Run an active workflow against a request."""
    await create_mock_request()
    requests = await caido.request.list().first(1).descending("req", "created_at")
    assert len(requests.edges) > 0
    request_id = requests.edges[0].node.request.id

    created = await caido.workflow.create(
        CreateWorkflowOptions(
            definition=ACTIVE_SET_COLOR_DEFINITION,
            global_=False,
        )
    )

    task = await caido.workflow.run(
        RunActiveWorkflowOptions(
            kind="active",
            id=created.id,
            request_id=request_id,
        )
    )
    assert task.id is not None
