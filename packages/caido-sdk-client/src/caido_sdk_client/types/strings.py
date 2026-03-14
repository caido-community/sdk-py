"""Typed string classes for IDs, cursors, and HTTPQL.

These are subclasses of str so they behave as plain strings at runtime,
while allowing the type system to distinguish them. Pydantic-compatible.
"""

from __future__ import annotations

from typing import Any

from pydantic_core import core_schema


def _make_str_subclass_schema(cls: type[str], handler: Any) -> core_schema.CoreSchema:
    """Build a Pydantic core schema that accepts str and returns an instance of cls."""
    return core_schema.union_schema(
        [
            core_schema.is_instance_schema(cls),
            core_schema.no_info_after_validator_function(cls, handler(str)),
        ]
    )


class Id(str):
    """Entity ID (project, finding, environment, etc.). Subclass of str; use for type clarity."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: Any
    ) -> core_schema.CoreSchema:
        return _make_str_subclass_schema(cls, handler)


class Cursor(str):
    """Pagination cursor. Subclass of str; use for type clarity."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: Any
    ) -> core_schema.CoreSchema:
        return _make_str_subclass_schema(cls, handler)


class Httpql(str):
    """HTTPQL filter clause. Subclass of str; use for type clarity."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: Any
    ) -> core_schema.CoreSchema:
        return _make_str_subclass_schema(cls, handler)
