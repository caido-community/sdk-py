"""Connection types for cursor-based pagination."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Generic, Literal, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class PageInfo:
    """Information on the current page of paginated data."""

    has_next_page: bool
    has_previous_page: bool
    start_cursor: str | None
    end_cursor: str | None


@dataclass(frozen=True, slots=True)
class Edge(Generic[T]):
    """An edge in a connection."""

    cursor: str
    node: T


@dataclass(frozen=True, slots=True)
class ConnectionQueryResult(Generic[T]):
    """Result of a single connection query (page)."""

    page_info: PageInfo
    edges: list[Edge[T]]


ConnectionQueryFn = Callable[
    [str, Literal["next", "prev"]], Awaitable[ConnectionQueryResult[T]]
]


@dataclass(slots=True)
class Connection(Generic[T]):
    """A connection of items with cursor-based pagination."""

    page_info: PageInfo
    edges: list[Edge[T]]
    _query_fn: ConnectionQueryFn[T]

    async def next(self) -> Connection[T] | None:
        """Fetch the next page if available."""
        if not self.page_info.has_next_page or not self.page_info.end_cursor:
            return None
        result = await self._query_fn(self.page_info.end_cursor, "next")
        return Connection(
            page_info=result.page_info,
            edges=result.edges,
            _query_fn=self._query_fn,
        )

    async def prev(self) -> Connection[T] | None:
        """Fetch the previous page if available."""
        if not self.page_info.has_previous_page or not self.page_info.start_cursor:
            return None
        result = await self._query_fn(self.page_info.start_cursor, "prev")
        return Connection(
            page_info=result.page_info,
            edges=result.edges,
            _query_fn=self._query_fn,
        )
