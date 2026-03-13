"""Workflow-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import WorkflowErrorReason


class WorkflowUserError(BaseError):
    code: str
    reason: WorkflowErrorReason
    node: str | None

    def __init__(
        self,
        code: str,
        reason: WorkflowErrorReason,
        message: str,
        node: str | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.reason = reason
        self.node = node
