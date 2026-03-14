"""Types for HTTP requests and responses."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from caido_sdk_client.types.strings import Id

RequestOrderField = (
    str  # "ext" | "host" | "id" | "method" | "path" | "query" | "created_at" | "source"
)
ResponseOrderField = str  # "length" | "roundtrip" | "code"


@dataclass(frozen=True, slots=True)
class RequestMetadata:
    """Request metadata (color, id)."""

    id: Id
    color: str | None = None


@dataclass(frozen=True, slots=True)
class Request:
    """Request (without raw when not requested)."""

    id: Id
    host: str
    port: int
    method: str
    path: str
    query: str
    is_tls: bool
    metadata: RequestMetadata
    created_at: datetime
    raw: bytes | None = None  # Present when include_raw was True


@dataclass(frozen=True, slots=True)
class Response:
    """Response (without raw when not requested)."""

    id: Id
    status_code: int
    roundtrip_time: int
    length: int
    created_at: datetime
    raw: bytes | None = None  # Present when include_raw was True


@dataclass(frozen=True, slots=True)
class RequestResponseOpt:
    """Request and optional response pair."""

    request: Request
    response: Response | None = None


@dataclass(frozen=True, slots=True)
class RequestGetOptions:
    """Options for getting a request and its response."""

    raw: bool | None = None
    """Include request and response raw body. Deprecated in favor of request_raw/response_raw. Default True."""
    request_raw: bool | None = None
    """Include request raw body. Default True."""
    response_raw: bool | None = None
    """Include response raw body. Default True."""
