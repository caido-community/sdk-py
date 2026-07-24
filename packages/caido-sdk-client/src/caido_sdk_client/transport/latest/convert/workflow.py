"""Conversion helpers for workflow-related GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.graphql.__generated__.schema import (
    RunConvertWorkflowRunconvertworkflow,
    TestWorkflowActiveTestworkflowactive,
    TestWorkflowConvertTestworkflowconvert,
    TestWorkflowPassiveTestworkflowpassive,
    WorkflowFull,
)
from caido_sdk_client.transport.latest.convert.blob import decode_blob
from caido_sdk_client.types.strings import Id
from caido_sdk_client.types.workflow import (
    RunConvertWorkflowResult,
    TestWorkflowConvertResult,
    TestWorkflowHttpResult,
    Workflow,
)


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


def map_to_test_workflow_convert_result(
    payload: TestWorkflowConvertTestworkflowconvert,
) -> TestWorkflowConvertResult:
    """Convert a test-convert payload into its public result."""
    return TestWorkflowConvertResult(
        output=decode_blob(payload.output),
        run_state=payload.runState,
    )


def map_to_test_workflow_http_result(
    payload: TestWorkflowPassiveTestworkflowpassive
    | TestWorkflowActiveTestworkflowactive,
) -> TestWorkflowHttpResult:
    """Convert a test HTTP-workflow payload into its public result."""
    return TestWorkflowHttpResult(run_state=payload.runState)


def map_to_run_convert_workflow_result(
    payload: RunConvertWorkflowRunconvertworkflow,
) -> RunConvertWorkflowResult:
    """Convert a run-convert payload into its public result."""
    return RunConvertWorkflowResult(output=decode_blob(payload.output))
