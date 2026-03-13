"""File-based token cache."""

from __future__ import annotations

import json
import os
from pathlib import Path

from caido_sdk_client.auth.cache.types import CachedToken
from caido_sdk_client.logger import Logger
from caido_sdk_client.utils.optional import Maybe, is_absent


class FileTokenCache:
    def __init__(
        self,
        *,
        path: str | None = None,
        logger: Logger | None = None,
    ) -> None:
        self._path = path or ".caido-token.json"
        self._logger = logger

    async def load(self) -> Maybe[CachedToken]:
        try:
            resolved = self._resolve_path()
            with open(resolved) as f:
                parsed = json.load(f)

            access_token = parsed.get("access_token")
            if is_absent(access_token):
                return None

            return CachedToken(
                access_token=access_token,
                refresh_token=parsed.get("refresh_token"),
                expires_at=parsed.get("expires_at"),
            )
        except Exception:
            if self._logger is not None:
                self._logger.debug("Failed to load cached token from file")
            return None

    async def save(self, token: CachedToken) -> None:
        try:
            resolved = self._resolve_path()
            Path(resolved).parent.mkdir(parents=True, exist_ok=True)

            data = {
                "access_token": token.access_token,
                "refresh_token": token.refresh_token,
                "expires_at": token.expires_at,
            }
            fd = os.open(resolved, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
            with os.fdopen(fd, "w") as f:
                json.dump(data, f, indent=2)
        except Exception:
            if self._logger is not None:
                self._logger.warn("Failed to save token cache to file")

    async def clear(self) -> None:
        try:
            resolved = self._resolve_path()
            os.unlink(resolved)
        except Exception:
            if self._logger is not None:
                self._logger.warn("Failed to clear token cache file")

    def _resolve_path(self) -> str:
        if os.path.isabs(self._path):
            return self._path
        return os.path.join(os.getcwd(), self._path)
