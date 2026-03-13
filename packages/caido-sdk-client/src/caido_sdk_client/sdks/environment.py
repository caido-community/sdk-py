"""Higher-level SDK for environment-related operations."""

from __future__ import annotations

from typing import List, Optional, cast

from caido_sdk_client.convert.environment import map_to_environment
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateEnvironment,
    DeleteEnvironment,
    EnvironmentQuery,
    Environments,
    EnvironmentVariableKind,
    SelectEnvironment,
    UpdateEnvironment,
)
from caido_sdk_client.types import (
    CreateEnvironmentOptions,
    Environment,
    EnvironmentVariable,
    UpdateEnvironmentOptions,
)
from caido_sdk_client.utils.errors import handle_graphql_error


class EnvironmentSDK:
    """Higher-level SDK for environment-related operations."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> List[Environment]:
        """List all environments."""
        result = await self._graphql.query(Environments.Meta.document)
        model = Environments.model_validate(result)
        return [map_to_environment(node) for node in model.environments]

    async def get(self, id: str) -> Optional["EnvironmentInstance"]:
        """Get an environment by ID.

        Returns an EnvironmentInstance for managing variables, or None if not found.
        """
        result = await self._graphql.query(
            EnvironmentQuery.Meta.document,
            variables={"id": id},
        )
        model = EnvironmentQuery.model_validate(result)
        if model.environment is None:
            return None
        return EnvironmentInstance(
            self._graphql,
            map_to_environment(model.environment),
        )

    async def create(self, options: CreateEnvironmentOptions) -> "EnvironmentInstance":
        """Create a new environment.

        Returns an EnvironmentInstance for managing variables.
        """
        result = await self._graphql.mutation(
            CreateEnvironment.Meta.document,
            variables={
                "input": {
                    "name": options.name,
                    "variables": [
                        {"name": v.name, "value": v.value, "kind": v.kind}
                        for v in options.variables
                    ],
                },
            },
        )
        model = CreateEnvironment.model_validate(result)
        payload = model.createEnvironment

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.environment is None:
            raise MissingExpectedValueError("createEnvironment.environment")

        return EnvironmentInstance(
            self._graphql,
            map_to_environment(payload.environment),
        )

    async def update(
        self,
        id: str,
        options: UpdateEnvironmentOptions,
        *,
        version: int,
    ) -> "EnvironmentInstance":
        """Update an environment.

        Returns an EnvironmentInstance for managing variables.
        """
        result = await self._graphql.mutation(
            UpdateEnvironment.Meta.document,
            variables={
                "id": id,
                "input": {
                    "name": options.name,
                    "variables": [
                        {"name": v.name, "value": v.value, "kind": v.kind}
                        for v in options.variables
                    ],
                    "version": version,
                },
            },
        )
        model = UpdateEnvironment.model_validate(result)
        payload = model.updateEnvironment

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.environment is None:
            raise MissingExpectedValueError("updateEnvironment.environment")

        return EnvironmentInstance(
            self._graphql,
            map_to_environment(payload.environment),
        )

    async def delete(self, id: str) -> None:
        """Delete an environment by ID."""
        result = await self._graphql.mutation(
            DeleteEnvironment.Meta.document,
            variables={"id": id},
        )
        model = DeleteEnvironment.model_validate(result)
        payload = model.deleteEnvironment

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

    async def select(self, id: Optional[str] = None) -> Optional["EnvironmentInstance"]:
        """Select an environment as the current environment.

        Pass None to deselect the current environment.
        """
        result = await self._graphql.mutation(
            SelectEnvironment.Meta.document,
            variables={"id": id},
        )
        model = SelectEnvironment.model_validate(result)
        payload = model.selectEnvironment

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

        if payload.environment is None:
            return None

        return EnvironmentInstance(
            self._graphql,
            map_to_environment(payload.environment),
        )


class EnvironmentInstance:
    """An environment instance that provides methods for managing variables.

    Similar to PluginPackage, this class holds state and provides
    higher-level methods for variable manipulation on a specific environment.
    """

    def __init__(self, graphql: GraphQLClient, environment: Environment) -> None:
        self._graphql = graphql
        self._state = environment

    @property
    def id(self) -> str:
        """The environment ID."""
        return self._state.id

    @property
    def name(self) -> str:
        """The environment name."""
        return self._state.name

    @property
    def version(self) -> int:
        """The environment version (for optimistic concurrency)."""
        return self._state.version

    @property
    def variables(self) -> List[EnvironmentVariable]:
        """The environment variables."""
        return list(self._state.variables)

    async def add_variable(self, variable: EnvironmentVariable) -> None:
        """Add a variable to the environment."""
        new_variables = [*self._state.variables, variable]
        await self._perform_update(
            UpdateEnvironmentOptions(
                name=self._state.name,
                variables=new_variables,
            )
        )

    async def delete_variable(self, name: str) -> None:
        """Delete a variable from the environment by name."""
        new_variables = [v for v in self._state.variables if v.name != name]
        await self._perform_update(
            UpdateEnvironmentOptions(
                name=self._state.name,
                variables=new_variables,
            )
        )

    async def update_variable(
        self,
        name: str,
        *,
        value: Optional[str] = None,
        kind: Optional[EnvironmentVariableKind] = None,
    ) -> None:
        """Update a variable in the environment by name."""
        new_variables: List[EnvironmentVariable] = []
        for v in self._state.variables:
            if v.name == name:
                new_variables.append(
                    EnvironmentVariable(
                        name=v.name,
                        value=value if value is not None else v.value,
                        kind=kind if kind is not None else v.kind,
                    )
                )
            else:
                new_variables.append(v)
        await self._perform_update(
            UpdateEnvironmentOptions(
                name=self._state.name,
                variables=new_variables,
            )
        )

    async def _perform_update(self, options: UpdateEnvironmentOptions) -> None:
        result = await self._graphql.mutation(
            UpdateEnvironment.Meta.document,
            variables={
                "id": self._state.id,
                "input": {
                    "name": options.name,
                    "variables": [
                        {"name": v.name, "value": v.value, "kind": v.kind}
                        for v in options.variables
                    ],
                    "version": self._state.version,
                },
            },
        )
        model = UpdateEnvironment.model_validate(result)
        payload = model.updateEnvironment

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.environment is None:
            raise MissingExpectedValueError("updateEnvironment.environment")

        self._state = map_to_environment(payload.environment)
