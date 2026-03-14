"""Higher-level SDK for workflow-related operations."""

from __future__ import annotations

import builtins
from typing import cast

from caido_sdk_client.convert.workflow import map_to_workflow
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateWorkflow,
    DeleteWorkflow,
    UpdateWorkflow,
    Workflow,
    Workflows,
)
from caido_sdk_client.types.strings import IdLike
from caido_sdk_client.types.workflow import (
    CreateWorkflowOptions,
    UpdateWorkflowOptions,
)
from caido_sdk_client.types.workflow import (
    Workflow as WorkflowType,
)
from caido_sdk_client.utils.errors import handle_graphql_error


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
