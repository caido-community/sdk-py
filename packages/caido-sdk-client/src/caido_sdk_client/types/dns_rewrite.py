"""DNS rewrite rule types."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from caido_sdk_client.types.strings import Id, IdLike


@dataclass(frozen=True, slots=True)
class DNSIPResolver:
    ip: str
    kind: Literal["ip"] = "ip"


@dataclass(frozen=True, slots=True)
class DNSUpstreamResolver:
    upstream_id: IdLike
    kind: Literal["upstream"] = "upstream"


DNSResolver: TypeAlias = DNSIPResolver | DNSUpstreamResolver


@dataclass(frozen=True, slots=True)
class DNSRewrite:
    id: Id
    allowlist: list[str]
    denylist: list[str]
    enabled: bool
    rank: str
    resolution: DNSResolver


@dataclass(frozen=True, slots=True)
class CreateDNSRewriteOptions:
    allowlist: list[str]
    denylist: list[str]
    resolution: DNSResolver
