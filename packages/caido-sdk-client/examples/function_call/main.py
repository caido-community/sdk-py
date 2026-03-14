"""Example: call plugin backend functions (e.g. QuickSSRF / Interactsh)."""

from __future__ import annotations

import asyncio
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

    plugin_package = await client.plugin.plugin_package("quickssrf")
    if plugin_package is None:
        print("Error: Plugin package not found", file=sys.stderr)
        return 1

    settings = await plugin_package.call_function("getSettings")
    if not isinstance(settings, dict):
        print("Error: getSettings did not return expected shape", file=sys.stderr)
        return 1

    await plugin_package.call_function(
        "startInteractsh",
        arguments=[
            {
                "serverURL": settings["serverURL"],
                "token": settings["token"],
                "pollingInterval": settings["pollingInterval"],
                "correlationIdLength": settings["correlationIdLength"],
                "correlationIdNonceLength": settings["correlationIdNonceLength"],
            },
        ],
    )

    result = await plugin_package.call_function(
        "generateInteractshUrl",
        arguments=[settings["serverURL"]],
    )
    if not isinstance(result, dict):
        print(
            "Error: generateInteractshUrl did not return expected shape",
            file=sys.stderr,
        )
        return 1

    print("Generated URL:", result.get("url", result))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
