"""Browser-based approver implementation."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from inspect import isawaitable
from typing import TypeAlias, cast

from ..types import AuthenticationRequest

OnRequestCallback: TypeAlias = Callable[[AuthenticationRequest], None | Awaitable[None]]


class BrowserApprover:
    """Approver that delegates display/approval prompts to a callback."""

    def __init__(self, on_request: OnRequestCallback) -> None:
        self._on_request = on_request

    async def approve(self, request: AuthenticationRequest) -> None:
        # Approval is manual; this callback typically displays URL/code to the user.
        result = self._on_request(request)
        if isawaitable(result):
            await cast(Awaitable[None], result)
