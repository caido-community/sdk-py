"""Tests for the Request SDK."""

from __future__ import annotations

import pytest
from caido_sdk_client import Client

from tests.utils import create_mock_request


@pytest.mark.usefixtures("test_project")
async def test_list_requests_with_pagination(caido: Client) -> None:
    """List requests with first(2), descending by created_at, then next page."""
    await create_mock_request()
    await create_mock_request()
    await create_mock_request()

    response = await caido.request.list().first(2).descending("req", "created_at")
    assert len(response.edges) == 2
    assert response.page_info.has_next_page is True
    # Descending created_at: newest first
    first_id = response.edges[0].node.request.id
    second_id = response.edges[1].node.request.id
    assert first_id != second_id

    next_response = await response.next()
    assert next_response is not None
    assert len(next_response.edges) == 1
    assert next_response.page_info.has_next_page is False
    assert next_response.edges[0].node.request.id not in (first_id, second_id)
