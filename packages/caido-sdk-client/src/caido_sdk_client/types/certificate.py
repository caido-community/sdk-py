"""Certificate SDK input types."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from gql import FileVar

CertificateFileLike = Union[bytes, Path, "FileVar"]


@dataclass(frozen=True, slots=True)
class ImportCertificateOptions:
    """Options for importing a PKCS#12 certificate bundle."""

    file: CertificateFileLike
    password: str | None = None
