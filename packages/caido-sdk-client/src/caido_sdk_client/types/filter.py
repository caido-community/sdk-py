"""Filter preset-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FilterPreset:
    """Filter preset information."""

    id: str
    name: str
    alias: str
    clause: str


@dataclass(frozen=True)
class CreateFilterPresetOptions:
    """Options for creating a filter preset."""

    name: str
    """The name of the filter preset."""

    alias: str
    """The alias of the filter preset."""

    clause: str
    """The HTTPQL clause of the filter preset."""


@dataclass(frozen=True)
class UpdateFilterPresetOptions:
    """Options for updating a filter preset."""

    name: str
    """The name of the filter preset."""

    alias: str
    """The alias of the filter preset."""

    clause: str
    """The HTTPQL clause of the filter preset."""
