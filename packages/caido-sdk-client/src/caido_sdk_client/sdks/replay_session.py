"""SDK for replay sessions across bundled transport schemas."""

from __future__ import annotations

import builtins
from typing import cast

from caido_sdk_client.convert.blob import encode_blob
from caido_sdk_client.convert.connection import map_to_page_info
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import ReplayEntryHttpFull
from caido_sdk_client.sdks.replay_entry import ReplayEntry, ReplayEntrySDK
from caido_sdk_client.transport.latest.__generated__ import schema as latest
from caido_sdk_client.transport.v0_56.__generated__ import schema as v0_56
from caido_sdk_client.types.connection import (
    ConnectionQueryResult,
    Edge,
    PageInfo,
)
from caido_sdk_client.types.replay_session import (
    CreateReplaySessionFromId,
    CreateReplaySessionFromRaw,
    CreateReplaySessionOptions,
)
from caido_sdk_client.types.strings import Cursor, Id, IdLike
from caido_sdk_client.types.versioned import TransportVersion, Versioned, versioned
from caido_sdk_client.utils.errors import handle_graphql_error
from caido_sdk_client.utils.list import ListBuilder, ListBuilderVars
from caido_sdk_client.version import Version

LatestSession = latest.ReplaySessionHttpMeta | latest.ReplaySessionWsMeta
V056Session = v0_56.ReplaySessionMeta
SessionFragment = LatestSession | V056Session


def _latest_session(data: object) -> LatestSession:
    if isinstance(data, (latest.ReplaySessionHttpMeta, latest.ReplaySessionWsMeta)):
        return data
    typename = getattr(data, "typename", type(data).__name__)
    raise ValueError(f"Unsupported replay session type: {typename}")


def _latest_entry(data: object) -> ReplayEntryHttpFull | latest.ReplayEntryWsFull:
    if isinstance(data, (ReplayEntryHttpFull, latest.ReplayEntryWsFull)):
        return data
    typename = getattr(data, "typename", type(data).__name__)
    raise ValueError(f"Unsupported replay entry type: {typename}")


def _map_request_source(
    request_source: CreateReplaySessionFromId | CreateReplaySessionFromRaw | None,
) -> dict[str, object] | None:
    if request_source is None:
        return None
    if isinstance(request_source, CreateReplaySessionFromId):
        return {"id": str(request_source.id)}
    return {
        "raw": {
            "connectionInfo": {
                "host": request_source.connection.host,
                "port": request_source.connection.port,
                "isTLS": request_source.connection.is_tls,
                "SNI": request_source.connection.sni,
            },
            "raw": encode_blob(request_source.raw),
        }
    }


def _empty_connection() -> ConnectionQueryResult[ReplayEntry]:
    return ConnectionQueryResult(
        page_info=PageInfo(
            has_next_page=False,
            has_previous_page=False,
            start_cursor=None,
            end_cursor=None,
        ),
        edges=[],
    )


class ReplaySessionsListBuilder(ListBuilder["ReplaySession", None, None]):
    """List builder for replay sessions."""

    def __init__(self, graphql: GraphQLClient, version: Version) -> None:
        super().__init__(graphql)
        self._version = version

    async def _query(
        self, vars: ListBuilderVars[None, None]
    ) -> ConnectionQueryResult[ReplaySession]:
        variables = {
            "first": vars.first,
            "after": vars.after,
            "last": vars.last,
            "before": vars.before,
        }

        if await self._version.gte(TransportVersion.V0_57.value):
            raw = await self._graphql.query(
                latest.ReplaySessions.Meta.document, variables=variables
            )
            model = latest.ReplaySessions.model_validate(raw)
            return ConnectionQueryResult(
                page_info=map_to_page_info(model.replaySessions.pageInfo),
                edges=[
                    Edge(
                        cursor=Cursor(edge.cursor),
                        node=ReplaySession(
                            self._graphql,
                            self._version,
                            versioned(
                                TransportVersion.V0_57,
                                _latest_session(edge.node),
                            ),
                        ),
                    )
                    for edge in model.replaySessions.edges
                ],
            )

        raw = await self._graphql.query(
            v0_56.ReplaySessions.Meta.document, variables=variables
        )
        model = v0_56.ReplaySessions.model_validate(raw)
        return ConnectionQueryResult(
            page_info=map_to_page_info(model.replaySessions.pageInfo),
            edges=[
                Edge(
                    cursor=Cursor(edge.cursor),
                    node=ReplaySession(
                        self._graphql,
                        self._version,
                        versioned(TransportVersion.V0_56, edge.node),
                    ),
                )
                for edge in model.replaySessions.edges
            ],
        )


