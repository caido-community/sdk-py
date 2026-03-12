"""PAT auto-approval authentication example."""

from __future__ import annotations

import asyncio
import os
import sys

from caido_server_auth import (
    AuthClient,
    AuthClientOptions,
    AuthenticationError,
    PATApprover,
    PATApproverOptions,
)


async def main() -> int:
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8080")
    pat = os.environ.get("CAIDO_PAT", "")
    if pat == "":
        print("Error: CAIDO_PAT environment variable is required", file=sys.stderr)
        print("Set it with: export CAIDO_PAT=caido_xxxxx", file=sys.stderr)
        return 1

    print(f"Connecting to Caido instance at: {instance_url}")

    approver = PATApprover(PATApproverOptions(pat=pat))
    auth = AuthClient(AuthClientOptions(instance_url=instance_url, approver=approver))

    try:
        print("Starting authentication flow...")
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
