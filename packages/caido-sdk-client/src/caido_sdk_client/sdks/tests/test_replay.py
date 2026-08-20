"""Unit tests for ReplaySDK.send buffering of fast-finishing tasks."""

from __future__ import annotations

import asyncio
from typing import Any, cast

from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.sdks.replay import ReplaySDK
from caido_sdk_client.types.network import ConnectionInfoInput
from caido_sdk_client.types.replay_session import ReplaySendOptions
from caido_sdk_client.version import Version

_DONE = object()

_TASK = {
    "__typename": "ReplayTask",
    "id": "task-1",
    "createdAt": "2026-01-01T00:00:00.000Z",
    "replayEntry": {"__typename": "ReplayEntry", "id": "entry-1"},
}


class _HotAsyncIterable:
    """Drop events unless a consumer is currently waiting (hot subject)."""

    def __init__(self) -> None:
        self._waiter: asyncio.Future[object] | None = None
        self._done = False

    def push(self, value: object) -> None:
        if self._waiter is not None and not self._waiter.done():
            self._waiter.set_result(value)

    def complete(self) -> None:
        self._done = True
        if self._waiter is not None and not self._waiter.done():
            self._waiter.set_result(_DONE)

    def __aiter__(self) -> _HotAsyncIterable:
        return self

    async def __anext__(self) -> object:
        if self._done:
            raise StopAsyncIteration
        self._waiter = asyncio.get_running_loop().create_future()
        result = await self._waiter
        if result is _DONE:
            raise StopAsyncIteration
        return result


class _FakeGraphQL:
    def __init__(self, subject: _HotAsyncIterable) -> None:
        self._subject = subject
        self.calls: list[str] = []

    def subscribe(
        self, document: object, variables: object = None
    ) -> _HotAsyncIterable:
        self.calls.append("subscribe")
        return self._subject

    async def mutation(
        self, document: object, variables: object = None, **kwargs: object
    ) -> dict[str, Any]:
        self.calls.append("mutation")
        # Yield so the buffered subscription is listening before the event is emitted.
        await asyncio.sleep(0)
        self._subject.push(
            {
                "finishedTask": {
                    "task": _TASK,
                    "status": "DONE",
                    "error": None,
                }
            }
        )
        self._subject.complete()
        return {
            "startReplayTask": {
                "task": _TASK,
                "error": None,
            }
        }

    async def query(self, document: object, variables: object = None) -> dict[str, Any]:
        return {
            "replayEntry": {
                "id": "entry-1",
                "createdAt": 1_767_225_600_000,
                "error": None,
                "raw": "",
                "connection": {
                    "__typename": "ConnectionInfo",
                    "host": "example.com",
                    "port": 80,
                    "isTLS": False,
                    "SNI": None,
                },
                "request": None,
                "session": {"id": "session-1"},
                "settings": {"placeholders": []},
            }
        }


async def test_send_resolves_when_task_finishes_before_start_mutation_returns() -> None:
    graphql = _FakeGraphQL(_HotAsyncIterable())
    replay = ReplaySDK(cast(GraphQLClient, graphql), Version.of("0.56.0"))

    result = await replay.send(
        "session-1",
        ReplaySendOptions(
            raw="GET / HTTP/1.1\r\nHost: example.com\r\n\r\n",
            connection=ConnectionInfoInput(
                host="example.com",
                port=80,
                is_tls=False,
            ),
        ),
    )

    assert result.status == "DONE"
    assert result.entry.id == "entry-1"
    assert graphql.calls[0] == "subscribe"
    assert "mutation" in graphql.calls
    assert graphql.calls.index("subscribe") < graphql.calls.index("mutation")
