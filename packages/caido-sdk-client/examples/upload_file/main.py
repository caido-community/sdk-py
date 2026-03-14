"""Example: connect to a Caido instance and upload a file."""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

from caido_sdk_client import (
    AuthCacheFile,
    Client,
    PATAuthOptions,
    UploadHostedFileOptions,
)


async def main() -> int:
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8080")

    pat = os.environ.get("CAIDO_PAT", "")
    if pat == "":
        print("Error: CAIDO_PAT environment variable is required", file=sys.stderr)
        print("   Set it with: export CAIDO_PAT=caido_xxxxx", file=sys.stderr)
        return 1

    file_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("test.txt")
    file_name = sys.argv[2] if len(sys.argv) > 2 else file_path.name

    if not file_path.exists():
        print(f'Error: Could not read file "{file_path}"', file=sys.stderr)
        print(f"   No such file or directory", file=sys.stderr)
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

    print(f'Uploading file "{file_name}"...')
    hosted_file = await client.hosted_file.upload(
        options=UploadHostedFileOptions(name=file_name, file=file_path),
    )

    print("File uploaded successfully!")
    print(f"   ID: {hosted_file.id}")
    print(f"   Name: {hosted_file.name}")
    print(f"   Path: {hosted_file.path}")
    print(f"   Size: {hosted_file.size} bytes")
    print(f"   Status: {hosted_file.status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
