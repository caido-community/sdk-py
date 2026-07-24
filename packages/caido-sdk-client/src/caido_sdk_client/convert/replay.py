"""Conversion helpers for replay GraphQL fragments."""

from __future__ import annotations

from datetime import datetime
from typing import cast

from caido_sdk_client.convert.blob import decode_blob
from caido_sdk_client.convert.network import map_to_connection_info
from caido_sdk_client.convert.request import map_to_request, map_to_response
from caido_sdk_client.graphql.__generated__.schema import (
    ConnectionInfoFull,
    ReplayEntryHttpFull,
    ReplayEntryWsFull,
    RequestFull,
)
from caido_sdk_client.transport.v0_56.__generated__.schema import (
    ReplayEntryFull as V056ReplayEntryFull,
)
from caido_sdk_client.types.replay_entry import ReplayEntry
from caido_sdk_client.types.strings import Id
from caido_sdk_client.types.versioned import Versioned

ReplayEntryFragment = ReplayEntryHttpFull | ReplayEntryWsFull | V056ReplayEntryFull


def map_to_replay_entry(fragment: Versioned[ReplayEntryFragment]) -> ReplayEntry:
    """Convert either replay transport shape to a public replay entry."""
    node = fragment.data
    session_id = node.session.id
    if isinstance(node, ReplayEntryWsFull):
        http_entry = node.http
        if http_entry is None:
            raise ValueError("SDK only supports WebSocket entries with an HTTP entry")
    else:
        http_entry = node

    raw_val = http_entry.raw
    request = cast(RequestFull | None, http_entry.request)
    return ReplayEntry(
        id=Id(http_entry.id),
        created_at=datetime.fromtimestamp(http_entry.createdAt / 1000.0),
        error=http_entry.error,
        raw=decode_blob(raw_val) if raw_val is not None else None,
        connection=map_to_connection_info(
            cast(ConnectionInfoFull, http_entry.connection)
        ),
        request=map_to_request(request) if request is not None else None,
        response=(
            map_to_response(request.response) if request and request.response else None
        ),
        session_id=Id(session_id),
        settings=getattr(http_entry, "settings", None),
    )
