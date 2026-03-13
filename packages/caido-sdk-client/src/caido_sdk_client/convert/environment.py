"""Conversion helpers for environment-related GraphQL fragments."""

from __future__ import annotations

from typing import Union

from caido_sdk_client.graphql.__generated__.schema import (
    EnvironmentFull,
    SelectEnvironmentSelectenvironmentEnvironment,
)
from caido_sdk_client.types import Environment, EnvironmentVariable


def map_to_environment(
    node: Union[EnvironmentFull, SelectEnvironmentSelectenvironmentEnvironment],
) -> Environment:
    """Convert an Environment fragment into the public Environment type."""
    return Environment(
        id=node.id,
        name=node.name,
        version=node.version,
        variables=[
            EnvironmentVariable(name=v.name, value=v.value, kind=v.kind)
            for v in node.variables
        ],
    )
