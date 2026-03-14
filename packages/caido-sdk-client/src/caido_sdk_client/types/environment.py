"""Environment-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass

from caido_sdk_client.graphql.__generated__.schema import EnvironmentVariableKind
from caido_sdk_client.types.strings import Id

__all__ = [
    "Environment",
    "EnvironmentVariable",
    "EnvironmentVariableKind",
    "CreateEnvironmentOptions",
    "UpdateEnvironmentOptions",
]


@dataclass(frozen=True)
class EnvironmentVariable:
    """Environment variable information."""

    name: str
    value: str
    kind: EnvironmentVariableKind


@dataclass(frozen=True)
class Environment:
    """Environment information."""

    id: Id
    name: str
    version: int
    variables: list[EnvironmentVariable]


@dataclass(frozen=True)
class CreateEnvironmentOptions:
    """Options for creating an environment."""

    name: str
    """The name of the environment."""
    variables: list[EnvironmentVariable]
    """The initial variables for the environment."""


@dataclass(frozen=True)
class UpdateEnvironmentOptions:
    """Options for updating an environment."""

    name: str
    """The name of the environment."""
    variables: list[EnvironmentVariable]
    """The variables for the environment."""
