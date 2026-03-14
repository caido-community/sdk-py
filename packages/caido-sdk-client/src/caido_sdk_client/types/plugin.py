"""Plugin-related types."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Union

from caido_sdk_client.types.strings import Id


@dataclass(frozen=True, slots=True)
class InstallPluginPackageOptions:
    """Options for installing a plugin package.

    Provide either source.file (path or file-like) or source.manifest_id.
    """

    source: Union[
        "InstallPluginPackageSourceFile", "InstallPluginPackageSourceManifest"
    ]
    force: bool = False


@dataclass(frozen=True, slots=True)
class InstallPluginPackageSourceFile:
    """Install from a plugin package file (e.g. a .zip path)."""

    file: str | Path | Any
    """Path to the plugin package file, or a gql FileVar for uploads."""


@dataclass(frozen=True, slots=True)
class InstallPluginPackageSourceManifest:
    """Install from the store by manifest ID."""

    manifest_id: str


@dataclass(frozen=True, slots=True)
class PluginBackend:
    """Backend plugin (can run and call functions)."""

    kind: Literal["PluginBackend"]
    id: Id
    manifest_id: str
    enabled: bool


@dataclass(frozen=True, slots=True)
class PluginFrontend:
    """Frontend plugin."""

    kind: Literal["PluginFrontend"]
    id: Id
    manifest_id: str
    enabled: bool


@dataclass(frozen=True, slots=True)
class PluginWorkflow:
    """Workflow plugin."""

    kind: Literal["PluginWorkflow"]
    id: Id
    manifest_id: str
    enabled: bool


Plugin = PluginBackend | PluginFrontend | PluginWorkflow
