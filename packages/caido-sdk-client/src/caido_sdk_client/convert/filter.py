"""Conversion helpers for filter preset-related GraphQL fragments."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import FilterPresetFull
from caido_sdk_client.types import FilterPreset


def map_to_filter_preset(node: FilterPresetFull) -> FilterPreset:
    """Convert a FilterPresetFull fragment into the public FilterPreset type."""
    return FilterPreset(
        id=node.id,
        name=node.name,
        alias=node.alias,
        clause=node.clause,
    )
