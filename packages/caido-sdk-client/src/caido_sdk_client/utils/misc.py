"""Miscellaneous utility functions."""

from __future__ import annotations

import asyncio


async def sleep(ms: float) -> None:
    """Sleep for a given number of milliseconds."""
    await asyncio.sleep(ms / 1000)
