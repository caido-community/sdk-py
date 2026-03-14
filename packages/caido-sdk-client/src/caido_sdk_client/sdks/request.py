"""SDK for HTTP requests and responses."""

from __future__ import annotations

from typing import Literal, overload

from caido_sdk_client.convert.connection import map_to_page_info
from caido_sdk_client.convert.request import map_to_request_response_opt
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    Ordering,
    Request,
    RequestResponseOrderBy,
    RequestResponseOrderInput,
    Requests,
)
from caido_sdk_client.types.connection import (
    ConnectionQueryResult,
    Edge,
)
from caido_sdk_client.types.request import (
    RequestGetOptions,
    RequestResponseOpt,
)
from caido_sdk_client.types.strings import Cursor, Httpql, IdLike
from caido_sdk_client.utils.list import ListBuilder, ListBuilderVars

# Request order field (req) -> GraphQL enum
_REQUEST_ORDER_BY: dict[str, RequestResponseOrderBy] = {
    "created_at": RequestResponseOrderBy.CREATED_AT,
    "ext": RequestResponseOrderBy.FILE_EXTENSION,
    "host": RequestResponseOrderBy.HOST,
    "id": RequestResponseOrderBy.ID,
    "method": RequestResponseOrderBy.METHOD,
    "path": RequestResponseOrderBy.PATH,
    "query": RequestResponseOrderBy.QUERY,
    "source": RequestResponseOrderBy.SOURCE,
}

# Response order field (resp) -> GraphQL enum
_RESP_ORDER_BY: dict[str, RequestResponseOrderBy] = {
    "length": RequestResponseOrderBy.RESP_LENGTH,
    "roundtrip": RequestResponseOrderBy.RESP_ROUNDTRIP_TIME,
    "code": RequestResponseOrderBy.RESP_STATUS_CODE,
}


class RequestsListBuilder(
    ListBuilder[RequestResponseOpt, Httpql, RequestResponseOrderInput]
):
    """List builder for requests."""

    def __init__(self, graphql: GraphQLClient) -> None:
        super().__init__(graphql)
        self._scope_id: str | None = None
        self._include_request_raw = True
        self._include_response_raw = True

    @overload
    def ascending(
        self,
        target: Literal["req"],
        field: Literal[
            "ext", "host", "id", "method", "path", "query", "created_at", "source"
        ],
    ) -> RequestsListBuilder: ...
    @overload
    def ascending(
        self, target: Literal["resp"], field: Literal["length", "roundtrip", "code"]
    ) -> RequestsListBuilder: ...
    def ascending(
        self,
        target: Literal["req", "resp"],
        field: str,
    ) -> RequestsListBuilder:
        by = _REQUEST_ORDER_BY[field] if target == "req" else _RESP_ORDER_BY[field]
        self.order(RequestResponseOrderInput(by=by, ordering=Ordering.ASC))
        return self

    @overload
    def descending(
        self,
        target: Literal["req"],
        field: Literal[
            "ext", "host", "id", "method", "path", "query", "created_at", "source"
        ],
    ) -> RequestsListBuilder: ...
    @overload
    def descending(
        self, target: Literal["resp"], field: Literal["length", "roundtrip", "code"]
    ) -> RequestsListBuilder: ...
    def descending(
        self,
        target: Literal["req", "resp"],
        field: str,
    ) -> RequestsListBuilder:
        by = _REQUEST_ORDER_BY[field] if target == "req" else _RESP_ORDER_BY[field]
        self.order(RequestResponseOrderInput(by=by, ordering=Ordering.DESC))
        return self

    def include_raw(
        self,
        options: bool | dict[str, bool] | None = None,
    ) -> RequestsListBuilder:
        """Include request/response raw body. Default both True."""
        if options is None:
            return self
        if isinstance(options, bool):
            self._include_request_raw = options
            self._include_response_raw = options
        else:
            self._include_request_raw = options.get("request", True)
            self._include_response_raw = options.get("response", True)
        return self

    def scope(self, scope_id: IdLike) -> RequestsListBuilder:
        """Filter requests by scope ID."""
        self._scope_id = str(scope_id)
        return self

    async def _query(
        self,
        vars: ListBuilderVars[Httpql, RequestResponseOrderInput],
    ) -> ConnectionQueryResult[RequestResponseOpt]:
        raw = await self._graphql.query(
            Requests.Meta.document,
            variables={
                "first": vars.first,
                "after": vars.after,
                "last": vars.last,
                "before": vars.before,
                "filter": vars.filter,
                "order": (
                    vars.order.model_dump(by_alias=True)
                    if vars.order is not None
                    else None
                ),
                "scopeId": self._scope_id,
                "includeRequestRaw": self._include_request_raw,
                "includeResponseRaw": self._include_response_raw,
            },
        )
        model = Requests.model_validate(raw)
        conn = model.requests
        page_info = map_to_page_info(conn.pageInfo)
        edges = [
            Edge(
                cursor=Cursor(e.cursor),
                node=map_to_request_response_opt(e.node),
            )
            for e in conn.edges
        ]
        return ConnectionQueryResult(page_info=page_info, edges=edges)


class RequestSDK:
    """SDK for HTTP requests and responses."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    def list(self) -> RequestsListBuilder:
        """List requests. Chain with .first(50), .filter(...), etc. then await the builder or await .execute()."""
        return RequestsListBuilder(self._graphql)

    async def get(
        self,
        id: IdLike,
        options: RequestGetOptions | None = None,
    ) -> RequestResponseOpt | None:
        """Get a request by ID. Returns None if it does not exist."""
        opts = options or RequestGetOptions()
        request_raw = (
            opts.request_raw
            if opts.request_raw is not None
            else (opts.raw if opts.raw is not None else True)
        )
        response_raw = (
            opts.response_raw
            if opts.response_raw is not None
            else (opts.raw if opts.raw is not None else True)
        )
        raw = await self._graphql.query(
            Request.Meta.document,
            variables={
                "id": id,
                "includeRequestRaw": request_raw,
                "includeResponseRaw": response_raw,
            },
        )
        model = Request.model_validate(raw)
        if model.request is None:
            return None
        return map_to_request_response_opt(model.request)
