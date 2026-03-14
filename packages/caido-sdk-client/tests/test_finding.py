"""Tests for the Finding SDK."""

from __future__ import annotations

import pytest

from caido_sdk_client import Client
from tests.utils import create_mock_finding, create_mock_request


@pytest.mark.usefixtures("test_project")
async def test_list_findings_with_pagination(caido: Client) -> None:
    """List findings with first(2) and next() page."""
    await create_mock_request()
    await create_mock_finding("1", client=caido)
    await create_mock_finding("1", client=caido)
    await create_mock_finding("1", client=caido)

    findings = await caido.findings.list().first(2)
    assert len(findings.edges) == 2
    assert findings.page_info.has_next_page is True
    assert findings.edges[0].node.request_id == "1"
    assert findings.edges[1].node.request_id == "1"

    next_findings = await findings.next()
    assert next_findings is not None
    assert len(next_findings.edges) == 1
    assert next_findings.page_info.has_next_page is False
    assert next_findings.edges[0].node.request_id == "1"
