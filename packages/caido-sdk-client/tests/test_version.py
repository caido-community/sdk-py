"""Focused tests for lazy version resolution and transport tagging."""

from __future__ import annotations

import asyncio
from typing import cast

from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.rest import RestClient
from caido_sdk_client.sdks.replay_entry import ReplayEntrySDK
from caido_sdk_client.types.versioned import TransportVersion, versioned
from caido_sdk_client.version import Version


class FakeRestClient:
    def __init__(self) -> None:
        self.calls = 0

    async def get(self, path: str) -> dict[str, str]:
        assert path == "/health"
        self.calls += 1
        await asyncio.sleep(0)
        return {"version": "0.57.1"}


class FakeGraphQLClient:
    def __init__(self) -> None:
        self.documents: list[str] = []

    async def query(
        self, document: str, *, variables: dict[str, object]
    ) -> dict[str, object]:
        self.documents.append(document)
        return {"replayEntry": None}


async def test_lazy_version_resolution_is_shared_and_cached() -> None:
    rest = FakeRestClient()
    version = Version.lazy(cast(RestClient, rest))

    assert await asyncio.gather(version.get(), version.get()) == ["0.57.1", "0.57.1"]
    assert await version.get() == "0.57.1"
    assert rest.calls == 1


async def test_seeded_version_and_semver_gte() -> None:
    version = Version.of("0.57.0-rc.1")

    assert await version.gte("0.56.0")
    assert not await version.gte("0.57.0")


def test_versioned_preserves_transport_discriminator() -> None:
    value = versioned(TransportVersion.V0_56, {"id": "entry"})

    assert value.version is TransportVersion.V0_56
    assert value.data == {"id": "entry"}


async def test_replay_entry_routes_by_seeded_version() -> None:
    latest_graphql = FakeGraphQLClient()
    legacy_graphql = FakeGraphQLClient()

    await ReplayEntrySDK(cast(GraphQLClient, latest_graphql), Version.of("0.57.0")).get(
        "entry"
    )
    await ReplayEntrySDK(cast(GraphQLClient, legacy_graphql), Version.of("0.56.9")).get(
        "entry"
    )

    assert "$sessionKind" in latest_graphql.documents[0]
    assert "$sessionKind" not in legacy_graphql.documents[0]
