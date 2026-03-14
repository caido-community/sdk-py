"""Tests for the Replay SDK."""

from __future__ import annotations

import base64

import pytest
from caido_sdk_client import Client
from caido_sdk_client.types import (
    ConnectionInfoInput,
    CreateReplaySessionFromRaw,
    CreateReplaySessionOptions,
    ReplaySendOptions,
)


@pytest.mark.usefixtures("test_project")
async def test_replay_send(caido: Client) -> None:
    """Create a replay session and send a request via replay."""
    session = await caido.replay.sessions.create(
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
        ),
    )

    result = await caido.replay.send(
        session.id,
        ReplaySendOptions(
            raw=b"GET / HTTP/1.1\r\nHost: httpforever.com\r\n\r\n",
            connection=ConnectionInfoInput(
                host="httpforever.com",
                port=80,
                is_tls=False,
            ),
        ),
    )
    assert result.entry.request is not None
    assert result.entry.request.host == "httpforever.com"
    assert result.entry.request.port == 80
    assert result.entry.response is not None
    assert result.entry.response.status_code == 200
    assert result.entry.response.raw is not None
    assert (
        b"reliably insecure" in result.entry.response.raw
        or b"A reliably" in result.entry.response.raw
    )
