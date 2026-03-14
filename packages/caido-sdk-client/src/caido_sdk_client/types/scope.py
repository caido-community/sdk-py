"""Scope-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass

from caido_sdk_client.types.strings import Id


@dataclass(frozen=True)
class Scope:
    """Scope information."""

    id: Id
    name: str
    allowlist: list[str]
    denylist: list[str]
    indexed: bool


@dataclass(frozen=True)
class CreateScopeOptions:
    """Options for creating a scope."""

    name: str
    """The name of the scope."""

    allowlist: list[str]
    """The allowlist of glob patterns."""

    denylist: list[str]
    """The denylist of glob patterns."""


@dataclass(frozen=True)
class UpdateScopeOptions:
    """Options for updating a scope."""

    name: str
    """The name of the scope."""

    allowlist: list[str]
    """The allowlist of glob patterns."""

    denylist: list[str]
    """The denylist of glob patterns."""
