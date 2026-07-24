"""Conversion helpers for filter preset-related GraphQL fragments."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import FilterPresetFull
from caido_sdk_client.types.filter import FilterClauseKind, FilterPreset
from caido_sdk_client.types.strings import Id


def map_to_filter_preset(node: FilterPresetFull) -> FilterPreset:
    """Convert a FilterPresetFull fragment into the public FilterPreset type."""
    c = node.clause
    return FilterPreset(
        id=Id(node.id),
        name=node.name,
        alias=node.alias,
        clause=c.code,
        kind=FilterClauseKind(c.typename),
    )
