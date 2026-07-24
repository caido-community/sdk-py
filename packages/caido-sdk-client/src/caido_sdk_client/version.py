"""Lazy handle for the connected Caido instance version."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import semver as semver_module

from caido_sdk_client.types.semver import SemverLiteral

if TYPE_CHECKING:
    from caido_sdk_client.rest import RestClient


def _gte(current: str, threshold: str) -> bool:
    return semver_module.Version.parse(current) >= semver_module.Version.parse(
        threshold
    )


class Version:
    """Readonly lazy/eager Caido instance version handle."""

    def __init__(
        self,
        version: SemverLiteral | None,
        rest: RestClient | None,
    ) -> None:
        self._version = version
        self._rest = rest
        self._resolution: asyncio.Task[SemverLiteral] | None = None

    @classmethod
    def of(cls, semver: SemverLiteral) -> Version:
        """Create an eager handle that never requests ``/health``."""
        semver_module.Version.parse(semver)
        return cls(semver, None)

    @classmethod
    def lazy(cls, rest: RestClient) -> Version:
        """Create a handle that resolves from ``/health`` on first use."""
        return cls(None, rest)

    async def get(self) -> SemverLiteral:
        """Return the version, resolving it once when necessary."""
        if self._version is not None:
            return self._version
        if self._resolution is None:
            self._resolution = asyncio.create_task(self._fetch_from_health())
        resolved = await asyncio.shield(self._resolution)
        self._version = resolved
        return resolved

    async def gte(self, threshold: SemverLiteral) -> bool:
        """Return whether the instance version is at least ``threshold``."""
        return _gte(await self.get(), threshold)

    async def _fetch_from_health(self) -> SemverLiteral:
        rest = self._rest
        if rest is None:
            raise RuntimeError("Version handle has no RestClient for lazy resolution")
        response: object = await rest.get("/health")
        if not isinstance(response, dict) or not isinstance(
            response.get("version"), str
        ):
            raise ValueError("Health response did not contain a semantic version")
        version = response["version"]
        semver_module.Version.parse(version)
        return version
