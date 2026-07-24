"""Higher-level SDK for workflow-related operations."""

from __future__ import annotations

import builtins
from typing import cast, overload

from caido_sdk_client.convert.blob import encode_blob
from caido_sdk_client.convert.workflow import (
    map_to_run_convert_workflow_result,
    map_to_test_workflow_convert_result,
    map_to_test_workflow_http_result,
    map_to_workflow,
)
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.misc import OtherUserError
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateWorkflow,
    DeleteWorkflow,
    RunActiveWorkflow,
    RunConvertWorkflow,
    TestWorkflowActive,
    TestWorkflowConvert,
    TestWorkflowPassive,
    ToggleWorkflow,
    UpdateWorkflow,
    Workflow,
    Workflows,
)
from caido_sdk_client.sdks.task import WorkflowTask
from caido_sdk_client.types.strings import IdLike
from caido_sdk_client.types.workflow import (
    CreateWorkflowOptions,
    RunActiveWorkflowOptions,
    RunConvertWorkflowOptions,
    RunConvertWorkflowResult,
    TestWorkflowActiveOptions,
    TestWorkflowConvertOptions,
    TestWorkflowConvertResult,
    TestWorkflowHttpResult,
    TestWorkflowPassiveOptions,
    UpdateWorkflowOptions,
)
from caido_sdk_client.types.workflow import (
    Workflow as WorkflowType,
)
from caido_sdk_client.utils.errors import handle_graphql_error


def _build_test_workflow_http_input(
    options: TestWorkflowPassiveOptions | TestWorkflowActiveOptions,
) -> dict[str, object]:
    connection = options.request.connection
    input_: dict[str, object] = {
        "definition": options.definition,
        "request": {
            "connectionInfo": {
                "host": connection.host,
                "port": connection.port,
                "isTLS": connection.is_tls,
                "SNI": connection.sni,
            },
            "raw": encode_blob(options.request.raw),
        },
    }
    if options.response is not None:
        input_["response"] = {"raw": encode_blob(options.response.raw)}
    return input_


