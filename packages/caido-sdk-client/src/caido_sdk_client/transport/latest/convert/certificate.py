"""Certificate conversion helpers."""

from __future__ import annotations

from caido_sdk_client.transport.latest.convert.blob import decode_blob


def map_to_certificate(p12: str) -> bytes:
    certificate = decode_blob(p12)
    if certificate is None:
        raise ValueError("Certificate payload was empty")
    return certificate


def map_to_certificate_generation(success: bool) -> bool:
    return success
