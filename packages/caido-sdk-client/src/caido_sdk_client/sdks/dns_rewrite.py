"""DNS rewrite SDK."""

from __future__ import annotations

from typing import cast

from caido_sdk_client.convert.dns_rewrite import map_to_dns_rewrite
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import CreateDnsRewrite
from caido_sdk_client.types.dns_rewrite import (
    CreateDNSRewriteOptions,
    DNSIPResolver,
    DNSRewrite,
)
from caido_sdk_client.utils.errors import handle_graphql_error


class DNSRewriteSDK:
    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def create(self, options: CreateDNSRewriteOptions) -> DNSRewrite:
        if isinstance(options.resolution, DNSIPResolver):
            resolution = {"ip": {"ip": options.resolution.ip}}
        else:
            resolution = {"upstream": {"id": str(options.resolution.upstream_id)}}
        raw = await self._graphql.mutation(
            CreateDnsRewrite.Meta.document,
            variables={
                "input": {
                    "allowlist": options.allowlist,
                    "denylist": options.denylist,
                    "resolution": resolution,
                }
            },
        )
        payload = CreateDnsRewrite.model_validate(raw).createDnsRewrite
        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))
        if payload.rewrite is None:
            raise MissingExpectedValueError("createDnsRewrite.rewrite")
        return map_to_dns_rewrite(payload.rewrite)
