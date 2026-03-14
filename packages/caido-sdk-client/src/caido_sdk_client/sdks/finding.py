"""SDK for findings: get, list, create, update."""

from __future__ import annotations

from typing import cast

from caido_sdk_client.convert.connection import map_to_page_info
from caido_sdk_client.convert.finding import map_to_finding
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    CreateFinding,
    FilterClauseFindingInput,
    Finding,
    FindingOrderInput,
    Findings,
    UpdateFinding,
)
from caido_sdk_client.types.connection import ConnectionQueryResult, Edge
from caido_sdk_client.types.finding import (
    CreateFindingOptions,
    UpdateFindingOptions,
)
from caido_sdk_client.types.finding import (
    Finding as FindingType,
)
from caido_sdk_client.utils.errors import handle_graphql_error
from caido_sdk_client.utils.list import ListBuilder, ListBuilderVars


class FindingsListBuilder(
    ListBuilder[FindingType, FilterClauseFindingInput, FindingOrderInput]
):
    """List builder for findings."""

    def __init__(self, graphql: GraphQLClient) -> None:
        super().__init__(graphql)
        self._graphql = graphql

    async def _query(
        self,
        vars: ListBuilderVars[FilterClauseFindingInput, FindingOrderInput],
    ) -> ConnectionQueryResult[FindingType]:
        raw = await self._graphql.query(
            Findings.Meta.document,
            variables={
                "first": vars.first,
                "after": vars.after,
                "last": vars.last,
                "before": vars.before,
                "filter": (
                    vars.filter.model_dump(by_alias=True)
                    if vars.filter is not None
                    else None
                ),
                "order": (
                    vars.order.model_dump(by_alias=True)
                    if vars.order is not None
                    else None
                ),
            },
        )
        model = Findings.model_validate(raw)
        conn = model.findings
        page_info = map_to_page_info(conn.pageInfo)
        edges = [Edge(cursor=e.cursor, node=map_to_finding(e.node)) for e in conn.edges]
        return ConnectionQueryResult(page_info=page_info, edges=edges)


class FindingSDK:
    """SDK for findings: get, list, create, update."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def get(self, id: str) -> FindingType | None:
        """Get a finding by ID. Returns None if it does not exist."""
        raw = await self._graphql.query(
            Finding.Meta.document,
            variables={"id": id},
        )
        model = Finding.model_validate(raw)
        if model.finding is None:
            return None
        return map_to_finding(model.finding)

    def list(self) -> FindingsListBuilder:
        """List findings. Chain with .first(50), .filter(...), etc. then await the builder or await .execute()."""
        return FindingsListBuilder(self._graphql)

    async def create(
        self, request_id: str, options: CreateFindingOptions
    ) -> FindingType:
        """Create a finding for the given request."""
        raw = await self._graphql.mutation(
            CreateFinding.Meta.document,
            variables={
                "requestId": request_id,
                "input": {
                    "title": options.title,
                    "reporter": options.reporter,
                    "description": options.description,
                    "dedupeKey": options.dedupe_key,
                },
            },
        )
        model = CreateFinding.model_validate(raw)
        payload = model.createFinding
        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))
        if payload.finding is None:
            raise MissingExpectedValueError("createFinding.finding")
        return map_to_finding(payload.finding)

    async def update(self, id: str, options: UpdateFindingOptions) -> FindingType:
        """Update a finding."""
        raw = await self._graphql.mutation(
            UpdateFinding.Meta.document,
            variables={
                "id": id,
                "input": {
                    "title": options.title,
                    "description": options.description,
                    "hidden": options.hidden,
                },
            },
        )
        model = UpdateFinding.model_validate(raw)
        payload = model.updateFinding
        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))
        if payload.finding is None:
            raise MissingExpectedValueError("updateFinding.finding")
        return map_to_finding(payload.finding)
