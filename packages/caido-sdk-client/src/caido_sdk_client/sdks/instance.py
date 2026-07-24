"""Top-level SDK for instance-wide features."""

from __future__ import annotations

from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.sdks.certificate import CertificateSDK
from caido_sdk_client.sdks.instance_settings import InstanceSettingsSDK


class InstanceSDK:
    """Top-level SDK for instance-wide features."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self.certificate = CertificateSDK(graphql)
        self.settings = InstanceSettingsSDK(graphql)
