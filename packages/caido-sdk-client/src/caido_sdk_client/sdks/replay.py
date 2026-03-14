"""Top-level Replay SDK: sessions, collections, entries, and send()."""

from __future__ import annotations

from typing import Any, Literal, cast

from caido_sdk_client.convert.blob import encode_blob
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.misc import OtherUserError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import StartReplayTask
from caido_sdk_client.sdks.replay_collection import ReplayCollectionSDK
from caido_sdk_client.sdks.replay_entry import ReplayEntrySDK
from caido_sdk_client.sdks.replay_session import ReplaySessionSDK
from caido_sdk_client.sdks.task import ReplayTask, TaskSDK
from caido_sdk_client.types.replay_session import (
    ReplaySendOptions,
    ReplaySendResult,
)
from caido_sdk_client.types.strings import IdLike
from caido_sdk_client.utils.errors import handle_graphql_error


def _build_start_replay_task_input(options: ReplaySendOptions) -> dict[str, Any]:
    """Build StartReplayTaskInput dict from ReplaySendOptions."""
    settings = options.settings
    connection_close = settings.connection_close if settings else False
    update_content_length = settings.update_content_length if settings else True
    placeholders = []
    if settings and settings.placeholders:
        for ph in settings.placeholders:
            placeholders.append(
                {
                    "inputRange": {
                        "start": ph.input_range.start,
                        "end": ph.input_range.end,
                    },
                    "outputRange": {
                        "start": ph.output_range.start,
                        "end": ph.output_range.end,
                    },
                    "preprocessors": ph.preprocessors or [],
                }
            )
    return {
        "connection": {
            "host": options.connection.host,
            "port": options.connection.port,
            "isTLS": options.connection.is_tls,
            "SNI": options.connection.sni,
        },
        "raw": encode_blob(options.raw),
        "settings": {
            "connectionClose": connection_close,
            "updateContentLength": update_content_length,
            "placeholders": placeholders,
        },
    }


class ReplaySDK:
    """Top-level Replay SDK: sessions, collections, entries, and send()."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql
        self.sessions = ReplaySessionSDK(graphql)
        self.collections = ReplayCollectionSDK(graphql)
        self.entries = ReplayEntrySDK(graphql)
        self._tasks = TaskSDK(graphql)

    async def send(
        self,
        session_id: IdLike,
        options: ReplaySendOptions,
    ) -> ReplaySendResult:
        """Send a request via replay. Starts a replay task and resolves when the task finishes."""
        input_data = _build_start_replay_task_input(options)
        raw = await self._graphql.mutation(
            StartReplayTask.Meta.document,
            variables={
                "sessionId": str(session_id),
                "input": input_data,
            },
        )
        payload_model = StartReplayTask.model_validate(raw)
        payload = payload_model.startReplayTask
        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))
        if payload.task is None:
            raise OtherUserError("INTERNAL", "startReplayTask returned no task")
        task = ReplayTask(self._graphql, payload.task)

        async for result in self._tasks.finished(
            lambda r: r.task.id == task.id,
        ):
            entry = await self.entries.get(task.replay_entry_id)
            if entry is None:
                raise OtherUserError("INTERNAL", "Replay entry not found")
            return ReplaySendResult(
                entry=entry,
                status=cast(Literal["DONE", "CANCELLED", "ERROR"], result.status),
                error=result.error,
            )

        raise OtherUserError(
            "INTERNAL",
            "Replay task subscription ended without finished event",
        )
