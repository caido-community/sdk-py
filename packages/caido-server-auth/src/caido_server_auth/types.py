"""Typed models for server authentication."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal, NotRequired, TypedDict


def _parse_iso8601(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


@dataclass(frozen=True, slots=True)
class AuthenticationRequest:
    """Device code authentication request details."""

    id: str
    user_code: str
    verification_url: str
    expires_at: datetime

    @classmethod
    def from_wire(cls, data: "RequestPayload") -> "AuthenticationRequest":
        return cls(
            id=data["id"],
            user_code=data["userCode"],
            verification_url=data["verificationUrl"],
            expires_at=_parse_iso8601(data["expiresAt"]),
        )


@dataclass(frozen=True, slots=True)
class AuthenticationToken:
    """Authentication token obtained after successful authorization."""

    access_token: str
    refresh_token: str
    expires_at: datetime
    scopes: tuple[str, ...]

    @classmethod
    def from_wire(cls, data: "TokenPayload") -> "AuthenticationToken":
        return cls(
            access_token=data["accessToken"],
            refresh_token=data["refreshToken"],
            expires_at=_parse_iso8601(data["expiresAt"]),
            scopes=tuple(data["scopes"]),
        )


@dataclass(frozen=True, slots=True)
class DeviceScope:
    """Scope information returned by the cloud device information API."""

    name: str
    description: str | None = None


@dataclass(frozen=True, slots=True)
class DeviceInformation:
    """Device information returned by the cloud API."""

    user_code: str
    scopes: tuple[DeviceScope, ...]

    @classmethod
    def from_wire(cls, data: "DeviceInformationPayload") -> "DeviceInformation":
        return cls(
            user_code=data["user_code"],
            scopes=tuple(
                DeviceScope(name=scope["name"], description=scope.get("description"))
                for scope in data["scopes"]
            ),
        )


class RequestPayload(TypedDict):
    id: str
    userCode: str
    verificationUrl: str
    expiresAt: str


class TokenPayload(TypedDict):
    accessToken: str
    refreshToken: str
    expiresAt: str
    scopes: list[str]


class AuthenticationUserError(TypedDict):
    code: str
    reason: str


class CloudUserError(TypedDict):
    code: str
    reason: str


class InternalUserError(TypedDict):
    code: str
    message: str


class OtherUserError(TypedDict):
    code: str


StartAuthenticationFlowError = (
    AuthenticationUserError | CloudUserError | InternalUserError | OtherUserError
)
CreatedAuthenticationTokenError = (
    AuthenticationUserError | InternalUserError | OtherUserError
)
RefreshAuthenticationTokenError = (
    AuthenticationUserError | CloudUserError | InternalUserError | OtherUserError
)


class StartAuthenticationFlowPayload(TypedDict):
    request: RequestPayload | None
    error: StartAuthenticationFlowError | None


class StartAuthenticationFlowResponse(TypedDict):
    startAuthenticationFlow: StartAuthenticationFlowPayload


class CreatedAuthenticationTokenPayload(TypedDict):
    token: TokenPayload | None
    error: CreatedAuthenticationTokenError | None


class CreatedAuthenticationTokenResponse(TypedDict):
    createdAuthenticationToken: CreatedAuthenticationTokenPayload


class RefreshAuthenticationTokenPayload(TypedDict):
    token: TokenPayload | None
    error: RefreshAuthenticationTokenError | None


class RefreshAuthenticationTokenResponse(TypedDict):
    refreshAuthenticationToken: RefreshAuthenticationTokenPayload


class OAuth2ErrorPayload(TypedDict, total=False):
    error: str
    error_description: str


class DeviceScopePayload(TypedDict):
    name: str
    description: NotRequired[str]


class DeviceInformationPayload(TypedDict):
    user_code: str
    scopes: list[DeviceScopePayload]


type OAuth2ErrorData = OAuth2ErrorPayload | str
type HttpMethod = Literal["GET", "POST"]
