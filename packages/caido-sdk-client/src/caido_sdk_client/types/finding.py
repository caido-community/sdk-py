"""Finding types (security finding attached to a request)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from caido_sdk_client.types.strings import Id


@dataclass(frozen=True, slots=True)
class Finding:
    """Security finding attached to a request."""

    id: Id
    request_id: Id
    title: str
    reporter: str
    description: str | None
    dedupe_key: str | None
    host: str
    path: str
    hidden: bool
    created_at: datetime


@dataclass(frozen=True, slots=True)
class CreateFindingOptions:
    """Options for creating a finding."""

    title: str
    reporter: str
    description: str | None = None
    dedupe_key: str | None = None


@dataclass(frozen=True, slots=True)
class UpdateFindingOptions:
    """Options for updating a finding."""

    title: str
    description: str
    hidden: bool
