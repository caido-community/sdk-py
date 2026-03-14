"""Higher-level SDK for plugin-related operations."""

from __future__ import annotations

import json
from typing import Any, cast

from gql import FileVar

from caido_sdk_client.errors import NotFoundUserError, PluginFunctionCallError
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    InstallPluginPackage,
    InstallPluginPackageInstallpluginpackage,
    PluginPackageMeta,
    PluginPackageMetaPluginsBasePluginBackend,
    PluginPackageMetaPluginsBasePluginFrontend,
    PluginPackageMetaPluginsBasePluginWorkflow,
    PluginPackages,
)
from caido_sdk_client.rest import RestClient
from caido_sdk_client.types.plugin import (
    InstallPluginPackageOptions,
    InstallPluginPackageSourceFile,
    InstallPluginPackageSourceManifest,
    Plugin,
    PluginBackend,
    PluginFrontend,
    PluginWorkflow,
)
from caido_sdk_client.types.strings import Id
from caido_sdk_client.utils.errors import handle_graphql_error


def _map_plugin(
    p: (
        PluginPackageMetaPluginsBasePluginBackend
        | PluginPackageMetaPluginsBasePluginFrontend
        | PluginPackageMetaPluginsBasePluginWorkflow
        | Any
    ),
) -> Plugin | None:
    """Map a GraphQL plugin fragment to a public Plugin type."""
    typename = getattr(p, "typename", None) or getattr(p, "__typename", None)
    if typename == "PluginBackend":
        return PluginBackend(
            kind="PluginBackend",
            id=Id(p.id),
            manifest_id=p.manifestId,
            enabled=p.enabled,
        )
    if typename == "PluginFrontend":
        return PluginFrontend(
            kind="PluginFrontend",
            id=Id(p.id),
            manifest_id=p.manifestId,
            enabled=p.enabled,
        )
    if typename == "PluginWorkflow":
        return PluginWorkflow(
            kind="PluginWorkflow",
            id=Id(p.id),
            manifest_id=p.manifestId,
            enabled=p.enabled,
        )
    return None


class PluginSDK:
    """Higher-level SDK for plugin-related operations."""

    def __init__(self, graphql: GraphQLClient, rest: RestClient) -> None:
        self._graphql = graphql
        self._rest = rest

    async def plugin_package(self, manifest_id: str) -> PluginPackage | None:
        """Return the plugin package with the given manifest ID, or None."""
        result = await self._graphql.query(PluginPackages.Meta.document)
        model = PluginPackages.model_validate(result)
        for pkg in model.pluginPackages:
            if pkg.manifestId == manifest_id:
                return PluginPackage(self._rest, pkg)
        return None

    async def install(self, options: InstallPluginPackageOptions) -> PluginPackage:
        """Install a plugin package from a manifest ID or file upload.

        Example:
            # Install from manifest ID
            plugin = await client.plugin.install(
                InstallPluginPackageOptions(
                    source=InstallPluginPackageSourceManifest(manifest_id="com.example.plugin")
                )
            )

            # Install from file
            plugin = await client.plugin.install(
                InstallPluginPackageOptions(
                    source=InstallPluginPackageSourceFile(file="/path/to/plugin.zip")
                )
            )
        """
        source = options.source
        if isinstance(source, InstallPluginPackageSourceFile):
            file_val = source.file
            if isinstance(file_val, FileVar):
                source_input = {"file": file_val}
            else:
                source_input = {"file": FileVar(str(file_val))}
        else:
            source_input = {"manifestId": source.manifest_id}

        result = await self._graphql.mutation(
            InstallPluginPackage.Meta.document,
            variables={
                "input": {
                    "source": source_input,
                    "force": options.force,
                },
            },
            upload_files=isinstance(source, InstallPluginPackageSourceFile),
        )
        model = InstallPluginPackage.model_validate(result)
        payload: InstallPluginPackageInstallpluginpackage = model.installPluginPackage

        if payload.error is not None:
            handle_graphql_error(cast(AllErrors, payload.error))

        if payload.package is None:
            raise MissingExpectedValueError("installPluginPackage.package")

        return PluginPackage(self._rest, payload.package)


class PluginPackage:
    """An installed plugin package with one or more plugins (backend, frontend, workflow)."""

    def __init__(self, rest: RestClient, definition: PluginPackageMeta) -> None:
        self._rest = rest
        self._definition = definition

    @property
    def id(self) -> str:
        return self._definition.id

    @property
    def manifest_id(self) -> str:
        return self._definition.manifestId

    @property
    def plugins(self) -> list[Plugin]:
        return [
            plugin
            for p in self._definition.plugins
            if (plugin := _map_plugin(p)) is not None
        ]

    async def call_function(
        self,
        name: str,
        *,
        manifest_id: str | None = None,
        arguments: list[Any] | None = None,
    ) -> Any:
        """Call a function on the plugin backend.

        Specify manifest_id if the package has multiple backend plugins.

        Raises NotFoundUserError if no matching backend plugin is found.
        Raises PluginFunctionCallError if the REST call returns an error.
        """
        backend = None
        for p in self._definition.plugins:
            typename = getattr(p, "typename", None) or getattr(p, "__typename", None)
            if typename != "PluginBackend":
                continue
            if manifest_id is not None and p.manifestId != manifest_id:
                continue
            backend = p
            break

        if backend is None:
            raise NotFoundUserError()

        body: dict[str, Any] = {
            "name": name,
            "args": [json.dumps(arg) for arg in (arguments or [])],
        }

        payload = await self._rest.post(
            f"/plugin/backend/{backend.id}/function",
            body,
        )

        if not isinstance(payload, dict):
            return None

        if payload.get("kind") == "success":
            returns = payload.get("returns")
            if returns is None:
                return None
            return json.loads(returns)

        if payload.get("kind") == "error":
            raise PluginFunctionCallError(name, payload.get("error", payload))
        return None
