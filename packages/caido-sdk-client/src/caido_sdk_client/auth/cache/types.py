"""Cache types for persisting authentication tokens."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from caido_sdk_client.utils.optional import Maybe


@dataclass(slots=True)
class CachedToken:
    access_token: str
    refresh_token: str | None = None
    expires_at: str | None = None


class TokenCache(Protocol):
    async def load(self) -> Maybe[CachedToken]: ...
    async def save(self, token: CachedToken) -> None: ...
    async def clear(self) -> None: ...
