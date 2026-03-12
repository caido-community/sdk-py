"""Browser-approval authentication example."""

from __future__ import annotations

import asyncio
import os
import sys

from caido_server_auth import (
    AuthClient,
    AuthClientOptions,
    AuthenticationError,
    AuthenticationRequest,
    BrowserApprover,
)


def on_request(request: AuthenticationRequest) -> None:
    print("=== Authentication Required ===")
    print(f"Visit: {request.verification_url}")
    print(f"Expires at: {request.expires_at.isoformat()}")
    print("===============================")
    print("Waiting for approval...")


async def main() -> int:
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8082")
    print(f"Connecting to Caido instance at: {instance_url}")

    approver = BrowserApprover(on_request)
    auth = AuthClient(AuthClientOptions(instance_url=instance_url, approver=approver))

    try:
        token = await auth.start_authentication_flow()
        print("\nAuthentication successful!")
        print(f"Access Token: {token.access_token[:20]}...")
        print(f"Expires at: {token.expires_at.isoformat()}")
        print(f"Refresh Token: {token.refresh_token[:20]}...")
    except AuthenticationError as exc:
        print(f"Authentication error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover - example fallback
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
