"""Hosted file types."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Union

from caido_sdk_client.graphql.__generated__.schema import HostedFileStatus
from caido_sdk_client.types.strings import Id

if TYPE_CHECKING:
    from gql import FileVar

# Path (str or Path) or gql FileVar for upload; avoid runtime gql import in types.
UploadHostedFileFileLike = Union[str, Path, "FileVar"]


@dataclass(frozen=True, slots=True)
class HostedFile:
    """Hosted file information."""

    id: Id
    name: str
    path: str
    size: int
    status: HostedFileStatus
    created_at: datetime
    updated_at: datetime


# Type for file input: path (str or Path) or a gql FileVar
UploadHostedFileFileLike = Union[str, Path, "FileVar"]


@dataclass(frozen=True, slots=True)
class UploadHostedFileOptions:
    """Options for uploading a hosted file."""

    name: str
    """The name of the hosted file."""

    file: UploadHostedFileFileLike
    """Path to the file (str or Path) or a gql FileVar instance."""
