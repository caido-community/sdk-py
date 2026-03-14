"""Types for replay entries."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from caido_sdk_client.types.network import ConnectionInfo
from caido_sdk_client.types.request import Request, Response
from caido_sdk_client.types.strings import Id


@dataclass(frozen=True, slots=True)
class ReplayEntry:
    """A replay entry (result of a replayed request)."""

    id: Id
    created_at: datetime
    error: str | None
    raw: bytes | None
    connection: ConnectionInfo
    request: Request | None
    response: Response | None
    session_id: Id
    settings: Any  # ReplayEntryFullSettings from GraphQL fragment
