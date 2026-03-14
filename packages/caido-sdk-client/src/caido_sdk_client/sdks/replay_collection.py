"""SDK for replay session collections."""

from __future__ import annotations

from caido_sdk_client.convert.connection import map_to_page_info
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateReplaySessionCollection,
    DeleteReplaySessionCollection,
    RenameReplaySessionCollection,
    ReplaySessionCollectionMeta,
    ReplaySessionCollections,
)
from caido_sdk_client.types.connection import ConnectionQueryResult, Edge
from caido_sdk_client.types.replay_collection import (
    CreateReplaySessionCollectionOptions,
)
from caido_sdk_client.types.strings import Cursor, Id, IdLike
from caido_sdk_client.utils.list import ListBuilder, ListBuilderVars


class ReplayCollectionsListBuilder(ListBuilder["ReplaySessionCollection", None, None]):
    """List builder for replay session collections."""

    async def _query(
        self,
        vars: ListBuilderVars[None, None],
    ) -> ConnectionQueryResult[ReplaySessionCollection]:
        raw = await self._graphql.query(
            ReplaySessionCollections.Meta.document,
            variables={
                "first": vars.first,
                "after": vars.after,
                "last": vars.last,
                "before": vars.before,
            },
        )
        model = ReplaySessionCollections.model_validate(raw)
        conn = model.replaySessionCollections
        page_info = map_to_page_info(conn.pageInfo)
        edges = [
            Edge(
                cursor=Cursor(e.cursor),
                node=ReplaySessionCollection(e.node),
            )
            for e in conn.edges
        ]
        return ConnectionQueryResult(page_info=page_info, edges=edges)


class ReplaySessionCollection:
    """Replay session collection."""

    def __init__(self, data: ReplaySessionCollectionMeta) -> None:
        self.id: Id = Id(data.id)
        self.name: str = data.name


class ReplayCollectionSDK:
    """SDK for replay session collections."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    def list(self) -> ReplayCollectionsListBuilder:
        """List replay session collections (cursor-based). Chain with .first(50) then await."""
        return ReplayCollectionsListBuilder(self._graphql)

    async def create(
        self,
        options: CreateReplaySessionCollectionOptions,
    ) -> ReplaySessionCollection:
        """Create a new replay session collection."""
        raw = await self._graphql.mutation(
            CreateReplaySessionCollection.Meta.document,
            variables={"input": {"name": options.name}},
        )
        model = CreateReplaySessionCollection.model_validate(raw)
        payload = model.createReplaySessionCollection
        if payload.collection is None:
            raise MissingExpectedValueError("createReplaySessionCollection.collection")
        return ReplaySessionCollection(payload.collection)

    async def delete(self, id: IdLike) -> None:
        """Delete a replay session collection."""
        await self._graphql.mutation(
            DeleteReplaySessionCollection.Meta.document,
            variables={"id": str(id)},
        )

    async def rename(
        self,
        id: IdLike,
        name: str,
    ) -> ReplaySessionCollection:
        """Rename a replay session collection."""
        raw = await self._graphql.mutation(
            RenameReplaySessionCollection.Meta.document,
            variables={"id": str(id), "name": name},
        )
        model = RenameReplaySessionCollection.model_validate(raw)
        payload = model.renameReplaySessionCollection
        if payload.collection is None:
            raise MissingExpectedValueError("renameReplaySessionCollection.collection")
        return ReplaySessionCollection(payload.collection)
