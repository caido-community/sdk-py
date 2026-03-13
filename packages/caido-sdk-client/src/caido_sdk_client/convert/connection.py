"""Conversion helpers for connection/pageInfo from GraphQL."""

from __future__ import annotations

from typing import Protocol

from caido_sdk_client.types.connection import PageInfo


class _PageInfoLike(Protocol):
    """Protocol for GraphQL pageInfo shape."""

    hasNextPage: bool
    hasPreviousPage: bool
    startCursor: str | None
    endCursor: str | None


def map_to_page_info(page_info: _PageInfoLike) -> PageInfo:
    """Convert GraphQL pageInfo into the public PageInfo type."""
    return PageInfo(
        has_next_page=page_info.hasNextPage,
        has_previous_page=page_info.hasPreviousPage,
        start_cursor=page_info.startCursor,
        end_cursor=page_info.endCursor,
    )
