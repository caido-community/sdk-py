"""SDK for replay entries."""

from __future__ import annotations

from datetime import datetime
from typing import Any, cast

from caido_sdk_client.convert.blob import decode_blob
from caido_sdk_client.convert.network import map_to_connection_info
from caido_sdk_client.convert.request import map_to_request, map_to_response
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    ConnectionInfoFull,
    ReplayEntryHttpFull,
    ReplayEntryWsFull,
    RequestFull,
)
from caido_sdk_client.graphql.__generated__.schema import (
    ReplayEntry as LatestReplayEntry,
)
from caido_sdk_client.transport.v0_56.__generated__.schema import (
    ReplayEntry as V056ReplayEntry,
)
from caido_sdk_client.transport.v0_56.__generated__.schema import (
    ReplayEntryFull as V056ReplayEntryFull,
)
from caido_sdk_client.types.network import ConnectionInfo
from caido_sdk_client.types.request import Request, Response
from caido_sdk_client.types.strings import Id, IdLike
from caido_sdk_client.types.versioned import TransportVersion, Versioned, versioned
from caido_sdk_client.version import Version

LatestReplayEntryFragment = ReplayEntryHttpFull | ReplayEntryWsFull
ReplayEntryVersionedFragment = Versioned[
    LatestReplayEntryFragment | V056ReplayEntryFull
]


class ReplayEntrySDK:
    """SDK for replay entries."""

    def __init__(self, graphql: GraphQLClient, version: Version | None = None) -> None:
        self._graphql = graphql
        self._version = version or Version.of(TransportVersion.V0_57.value)

    async def get(self, id: IdLike) -> ReplayEntry | None:
        """Get a replay entry by ID. Returns None if it does not exist."""
        variables = {
            "id": str(id),
            "includeReplayRaw": True,
            "includeRequestRaw": True,
            "includeResponseRaw": True,
        }
        if await self._version.gte(TransportVersion.V0_57.value):
            variables["sessionKind"] = "HTTP"
            raw = await self._graphql.query(
                LatestReplayEntry.Meta.document, variables=variables
            )
            model = LatestReplayEntry.model_validate(raw)
            entry = model.replayEntry
            if entry is None:
                return None
            if not isinstance(entry, (ReplayEntryHttpFull, ReplayEntryWsFull)):
                raise ValueError(f"Unsupported replay entry type: {entry.typename}")
            return ReplayEntry(
                self._graphql,
                versioned(TransportVersion.V0_57, entry),
            )

        raw = await self._graphql.query(
            V056ReplayEntry.Meta.document, variables=variables
        )
        model = V056ReplayEntry.model_validate(raw)
        if model.replayEntry is None:
            return None
        return ReplayEntry(
            self._graphql,
            versioned(TransportVersion.V0_56, model.replayEntry),
        )


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
    settings: Any

    def __init__(
        self, graphql: GraphQLClient, fragment: ReplayEntryVersionedFragment
    ) -> None:
        self._graphql = graphql

        match fragment.version:
            case TransportVersion.V0_57:
                data = cast(LatestReplayEntryFragment, fragment.data)
                http = data.http if isinstance(data, ReplayEntryWsFull) else data
                self.id = Id(http.id)
                self.created_at = datetime.fromtimestamp(http.createdAt / 1000.0)
                self.error = http.error
                self.raw = decode_blob(http.raw)
                self.connection = map_to_connection_info(http.connection)
                request = http.request
                self.request = map_to_request(request) if request is not None else None
                self.response = (
                    map_to_response(request.response)
                    if request is not None and request.response is not None
                    else None
                )
                self.session_id = Id(data.session.id)
                self.settings = http.settings
            case TransportVersion.V0_56:
                data = cast(V056ReplayEntryFull, fragment.data)
                self.id = Id(data.id)
                self.created_at = datetime.fromtimestamp(data.createdAt / 1000.0)
                self.error = data.error
                self.raw = decode_blob(data.raw)
                self.connection = map_to_connection_info(
                    cast(ConnectionInfoFull, data.connection)
                )
                request = cast(RequestFull | None, data.request)
                self.request = map_to_request(request) if request is not None else None
                self.response = (
                    map_to_response(request.response)
                    if request is not None and request.response is not None
                    else None
                )
                self.session_id = Id(data.session.id)
                self.settings = data.settings
