"""Higher-level SDK for hosted file-related operations."""

from __future__ import annotations

from typing import List

from gql import FileVar

from caido_sdk_client.convert.hosted_file import map_to_hosted_file
from caido_sdk_client.errors.sdk import MissingExpectedValueError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    DeleteHostedFile,
    HostedFiles,
    RenameHostedFile,
    UploadHostedFile,
)
from caido_sdk_client.types import HostedFile, UploadHostedFileOptions
from caido_sdk_client.types.strings import IdLike


class HostedFileSDK:
    """Higher-level SDK for hosted file-related operations."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def list(self) -> List[HostedFile]:
        """List all hosted files."""
        result = await self._graphql.query(HostedFiles.Meta.document)
        model = HostedFiles.model_validate(result)
        return [map_to_hosted_file(node) for node in model.hostedFiles]

    async def upload(self, options: UploadHostedFileOptions) -> HostedFile:
        """Upload a new hosted file."""
        file_var = (
            options.file
            if isinstance(options.file, FileVar)
            else FileVar(str(options.file))
        )
        result = await self._graphql.mutation(
            UploadHostedFile.Meta.document,
            variables={
                "input": {
                    "name": options.name,
                    "file": file_var,
                },
            },
            upload_files=True,
        )
        model = UploadHostedFile.model_validate(result)
        payload = model.uploadHostedFile

        if payload.hostedFile is None:
            raise MissingExpectedValueError("uploadHostedFile.hostedFile")

        return map_to_hosted_file(payload.hostedFile)

    async def rename(self, id: IdLike, name: str) -> HostedFile:
        """Rename a hosted file."""
        result = await self._graphql.mutation(
            RenameHostedFile.Meta.document,
            variables={"id": id, "name": name},
        )
        model = RenameHostedFile.model_validate(result)
        payload = model.renameHostedFile

        if payload.hostedFile is None:
            raise MissingExpectedValueError("renameHostedFile.hostedFile")

        return map_to_hosted_file(payload.hostedFile)

    async def delete(self, id: IdLike) -> None:
        """Delete a hosted file by ID."""
        result = await self._graphql.mutation(
            DeleteHostedFile.Meta.document,
            variables={"id": id},
        )
        DeleteHostedFile.model_validate(result)
