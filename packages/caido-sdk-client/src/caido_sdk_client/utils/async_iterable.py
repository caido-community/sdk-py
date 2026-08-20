"""Async iterable helpers."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterable, AsyncIterator, Callable, Coroutine
from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")


async def map_async_iterable(
    f: Callable[[T, int], U | Coroutine[object, object, U]],
    source: AsyncIterable[T],
) -> AsyncIterator[U]:
    """Map over an async iterable. f(item, index) may be sync or async."""
    index = 0
    async for item in source:
        out = f(item, index)
        if hasattr(out, "__await__"):
            out = await out  # type: ignore[misc]
        yield out
        index += 1


async def filter_async_iterable(
    f: Callable[[T], bool | Coroutine[object, object, bool]],
    source: AsyncIterable[T],
) -> AsyncIterator[T]:
    """Filter an async iterable. f(item) may be sync or async."""
    async for item in source:
        pred = f(item)
        if hasattr(pred, "__await__"):
            pred = await pred
        if pred:
            yield item


def buffer_async_iterable(source: AsyncIterable[T]) -> AsyncIterator[T]:
    """Start pulling from ``source`` immediately so early items are not missed."""
    iterator = aiter(source)

    async def _next() -> T:
        return await anext(iterator)

    first = asyncio.create_task(_next())

    async def _buffered() -> AsyncIterator[T]:
        try:
            try:
                result = await first
            except StopAsyncIteration:
                return
            while True:
                yield result
                result = await anext(iterator)
        except StopAsyncIteration:
            return
        finally:
            closer = getattr(iterator, "aclose", None)
            if closer is not None:
                await closer()

    return _buffered()
