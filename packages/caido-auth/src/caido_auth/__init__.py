"""Caido Auth SDK for OAuth2 device code authentication."""

from .client import CaidoAuth
from .models import (
    AuthenticationError,
    AuthenticationFlowError,
    AuthenticationRequest,
    AuthenticationScope,
    AuthenticationToken,
    TokenRefreshError,
)

__all__ = [
    "CaidoAuth",
    "AuthenticationToken",
    "AuthenticationRequest",
    "AuthenticationScope",
    "AuthenticationError",
    "AuthenticationFlowError",
    "TokenRefreshError",
]
