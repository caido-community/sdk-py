"""DNS upstream resolver types."""

from __future__ import annotations

from dataclasses import dataclass

from caido_sdk_client.types.strings import Id


@dataclass(frozen=True, slots=True)
class DNSUpstream:
    id: Id
    ip: str
    name: str


@dataclass(frozen=True, slots=True)
class CreateDNSUpstreamOptions:
    ip: str
    name: str
