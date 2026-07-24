"""Test helpers: create mock requests and findings via the Caido instance."""

from __future__ import annotations

import base64
import os

import aiohttp
from caido_sdk_client import Client, ReplaySession
from caido_sdk_client.types import (
    ConnectionInfoInput,
    CreateFindingOptions,
    CreateReplaySessionFromRaw,
    CreateReplaySessionOptions,
    Finding,
)


async def create_mock_request() -> None:
    """Send a request through the Caido instance proxy to create a request in the project."""
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8080")
    # Disable SSL verification for the proxied request (mirrors JS NODE_TLS_REJECT_UNAUTHORIZED=0)
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get("https://perdu.com", proxy=instance_url) as _:
            pass


async def create_mock_finding(
    request_id: str,
    *,
    client: Client,
) -> Finding:
    """Create a finding for the given request ID using the provided client."""
    return await client.findings.create(
        request_id,
        CreateFindingOptions(
            title="Test Finding",
            reporter="Test Reporter",
            description="Test Description",
        ),
    )


async def create_mock_replay_session(*, client: Client) -> ReplaySession:
    """Create an empty replay session for integration tests."""
    return await client.replay.sessions.create(
        CreateReplaySessionOptions(
            request_source=CreateReplaySessionFromRaw(
                raw=base64.b64encode(b"").decode(),
                connection=ConnectionInfoInput(
                    host="localhost",
                    port=8080,
                    is_tls=False,
                    sni="",
                ),
            ),
        )
    )
