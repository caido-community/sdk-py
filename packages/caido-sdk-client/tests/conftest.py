"""Pytest configuration and fixtures for SDK client integration tests.

Requires a running Caido instance. Set CAIDO_INSTANCE_URL (default http://localhost:8080)
and CAIDO_PAT (required).
"""

from __future__ import annotations

import os
import random
import string
import time
from collections.abc import AsyncGenerator

import pytest
from caido_sdk_client import Client
from caido_sdk_client.auth import AuthCacheFile, PATAuthOptions
from caido_sdk_client.types import CreateProjectOptions, Project


@pytest.fixture(scope="session")
def caido_client() -> Client:
    """Create a single client for the whole test session (not connected)."""
    instance_url = os.environ.get("CAIDO_INSTANCE_URL", "http://localhost:8080")
    pat = os.environ.get("CAIDO_PAT", "")
    if not pat:
        pytest.skip(
            "CAIDO_PAT environment variable is required for integration tests.",
            allow_module_level=True,
        )

    return Client(
        instance_url,
        auth=PATAuthOptions(
            pat=pat,
            cache=AuthCacheFile(file=".secrets.json"),
        ),
    )


@pytest.fixture(scope="session")
async def caido(caido_client: Client) -> Client:
    """Session-scoped connected client. Connect once per session."""
    await caido_client.connect()
    return caido_client


@pytest.fixture
async def test_project(caido: Client) -> AsyncGenerator[Project, None]:
    """Create a temporary project per test and select it. Deleted after the test."""
    name = f"sdk-test-{int(time.time() * 1000)}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}"
    project = await caido.project.create(
        CreateProjectOptions(name=name, temporary=True)
    )
    await caido.project.select(project.id)
    yield project
    await caido.project.delete(project.id)
