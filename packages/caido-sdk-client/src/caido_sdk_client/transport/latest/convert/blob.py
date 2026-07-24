"""Blob encoding/decoding for raw request/response bodies."""

from __future__ import annotations

import base64


def decode_blob(raw: str | None) -> bytes | None:
    """Decode a base64-encoded raw string to bytes. Returns None if raw is None or empty."""
    if not raw:
        return None
    return base64.b64decode(raw)


def encode_blob(data: str | bytes) -> str:
    """Encode a string or bytes to base64."""
    if isinstance(data, str):
        return base64.b64encode(data.encode()).decode()
    return base64.b64encode(data).decode()