class ReplaySessionEntriesListBuilder(ListBuilder[ReplayEntry, None, None]):
    """List builder for replay session entries."""

    def __init__(
        self, graphql: GraphQLClient, version: Version, session_id: IdLike
    ) -> None:
        super().__init__(graphql)
        self._version = version
        self._session_id = str(session_id)
        self._include_replay_raw = True
        self._include_request_raw = True
        self._include_response_raw = True

    def include_raw(
        self, options: bool | dict[str, bool] | None = None
    ) -> ReplaySessionEntriesListBuilder:
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
        self, vars: ListBuilderVars[None, None]
    ) -> ConnectionQueryResult[ReplayEntry]:
        variables = {
            "id": self._session_id,
            "first": vars.first,
            "after": vars.after,
            "last": vars.last,
            "before": vars.before,
            "includeReplayRaw": self._include_replay_raw,
            "includeRequestRaw": self._include_request_raw,
            "includeResponseRaw": self._include_response_raw,
        }
        if await self._version.gte(TransportVersion.V0_57.value):
            raw = await self._graphql.query(
                latest.ReplaySessionEntries.Meta.document, variables=variables
            )
            model = latest.ReplaySessionEntries.model_validate(raw)
            session = model.replaySession
            if not isinstance(
                session,
                (
                    latest.ReplaySessionEntriesReplaysessionBaseReplaySessionHttp,
                    latest.ReplaySessionEntriesReplaysessionBaseReplaySessionWs,
                ),
            ):
                return _empty_connection()
            connection = session.entries
            return ConnectionQueryResult(
                page_info=map_to_page_info(connection.pageInfo),
                edges=[
                    Edge(
                        cursor=Cursor(edge.cursor),
                        node=ReplayEntry(
                            self._graphql,
                            versioned(
                                TransportVersion.V0_57,
                                _latest_entry(edge.node),
                            ),
                        ),
                    )
                    for edge in connection.edges
                ],
            )

        raw = await self._graphql.query(
            v0_56.ReplaySessionEntries.Meta.document, variables=variables
        )
        model = v0_56.ReplaySessionEntries.model_validate(raw)
        if model.replaySession is None:
            return _empty_connection()
        connection = model.replaySession.entries
        return ConnectionQueryResult(
            page_info=map_to_page_info(connection.pageInfo),
            edges=[
                Edge(
                    cursor=Cursor(edge.cursor),
                    node=ReplayEntry(
                        self._graphql,
                        versioned(TransportVersion.V0_56, edge.node),
                    ),
                )
                for edge in connection.edges
            ],
        )


class ReplaySession:
    """Replay session."""

    def __init__(
        self,
        graphql: GraphQLClient,
        version: Version,
        fragment: Versioned[SessionFragment],
        entry_sdk: ReplayEntrySDK | None = None,
    ) -> None:
        self._graphql = graphql
        self._version = version
        self._entry_sdk = entry_sdk or ReplayEntrySDK(graphql, version)
        data = fragment.data
        self.id = Id(data.id)
        self.name = data.name
        self.collection_id = Id(data.collection.id)
        self.active_entry_id = (
            Id(data.activeEntry.id) if data.activeEntry is not None else None
        )

    def entries(self) -> ReplaySessionEntriesListBuilder:
        return ReplaySessionEntriesListBuilder(self._graphql, self._version, self.id)

    async def set_active_entry(self, entry_id: IdLike) -> ReplaySession:
        variables = {"id": str(self.id), "entryId": str(entry_id)}
        if await self._version.gte(TransportVersion.V0_57.value):
            raw = await self._graphql.mutation(
                latest.SetActiveReplaySessionEntry.Meta.document,
                variables=variables,
            )
            session = latest.SetActiveReplaySessionEntry.model_validate(
                raw
            ).setActiveReplaySessionEntry.session
            if session is None:
                return self
            return ReplaySession(
                self._graphql,
                self._version,
                versioned(TransportVersion.V0_57, _latest_session(session)),
                self._entry_sdk,
            )

        raw = await self._graphql.mutation(
            v0_56.SetActiveReplaySessionEntry.Meta.document,
            variables=variables,
        )
        session = v0_56.SetActiveReplaySessionEntry.model_validate(
            raw
        ).setActiveReplaySessionEntry.session
        if session is None:
            return self
        return ReplaySession(
            self._graphql,
            self._version,
            versioned(TransportVersion.V0_56, session),
            self._entry_sdk,
        )


