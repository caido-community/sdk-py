"""Top-level SDK client composed of lower-level and high-level APIs."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

import aiohttp

from caido_sdk_client.auth import AuthManager, AuthOptions
from caido_sdk_client.errors import InstanceNotReadyError
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.logger import ConsoleLogger, Logger
from caido_sdk_client.sdks import (
    EnvironmentSDK,
    FilterSDK,
    FindingSDK,
    HostedFileSDK,
    InstanceSDK,
    ProjectSDK,
    UserSDK,
)
from caido_sdk_client.utils import sleep


@dataclass(frozen=True, slots=True)
class ReadyOptions:
    """Options for the ready() method."""

    interval: int = 5000
    """Interval between health checks in milliseconds."""

    retries: int = 5
    """Maximum number of retries before giving up."""

    timeout: int = 5000
    """Per-request timeout in milliseconds."""


@dataclass(frozen=True, slots=True)
class ConnectOptions:
    """Options for the connect() method."""

    ready: ReadyOptions | bool = True
    """Whether to wait for the instance to be ready after authentication.
    If True, uses default ready options.
    If False, skips the ready check.
    If a ReadyOptions object, uses those options for the ready check.
    """


@dataclass(frozen=True, slots=True)
class Health:
    """Health status of a Caido instance."""

    name: str
    version: str
    ready: bool


class Client:
    """Client for interacting with a Caido instance."""

    graphql: GraphQLClient
    user: UserSDK
    project: ProjectSDK
    environment: EnvironmentSDK
    filter: FilterSDK
    findings: FindingSDK
    hosted_file: HostedFileSDK
    instance: InstanceSDK

    def __init__(
        self,
        url: str,
        *,
        auth: AuthOptions | None = None,
        headers: Mapping[str, str] | None = None,
        timeout_ms: int | None = None,
        logger: Logger | None = None,
    ) -> None:
        self._url = url.rstrip("/")
        self._logger = logger or ConsoleLogger()
        self._auth = AuthManager(
            instance_url=self._url,
            logger=self._logger,
            auth_options=auth,
        )
        self.graphql = GraphQLClient(
            url,
            self._auth,
            headers=headers,
            timeout_ms=timeout_ms,
        )
        self.user = UserSDK(self.graphql)
        self.project = ProjectSDK(self.graphql)
        self.environment = EnvironmentSDK(self.graphql)
        self.filter = FilterSDK(self.graphql)
        self.findings = FindingSDK(self.graphql)
        self.hosted_file = HostedFileSDK(self.graphql)
        self.instance = InstanceSDK(self.graphql)

    async def __aenter__(self) -> Client:
        return self

    async def __aexit__(
        self,
        exc_type: object,
        exc_val: object,
        exc_tb: object,
    ) -> None:
        return None

    async def aclose(self) -> None:
        """Close the client (no-op for now)."""
        return None

    async def connect(self, options: ConnectOptions | None = None) -> None:
        """Connect to the Caido instance.

        This must be called before making any API requests.
        It will wait for the instance to be ready and then authenticate.
        """
        ready_option = options.ready if options is not None else True
        if ready_option is not False:
            await self.ready(
                ready_option if isinstance(ready_option, ReadyOptions) else None
            )

        await self._auth.authenticate()

    async def health(self, *, timeout: int | None = None) -> Health:
        """Check the health status of the Caido instance.

        Pings the /health endpoint and returns instance metadata.
        """
        url = f"{self._url}/health"
        client_timeout = (
            aiohttp.ClientTimeout(total=timeout / 1000)
            if timeout is not None
            else aiohttp.ClientTimeout(total=5)
        )
        async with aiohttp.ClientSession(timeout=client_timeout) as session:
            async with session.get(url) as response:
                data = await response.json()
                return Health(
                    name=data["name"],
                    version=data["version"],
                    ready=data["ready"],
                )

    async def ready(self, options: ReadyOptions | None = None) -> None:
        """Wait for the Caido instance to be ready.

        Polls the health endpoint until the instance reports ready,
        or raises InstanceNotReadyError after exhausting retries.
        """
        opts = options or ReadyOptions()
        interval = opts.interval
        max_retries = opts.retries
        timeout = opts.timeout

        attempts = 0

        async def check_health() -> bool:
            try:
                result = await self.health(timeout=timeout)
                return result.ready
            except Exception:
                return False

        while attempts < max_retries:
            is_ready = await check_health()
            if is_ready:
                return

            attempts += 1
            if attempts < max_retries:
                await sleep(interval)

        raise InstanceNotReadyError(max_retries)
