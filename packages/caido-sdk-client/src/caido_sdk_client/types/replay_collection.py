"""Types for replay session collections."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateReplaySessionCollectionOptions:
    """Options for creating a replay session collection."""

    name: str
