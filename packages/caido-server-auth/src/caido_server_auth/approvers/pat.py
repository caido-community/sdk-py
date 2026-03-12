"""PAT-based approver that auto-approves device flows."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode

import aiohttp

from ..errors import CloudError
from ..types import (
    AuthenticationRequest,
    DeviceInformation,
    DeviceInformationPayload,
    DeviceScopePayload,
    HttpMethod,
    OAuth2ErrorPayload,
)

DEFAULT_API_URL = "https://api.caido.io"


@dataclass(frozen=True, slots=True)
class PATApproverOptions:
    """Options for PATApprover."""

    pat: str
    allowed_scopes: tuple[str, ...] | None = None
    api_url: str = DEFAULT_API_URL
    timeout_ms: int | None = None


class PATApprover:
    """Approver that uses a Personal Access Token for auto-approval."""

    def __init__(self, options: PATApproverOptions) -> None:
        self._pat = options.pat
        self._allowed_scopes = options.allowed_scopes
        self._api_url = options.api_url.rstrip("/")
        self._timeout_seconds = (
            options.timeout_ms / 1000 if options.timeout_ms is not None else None
        )

    async def approve(self, request: AuthenticationRequest) -> None:
        # Step 1: Retrieve device information to discover request scopes.
        device_info = await self._get_device_information(request.user_code)
        scopes_to_approve = [scope.name for scope in device_info.scopes]

        # Step 2: Optionally filter scopes if allowed_scopes is configured.
        if self._allowed_scopes is not None:
            allowed = set(self._allowed_scopes)
            scopes_to_approve = [
                scope for scope in scopes_to_approve if scope in allowed
            ]

        # Step 3: Approve the device with the final scope list.
        await self._approve_device(request.user_code, scopes_to_approve)

    async def _send_request(
        self, *, method: HttpMethod, url: str, headers: dict[str, str]
    ) -> tuple[int, bytes]:
        """Send a cloud API request and return status/body."""
        session_timeout = (
            aiohttp.ClientTimeout(total=self._timeout_seconds)
            if self._timeout_seconds is not None
            else None
        )
        session_kwargs: dict[str, Any] = {}
        if session_timeout is not None:
            session_kwargs["timeout"] = session_timeout

        async with aiohttp.ClientSession(**session_kwargs) as session:
            response = await session.request(method=method, url=url, headers=headers)
            body = await response.read()
            return response.status, body

    @staticmethod
    def _parse_oauth2_error(body: bytes) -> tuple[str, str | None, str | None]:
        """Parse OAuth2 error payloads from cloud API responses."""
        error_text = "Unknown error"
        error_code: str | None = None
        error_description: str | None = None

        try:
            raw_data = json.loads(body.decode("utf-8"))
            data = raw_data if isinstance(raw_data, dict) else raw_data
            if isinstance(data, str):
                error_text = data
            else:
                payload: OAuth2ErrorPayload = data
                error_code = payload.get("error")
                error_description = payload.get("error_description")
                error_text = error_description or error_code or error_text
        except Exception:
            text = body.decode("utf-8", errors="replace")
            if text:
                error_text = text

        return error_text, error_code, error_description

    @staticmethod
    def _parse_device_information(body: bytes) -> DeviceInformation:
        """Normalize cloud device information payload into typed models."""
        raw_data = json.loads(body.decode("utf-8"))
        payload = raw_data if isinstance(raw_data, dict) else {}

        raw_scopes = payload.get("scopes", [])
        scopes: list[DeviceScopePayload] = []
        if isinstance(raw_scopes, list):
            for scope in raw_scopes:
                if not isinstance(scope, dict):
                    continue
                name = scope.get("name")
                if not isinstance(name, str):
                    continue
                description = scope.get("description")
                if isinstance(description, str):
                    scopes.append({"name": name, "description": description})
                else:
                    scopes.append({"name": name})

        typed_payload = DeviceInformationPayload(
            user_code=str(payload.get("user_code", "")),
            scopes=scopes,
        )
        return DeviceInformation.from_wire(typed_payload)

    async def _get_device_information(self, user_code: str) -> DeviceInformation:
        query = urlencode({"user_code": user_code})
        url = f"{self._api_url}/oauth2/device/information?{query}"

        status, body = await self._send_request(
            method="GET",
            url=url,
            headers={
                "Authorization": f"Bearer {self._pat}",
                "Accept": "application/json",
            },
        )

        if status < 200 or status >= 300:
            error_text, error_code, error_description = self._parse_oauth2_error(body)
            raise CloudError(
                f"Failed to get device information: {error_text}",
                status_code=status,
                code=error_code,
                reason=error_description,
            )

        try:
            return self._parse_device_information(body)
        except Exception as exc:
            raise CloudError(
                "Failed to parse device information response",
                status_code=status,
            ) from exc

    async def _approve_device(self, user_code: str, scopes: list[str]) -> None:
        query = urlencode({"user_code": user_code, "scope": ",".join(scopes)})
        url = f"{self._api_url}/oauth2/device/approve?{query}"

        status, body = await self._send_request(
            method="POST",
            url=url,
            headers={
                "Authorization": f"Bearer {self._pat}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

        if status < 200 or status >= 300:
            error_text, error_code, error_description = self._parse_oauth2_error(body)
            raise CloudError(
                f"Failed to approve device: {error_text}",
                status_code=status,
                code=error_code,
                reason=error_description,
            )
