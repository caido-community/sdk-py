"""SDK for replay sessions."""

from __future__ import annotations

from typing import List

from caido_sdk_client.convert.blob import encode_blob
from caido_sdk_client.convert.connection import map_to_page_info
from caido_sdk_client.convert.replay import map_to_replay_entry
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateReplaySession,
    DeleteReplaySessions,
    MoveReplaySession,
    RenameReplaySession,
    ReplaySessionEntries,
    ReplaySessionMeta,
    ReplaySessions,
    SetActiveReplaySessionEntry,
)
from caido_sdk_client.graphql.__generated__.schema import (
    ReplaySession as ReplaySessionQuery,
)
from caido_sdk_client.types.connection import ConnectionQueryResult, Edge
from caido_sdk_client.types.network import ConnectionInfoInput
from caido_sdk_client.types.replay_entry import ReplayEntry
from caido_sdk_client.types.replay_session import (
    CreateReplaySessionFromId,
    CreateReplaySessionFromRaw,
    CreateReplaySessionOptions,
)
from caido_sdk_client.types.strings import Cursor, Id, IdLike
from caido_sdk_client.utils.list import ListBuilder, ListBuilderVars


def _connection_info_to_input(connection: ConnectionInfoInput) -> dict[str, object]:
    """Convert ConnectionInfoInput to GraphQL input dict."""
    return {
        "host": connection.host,
        "port": connection.port,
        "isTLS": connection.is_tls,
        "SNI": connection.sni,
    }


class ReplaySessionsListBuilder(ListBuilder["ReplaySession", None, None]):
    """List builder for replay sessions."""

    async def _query(
        self,
        vars: ListBuilderVars[None, None],
    ) -> ConnectionQueryResult[ReplaySession]:
        raw = await self._graphql.query(
            ReplaySessions.Meta.document,
            variables={
                "first": vars.first,
                "after": vars.after,
                "last": vars.last,
                "before": vars.before,
            },
        )
        model = ReplaySessions.model_validate(raw)
        conn = model.replaySessions
        page_info = map_to_page_info(conn.pageInfo)
        edges = [
            Edge(
                cursor=Cursor(e.cursor),
                node=ReplaySession(self._graphql, e.node),
            )
            for e in conn.edges
        ]
        return ConnectionQueryResult(page_info=page_info, edges=edges)


class ReplaySessionEntriesListBuilder(ListBuilder[ReplayEntry, None, None]):
    """List builder for replay session entries."""

    def __init__(self, graphql: GraphQLClient, session_id: IdLike) -> None:
        super().__init__(graphql)
        self._session_id = str(session_id)
        self._include_replay_raw = True
        self._include_request_raw = True
        self._include_response_raw = True

    def include_raw(
        self,
        options: bool | dict[str, bool] | None = None,
    ) -> ReplaySessionEntriesListBuilder:
        """Include raw bodies. Default all True. Pass False or dict with replay/request/response keys."""
        if options is None:
            return self
        if isinstance(options, bool):
            self._include_replay_raw = options
            self._include_request_raw = options
            self._include_response_raw = options
        else:
            self._include_replay_raw = options.get("replay", True)
            self._include_request_raw = options.get("request", True)
            self._include_response_raw = options.get("response", True)
        return self

    async def _query(
        self,
        vars: ListBuilderVars[None, None],
    ) -> ConnectionQueryResult[ReplayEntry]:
        raw = await self._graphql.query(
            ReplaySessionEntries.Meta.document,
            variables={
                "id": self._session_id,
                "first": vars.first,
                "after": vars.after,
                "last": vars.last,
                "before": vars.before,
                "includeReplayRaw": self._include_replay_raw,
                "includeRequestRaw": self._include_request_raw,
                "includeResponseRaw": self._include_response_raw,
            },
        )
        model = ReplaySessionEntries.model_validate(raw)
        if model.replaySession is None:
            from caido_sdk_client.types.connection import PageInfo

            return ConnectionQueryResult(
                page_info=PageInfo(
                    has_next_page=False,
                    has_previous_page=False,
                    start_cursor=None,
                    end_cursor=None,
                ),
                edges=[],
            )
        conn = model.replaySession.entries
        page_info = map_to_page_info(conn.pageInfo)
        edges = [
            Edge(
                cursor=Cursor(e.cursor),
                node=map_to_replay_entry(e.node),
            )
            for e in conn.edges
        ]
        return ConnectionQueryResult(page_info=page_info, edges=edges)


