"""DNS rewrite conversion helpers."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import (
    DnsRewriteFull,
    DnsRewriteFullDNSIpResolverInlineFragment,
    DnsRewriteFullDNSUpstreamResolverInlineFragment,
)
from caido_sdk_client.types.dns_rewrite import (
    DNSIPResolver,
    DNSRewrite,
    DNSUpstreamResolver,
)
from caido_sdk_client.types.strings import Id


def map_to_dns_rewrite(node: DnsRewriteFull) -> DNSRewrite:
    if node.resolution.typename == "DNSIpResolver":
        ip = DnsRewriteFullDNSIpResolverInlineFragment.model_validate(node.resolution)
        resolution = DNSIPResolver(ip=ip.ip)
    else:
        upstream = DnsRewriteFullDNSUpstreamResolverInlineFragment.model_validate(
            node.resolution
        )
        resolution = DNSUpstreamResolver(upstream_id=Id(upstream.id))
    return DNSRewrite(
        id=Id(node.id),
        allowlist=node.allowlist,
        denylist=node.denylist,
        enabled=node.enabled,
        rank=node.rank,
        resolution=resolution,
    )
