"""Tests for the DNS Upstream SDK."""

from __future__ import annotations

from caido_sdk_client import Client
from caido_sdk_client.types import CreateDNSUpstreamOptions


async def test_list_dns_upstreams(caido: Client) -> None:
    """List the instance's DNS upstream resolvers."""
    upstreams = await caido.dns_upstream.list()
    assert isinstance(upstreams, list)


async def test_create_dns_upstream(caido: Client) -> None:
    """Create a DNS upstream resolver."""
    upstream = await caido.dns_upstream.create(
        CreateDNSUpstreamOptions(ip="1.1.1.1", name="Cloudflare DNS")
    )

    assert upstream.id
    assert upstream.ip == "1.1.1.1"
    assert upstream.name == "Cloudflare DNS"
