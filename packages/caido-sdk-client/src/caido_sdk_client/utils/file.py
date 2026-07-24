"""File upload utilities."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

from gql import FileVar


def to_file_var(
    file: bytes | str | Path | FileVar,
    *,
    filename: str | None = None,
) -> FileVar:
    """Convert raw bytes or a filesystem path to a GraphQL upload variable.

    Existing ``FileVar`` instances are preserved so callers can provide
    in-memory or streaming content explicitly.
    """
    if isinstance(file, FileVar):
        return file

    if isinstance(file, bytes):
        return FileVar(BytesIO(file), filename=filename)

    return FileVar(str(file))
