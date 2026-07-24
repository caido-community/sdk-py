"""Certificate operation errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import (
    CertificateErrorReason,
)


class CertificateUserError(BaseError):
    def __init__(self, reason: CertificateErrorReason) -> None:
        super().__init__(f"Certificate operation failed: {reason.value}")
        self.reason = reason
