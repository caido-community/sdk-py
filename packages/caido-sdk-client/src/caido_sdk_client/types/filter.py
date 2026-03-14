"""Filter preset-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass

from caido_sdk_client.types.strings import Httpql, HttpqlLike, Id


@dataclass(frozen=True)
class FilterPreset:
    """Filter preset information."""

    id: Id
    name: str
    alias: str
    clause: Httpql


@dataclass(frozen=True)
class CreateFilterPresetOptions:
    """Options for creating a filter preset."""

    name: str
    """The name of the filter preset."""

    alias: str
    """The alias of the filter preset."""

    clause: HttpqlLike
    """The HTTPQL clause of the filter preset (accepts str or Httpql)."""


@dataclass(frozen=True)
class UpdateFilterPresetOptions:
    """Options for updating a filter preset."""

    name: str
    """The name of the filter preset."""

    alias: str
    """The alias of the filter preset."""

    clause: HttpqlLike
    """The HTTPQL clause of the filter preset (accepts str or Httpql)."""
