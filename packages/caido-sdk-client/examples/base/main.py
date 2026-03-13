"""Basic example: connect to a Caido instance and fetch viewer info."""

from __future__ import annotations

import asyncio
import dataclasses
import json
import os
import sys

from caido_sdk_client import AuthCacheFile, Client, PATAuthOptions


async def main() -> int:
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8080")

    pat = os.environ.get("CAIDO_PAT", "")
    if pat == "":
        print("Error: CAIDO_PAT environment variable is required", file=sys.stderr)
        print("   Set it with: export CAIDO_PAT=caido_xxxxx", file=sys.stderr)
        return 1

    client = Client(
        instance_url,
        auth=PATAuthOptions(
            pat=pat,
            cache=AuthCacheFile(file=".secrets.json"),
        ),
    )

    await client.connect()
    print("Connected to Caido instance")

    viewer = await client.user.viewer()
    print("Viewer:", json.dumps(dataclasses.asdict(viewer), indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
