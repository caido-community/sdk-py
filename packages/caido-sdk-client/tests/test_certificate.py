"""Tests for the Certificate SDK."""

from __future__ import annotations

import time

from caido_sdk_client import Client
from caido_sdk_client.types import ImportCertificateOptions


async def test_export_generate_and_restore_instance_certificate(
    caido: Client,
) -> None:
    """Export, regenerate, and restore the instance certificate."""
    password = f"sdk-test-{int(time.time() * 1000)}"
    original = await caido.instance.certificate.export(password)

    assert len(original) > 0

    try:
        generated = await caido.instance.certificate.generate()
        assert generated is True

        replacement = await caido.instance.certificate.export(password)
        assert len(replacement) > 0
        assert replacement != original
    finally:
        await caido.instance.certificate.import_(
            ImportCertificateOptions(file=original, password=password)
        )

    restored = await caido.instance.certificate.export(password)
    assert len(restored) > 0
