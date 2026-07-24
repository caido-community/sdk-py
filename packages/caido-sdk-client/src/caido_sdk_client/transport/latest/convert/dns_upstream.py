"""DNS upstream conversion helpers."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import DnsUpstreamFull
from caido_sdk_client.types.dns_upstream import DNSUpstream
from caido_sdk_client.types.strings import Id


def map_to_dns_upstream(node: DnsUpstreamFull) -> DNSUpstream:
    return DNSUpstream(id=Id(node.id), ip=node.ip, name=node.name)