class ReplaySession:
    """Replay session."""

    def __init__(self, graphql: GraphQLClient, data: ReplaySessionMeta) -> None:
        self._graphql = graphql
        self.id: Id = Id(data.id)
        self.name: str = data.name
        self.collection_id: Id = Id(data.collection.id)
        self.active_entry_id: Id | None = (
            Id(data.activeEntry.id) if data.activeEntry is not None else None
        )

    def entries(self) -> ReplaySessionEntriesListBuilder:
        """Return a list builder for this session's entries."""
        return ReplaySessionEntriesListBuilder(self._graphql, self.id)

    async def set_active_entry(self, entry_id: IdLike) -> ReplaySession:
        """Set the active entry for this session."""
        raw = await self._graphql.mutation(
            SetActiveReplaySessionEntry.Meta.document,
            variables={"id": str(self.id), "entryId": str(entry_id)},
        )
        model = SetActiveReplaySessionEntry.model_validate(raw)
        payload = model.setActiveReplaySessionEntry
        if payload.session is None:
            return self
        return ReplaySession(self._graphql, payload.session)


class ReplaySessionSDK:
    """SDK for replay sessions."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    def list(self) -> ReplaySessionsListBuilder:
        """List replay sessions. Chain with .first(50) then await."""
        return ReplaySessionsListBuilder(self._graphql)

    async def get(self, id: IdLike) -> ReplaySession | None:
        """Get a replay session by ID. Returns None if it does not exist."""
        raw = await self._graphql.query(
            ReplaySessionQuery.Meta.document,
            variables={"id": str(id)},
        )
        model = ReplaySessionQuery.model_validate(raw)
        if model.replaySession is None:
            return None
        return ReplaySession(self._graphql, model.replaySession)

    async def create(
        self,
        options: CreateReplaySessionOptions | None = None,
    ) -> ReplaySession:
        """Create a new replay session."""
        opts = options or CreateReplaySessionOptions()
        input: dict[str, object] = {}
        if opts.collection_id is not None:
            input["collectionId"] = str(opts.collection_id)
        if opts.request_source is not None:
            src = opts.request_source
            if isinstance(src, CreateReplaySessionFromId):
                input["requestSource"] = {"id": str(src.id)}
            else:
                assert isinstance(src, CreateReplaySessionFromRaw)
                raw_b64 = encode_blob(src.raw)
                input["requestSource"] = {
                    "raw": {
                        "connectionInfo": _connection_info_to_input(src.connection),
                        "raw": raw_b64,
                    },
                }
        raw = await self._graphql.mutation(
            CreateReplaySession.Meta.document,
            variables={"input": input},
        )
        model = CreateReplaySession.model_validate(raw)
        payload = model.createReplaySession
        if payload.session is None:
            raise MissingExpectedValueError("createReplaySession.session")
        return ReplaySession(self._graphql, payload.session)

    async def delete(self, ids: List[IdLike]) -> None:
        """Delete replay sessions by ID."""
        await self._graphql.mutation(
            DeleteReplaySessions.Meta.document,
            variables={"ids": [str(i) for i in ids]},
        )

    async def move(self, id: IdLike, collection_id: IdLike) -> ReplaySession:
        """Move a replay session to a new collection."""
        raw = await self._graphql.mutation(
            MoveReplaySession.Meta.document,
            variables={"id": str(id), "collectionId": str(collection_id)},
        )
        model = MoveReplaySession.model_validate(raw)
        payload = model.moveReplaySession
        if payload.session is None:
            raise MissingExpectedValueError("moveReplaySession.session")
        return ReplaySession(self._graphql, payload.session)

    async def rename(self, id: IdLike, name: str) -> ReplaySession:
        """Rename a replay session."""
        raw = await self._graphql.mutation(
            RenameReplaySession.Meta.document,
            variables={"id": str(id), "name": name},
        )
        model = RenameReplaySession.model_validate(raw)
        payload = model.renameReplaySession
        if payload.session is None:
            raise MissingExpectedValueError("renameReplaySession.session")
        return ReplaySession(self._graphql, payload.session)

    async def set_active_entry(self, session_id: IdLike, entry_id: IdLike) -> None:
        """Set the active entry for a replay session."""
        await self._graphql.mutation(
            SetActiveReplaySessionEntry.Meta.document,
            variables={"id": str(session_id), "entryId": str(entry_id)},
        )
