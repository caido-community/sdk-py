"""Cache types for persisting authentication tokens."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class CachedToken:
    access_token: str
    refresh_token: str | None = None
    expires_at: str | None = None


class TokenCache(Protocol):
    async def load(self) -> CachedToken | None: ...
    async def save(self, token: CachedToken) -> None: ...
    async def clear(self) -> None: ...
