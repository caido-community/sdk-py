"""SDK for replay entries."""

from __future__ import annotations

from caido_sdk_client.convert.replay import map_to_replay_entry
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import ReplayEntry as ReplayEntryOp
from caido_sdk_client.types.replay_entry import ReplayEntry
from caido_sdk_client.types.strings import IdLike


class ReplayEntrySDK:
    """SDK for replay entries."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def get(self, id: IdLike) -> ReplayEntry | None:
        """Get a replay entry by ID. Returns None if it does not exist."""
        raw = await self._graphql.query(
            ReplayEntryOp.Meta.document,
            variables={
                "id": str(id),
                "includeReplayRaw": True,
                "includeRequestRaw": True,
                "includeResponseRaw": True,
            },
        )
        model = ReplayEntryOp.model_validate(raw)
        if model.replayEntry is None:
            return None
        return map_to_replay_entry(model.replayEntry)
