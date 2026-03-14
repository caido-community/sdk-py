"""Higher-level SDK for scope-related operations."""

from __future__ import annotations

from typing import List, cast

from caido_sdk_client.convert.scope import map_to_scope
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateScope,
    DeleteScope,
    Scopes,
    UpdateScope,
)
from caido_sdk_client.graphql.__generated__.schema import (
    Scope as ScopeQuery,
)
from caido_sdk_client.types import CreateScopeOptions, Scope, UpdateScopeOptions
from caido_sdk_client.types.strings import IdLike
from caido_sdk_client.utils.errors import handle_graphql_error


class ScopeSDK:
    """Higher-level SDK for scope-related operations."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> List[Scope]:
        """List all scopes."""
        result = await self._graphql.query(Scopes.Meta.document)
        model = Scopes.model_validate(result)
        return [map_to_scope(node) for node in model.scopes]

    async def get(self, id: IdLike) -> Scope | None:
        """Get a scope by ID."""
        result = await self._graphql.query(
            ScopeQuery.Meta.document,
            variables={"id": id},
        )
        model = ScopeQuery.model_validate(result)
        if model.scope is None:
            return None
        return map_to_scope(model.scope)

    async def create(self, options: CreateScopeOptions) -> Scope:
        """Create a new scope."""
        result = await self._graphql.mutation(
            CreateScope.Meta.document,
            variables={
                "input": {
                    "name": options.name,
                    "allowlist": options.allowlist,
                    "denylist": options.denylist,
                },
            },
        )
        model = CreateScope.model_validate(result)
        payload = model.createScope

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.scope is None:
            raise MissingExpectedValueError("createScope.scope")

        return map_to_scope(payload.scope)

    async def update(self, id: IdLike, options: UpdateScopeOptions) -> Scope:
        """Update a scope."""
        result = await self._graphql.mutation(
            UpdateScope.Meta.document,
            variables={
                "id": id,
                "input": {
                    "name": options.name,
                    "allowlist": options.allowlist,
                    "denylist": options.denylist,
                },
            },
        )
        model = UpdateScope.model_validate(result)
        payload = model.updateScope

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.scope is None:
            raise MissingExpectedValueError("updateScope.scope")

        return map_to_scope(payload.scope)

    async def delete(self, id: IdLike) -> None:
        """Delete a scope by ID."""
        result = await self._graphql.mutation(
            DeleteScope.Meta.document,
            variables={"id": id},
        )
        DeleteScope.model_validate(result)
