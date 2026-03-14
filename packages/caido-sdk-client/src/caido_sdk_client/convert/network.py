"""Conversion helpers for network/connection GraphQL fragments."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import ConnectionInfoFull
from caido_sdk_client.types.network import ConnectionInfo


def map_to_connection_info(node: ConnectionInfoFull) -> ConnectionInfo:
    """Convert ConnectionInfoFull fragment to public ConnectionInfo type."""
    return ConnectionInfo(
        host=node.host,
        port=node.port,
        is_tls=node.isTLS,
        sni=node.SNI,
    )
