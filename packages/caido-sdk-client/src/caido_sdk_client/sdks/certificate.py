"""Higher-level certificate operations."""

from __future__ import annotations

from typing import cast

from caido_sdk_client.convert.certificate import (
    map_to_certificate,
    map_to_certificate_generation,
)
from caido_sdk_client.errors.all_errors import AllErrors
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    GetCertificate,
    ImportCertificate,
    RegenerateCertificate,
)
from caido_sdk_client.types.certificate import ImportCertificateOptions
from caido_sdk_client.utils.errors import handle_graphql_error
from caido_sdk_client.utils.file import to_file_var


class CertificateSDK:
    """SDK for exporting, importing, and regenerating certificates."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def export(self, password: str | None = None) -> bytes:
        raw = await self._graphql.query(
            GetCertificate.Meta.document, variables={"password": password}
        )
        model = GetCertificate.model_validate(raw)
        return map_to_certificate(model.runtime.certificate.p12)

    async def import_(self, options: ImportCertificateOptions) -> None:
        raw = await self._graphql.mutation(
            ImportCertificate.Meta.document,
            variables={
                "input": {
                    "certificate": {
                        "p12": {
                            "file": to_file_var(
                                options.file, filename="certificate.p12"
                            ),
                            "password": options.password,
                        }
                    }
                }
            },
            upload_files=True,
        )
        error = ImportCertificate.model_validate(raw).importCertificate.error
        if error is not None:
            handle_graphql_error(cast(AllErrors, error))

    async def generate(self) -> bool:
        raw = await self._graphql.mutation(RegenerateCertificate.Meta.document)
        model = RegenerateCertificate.model_validate(raw)
        return map_to_certificate_generation(model.regenerateCertificate.success)
