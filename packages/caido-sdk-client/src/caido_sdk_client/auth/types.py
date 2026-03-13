"""Authentication option types."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Union

from caido_sdk_client.auth.cache.types import TokenCache


@dataclass(frozen=True, slots=True)
class AuthCacheFile:
    """File-based cache configuration. Path is relative to cwd or absolute."""

    file: str


@dataclass(frozen=True, slots=True)
class AuthCacheLocalStorage:
    """LocalStorage-based cache configuration (browser only)."""

    localstorage: str


AuthCacheOptions = Union[AuthCacheFile, AuthCacheLocalStorage, TokenCache]


@dataclass(frozen=True, slots=True)
class TokenPair:
    """A pair of access and refresh tokens."""

    access_token: str
    refresh_token: str | None = None


@dataclass(frozen=True, slots=True)
class PATAuthOptions:
    """Authenticate using a Personal Access Token (PAT)."""

    pat: str
    cache: AuthCacheOptions | None = None


@dataclass(frozen=True, slots=True)
class TokenAuthOptions:
    """Authenticate with a direct access token or token pair."""

    token: str | TokenPair
    cache: AuthCacheOptions | None = None


@dataclass(frozen=True, slots=True)
class BrowserAuthOptions:
    """Authenticate via browser-based device code flow."""

    on_request: Callable[[Any], None] | None = None
    cache: AuthCacheOptions | None = None


AuthOptions = Union[PATAuthOptions, TokenAuthOptions, BrowserAuthOptions]