class ReplaySessionSDK:
    """SDK for replay sessions."""

    def __init__(
        self,
        graphql: GraphQLClient,
        version: Version | None = None,
        entries: ReplayEntrySDK | None = None,
    ) -> None:
        self._graphql = graphql
        self._version = version or Version.of(TransportVersion.V0_57.value)
        self._entries = entries or ReplayEntrySDK(graphql, self._version)

    def list(self) -> ReplaySessionsListBuilder:
        return ReplaySessionsListBuilder(self._graphql, self._version)

    async def get(self, id: IdLike) -> ReplaySession | None:
        variables = {"id": str(id)}
        if await self._version.gte(TransportVersion.V0_57.value):
            raw = await self._graphql.query(
                latest.ReplaySession.Meta.document, variables=variables
            )
            session = latest.ReplaySession.model_validate(raw).replaySession
            if session is None:
                return None
            return ReplaySession(
                self._graphql,
                self._version,
                versioned(TransportVersion.V0_57, _latest_session(session)),
                self._entries,
            )

        raw = await self._graphql.query(
            v0_56.ReplaySession.Meta.document, variables=variables
        )
        session = v0_56.ReplaySession.model_validate(raw).replaySession
        if session is None:
            return None
        return ReplaySession(
            self._graphql,
            self._version,
            versioned(TransportVersion.V0_56, session),
            self._entries,
        )

    async def create(
        self, options: CreateReplaySessionOptions | None = None
    ) -> ReplaySession:
        opts = options or CreateReplaySessionOptions()
        input_data: dict[str, object] = {}
        if opts.collection_id is not None:
            input_data["collectionId"] = str(opts.collection_id)
        request_source = _map_request_source(opts.request_source)
        if request_source is not None:
            input_data["requestSource"] = request_source
        if await self._version.gte(TransportVersion.V0_57.value):
            input_data["kind"] = "HTTP"
            raw = await self._graphql.mutation(
                latest.CreateReplaySession.Meta.document,
                variables={"input": input_data},
            )
            payload = latest.CreateReplaySession.model_validate(raw).createReplaySession
            if payload.error is not None:
                handle_graphql_error(cast(AllErrors, payload.error))
            if payload.session is None:
                raise MissingExpectedValueError("createReplaySession.session")
            return ReplaySession(
                self._graphql,
                self._version,
                versioned(TransportVersion.V0_57, _latest_session(payload.session)),
                self._entries,
            )

        raw = await self._graphql.mutation(
            v0_56.CreateReplaySession.Meta.document,
            variables={"input": input_data},
        )
        session = v0_56.CreateReplaySession.model_validate(
            raw
        ).createReplaySession.session
        if session is None:
            raise MissingExpectedValueError("createReplaySession.session")
        return ReplaySession(
            self._graphql,
            self._version,
            versioned(TransportVersion.V0_56, session),
            self._entries,
        )

    async def delete(self, ids: builtins.list[IdLike]) -> None:
        variables = {"ids": [str(id) for id in ids]}
        if await self._version.gte(TransportVersion.V0_57.value):
            await self._graphql.mutation(
                latest.DeleteReplaySessions.Meta.document, variables=variables
            )
            return
        await self._graphql.mutation(
            v0_56.DeleteReplaySessions.Meta.document, variables=variables
        )

    async def move(self, id: IdLike, collection_id: IdLike) -> ReplaySession:
        variables = {"id": str(id), "collectionId": str(collection_id)}
        if await self._version.gte(TransportVersion.V0_57.value):
            raw = await self._graphql.mutation(
                latest.MoveReplaySession.Meta.document, variables=variables
            )
            session = latest.MoveReplaySession.model_validate(
                raw
            ).moveReplaySession.session
            if session is None:
                raise MissingExpectedValueError("moveReplaySession.session")
            return ReplaySession(
                self._graphql,
                self._version,
                versioned(TransportVersion.V0_57, _latest_session(session)),
                self._entries,
            )

        raw = await self._graphql.mutation(
            v0_56.MoveReplaySession.Meta.document, variables=variables
        )
        session = v0_56.MoveReplaySession.model_validate(raw).moveReplaySession.session
        if session is None:
            raise MissingExpectedValueError("moveReplaySession.session")
        return ReplaySession(
            self._graphql,
            self._version,
            versioned(TransportVersion.V0_56, session),
            self._entries,
        )

    async def rename(self, id: IdLike, name: str) -> ReplaySession:
        variables = {"id": str(id), "name": name}
        if await self._version.gte(TransportVersion.V0_57.value):
            raw = await self._graphql.mutation(
                latest.RenameReplaySession.Meta.document, variables=variables
            )
            session = latest.RenameReplaySession.model_validate(
                raw
            ).renameReplaySession.session
            if session is None:
                raise MissingExpectedValueError("renameReplaySession.session")
            return ReplaySession(
                self._graphql,
                self._version,
                versioned(TransportVersion.V0_57, _latest_session(session)),
                self._entries,
            )

        raw = await self._graphql.mutation(
            v0_56.RenameReplaySession.Meta.document, variables=variables
        )
        session = v0_56.RenameReplaySession.model_validate(
            raw
        ).renameReplaySession.session
        if session is None:
            raise MissingExpectedValueError("renameReplaySession.session")
        return ReplaySession(
            self._graphql,
            self._version,
            versioned(TransportVersion.V0_56, session),
            self._entries,
        )

    async def set_active_entry(self, session_id: IdLike, entry_id: IdLike) -> None:
        variables = {"id": str(session_id), "entryId": str(entry_id)}
        if await self._version.gte(TransportVersion.V0_57.value):
            await self._graphql.mutation(
                latest.SetActiveReplaySessionEntry.Meta.document,
                variables=variables,
            )
            return
        await self._graphql.mutation(
            v0_56.SetActiveReplaySessionEntry.Meta.document,
            variables=variables,
        )
