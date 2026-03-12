"""Data models for Caido authentication."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class AuthenticationScope(str, Enum):
    """Available authentication scopes."""

    ASSISTANT = "ASSISTANT"
    OFFLINE = "OFFLINE"
    PROFILE_READ = "PROFILE_READ"


@dataclass
class AuthenticationRequest:
    """Device code authentication request details."""

    id: str
    user_code: str
    verification_url: str
    expires_at: datetime

    @classmethod
    def from_graphql(cls, data: dict) -> "AuthenticationRequest":
        """Create from GraphQL response data."""
        return cls(
            id=data["id"],
            user_code=data["userCode"],
            verification_url=data["verificationUrl"],
            expires_at=datetime.fromisoformat(data["expiresAt"].replace("Z", "+00:00")),
        )


@dataclass
class AuthenticationToken:
    """Authentication token with access and optional refresh tokens."""

    access_token: str
    expires_at: datetime
    scopes: list[AuthenticationScope]
    refresh_token: Optional[str] = None

    @classmethod
    def from_graphql(cls, data: dict) -> "AuthenticationToken":
        """Create from GraphQL response data."""
        return cls(
            access_token=data["accessToken"],
            expires_at=datetime.fromisoformat(data["expiresAt"].replace("Z", "+00:00")),
            scopes=[AuthenticationScope(scope) for scope in data["scopes"]],
            refresh_token=data.get("refreshToken"),
        )

    def is_expired(self) -> bool:
        """Check if the access token has expired."""
        return datetime.now(self.expires_at.tzinfo) >= self.expires_at


class AuthenticationError(Exception):
    """Base exception for authentication errors."""

    pass


class AuthenticationFlowError(AuthenticationError):
    """Error during authentication flow initiation."""

    def __init__(self, reason: str, message: str):
        self.reason = reason
        self.message = message
        super().__init__(f"{reason}: {message}")


class TokenRefreshError(AuthenticationError):
    """Error during token refresh."""

    def __init__(self, reason: str, message: str):
        self.reason = reason
        self.message = message
        super().__init__(f"{reason}: {message}")
