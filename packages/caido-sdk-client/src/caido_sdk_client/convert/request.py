"""Conversion helpers for request/response GraphQL fragments."""

from __future__ import annotations

from datetime import datetime

from caido_sdk_client.convert.blob import decode_blob
from caido_sdk_client.graphql.__generated__.schema import RequestFull, ResponseFull
from caido_sdk_client.types.request import (
    Request,
    RequestMetadata,
    RequestResponseOpt,
    Response,
)
from caido_sdk_client.types.strings import Id


def map_to_request(node: RequestFull) -> Request:
    """Convert RequestFull fragment to public Request type."""
    raw_val = getattr(node, "raw", None)
    return Request(
        id=Id(node.id),
        host=node.host,
        port=node.port,
        method=node.method,
        path=node.path,
        query=node.query,
        is_tls=node.isTls,
        metadata=RequestMetadata(
            id=Id(node.metadata.id),
            color=node.metadata.color,
        ),
        created_at=datetime.fromtimestamp(node.createdAt / 1000.0),
        raw=decode_blob(raw_val),
    )


def map_to_response(node: ResponseFull) -> Response:
    """Convert ResponseFull fragment to public Response type."""
    raw_val = getattr(node, "raw", None)
    return Response(
        id=Id(node.id),
        status_code=node.statusCode,
        roundtrip_time=node.roundtripTime,
        length=node.length,
        created_at=datetime.fromtimestamp(node.createdAt / 1000.0),
        raw=decode_blob(raw_val),
    )


def map_to_request_response_opt(node: RequestFull) -> RequestResponseOpt:
    """Convert RequestFull (with optional response) to RequestResponseOpt."""
    return RequestResponseOpt(
        request=map_to_request(node),
        response=map_to_response(node.response) if node.response is not None else None,
    )
