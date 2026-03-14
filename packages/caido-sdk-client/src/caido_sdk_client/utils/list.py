"""List builder for cursor-based paginated queries."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Literal, TypeVar

from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.types.connection import (
    Connection,
    ConnectionQueryResult,
)

T = TypeVar("T")
FilterT = TypeVar("FilterT")
OrderT = TypeVar("OrderT")


@dataclass
class ListBuilderVars(Generic[FilterT, OrderT]):
    """Variables for a list/connection query."""

    first: int | None = None
    after: str | None = None
    last: int | None = None
    before: str | None = None
    filter: FilterT | None = None
    order: OrderT | None = None


class ListBuilder(ABC, Generic[T, FilterT, OrderT]):
    """List builder: chain methods then await the builder or await execute() to run the query."""

    def __await__(self):
        """Make the builder directly awaitable so you can await the chain without calling .execute()."""
        return self.execute().__await__()

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql
        self._vars: ListBuilderVars[FilterT, OrderT] = ListBuilderVars()

    def after(self, cursor: str) -> ListBuilder[T, FilterT, OrderT]:
        self._vars.after = cursor
        return self

    def before(self, cursor: str) -> ListBuilder[T, FilterT, OrderT]:
        self._vars.before = cursor
        return self

    def first(self, n: int) -> ListBuilder[T, FilterT, OrderT]:
        self._vars.first = n
        return self

    def last(self, n: int) -> ListBuilder[T, FilterT, OrderT]:
        self._vars.last = n
        return self

    def filter(self, filter: FilterT) -> ListBuilder[T, FilterT, OrderT]:
        self._vars.filter = filter
        return self

    def order(self, order: OrderT) -> ListBuilder[T, FilterT, OrderT]:
        self._vars.order = order
        return self

    async def execute(self) -> Connection[T]:
        result = await self._query(self._vars)
        default_first = 100

        async def query_fn(
            cursor: str, direction: Literal["next", "prev"]
        ) -> ConnectionQueryResult[T]:
            vars = ListBuilderVars[FilterT, OrderT](
                first=self._vars.first
                if self._vars.first is not None
                else default_first,
                after=self._vars.after,
                last=self._vars.last,
                before=self._vars.before,
                filter=self._vars.filter,
                order=self._vars.order,
            )
            if direction == "next":
                vars.after = cursor
            else:
                vars.before = cursor
            return await self._query(vars)

        return Connection(
            page_info=result.page_info,
            edges=result.edges,
            _query_fn=query_fn,
        )

    @abstractmethod
    async def _query(
        self, vars: ListBuilderVars[FilterT, OrderT]
    ) -> ConnectionQueryResult[T]:
        """Run the connection query with the given variables. Subclasses must implement."""
