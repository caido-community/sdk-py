"""DNS upstream resolver SDK."""

from __future__ import annotations

import builtins

from caido_sdk_client.convert.dns_upstream import map_to_dns_upstream
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateDnsUpstream,
    DnsUpstreams,
)
from caido_sdk_client.types.dns_upstream import (
    CreateDNSUpstreamOptions,
    DNSUpstream,
)


class DNSUpstreamSDK:
    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> builtins.list[DNSUpstream]:
        raw = await self._graphql.query(DnsUpstreams.Meta.document)
        model = DnsUpstreams.model_validate(raw)
        return [map_to_dns_upstream(node) for node in model.dnsUpstreams]

    async def create(self, options: CreateDNSUpstreamOptions) -> DNSUpstream:
        raw = await self._graphql.mutation(
            CreateDnsUpstream.Meta.document,
            variables={"input": {"ip": options.ip, "name": options.name}},
        )
        model = CreateDnsUpstream.model_validate(raw)
        return map_to_dns_upstream(model.createDnsUpstream.upstream)
