"""Tests for the User SDK."""

from __future__ import annotations

from caido_sdk_client import Client


async def test_viewer_returns_cloud_user(caido: Client) -> None:
    """Get the currently authenticated viewer."""
    viewer = await caido.user.viewer()
    assert viewer.kind == "CloudUser"