class WorkflowSDK:
    """Higher-level SDK for workflow-related operations."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> builtins.list[WorkflowType]:
        """List all workflows."""
        result = await self._graphql.query(Workflows.Meta.document)
        model = Workflows.model_validate(result)
        return [map_to_workflow(node) for node in model.workflows]

    async def get(self, id: IdLike) -> WorkflowType | None:
        """Get a workflow by ID."""
        result = await self._graphql.query(
            Workflow.Meta.document,
            variables={"id": str(id)},
        )
        model = Workflow.model_validate(result)
        if model.workflow is None:
            return None
        return map_to_workflow(model.workflow)

    async def create(self, options: CreateWorkflowOptions) -> WorkflowType:
        """Create a new workflow."""
        result = await self._graphql.mutation(
            CreateWorkflow.Meta.document,
            variables={
                "input": {
                    "definition": options.definition,
                    "global": options.global_,
                },
            },
        )
        model = CreateWorkflow.model_validate(result)
        payload = model.createWorkflow

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.workflow is None:
            raise MissingExpectedValueError("createWorkflow.workflow")

        return map_to_workflow(payload.workflow)

    async def update(
        self,
        id: IdLike,
        options: UpdateWorkflowOptions,
    ) -> WorkflowType:
        """Update a workflow."""
        result = await self._graphql.mutation(
            UpdateWorkflow.Meta.document,
            variables={
                "id": str(id),
                "input": {"definition": options.definition},
            },
        )
        model = UpdateWorkflow.model_validate(result)
        payload = model.updateWorkflow

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.workflow is None:
            raise MissingExpectedValueError("updateWorkflow.workflow")

        return map_to_workflow(payload.workflow)

    async def delete(self, id: IdLike) -> None:
        """Delete a workflow by ID."""
        result = await self._graphql.mutation(
            DeleteWorkflow.Meta.document,
            variables={"id": str(id)},
        )
        model = DeleteWorkflow.model_validate(result)
        payload = model.deleteWorkflow

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

    async def toggle(self, id: IdLike, enabled: bool) -> WorkflowType:
        """Toggle a workflow's enabled state."""
        result = await self._graphql.mutation(
            ToggleWorkflow.Meta.document,
            variables={"id": str(id), "enabled": enabled},
        )
        model = ToggleWorkflow.model_validate(result)
        payload = model.toggleWorkflow

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.workflow is None:
            raise MissingExpectedValueError("toggleWorkflow.workflow")

        return map_to_workflow(payload.workflow)

    @overload
    async def test(
        self,
        options: TestWorkflowConvertOptions,
    ) -> TestWorkflowConvertResult: ...

    @overload
    async def test(
        self,
        options: TestWorkflowPassiveOptions,
    ) -> TestWorkflowHttpResult: ...

    @overload
    async def test(
        self,
        options: TestWorkflowActiveOptions,
    ) -> TestWorkflowHttpResult: ...

    async def test(
        self,
        options: TestWorkflowConvertOptions
        | TestWorkflowPassiveOptions
        | TestWorkflowActiveOptions,
    ) -> TestWorkflowConvertResult | TestWorkflowHttpResult:
        """Test a workflow against input without saving it."""
        if isinstance(options, TestWorkflowConvertOptions):
            result = await self._graphql.mutation(
                TestWorkflowConvert.Meta.document,
                variables={
                    "input": {
                        "definition": options.definition,
                        "data": encode_blob(options.data),
                    }
                },
            )
            model = TestWorkflowConvert.model_validate(result)
            payload = model.testWorkflowConvert
            if (error := payload.error) is not None:
                handle_graphql_error(cast(AllErrors, error))
            return map_to_test_workflow_convert_result(payload)

        if isinstance(options, TestWorkflowPassiveOptions):
            result = await self._graphql.mutation(
                TestWorkflowPassive.Meta.document,
                variables={"input": _build_test_workflow_http_input(options)},
            )
            model = TestWorkflowPassive.model_validate(result)
            payload = model.testWorkflowPassive
            if (error := payload.error) is not None:
                handle_graphql_error(cast(AllErrors, error))
            return map_to_test_workflow_http_result(payload)

        if isinstance(options, TestWorkflowActiveOptions):
            result = await self._graphql.mutation(
                TestWorkflowActive.Meta.document,
                variables={"input": _build_test_workflow_http_input(options)},
            )
            model = TestWorkflowActive.model_validate(result)
            payload = model.testWorkflowActive
            if (error := payload.error) is not None:
                handle_graphql_error(cast(AllErrors, error))
            return map_to_test_workflow_http_result(payload)

        raise OtherUserError("INTERNAL", "Unhandled workflow kind")

    @overload
    async def run(
        self,
        options: RunConvertWorkflowOptions,
    ) -> RunConvertWorkflowResult: ...

    @overload
    async def run(self, options: RunActiveWorkflowOptions) -> WorkflowTask: ...

    async def run(
        self,
        options: RunConvertWorkflowOptions | RunActiveWorkflowOptions,
    ) -> RunConvertWorkflowResult | WorkflowTask:
        """Run a workflow."""
        if isinstance(options, RunConvertWorkflowOptions):
            result = await self._graphql.mutation(
                RunConvertWorkflow.Meta.document,
                variables={
                    "id": str(options.id),
                    "input": encode_blob(options.data),
                },
            )
            model = RunConvertWorkflow.model_validate(result)
            payload = model.runConvertWorkflow
            if (error := payload.error) is not None:
                handle_graphql_error(cast(AllErrors, error))
            return map_to_run_convert_workflow_result(payload)

        if isinstance(options, RunActiveWorkflowOptions):
            result = await self._graphql.mutation(
                RunActiveWorkflow.Meta.document,
                variables={
                    "id": str(options.id),
                    "input": {"requestId": str(options.request_id)},
                },
            )
            model = RunActiveWorkflow.model_validate(result)
            payload = model.runActiveWorkflow
            if (error := payload.error) is not None:
                handle_graphql_error(cast(AllErrors, error))
            if payload.task is None:
                raise MissingExpectedValueError("runActiveWorkflow.task")
            return WorkflowTask(self._graphql, payload.task)

        raise OtherUserError("INTERNAL", "Unhandled workflow kind")
