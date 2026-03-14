"""Network/connection types used by replay and other features."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConnectionInfoInput:
    """Connection info for replay send and similar inputs."""

    host: str
    port: int
    is_tls: bool
    sni: str | None = None


@dataclass(frozen=True, slots=True)
class ConnectionInfo:
    """Connection info (output)."""

    host: str
    port: int
    is_tls: bool
    sni: str | None = None
