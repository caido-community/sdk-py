"""SDK for the generic task system."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Callable
from typing import Any, cast

from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    FinishedTask,
    FinishedTaskFinishedtask,
    Tasks,
    cancelTask,
)
from caido_sdk_client.types.strings import Id, IdLike
from caido_sdk_client.types.task import TaskResult
from caido_sdk_client.utils.async_iterable import (
    filter_async_iterable,
    map_async_iterable,
)
from caido_sdk_client.utils.errors import handle_graphql_error


def _task_from_fragment(graphql: GraphQLClient, node: Any) -> Task | ReplayTask:
    """Build Task or ReplayTask from a task fragment (query/subscription)."""
    if getattr(node, "typename", None) == "ReplayTask":
        return ReplayTask(graphql, node)
    return Task(graphql, node)


class TaskSDK:
    """SDK for the generic task system."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> builtins.list[Task | ReplayTask]:
        """List all tasks."""
        raw = await self._graphql.query(Tasks.Meta.document)
        model = Tasks.model_validate(raw)
        return [_task_from_fragment(self._graphql, node) for node in model.tasks]

    async def cancel(self, id: IdLike) -> None:
        """Cancel a task by ID."""
        await self._graphql.mutation(
            cancelTask.Meta.document,
            variables={"id": str(id)},
        )

    def finished(
        self,
        filter_pred: Callable[[TaskResult], bool],
    ) -> AsyncIterator[TaskResult]:
        """Subscribe to finished tasks and yield those matching the filter."""

        async def map_event(event: dict[str, Any]) -> TaskResult:
            payload = FinishedTask.model_validate(event)
            ft: FinishedTaskFinishedtask = payload.finishedTask
            task = _task_from_fragment(self._graphql, ft.task)
            error_payload: dict[str, str] | None = None
            if ft.error is not None:
                error_payload = {"code": getattr(ft.error, "code", "") or ""}
            return TaskResult(
                task=task,
                status=ft.status,
                error=error_payload,
            )

        async def filtered(
            source: AsyncIterator[dict[str, Any]],
        ) -> AsyncIterator[TaskResult]:
            mapped = map_async_iterable(
                lambda ev, _: map_event(ev),
                source,
            )
            async for result in filter_async_iterable(filter_pred, mapped):
                yield result

        subscription = self._graphql.subscribe(FinishedTask.Meta.document)
        return filtered(subscription)


class Task:
    """A task."""

    def __init__(self, graphql: GraphQLClient, data: Any) -> None:
        self._graphql = graphql
        self.id: Id = Id(data.id)
        self.created_at: str = data.createdAt

    async def cancel(self) -> None:
        """Cancel this task."""
        raw = await self._graphql.mutation(
            cancelTask.Meta.document,
            variables={"id": str(self.id)},
        )
        payload = cancelTask.model_validate(raw)
        if payload.cancelTask.error is not None:
            handle_graphql_error(cast(AllErrors, payload.cancelTask.error))


class ReplayTask(Task):
    """A replay task."""

    def __init__(self, graphql: GraphQLClient, data: Any) -> None:
        super().__init__(graphql, data)
        replay_entry = getattr(data, "replayEntry", None)
        self.replay_entry_id: Id = (
            Id(replay_entry.id) if replay_entry is not None else Id("")
        )
