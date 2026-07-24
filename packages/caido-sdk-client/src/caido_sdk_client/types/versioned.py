"""Version-tagged GraphQL transport values."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar


class TransportVersion(str, Enum):
    """Bundled GraphQL transport schemas."""

    V0_56 = "0.56.0"
    V0_57 = "0.57.0"


T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Versioned(Generic[T]):
    """Wire data tagged with the schema version that produced it."""

    version: TransportVersion
    data: T


def versioned(version: TransportVersion, data: T) -> Versioned[T]:
    """Tag transport data with its schema version."""
    return Versioned(version=version, data=data)
