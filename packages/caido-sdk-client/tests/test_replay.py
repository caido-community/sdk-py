"""Tests for the Replay SDK."""

from __future__ import annotations

import pytest
from caido_sdk_client import Client
from caido_sdk_client.types import (
    ConnectionInfoInput,
    ReplaySendOptions,
)

from tests.utils import create_mock_replay_session


@pytest.mark.usefixtures("test_project")
async def test_replay_send(caido: Client) -> None:
    """Create a replay session and send a request via replay."""
    session = await create_mock_replay_session(client=caido)

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
    assert b"A reliably insecure connection" in result.entry.response.raw
