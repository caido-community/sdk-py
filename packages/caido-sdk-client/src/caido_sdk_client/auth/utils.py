"""Authentication utility functions."""

from __future__ import annotations

from caido_sdk_client.auth.cache.file import FileTokenCache
from caido_sdk_client.auth.cache.types import TokenCache
from caido_sdk_client.auth.types import (
    AuthCacheFile,
    AuthCacheLocalStorage,
    AuthCacheOptions,
    AuthOptions,
    PATAuthOptions,
    TokenAuthOptions,
)
from caido_sdk_client.logger import Logger


def is_pat_auth(auth: AuthOptions) -> bool:
    return isinstance(auth, PATAuthOptions)


def is_token_auth(auth: AuthOptions) -> bool:
    return isinstance(auth, TokenAuthOptions)


def resolve_cache(options: AuthCacheOptions, logger: Logger) -> TokenCache:
    if isinstance(options, AuthCacheFile):
        return FileTokenCache(path=options.file, logger=logger)
    if isinstance(options, AuthCacheLocalStorage):
        raise NotImplementedError("LocalStorage cache is not supported in Python")
    return options
