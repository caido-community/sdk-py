"""Higher-level SDK for project-related operations."""

from __future__ import annotations

from typing import List, cast

from caido_sdk_client.convert import map_to_project
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateProject,
    DeleteProject,
    Projects,
    RenameProject,
    SelectProject,
    SelectProjectSelectprojectCurrentproject,
)
from caido_sdk_client.types import CreateProjectOptions, Project
from caido_sdk_client.types.strings import IdLike
from caido_sdk_client.utils.errors import handle_graphql_error


class ProjectSDK:
    """Higher-level SDK for project-related operations."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> List[Project]:
        """List all projects."""
        result = await self._graphql.query(Projects.Meta.document)
        model = Projects.model_validate(result)
        return [map_to_project(node) for node in model.projects]

    async def create(self, options: CreateProjectOptions) -> Project:
        """Create a new project."""
        result = await self._graphql.mutation(
            CreateProject.Meta.document,
            variables={
                "input": {
                    "name": options.name,
                    "temporary": options.temporary,
                },
            },
        )
        model = CreateProject.model_validate(result)
        payload = model.createProject

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.project is None:
            raise MissingExpectedValueError("createProject.project")

        return map_to_project(payload.project)

    async def delete(self, project_id: IdLike) -> None:
        """Delete a project by ID."""
        result = await self._graphql.mutation(
            DeleteProject.Meta.document,
            variables={"id": project_id},
        )
        model = DeleteProject.model_validate(result)
        payload = model.deleteProject

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

    async def rename(self, project_id: IdLike, name: str) -> Project:
        """Rename a project."""
        result = await self._graphql.mutation(
            RenameProject.Meta.document,
            variables={
                "id": project_id,
                "name": name,
            },
        )
        model = RenameProject.model_validate(result)
        payload = model.renameProject

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

        if payload.project is None:
            raise MissingExpectedValueError("renameProject.project")

        return map_to_project(payload.project)

    async def select(self, project_id: IdLike) -> Project:
        """Select a project as the current project."""
        result = await self._graphql.mutation(
            SelectProject.Meta.document,
            variables={"id": project_id},
        )
        model = SelectProject.model_validate(result)
        payload = model.selectProject

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

        current: SelectProjectSelectprojectCurrentproject | None = (
            payload.currentProject
        )
        if current is None:
            raise MissingExpectedValueError("selectProject.currentProject")

        return map_to_project(current.project)
