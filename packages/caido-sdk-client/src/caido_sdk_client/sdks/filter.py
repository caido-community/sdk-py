"""Higher-level SDK for filter preset-related operations."""

from __future__ import annotations

from typing import List, cast

from caido_sdk_client.convert import map_to_filter_preset
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateFilterPreset,
    DeleteFilterPreset,
    FilterPreset as FilterPresetOp,
    FilterPresets,
    UpdateFilterPreset,
)
from caido_sdk_client.types import (
    CreateFilterPresetOptions,
    FilterPreset,
    UpdateFilterPresetOptions,
)
from caido_sdk_client.types.strings import IdLike
from caido_sdk_client.utils.errors import handle_graphql_error


class FilterSDK:
    """Higher-level SDK for filter preset-related operations."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> List[FilterPreset]:
        """List all filter presets."""
        result = await self._graphql.query(FilterPresets.Meta.document)
        model = FilterPresets.model_validate(result)
        return [map_to_filter_preset(node) for node in model.filterPresets]

    async def get(self, id: IdLike) -> FilterPreset | None:
        """Get a filter preset by ID."""
        result = await self._graphql.query(
            FilterPresetOp.Meta.document,
            variables={"id": id},
        )
        model = FilterPresetOp.model_validate(result)
        if model.filterPreset is None:
            return None
        return map_to_filter_preset(model.filterPreset)

    async def create(self, options: CreateFilterPresetOptions) -> FilterPreset:
        """Create a new filter preset."""
        result = await self._graphql.mutation(
            CreateFilterPreset.Meta.document,
            variables={
                "input": {
                    "name": options.name,
                    "alias": options.alias,
                    "clause": options.clause,
                },
            },
        )
        model = CreateFilterPreset.model_validate(result)
        payload = model.createFilterPreset

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.filter is None:
            raise MissingExpectedValueError("createFilterPreset.filter")

        return map_to_filter_preset(payload.filter)

    async def update(
        self,
        id: IdLike,
        options: UpdateFilterPresetOptions,
    ) -> FilterPreset:
        """Update a filter preset."""
        result = await self._graphql.mutation(
            UpdateFilterPreset.Meta.document,
            variables={
                "id": id,
                "input": {
                    "name": options.name,
                    "alias": options.alias,
                    "clause": options.clause,
                },
            },
        )
        model = UpdateFilterPreset.model_validate(result)
        payload = model.updateFilterPreset

        if (error := payload.error) is not None:
            handle_graphql_error(cast(AllErrors, error))

        if payload.filter is None:
            raise MissingExpectedValueError("updateFilterPreset.filter")

        return map_to_filter_preset(payload.filter)

    async def delete(self, id: IdLike) -> None:
        """Delete a filter preset by ID."""
        result = await self._graphql.mutation(
            DeleteFilterPreset.Meta.document,
            variables={"id": id},
        )
        DeleteFilterPreset.model_validate(result)
