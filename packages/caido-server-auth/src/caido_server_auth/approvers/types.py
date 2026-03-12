"""Approver protocol for authentication approval strategies."""

from __future__ import annotations

from typing import Protocol

from ..types import AuthenticationRequest


class AuthApprover(Protocol):
    """Contract used by AuthClient to approve a device flow request."""

    async def approve(self, request: AuthenticationRequest) -> None:
        """Approve an authentication request."""
