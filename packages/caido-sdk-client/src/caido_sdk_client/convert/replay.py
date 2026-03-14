"""Conversion helpers for replay GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.convert.blob import decode_blob
from caido_sdk_client.convert.network import map_to_connection_info
from caido_sdk_client.convert.request import map_to_request, map_to_response
from caido_sdk_client.graphql.__generated__.schema import ReplayEntryFull
from caido_sdk_client.types.replay_entry import ReplayEntry
from caido_sdk_client.types.request import Request, Response
from caido_sdk_client.types.strings import Id


def map_to_replay_entry(node: ReplayEntryFull) -> ReplayEntry:
    """Convert ReplayEntryFull fragment to public ReplayEntry type."""
    raw_val = getattr(node, "raw", None)
    request = node.request
    return ReplayEntry(
        id=Id(node.id),
        created_at=datetime.fromtimestamp(node.createdAt / 1000.0),
        error=node.error,
        raw=decode_blob(raw_val) if raw_val is not None else None,
        connection=map_to_connection_info(node.connection),
        request=map_to_request(request) if request is not None else None,
        response=(
            map_to_response(request.response) if request and request.response else None
        ),
        session_id=Id(node.session.id),
        settings=node.settings,
    )
