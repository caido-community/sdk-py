"""Low-level REST client for the Caido REST API."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import aiohttp

from caido_sdk_client.errors.rest import RestRequestError
from caido_sdk_client.logger import Logger


class RestClient:
    """Low-level REST client for making HTTP requests to a Caido instance."""

    def __init__(
        self,
        base_url: str,
        auth: Any,
        logger: Logger,
        *,
        timeout_ms: int | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._auth = auth
        self._logger = logger
        self._timeout_seconds = (
            int(timeout_ms / 1000) if timeout_ms is not None else None
        )

    async def get(
        self,
        path: str,
        *,
        headers: Mapping[str, str] | None = None,
        timeout_ms: int | None = None,
        params: Mapping[str, str] | None = None,
    ) -> Any:
        """Perform a GET request.

        Returns the parsed JSON response.
        """
        return await self._request(
            "GET",
            path,
            body=None,
            headers=headers,
            timeout_ms=timeout_ms,
            params=params,
        )

    async def post(
        self,
        path: str,
        body: Any = None,
        *,
        headers: Mapping[str, str] | None = None,
        timeout_ms: int | None = None,
    ) -> Any:
        """Perform a POST request.

        Body is JSON-serialized. Returns the parsed JSON response.
        """
        return await self._request(
            "POST", path, body=body, headers=headers, timeout_ms=timeout_ms
        )

    async def _request(
        self,
        method: str,
        path: str,
        *,
        body: Any = None,
        headers: Mapping[str, str] | None = None,
        timeout_ms: int | None = None,
        params: Mapping[str, str] | None = None,
    ) -> Any:
        url = f"{self._base_url}{path}"
        if params:
            from urllib.parse import urlencode

            url = f"{url}?{urlencode(params)}"

        request_headers: dict[str, str] = {
            "Accept": "application/json",
            **(dict(headers) if headers else {}),
        }
        access_token = self._auth.get_access_token()
        if access_token is not None:
            request_headers["Authorization"] = f"Bearer {access_token}"

        if body is not None:
            request_headers["Content-Type"] = "application/json"

        timeout_seconds = (
            int(timeout_ms / 1000) if timeout_ms is not None else self._timeout_seconds
        )
        timeout = (
            aiohttp.ClientTimeout(total=timeout_seconds)
            if timeout_seconds is not None
            else aiohttp.ClientTimeout(total=5)
        )

        has_refreshed = False

        async with aiohttp.ClientSession(timeout=timeout) as session:
            response = await self._do_request(
                session, method, url, body, request_headers
            )

            if (
                response.status == 401
                and not has_refreshed
                and self._auth.can_refresh()
            ):
                self._logger.debug("Received 401, attempting token refresh")
                await self._auth.refresh()
                has_refreshed = True
                request_headers["Authorization"] = (
                    f"Bearer {self._auth.get_access_token()}"
                )
                response = await self._do_request(
                    session, method, url, body, request_headers
                )

            if not response.ok:
                error_text = await response.text()
                raise RestRequestError(method, path, response.status, error_text)

            content_type = response.headers.get("Content-Type") or ""
            if "application/json" in content_type:
                return await response.json()
            return None

    async def _do_request(
        self,
        session: aiohttp.ClientSession,
        method: str,
        url: str,
        body: Any,
        headers: dict[str, str],
    ) -> aiohttp.ClientResponse:
        kwargs: dict[str, Any] = {"headers": headers}
        if body is not None:
            import json

            kwargs["data"] = json.dumps(body)
        return await session.request(method, url, **kwargs)
