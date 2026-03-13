"""Task-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError


class TaskInProgressUserError(BaseError):
    task_id: str

    def __init__(self, task_id: str) -> None:
        super().__init__(
            f"Could not perform operation, task {task_id} is still in progress"
        )
        self.task_id = task_id
