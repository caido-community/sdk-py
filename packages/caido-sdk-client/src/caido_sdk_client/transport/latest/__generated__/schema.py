from enum import Enum
from typing import Annotated, List, Literal, Optional, Union

from caido_sdk_client.utils.pydantic import Model
from gql import FileVar
from pydantic import ConfigDict, Field


class Deprecated:
    """Marks a field as deprecated, carrying the GraphQL deprecation reason."""

    def __init__(self, reason=None):
        self.reason = reason

    def __repr__(self):
        return "Deprecated(" + repr(self.reason) + ")"


class CertificateErrorReason(str, Enum):
    """No documentation"""

    INVALID_CERTIFICATE = "INVALID_CERTIFICATE"
    INVALID_P12 = "INVALID_P12"
    INVALID_PASSWORD = "INVALID_PASSWORD"
    INVALID_PRIVATE_KEY = "INVALID_PRIVATE_KEY"


class CloudErrorReason(str, Enum):
    """No documentation"""

    UNAVAILABLE = "UNAVAILABLE"
    UNEXPECTED = "UNEXPECTED"


class EnvironmentVariableKind(str, Enum):
    """No documentation"""

    PLAIN = "PLAIN"
    SECRET = "SECRET"


class FindingOrderBy(str, Enum):
    """No documentation"""

    CREATED_AT = "CREATED_AT"
    HOST = "HOST"
    ID = "ID"
    PATH = "PATH"
    REPORTER = "REPORTER"
    TITLE = "TITLE"


class HostedFileStatus(str, Enum):
    """No documentation"""

    ERROR = "ERROR"
    READY = "READY"


class Ordering(str, Enum):
    """No documentation"""

    ASC = "ASC"
    DESC = "DESC"


class PermissionDeniedErrorReason(str, Enum):
    """No documentation"""

    ENTITLEMENT = "ENTITLEMENT"
    GUEST_USER = "GUEST_USER"
    SCRIPT_USER = "SCRIPT_USER"


class PluginErrorReason(str, Enum):
    """No documentation"""

    ALREADY_INSTALLED = "ALREADY_INSTALLED"
    INVALID_MANIFEST = "INVALID_MANIFEST"
    INVALID_OPERATION = "INVALID_OPERATION"
    INVALID_PACKAGE = "INVALID_PACKAGE"
    MISSING_FILE = "MISSING_FILE"


class ProjectErrorReason(str, Enum):
    """No documentation"""

    DELETING = "DELETING"
    EXPORTING = "EXPORTING"
    INVALID_VERSION = "INVALID_VERSION"
    NOT_READY = "NOT_READY"
    TOO_RECENT = "TOO_RECENT"


class ProjectStatus(str, Enum):
    """No documentation"""

    ERROR = "ERROR"
    READY = "READY"
    RESTORING = "RESTORING"


class RankErrorReason(str, Enum):
    """No documentation"""

    CONCURRENT_UPDATE = "CONCURRENT_UPDATE"
    INVALID_AFTER_BEFORE = "INVALID_AFTER_BEFORE"
    NOT_ENABLED = "NOT_ENABLED"


class ReplaySessionKind(str, Enum):
    """No documentation"""

    HTTP = "HTTP"
    WS = "WS"


class RequestResponseOrderBy(str, Enum):
    """No documentation"""

    CREATED_AT = "CREATED_AT"
    FILE_EXTENSION = "FILE_EXTENSION"
    HOST = "HOST"
    ID = "ID"
    METHOD = "METHOD"
    PATH = "PATH"
    QUERY = "QUERY"
    RESP_LENGTH = "RESP_LENGTH"
    RESP_ROUNDTRIP_TIME = "RESP_ROUNDTRIP_TIME"
    RESP_STATUS_CODE = "RESP_STATUS_CODE"
    SOURCE = "SOURCE"


class SettingsNetworkStack(str, Enum):
    """No documentation"""

    V1 = "V1"
    V2 = "V2"


class StoreErrorReason(str, Enum):
    """No documentation"""

    FILE_UNAVAILABLE = "FILE_UNAVAILABLE"
    INVALID_PUBLIC_KEY = "INVALID_PUBLIC_KEY"
    INVALID_SIGNATURE = "INVALID_SIGNATURE"
    PACKAGE_TOO_LARGE = "PACKAGE_TOO_LARGE"
    PACKAGE_UNKNOWN = "PACKAGE_UNKNOWN"


class StreamMessageDirection(str, Enum):
    """No documentation"""

    CLIENT = "CLIENT"
    SERVER = "SERVER"


class StreamWsMessageFormat(str, Enum):
    """No documentation"""

    BINARY = "BINARY"
    CLOSE = "CLOSE"
    PING = "PING"
    PONG = "PONG"
    TEXT = "TEXT"


class TaskStatus(str, Enum):
    """No documentation"""

    CANCELLED = "CANCELLED"
    DONE = "DONE"
    ERROR = "ERROR"


class WorkflowErrorReason(str, Enum):
    """No documentation"""

    EXECUTION_ERROR = "EXECUTION_ERROR"
    INVALID_INPUT = "INVALID_INPUT"
    INVALID_PROPERTY = "INVALID_PROPERTY"
    INVALID_TRIGGER = "INVALID_TRIGGER"
    INVALID_WORKFLOW = "INVALID_WORKFLOW"


class WorkflowKind(str, Enum):
    """No documentation"""

    ACTIVE = "ACTIVE"
    CONVERT = "CONVERT"
    PASSIVE = "PASSIVE"


class AIProviderAnthropicInput(Model):
    """No documentation"""

    apiKey: str


class AIProviderGoogleInput(Model):
    """No documentation"""

    apiKey: str


class AIProviderOpenAIInput(Model):
    """No documentation"""

    apiKey: str
    url: Optional[str] = None


class AIProviderOpenRouterInput(Model):
    """No documentation"""

    apiKey: str


class CertificateInput(Model):
    """No documentation"""

    p12: Optional["CertificateInputP12"] = None


class CertificateInputP12(Model):
    """No documentation"""

    file: FileVar
    password: Optional[str] = None


class ConnectionInfoInput(Model):
    """No documentation"""

    SNI: Optional[str] = None
    host: str
    isTLS: bool
    port: int


class CreateDNSRewriteInput(Model):
    """No documentation"""

    allowlist: List[str]
    denylist: List[str]
    resolution: "DNSResolverInput"


class CreateDNSUpstreamInput(Model):
    """No documentation"""

    ip: str
    name: str


class CreateEnvironmentInput(Model):
    """No documentation"""

    name: str
    variables: List["EnvironmentVariableInput"]


class CreateFilterPresetInput(Model):
    """No documentation"""

    alias: str
    clause: "QueryInput"
    global_: bool = Field(alias="global")
    name: str


class CreateFindingInput(Model):
    """No documentation"""

    dedupeKey: Optional[str] = None
    description: Optional[str] = None
    reporter: str
    title: str


class CreateProjectInput(Model):
    """No documentation"""

    name: str
    temporary: bool


class CreateReplaySessionCollectionInput(Model):
    """No documentation"""

    name: str


class CreateReplaySessionInput(Model):
    """No documentation"""

    collectionId: Optional[str] = None
    kind: ReplaySessionKind
    requestSource: Optional["RequestSourceInput"] = None
    settings: Optional["ReplaySessionSettingsInput"] = None


class CreateScopeInput(Model):
    """No documentation"""

    allowlist: List[str]
    denylist: List[str]
    name: str


class CreateWorkflowInput(Model):
    """No documentation"""

    definition: dict
    global_: bool = Field(alias="global")


class DNSIpResolverInput(Model):
    """No documentation"""

    ip: str


class DNSResolverInput(Model):
    """No documentation"""

    ip: Optional[DNSIpResolverInput] = None
    upstream: Optional["DNSUpstreamResolverInput"] = None


class DNSUpstreamResolverInput(Model):
    """No documentation"""

    id: str


class DeleteFindingsInput(Model):
    """No documentation"""

    ids: Optional[List[str]] = None
    reporter: Optional[str] = None


class EnvironmentVariableInput(Model):
    """No documentation"""

    kind: EnvironmentVariableKind
    name: str
    value: str


class FilterClauseFindingInput(Model):
    """No documentation"""

    reporter: Optional[str] = None


class FindingOrderInput(Model):
    """No documentation"""

    by: FindingOrderBy
    ordering: Ordering


class HTTPQLInput(Model):
    """No documentation"""

    code: str


class ImportCertificateInput(Model):
    """No documentation"""

    certificate: CertificateInput


class InstallPluginPackageInput(Model):
    """No documentation"""

    force: Optional[bool] = None
    source: "PluginPackageSource"


class PluginPackageSource(Model):
    """No documentation"""

    file: Optional[FileVar] = None
    manifestId: Optional[str] = None
    url: Optional[str] = None


class QueryInput(Model):
    """No documentation"""

    HTTPQL: Optional[HTTPQLInput] = None
    streamQL: Optional["StreamQLInput"] = None


class RangeInput(Model):
    """No documentation"""

    end: int
    start: int


class ReplayEntryHttpSettingsInput(Model):
    """No documentation"""

    placeholders: List["ReplayPlaceholderInput"]


class ReplayEntryWsSettingsInput(Model):
    """No documentation"""

    serverTimeoutMs: int


class ReplayEnvironmentPreprocessorInput(Model):
    """No documentation"""

    variableName: str


class ReplayPlaceholderInput(Model):
    """No documentation"""

    inputRange: RangeInput
    outputRange: RangeInput
    preprocessors: List["ReplayPreprocessorInput"]


class ReplayPrefixPreprocessorInput(Model):
    """No documentation"""

    value: str


class ReplayPreprocessorInput(Model):
    """No documentation"""

    options: "ReplayPreprocessorOptionsInput"


class ReplayPreprocessorOptionsInput(Model):
    """No documentation"""

    environment: Optional[ReplayEnvironmentPreprocessorInput] = None
    prefix: Optional[ReplayPrefixPreprocessorInput] = None
    suffix: Optional["ReplaySuffixPreprocessorInput"] = None
    urlEncode: Optional["ReplayUrlEncodePreprocessorInput"] = None
    workflow: Optional["ReplayWorkflowPreprocessorInput"] = None


class ReplaySessionHttpSettingsInput(Model):
    """No documentation"""

    connectionClose: bool
    updateContentLength: bool


class ReplaySessionSettingsInput(Model):
    """No documentation"""

    http: Optional[ReplaySessionHttpSettingsInput] = None


class ReplaySuffixPreprocessorInput(Model):
    """No documentation"""

    value: str


class ReplayUrlEncodePreprocessorInput(Model):
    """No documentation"""

    charset: Optional[str] = None
    nonAscii: bool


class ReplayWorkflowPreprocessorInput(Model):
    """No documentation"""

    id: str


class RequestRawInput(Model):
    """No documentation"""

    connectionInfo: ConnectionInfoInput
    raw: str


class RequestResponseOrderInput(Model):
    """No documentation"""

    by: RequestResponseOrderBy
    ordering: Ordering


class RequestSourceInput(Model):
    """No documentation"""

    id: Optional[str] = None
    raw: Optional[RequestRawInput] = None


class ResponseRawInput(Model):
    """No documentation"""

    raw: str


class RunActiveWorkflowInput(Model):
    """No documentation"""

    requestId: str


class SetInstanceSettingsInput(Model):
    """No documentation"""

    aiProvider: Optional["SettingsAIProviderInput"] = None
    analytics: Optional["SettingsAnalyticInput"] = None
    network: Optional["SettingsNetworkInput"] = None
    onboarding: Optional["SettingsOnboardingInput"] = None


class SettingsAIProviderInput(Model):
    """No documentation"""

    anthropic: Optional[AIProviderAnthropicInput] = None
    google: Optional[AIProviderGoogleInput] = None
    openai: Optional[AIProviderOpenAIInput] = None
    openrouter: Optional[AIProviderOpenRouterInput] = None


class SettingsAnalyticInput(Model):
    """No documentation"""

    enabled: bool


class SettingsNetworkInput(Model):
    """No documentation"""

    stack: SettingsNetworkStack


class SettingsOnboardingInput(Model):
    """No documentation"""

    analytic: bool


class StreamQLInput(Model):
    """No documentation"""

    code: str


class TestWorkflowActiveInput(Model):
    """No documentation"""

    definition: dict
    request: RequestRawInput
    response: Optional[ResponseRawInput] = None


class TestWorkflowConvertInput(Model):
    """No documentation"""

    data: str
    definition: dict


class TestWorkflowPassiveInput(Model):
    """No documentation"""

    definition: dict
    request: RequestRawInput
    response: Optional[ResponseRawInput] = None


class UpdateEnvironmentInput(Model):
    """No documentation"""

    name: str
    variables: List[EnvironmentVariableInput]
    version: int


class UpdateFilterPresetInput(Model):
    """No documentation"""

    alias: str
    clause: QueryInput
    global_: bool = Field(alias="global")
    name: str


class UpdateFindingInput(Model):
    """No documentation"""

    description: Optional[str] = None
    hidden: Optional[bool] = None
    title: Optional[str] = None


class UpdateReplayEntryDraftInput(Model):
    """No documentation"""

    http: Optional["UpdateReplayEntryHttpDraftInput"] = None
    ws: Optional["UpdateReplayEntryWsDraftInput"] = None


class UpdateReplayEntryHttpDraftInput(Model):
    """No documentation"""

    connection: ConnectionInfoInput
    editorState: str
    raw: str
    settings: ReplayEntryHttpSettingsInput


class UpdateReplayEntryWsDraftInput(Model):
    """No documentation"""

    direction: StreamMessageDirection
    editorState: str
    format: StreamWsMessageFormat
    raw: str
    settings: ReplayEntryWsSettingsInput


class UpdateScopeInput(Model):
    """No documentation"""

    allowlist: List[str]
    denylist: List[str]
    name: str


class UpdateWorkflowInput(Model):
    """No documentation"""

    definition: dict


class UploadHostedFileInput(Model):
    """No documentation"""

    file: FileVar
    name: str


class ConnectionInfoFull(Model):
    """No documentation"""

    typename: Literal["ConnectionInfo"] = Field(
        alias="__typename", default="ConnectionInfo"
    )
    host: str
    port: int
    isTLS: bool
    SNI: Optional[str] = Field(default=None)

    class Meta:
        """Meta class for ConnectionInfoFull"""

        document = "fragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}"
        name = "ConnectionInfoFull"
        type = "ConnectionInfo"


class DnsRewriteFullDNSIpResolverInlineFragment(Model):
    typename: Literal["DNSIpResolver"] = Field(
        alias="__typename", default="DNSIpResolver"
    )
    ip: str


class DnsRewriteFullDNSUpstreamResolverInlineFragment(Model):
    typename: Literal["DNSUpstreamResolver"] = Field(
        alias="__typename", default="DNSUpstreamResolver"
    )
    id: str


class DnsRewriteFull(Model):
    """No documentation"""

    typename: Literal["DNSRewrite"] = Field(alias="__typename", default="DNSRewrite")
    id: str
    allowlist: List[str]
    denylist: List[str]
    enabled: bool
    rank: str
    resolution: Union[
        DnsRewriteFullDNSIpResolverInlineFragment,
        DnsRewriteFullDNSUpstreamResolverInlineFragment,
    ]

    class Meta:
        """Meta class for DnsRewriteFull"""

        document = "fragment DnsRewriteFull on DNSRewrite {\n  id\n  allowlist\n  denylist\n  enabled\n  rank\n  resolution {\n    __typename\n    ... on DNSIpResolver {\n      ip\n    }\n    ... on DNSUpstreamResolver {\n      id\n    }\n  }\n  __typename\n}"
        name = "DnsRewriteFull"
        type = "DNSRewrite"


class DnsUpstreamFull(Model):
    """No documentation"""

    typename: Literal["DNSUpstream"] = Field(alias="__typename", default="DNSUpstream")
    id: str
    ip: str
    name: str

    class Meta:
        """Meta class for DnsUpstreamFull"""

        document = "fragment DnsUpstreamFull on DNSUpstream {\n  id\n  ip\n  name\n  __typename\n}"
        name = "DnsUpstreamFull"
        type = "DNSUpstream"


class EnvironmentFullVariables(Model):
    """No documentation"""

    typename: Literal["EnvironmentVariable"] = Field(
        alias="__typename", default="EnvironmentVariable"
    )
    name: str
    value: str
    kind: EnvironmentVariableKind


class EnvironmentFull(Model):
    """No documentation"""

    typename: Literal["Environment"] = Field(alias="__typename", default="Environment")
    id: str
    name: str
    variables: List[EnvironmentFullVariables]
    version: int

    class Meta:
        """Meta class for EnvironmentFull"""

        document = "fragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}"
        name = "EnvironmentFull"
        type = "Environment"


class UserErrorFullBase(Model):
    """No documentation"""

    code: str


class UserErrorFullCatch(UserErrorFullBase):
    """Catch all class for UserErrorFullBase"""

    typename: str = Field(alias="__typename")
    "No documentation"
    code: str


class UserErrorFullAIUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["AIUserError"] = Field(alias="__typename", default="AIUserError")


class UserErrorFullAliasTakenUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["AliasTakenUserError"] = Field(
        alias="__typename", default="AliasTakenUserError"
    )


class UserErrorFullAssistantUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["AssistantUserError"] = Field(
        alias="__typename", default="AssistantUserError"
    )


class UserErrorFullAuthenticationUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["AuthenticationUserError"] = Field(
        alias="__typename", default="AuthenticationUserError"
    )


class UserErrorFullAuthorizationUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["AuthorizationUserError"] = Field(
        alias="__typename", default="AuthorizationUserError"
    )


class UserErrorFullAutomateTaskUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["AutomateTaskUserError"] = Field(
        alias="__typename", default="AutomateTaskUserError"
    )


class UserErrorFullBackupUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["BackupUserError"] = Field(
        alias="__typename", default="BackupUserError"
    )


class UserErrorFullCertificateUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["CertificateUserError"] = Field(
        alias="__typename", default="CertificateUserError"
    )


class UserErrorFullCloudUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["CloudUserError"] = Field(
        alias="__typename", default="CloudUserError"
    )


class UserErrorFullInternalUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InternalUserError"] = Field(
        alias="__typename", default="InternalUserError"
    )


class UserErrorFullInvalidGlobTermsUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InvalidGlobTermsUserError"] = Field(
        alias="__typename", default="InvalidGlobTermsUserError"
    )


class UserErrorFullInvalidHTTPQLUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InvalidHTTPQLUserError"] = Field(
        alias="__typename", default="InvalidHTTPQLUserError"
    )


class UserErrorFullInvalidRangeUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InvalidRangeUserError"] = Field(
        alias="__typename", default="InvalidRangeUserError"
    )


class UserErrorFullInvalidRegexUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InvalidRegexUserError"] = Field(
        alias="__typename", default="InvalidRegexUserError"
    )


class UserErrorFullInvalidStreamQLUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InvalidStreamQLUserError"] = Field(
        alias="__typename", default="InvalidStreamQLUserError"
    )


class UserErrorFullNameTakenUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["NameTakenUserError"] = Field(
        alias="__typename", default="NameTakenUserError"
    )


class UserErrorFullNewerVersionUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["NewerVersionUserError"] = Field(
        alias="__typename", default="NewerVersionUserError"
    )


class UserErrorFullOtherUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["OtherUserError"] = Field(
        alias="__typename", default="OtherUserError"
    )


class UserErrorFullPermissionDeniedUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["PermissionDeniedUserError"] = Field(
        alias="__typename", default="PermissionDeniedUserError"
    )


class UserErrorFullPluginUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["PluginUserError"] = Field(
        alias="__typename", default="PluginUserError"
    )


class UserErrorFullProjectUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["ProjectUserError"] = Field(
        alias="__typename", default="ProjectUserError"
    )


class UserErrorFullRankUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["RankUserError"] = Field(
        alias="__typename", default="RankUserError"
    )


class UserErrorFullReadOnlyUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["ReadOnlyUserError"] = Field(
        alias="__typename", default="ReadOnlyUserError"
    )


class UserErrorFullRenderFailedUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["RenderFailedUserError"] = Field(
        alias="__typename", default="RenderFailedUserError"
    )


class UserErrorFullStoreUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["StoreUserError"] = Field(
        alias="__typename", default="StoreUserError"
    )


class UserErrorFullTaskInProgressUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["TaskInProgressUserError"] = Field(
        alias="__typename", default="TaskInProgressUserError"
    )


class UserErrorFullUnknownIdUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["UnknownIdUserError"] = Field(
        alias="__typename", default="UnknownIdUserError"
    )


class UserErrorFullUnsupportedPlatformUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["UnsupportedPlatformUserError"] = Field(
        alias="__typename", default="UnsupportedPlatformUserError"
    )


class UserErrorFullWSUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["WSUserError"] = Field(alias="__typename", default="WSUserError")


class UserErrorFullWorkflowUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["WorkflowUserError"] = Field(
        alias="__typename", default="WorkflowUserError"
    )


class HTTPQLQueryFull(Model):
    """No documentation"""

    typename: Literal["HTTPQL"] = Field(alias="__typename", default="HTTPQL")
    code: str

    class Meta:
        """Meta class for HTTPQLQueryFull"""

        document = "fragment HTTPQLQueryFull on HTTPQL {\n  __typename\n  code\n}"
        name = "HTTPQLQueryFull"
        type = "HTTPQL"


class StreamQLQueryFull(Model):
    """No documentation"""

    typename: Literal["StreamQL"] = Field(alias="__typename", default="StreamQL")
    code: str

    class Meta:
        """Meta class for StreamQLQueryFull"""

        document = "fragment StreamQLQueryFull on StreamQL {\n  __typename\n  code\n}"
        name = "StreamQLQueryFull"
        type = "StreamQL"


class FindingFullRequest(Model):
    """No documentation"""

    typename: Literal["Request"] = Field(alias="__typename", default="Request")
    id: str


class FindingFull(Model):
    """No documentation"""

    typename: Literal["Finding"] = Field(alias="__typename", default="Finding")
    id: str
    request: FindingFullRequest
    title: str
    reporter: str
    description: Optional[str] = Field(default=None)
    dedupeKey: Optional[str] = Field(default=None)
    host: str
    path: str
    hidden: bool
    createdAt: int

    class Meta:
        """Meta class for FindingFull"""

        document = "fragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}"
        name = "FindingFull"
        type = "Finding"


class HostedFileFull(Model):
    """No documentation"""

    typename: Literal["HostedFile"] = Field(alias="__typename", default="HostedFile")
    id: str
    name: str
    path: str
    size: int
    status: HostedFileStatus
    createdAt: str
    updatedAt: str

    class Meta:
        """Meta class for HostedFileFull"""

        document = "fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}"
        name = "HostedFileFull"
        type = "HostedFile"


class InstanceAIProviderAnthropicFull(Model):
    """No documentation"""

    typename: Literal["AIProviderAnthropic"] = Field(
        alias="__typename", default="AIProviderAnthropic"
    )
    apiKey: str

    class Meta:
        """Meta class for InstanceAIProviderAnthropicFull"""

        document = "fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}"
        name = "InstanceAIProviderAnthropicFull"
        type = "AIProviderAnthropic"


class InstanceAIProviderGoogleFull(Model):
    """No documentation"""

    typename: Literal["AIProviderGoogle"] = Field(
        alias="__typename", default="AIProviderGoogle"
    )
    apiKey: str

    class Meta:
        """Meta class for InstanceAIProviderGoogleFull"""

        document = "fragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}"
        name = "InstanceAIProviderGoogleFull"
        type = "AIProviderGoogle"


class InstanceAIProviderOpenAIFull(Model):
    """No documentation"""

    typename: Literal["AIProviderOpenAI"] = Field(
        alias="__typename", default="AIProviderOpenAI"
    )
    apiKey: str
    url: Optional[str] = Field(default=None)

    class Meta:
        """Meta class for InstanceAIProviderOpenAIFull"""

        document = "fragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}"
        name = "InstanceAIProviderOpenAIFull"
        type = "AIProviderOpenAI"


class InstanceAIProviderOpenRouterFull(Model):
    """No documentation"""

    typename: Literal["AIProviderOpenRouter"] = Field(
        alias="__typename", default="AIProviderOpenRouter"
    )
    apiKey: str

    class Meta:
        """Meta class for InstanceAIProviderOpenRouterFull"""

        document = "fragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}"
        name = "InstanceAIProviderOpenRouterFull"
        type = "AIProviderOpenRouter"


class PluginPackageMetaPluginsBase(Model):
    """No documentation"""

    id: str
    manifestId: str
    enabled: bool


class PluginPackageMetaPluginsBasePluginBackend(PluginPackageMetaPluginsBase, Model):
    """No documentation"""

    typename: Literal["PluginBackend"] = Field(
        alias="__typename", default="PluginBackend"
    )


class PluginPackageMetaPluginsBasePluginFrontend(PluginPackageMetaPluginsBase, Model):
    """No documentation"""

    typename: Literal["PluginFrontend"] = Field(
        alias="__typename", default="PluginFrontend"
    )


class PluginPackageMetaPluginsBasePluginWorkflow(PluginPackageMetaPluginsBase, Model):
    """No documentation"""

    typename: Literal["PluginWorkflow"] = Field(
        alias="__typename", default="PluginWorkflow"
    )


class PluginPackageMetaPluginsBaseCatchAll(PluginPackageMetaPluginsBase, Model):
    """Catch all class for PluginPackageMetaPluginsBase"""

    typename: str = Field(alias="__typename")


class PluginPackageMeta(Model):
    """No documentation"""

    typename: Literal["PluginPackage"] = Field(
        alias="__typename", default="PluginPackage"
    )
    id: str
    manifestId: str
    plugins: List[
        Union[
            Annotated[
                Union[
                    PluginPackageMetaPluginsBasePluginBackend,
                    PluginPackageMetaPluginsBasePluginFrontend,
                    PluginPackageMetaPluginsBasePluginWorkflow,
                ],
                Field(discriminator="typename"),
            ],
            PluginPackageMetaPluginsBaseCatchAll,
        ]
    ]

    class Meta:
        """Meta class for PluginPackageMeta"""

        document = "fragment PluginPackageMeta on PluginPackage {\n  id\n  manifestId\n  plugins {\n    __typename\n    id\n    manifestId\n    enabled\n  }\n  __typename\n}"
        name = "PluginPackageMeta"
        type = "PluginPackage"


class ProjectFull(Model):
    """No documentation"""

    typename: Literal["Project"] = Field(alias="__typename", default="Project")
    id: str
    name: str
    path: str
    status: ProjectStatus
    temporary: bool
    createdAt: str
    updatedAt: str
    version: str
    size: int
    readOnly: bool
    "Defines if the project would be read-only if selected by the caller"

    class Meta:
        """Meta class for ProjectFull"""

        document = "fragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}"
        name = "ProjectFull"
        type = "Project"


class RangeFull(Model):
    """No documentation"""

    typename: Literal["Range"] = Field(alias="__typename", default="Range")
    start: int
    end: int

    class Meta:
        """Meta class for RangeFull"""

        document = "fragment RangeFull on Range {\n  start\n  end\n  __typename\n}"
        name = "RangeFull"
        type = "Range"


class ReplayPrefixPreprocessorFull(Model):
    """No documentation"""

    typename: Literal["ReplayPrefixPreprocessor"] = Field(
        alias="__typename", default="ReplayPrefixPreprocessor"
    )
    value: str

    class Meta:
        """Meta class for ReplayPrefixPreprocessorFull"""

        document = "fragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}"
        name = "ReplayPrefixPreprocessorFull"
        type = "ReplayPrefixPreprocessor"


class ReplaySuffixPreprocessorFull(Model):
    """No documentation"""

    typename: Literal["ReplaySuffixPreprocessor"] = Field(
        alias="__typename", default="ReplaySuffixPreprocessor"
    )
    value: str

    class Meta:
        """Meta class for ReplaySuffixPreprocessorFull"""

        document = "fragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}"
        name = "ReplaySuffixPreprocessorFull"
        type = "ReplaySuffixPreprocessor"


class ReplayUrlEncodePreprocessorFull(Model):
    """No documentation"""

    typename: Literal["ReplayUrlEncodePreprocessor"] = Field(
        alias="__typename", default="ReplayUrlEncodePreprocessor"
    )
    charset: Optional[str] = Field(default=None)
    nonAscii: bool

    class Meta:
        """Meta class for ReplayUrlEncodePreprocessorFull"""

        document = "fragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}"
        name = "ReplayUrlEncodePreprocessorFull"
        type = "ReplayUrlEncodePreprocessor"


class ReplayWorkflowPreprocessorFull(Model):
    """No documentation"""

    typename: Literal["ReplayWorkflowPreprocessor"] = Field(
        alias="__typename", default="ReplayWorkflowPreprocessor"
    )
    id: str

    class Meta:
        """Meta class for ReplayWorkflowPreprocessorFull"""

        document = "fragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}"
        name = "ReplayWorkflowPreprocessorFull"
        type = "ReplayWorkflowPreprocessor"


class ReplayEnvironmentPreprocessorFull(Model):
    """No documentation"""

    typename: Literal["ReplayEnvironmentPreprocessor"] = Field(
        alias="__typename", default="ReplayEnvironmentPreprocessor"
    )
    variableName: str

    class Meta:
        """Meta class for ReplayEnvironmentPreprocessorFull"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}"
        name = "ReplayEnvironmentPreprocessorFull"
        type = "ReplayEnvironmentPreprocessor"


class ReplaySessionHttpMetaCollection(Model):
    """No documentation"""

    typename: Literal["ReplaySessionCollection"] = Field(
        alias="__typename", default="ReplaySessionCollection"
    )
    id: str


class ReplaySessionHttpMetaActiveentryBase(Model):
    """No documentation"""

    id: str


class ReplaySessionHttpMetaActiveentryBaseReplayEntryHttp(
    ReplaySessionHttpMetaActiveentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplaySessionHttpMetaActiveentryBaseReplayEntryWs(
    ReplaySessionHttpMetaActiveentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplaySessionHttpMetaActiveentryBaseCatchAll(
    ReplaySessionHttpMetaActiveentryBase, Model
):
    """Catch all class for ReplaySessionHttpMetaActiveentryBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionHttpMetaEntriesEdgesNodeBase(Model):
    """No documentation"""

    id: str


class ReplaySessionHttpMetaEntriesEdgesNodeBaseReplayEntryHttp(
    ReplaySessionHttpMetaEntriesEdgesNodeBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplaySessionHttpMetaEntriesEdgesNodeBaseReplayEntryWs(
    ReplaySessionHttpMetaEntriesEdgesNodeBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplaySessionHttpMetaEntriesEdgesNodeBaseCatchAll(
    ReplaySessionHttpMetaEntriesEdgesNodeBase, Model
):
    """Catch all class for ReplaySessionHttpMetaEntriesEdgesNodeBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionHttpMetaEntriesEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplayEntryEdge"] = Field(
        alias="__typename", default="ReplayEntryEdge"
    )
    node: Union[
        Annotated[
            Union[
                ReplaySessionHttpMetaEntriesEdgesNodeBaseReplayEntryHttp,
                ReplaySessionHttpMetaEntriesEdgesNodeBaseReplayEntryWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplaySessionHttpMetaEntriesEdgesNodeBaseCatchAll,
    ]
    "The item at the end of the edge"


class ReplaySessionHttpMetaEntries(Model):
    """No documentation"""

    typename: Literal["ReplayEntryConnection"] = Field(
        alias="__typename", default="ReplayEntryConnection"
    )
    edges: List[ReplaySessionHttpMetaEntriesEdges]
    "A list of edges."


class ReplaySessionHttpMetaSettings(Model):
    """No documentation"""

    typename: Literal["ReplaySessionHttpSettings"] = Field(
        alias="__typename", default="ReplaySessionHttpSettings"
    )
    connectionClose: bool
    updateContentLength: bool


class ReplaySessionHttpMeta(Model):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )
    id: str
    name: str
    collection: ReplaySessionHttpMetaCollection
    activeEntry: Optional[
        Union[
            Annotated[
                Union[
                    ReplaySessionHttpMetaActiveentryBaseReplayEntryHttp,
                    ReplaySessionHttpMetaActiveentryBaseReplayEntryWs,
                ],
                Field(discriminator="typename"),
            ],
            ReplaySessionHttpMetaActiveentryBaseCatchAll,
        ]
    ] = Field(default=None)
    entries: ReplaySessionHttpMetaEntries
    settings: Optional[ReplaySessionHttpMetaSettings] = Field(default=None)

    class Meta:
        """Meta class for ReplaySessionHttpMeta"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}"
        name = "ReplaySessionHttpMeta"
        type = "ReplaySessionHttp"


class ReplaySessionWsMetaCollection(Model):
    """No documentation"""

    typename: Literal["ReplaySessionCollection"] = Field(
        alias="__typename", default="ReplaySessionCollection"
    )
    id: str


class ReplaySessionWsMetaActiveentryBase(Model):
    """No documentation"""

    id: str


class ReplaySessionWsMetaActiveentryBaseReplayEntryHttp(
    ReplaySessionWsMetaActiveentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplaySessionWsMetaActiveentryBaseReplayEntryWs(
    ReplaySessionWsMetaActiveentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplaySessionWsMetaActiveentryBaseCatchAll(
    ReplaySessionWsMetaActiveentryBase, Model
):
    """Catch all class for ReplaySessionWsMetaActiveentryBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionWsMetaEntriesEdgesNodeBase(Model):
    """No documentation"""

    id: str


class ReplaySessionWsMetaEntriesEdgesNodeBaseReplayEntryHttp(
    ReplaySessionWsMetaEntriesEdgesNodeBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplaySessionWsMetaEntriesEdgesNodeBaseReplayEntryWs(
    ReplaySessionWsMetaEntriesEdgesNodeBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplaySessionWsMetaEntriesEdgesNodeBaseCatchAll(
    ReplaySessionWsMetaEntriesEdgesNodeBase, Model
):
    """Catch all class for ReplaySessionWsMetaEntriesEdgesNodeBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionWsMetaEntriesEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplayEntryEdge"] = Field(
        alias="__typename", default="ReplayEntryEdge"
    )
    node: Union[
        Annotated[
            Union[
                ReplaySessionWsMetaEntriesEdgesNodeBaseReplayEntryHttp,
                ReplaySessionWsMetaEntriesEdgesNodeBaseReplayEntryWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplaySessionWsMetaEntriesEdgesNodeBaseCatchAll,
    ]
    "The item at the end of the edge"


class ReplaySessionWsMetaEntries(Model):
    """No documentation"""

    typename: Literal["ReplayEntryConnection"] = Field(
        alias="__typename", default="ReplayEntryConnection"
    )
    edges: List[ReplaySessionWsMetaEntriesEdges]
    "A list of edges."


class ReplaySessionWsMeta(Model):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )
    id: str
    name: str
    collection: ReplaySessionWsMetaCollection
    activeEntry: Optional[
        Union[
            Annotated[
                Union[
                    ReplaySessionWsMetaActiveentryBaseReplayEntryHttp,
                    ReplaySessionWsMetaActiveentryBaseReplayEntryWs,
                ],
                Field(discriminator="typename"),
            ],
            ReplaySessionWsMetaActiveentryBaseCatchAll,
        ]
    ] = Field(default=None)
    entries: ReplaySessionWsMetaEntries

    class Meta:
        """Meta class for ReplaySessionWsMeta"""

        document = "fragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"
        name = "ReplaySessionWsMeta"
        type = "ReplaySessionWs"


class ReplaySessionCollectionMeta(Model):
    """No documentation"""

    typename: Literal["ReplaySessionCollection"] = Field(
        alias="__typename", default="ReplaySessionCollection"
    )
    id: str
    name: str

    class Meta:
        """Meta class for ReplaySessionCollectionMeta"""

        document = "fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}"
        name = "ReplaySessionCollectionMeta"
        type = "ReplaySessionCollection"


class ResponseFull(Model):
    """No documentation"""

    typename: Literal["Response"] = Field(alias="__typename", default="Response")
    id: str
    statusCode: int
    roundtripTime: int
    length: int
    createdAt: int
    raw: str

    class Meta:
        """Meta class for ResponseFull"""

        document = "fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}"
        name = "ResponseFull"
        type = "Response"


class ScopeFull(Model):
    """No documentation"""

    typename: Literal["Scope"] = Field(alias="__typename", default="Scope")
    id: str
    name: str
    allowlist: List[str]
    denylist: List[str]
    indexed: bool

    class Meta:
        """Meta class for ScopeFull"""

        document = "fragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}"
        name = "ScopeFull"
        type = "Scope"


class TaskMetaBase(Model):
    """No documentation"""

    id: str
    createdAt: str


class TaskMetaCatch(TaskMetaBase):
    """Catch all class for TaskMetaBase"""

    typename: str = Field(alias="__typename")
    "No documentation"
    id: str
    createdAt: str


class TaskMetaDataExportTask(TaskMetaBase, Model):
    """No documentation"""

    typename: Literal["DataExportTask"] = Field(
        alias="__typename", default="DataExportTask"
    )


class TaskMetaDeleteStreamWsMessageTask(TaskMetaBase, Model):
    """No documentation"""

    typename: Literal["DeleteStreamWsMessageTask"] = Field(
        alias="__typename", default="DeleteStreamWsMessageTask"
    )


class TaskMetaReplayTask(TaskMetaBase, Model):
    """No documentation"""

    typename: Literal["ReplayTask"] = Field(alias="__typename", default="ReplayTask")


class TaskMetaWorkflowTask(TaskMetaBase, Model):
    """No documentation"""

    typename: Literal["WorkflowTask"] = Field(
        alias="__typename", default="WorkflowTask"
    )


class WorkflowFull(Model):
    """No documentation"""

    typename: Literal["Workflow"] = Field(alias="__typename", default="Workflow")
    id: str
    name: str
    kind: WorkflowKind
    definition: dict
    enabled: bool
    global_: bool = Field(alias="global")
    readOnly: bool
    createdAt: str
    updatedAt: str

    class Meta:
        """Meta class for WorkflowFull"""

        document = "fragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}"
        name = "WorkflowFull"
        type = "Workflow"


class CloudUserErrorFull(UserErrorFullCloudUserError, Model):
    """No documentation"""

    typename: Literal["CloudUserError"] = Field(
        alias="__typename", default="CloudUserError"
    )
    cloudReason: CloudErrorReason

    class Meta:
        """Meta class for CloudUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}"
        name = "CloudUserErrorFull"
        type = "CloudUserError"


class NameTakenUserErrorFull(UserErrorFullNameTakenUserError, Model):
    """No documentation"""

    typename: Literal["NameTakenUserError"] = Field(
        alias="__typename", default="NameTakenUserError"
    )
    name: str

    class Meta:
        """Meta class for NameTakenUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}"
        name = "NameTakenUserErrorFull"
        type = "NameTakenUserError"


class UnknownIdUserErrorFull(UserErrorFullUnknownIdUserError, Model):
    """No documentation"""

    typename: Literal["UnknownIdUserError"] = Field(
        alias="__typename", default="UnknownIdUserError"
    )
    id: str

    class Meta:
        """Meta class for UnknownIdUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}"
        name = "UnknownIdUserErrorFull"
        type = "UnknownIdUserError"


class PermissionDeniedUserErrorFull(UserErrorFullPermissionDeniedUserError, Model):
    """No documentation"""

    typename: Literal["PermissionDeniedUserError"] = Field(
        alias="__typename", default="PermissionDeniedUserError"
    )
    permissionReason: PermissionDeniedErrorReason

    class Meta:
        """Meta class for PermissionDeniedUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}"
        name = "PermissionDeniedUserErrorFull"
        type = "PermissionDeniedUserError"


class ProjectUserErrorFull(UserErrorFullProjectUserError, Model):
    """No documentation"""

    typename: Literal["ProjectUserError"] = Field(
        alias="__typename", default="ProjectUserError"
    )
    projectReason: ProjectErrorReason

    class Meta:
        """Meta class for ProjectUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment ProjectUserErrorFull on ProjectUserError {\n  ...UserErrorFull\n  projectReason: reason\n  __typename\n}"
        name = "ProjectUserErrorFull"
        type = "ProjectUserError"


class OtherUserErrorFull(UserErrorFullOtherUserError, Model):
    """No documentation"""

    typename: Literal["OtherUserError"] = Field(
        alias="__typename", default="OtherUserError"
    )

    class Meta:
        """Meta class for OtherUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}"
        name = "OtherUserErrorFull"
        type = "OtherUserError"


class CertificateUserErrorFull(UserErrorFullCertificateUserError, Model):
    """No documentation"""

    typename: Literal["CertificateUserError"] = Field(
        alias="__typename", default="CertificateUserError"
    )
    reason: CertificateErrorReason

    class Meta:
        """Meta class for CertificateUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CertificateUserErrorFull on CertificateUserError {\n  ...UserErrorFull\n  reason\n  __typename\n}"
        name = "CertificateUserErrorFull"
        type = "CertificateUserError"


class ReadOnlyUserErrorFull(UserErrorFullReadOnlyUserError, Model):
    """No documentation"""

    typename: Literal["ReadOnlyUserError"] = Field(
        alias="__typename", default="ReadOnlyUserError"
    )

    class Meta:
        """Meta class for ReadOnlyUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment ReadOnlyUserErrorFull on ReadOnlyUserError {\n  ...UserErrorFull\n  __typename\n}"
        name = "ReadOnlyUserErrorFull"
        type = "ReadOnlyUserError"


class InvalidGlobTermsUserErrorFull(UserErrorFullInvalidGlobTermsUserError, Model):
    """No documentation"""

    typename: Literal["InvalidGlobTermsUserError"] = Field(
        alias="__typename", default="InvalidGlobTermsUserError"
    )
    terms: List[str]

    class Meta:
        """Meta class for InvalidGlobTermsUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment InvalidGlobTermsUserErrorFull on InvalidGlobTermsUserError {\n  ...UserErrorFull\n  terms\n  __typename\n}"
        name = "InvalidGlobTermsUserErrorFull"
        type = "InvalidGlobTermsUserError"


class AliasTakenUserErrorFull(UserErrorFullAliasTakenUserError, Model):
    """No documentation"""

    typename: Literal["AliasTakenUserError"] = Field(
        alias="__typename", default="AliasTakenUserError"
    )
    alias: str

    class Meta:
        """Meta class for AliasTakenUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment AliasTakenUserErrorFull on AliasTakenUserError {\n  ...UserErrorFull\n  alias\n  __typename\n}"
        name = "AliasTakenUserErrorFull"
        type = "AliasTakenUserError"


class NewerVersionUserErrorFull(UserErrorFullNewerVersionUserError, Model):
    """No documentation"""

    typename: Literal["NewerVersionUserError"] = Field(
        alias="__typename", default="NewerVersionUserError"
    )
    version: int

    class Meta:
        """Meta class for NewerVersionUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment NewerVersionUserErrorFull on NewerVersionUserError {\n  ...UserErrorFull\n  version\n  __typename\n}"
        name = "NewerVersionUserErrorFull"
        type = "NewerVersionUserError"


class PluginUserErrorFull(UserErrorFullPluginUserError, Model):
    """No documentation"""

    typename: Literal["PluginUserError"] = Field(
        alias="__typename", default="PluginUserError"
    )
    reason: PluginErrorReason

    class Meta:
        """Meta class for PluginUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment PluginUserErrorFull on PluginUserError {\n  ...UserErrorFull\n  reason\n  __typename\n}"
        name = "PluginUserErrorFull"
        type = "PluginUserError"


class StoreUserErrorFull(UserErrorFullStoreUserError, Model):
    """No documentation"""

    typename: Literal["StoreUserError"] = Field(
        alias="__typename", default="StoreUserError"
    )
    storeReason: StoreErrorReason

    class Meta:
        """Meta class for StoreUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment StoreUserErrorFull on StoreUserError {\n  ...UserErrorFull\n  storeReason: reason\n  __typename\n}"
        name = "StoreUserErrorFull"
        type = "StoreUserError"


class RankUserErrorFull(UserErrorFullRankUserError, Model):
    """No documentation"""

    typename: Literal["RankUserError"] = Field(
        alias="__typename", default="RankUserError"
    )
    rankReason: RankErrorReason

    class Meta:
        """Meta class for RankUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment RankUserErrorFull on RankUserError {\n  ...UserErrorFull\n  rankReason: reason\n  __typename\n}"
        name = "RankUserErrorFull"
        type = "RankUserError"


class TaskInProgressUserErrorFull(UserErrorFullTaskInProgressUserError, Model):
    """No documentation"""

    typename: Literal["TaskInProgressUserError"] = Field(
        alias="__typename", default="TaskInProgressUserError"
    )
    taskId: str

    class Meta:
        """Meta class for TaskInProgressUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment TaskInProgressUserErrorFull on TaskInProgressUserError {\n  ...UserErrorFull\n  taskId\n  __typename\n}"
        name = "TaskInProgressUserErrorFull"
        type = "TaskInProgressUserError"


class WorkflowUserErrorFull(UserErrorFullWorkflowUserError, Model):
    """No documentation"""

    typename: Literal["WorkflowUserError"] = Field(
        alias="__typename", default="WorkflowUserError"
    )
    node: Optional[str] = Field(default=None)
    message: str
    reason: WorkflowErrorReason

    class Meta:
        """Meta class for WorkflowUserErrorFull"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}"
        name = "WorkflowUserErrorFull"
        type = "WorkflowUserError"


class FilterPresetFullHTTPQLInlineFragment(HTTPQLQueryFull, Model):
    pass


class FilterPresetFullStreamQLInlineFragment(StreamQLQueryFull, Model):
    pass


class FilterPresetFull(Model):
    """No documentation"""

    typename: Literal["FilterPreset"] = Field(
        alias="__typename", default="FilterPreset"
    )
    id: str
    name: str
    alias: str
    clause: Union[
        FilterPresetFullHTTPQLInlineFragment, FilterPresetFullStreamQLInlineFragment
    ]

    class Meta:
        """Meta class for FilterPresetFull"""

        document = "fragment HTTPQLQueryFull on HTTPQL {\n  __typename\n  code\n}\n\nfragment StreamQLQueryFull on StreamQL {\n  __typename\n  code\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause {\n    ... on HTTPQL {\n      ...HTTPQLQueryFull\n    }\n    ... on StreamQL {\n      ...StreamQLQueryFull\n    }\n    __typename\n  }\n  __typename\n}"
        name = "FilterPresetFull"
        type = "FilterPreset"


class InstanceSettingsFullAiproviders(Model):
    """No documentation"""

    typename: Literal["AIProviders"] = Field(alias="__typename", default="AIProviders")
    anthropic: Optional[InstanceAIProviderAnthropicFull] = Field(default=None)
    google: Optional[InstanceAIProviderGoogleFull] = Field(default=None)
    openai: Optional[InstanceAIProviderOpenAIFull] = Field(default=None)
    openrouter: Optional[InstanceAIProviderOpenRouterFull] = Field(default=None)


class InstanceSettingsFullAnalytic(Model):
    """No documentation"""

    typename: Literal["AnalyticStatus"] = Field(
        alias="__typename", default="AnalyticStatus"
    )
    enabled: bool
    cloud: bool
    local: bool


class InstanceSettingsFullOnboarding(Model):
    """No documentation"""

    typename: Literal["OnboardingState"] = Field(
        alias="__typename", default="OnboardingState"
    )
    analytic: bool


class InstanceSettingsFull(Model):
    """No documentation"""

    typename: Literal["InstanceSettings"] = Field(
        alias="__typename", default="InstanceSettings"
    )
    aiProviders: InstanceSettingsFullAiproviders
    analytic: InstanceSettingsFullAnalytic
    onboarding: InstanceSettingsFullOnboarding

    class Meta:
        """Meta class for InstanceSettingsFull"""

        document = "fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}\n\nfragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}\n\nfragment InstanceSettingsFull on InstanceSettings {\n  aiProviders {\n    anthropic {\n      ...InstanceAIProviderAnthropicFull\n      __typename\n    }\n    google {\n      ...InstanceAIProviderGoogleFull\n      __typename\n    }\n    openai {\n      ...InstanceAIProviderOpenAIFull\n      __typename\n    }\n    openrouter {\n      ...InstanceAIProviderOpenRouterFull\n      __typename\n    }\n    __typename\n  }\n  analytic {\n    enabled\n    cloud\n    local\n    __typename\n  }\n  onboarding {\n    analytic\n    __typename\n  }\n  __typename\n}"
        name = "InstanceSettingsFull"
        type = "InstanceSettings"


class ReplayPreprocessorFullReplayPrefixPreprocessorInlineFragment(
    ReplayPrefixPreprocessorFull, Model
):
    pass


class ReplayPreprocessorFullReplaySuffixPreprocessorInlineFragment(
    ReplaySuffixPreprocessorFull, Model
):
    pass


class ReplayPreprocessorFullReplayUrlEncodePreprocessorInlineFragment(
    ReplayUrlEncodePreprocessorFull, Model
):
    pass


class ReplayPreprocessorFullReplayWorkflowPreprocessorInlineFragment(
    ReplayWorkflowPreprocessorFull, Model
):
    pass


class ReplayPreprocessorFullReplayEnvironmentPreprocessorInlineFragment(
    ReplayEnvironmentPreprocessorFull, Model
):
    pass


class ReplayPreprocessorFull(Model):
    """No documentation"""

    typename: Literal["ReplayPreprocessor"] = Field(
        alias="__typename", default="ReplayPreprocessor"
    )
    options: Union[
        ReplayPreprocessorFullReplayPrefixPreprocessorInlineFragment,
        ReplayPreprocessorFullReplaySuffixPreprocessorInlineFragment,
        ReplayPreprocessorFullReplayUrlEncodePreprocessorInlineFragment,
        ReplayPreprocessorFullReplayWorkflowPreprocessorInlineFragment,
        ReplayPreprocessorFullReplayEnvironmentPreprocessorInlineFragment,
    ]

    class Meta:
        """Meta class for ReplayPreprocessorFull"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}"
        name = "ReplayPreprocessorFull"
        type = "ReplayPreprocessor"


class ReplaySessionMetaBase(Model):
    """No documentation"""


class ReplaySessionMetaCatch(ReplaySessionMetaBase):
    """Catch all class for ReplaySessionMetaBase"""

    typename: str = Field(alias="__typename")
    "No documentation"


class ReplaySessionMetaReplaySessionHttp(
    ReplaySessionHttpMeta, ReplaySessionMetaBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class ReplaySessionMetaReplaySessionWs(
    ReplaySessionWsMeta, ReplaySessionMetaBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class RequestFullMetadata(Model):
    """No documentation"""

    typename: Literal["RequestMetadata"] = Field(
        alias="__typename", default="RequestMetadata"
    )
    id: str
    color: Optional[str] = Field(default=None)


class RequestFull(Model):
    """No documentation"""

    typename: Literal["Request"] = Field(alias="__typename", default="Request")
    id: str
    host: str
    port: int
    method: str
    path: str
    query: str
    isTls: bool
    metadata: RequestFullMetadata
    createdAt: int
    raw: str
    response: Optional[ResponseFull] = Field(default=None)

    class Meta:
        """Meta class for RequestFull"""

        document = "fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}"
        name = "RequestFull"
        type = "Request"


class ReplayTaskMetaReplayentryBase(Model):
    """No documentation"""

    id: str


class ReplayTaskMetaReplayentryBaseReplayEntryHttp(
    ReplayTaskMetaReplayentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplayTaskMetaReplayentryBaseReplayEntryWs(ReplayTaskMetaReplayentryBase, Model):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplayTaskMetaReplayentryBaseCatchAll(ReplayTaskMetaReplayentryBase, Model):
    """Catch all class for ReplayTaskMetaReplayentryBase"""

    typename: str = Field(alias="__typename")


class ReplayTaskMeta(TaskMetaReplayTask, Model):
    """No documentation"""

    typename: Literal["ReplayTask"] = Field(alias="__typename", default="ReplayTask")
    replayEntry: Union[
        Annotated[
            Union[
                ReplayTaskMetaReplayentryBaseReplayEntryHttp,
                ReplayTaskMetaReplayentryBaseReplayEntryWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplayTaskMetaReplayentryBaseCatchAll,
    ]

    class Meta:
        """Meta class for ReplayTaskMeta"""

        document = "fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}"
        name = "ReplayTaskMeta"
        type = "ReplayTask"


class WorkflowTaskMetaWorkflow(Model):
    """No documentation"""

    typename: Literal["Workflow"] = Field(alias="__typename", default="Workflow")
    id: str


class WorkflowTaskMeta(TaskMetaWorkflowTask, Model):
    """No documentation"""

    typename: Literal["WorkflowTask"] = Field(
        alias="__typename", default="WorkflowTask"
    )
    workflow: WorkflowTaskMetaWorkflow

    class Meta:
        """Meta class for WorkflowTaskMeta"""

        document = "fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment WorkflowTaskMeta on WorkflowTask {\n  ...TaskMeta\n  workflow {\n    id\n    __typename\n  }\n  __typename\n}"
        name = "WorkflowTaskMeta"
        type = "WorkflowTask"


class ReplayPlaceholderFull(Model):
    """No documentation"""

    typename: Literal["ReplayPlaceholder"] = Field(
        alias="__typename", default="ReplayPlaceholder"
    )
    inputRange: RangeFull
    outputRange: RangeFull
    preprocessors: List[ReplayPreprocessorFull]

    class Meta:
        """Meta class for ReplayPlaceholderFull"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}"
        name = "ReplayPlaceholderFull"
        type = "ReplayPlaceholder"


class ReplayEntryHttpFullSessionBase(Model):
    """No documentation"""

    id: str


class ReplayEntryHttpFullSessionBaseReplaySessionHttp(
    ReplayEntryHttpFullSessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class ReplayEntryHttpFullSessionBaseReplaySessionWs(
    ReplayEntryHttpFullSessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class ReplayEntryHttpFullSessionBaseCatchAll(ReplayEntryHttpFullSessionBase, Model):
    """Catch all class for ReplayEntryHttpFullSessionBase"""

    typename: str = Field(alias="__typename")


class ReplayEntryHttpFullSettings(Model):
    """No documentation"""

    typename: Literal["ReplayEntryHttpSettings"] = Field(
        alias="__typename", default="ReplayEntryHttpSettings"
    )
    placeholders: List[ReplayPlaceholderFull]


class ReplayEntryHttpFull(Model):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )
    connection: ConnectionInfoFull
    createdAt: int
    error: Optional[str] = Field(default=None)
    id: str
    raw: str
    request: Optional[RequestFull] = Field(default=None)
    session: Union[
        Annotated[
            Union[
                ReplayEntryHttpFullSessionBaseReplaySessionHttp,
                ReplayEntryHttpFullSessionBaseReplaySessionWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplayEntryHttpFullSessionBaseCatchAll,
    ]
    settings: ReplayEntryHttpFullSettings

    class Meta:
        """Meta class for ReplayEntryHttpFull"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryHttpFull on ReplayEntryHttp {\n  __typename\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n}"
        name = "ReplayEntryHttpFull"
        type = "ReplayEntryHttp"


class ReplayEntryWsFullSessionBase(Model):
    """No documentation"""

    id: str


class ReplayEntryWsFullSessionBaseReplaySessionHttp(
    ReplayEntryWsFullSessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class ReplayEntryWsFullSessionBaseReplaySessionWs(ReplayEntryWsFullSessionBase, Model):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class ReplayEntryWsFullSessionBaseCatchAll(ReplayEntryWsFullSessionBase, Model):
    """Catch all class for ReplayEntryWsFullSessionBase"""

    typename: str = Field(alias="__typename")


class ReplayEntryWsFull(Model):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )
    createdAt: int
    error: Optional[str] = Field(default=None)
    id: str
    http: ReplayEntryHttpFull
    session: Union[
        Annotated[
            Union[
                ReplayEntryWsFullSessionBaseReplaySessionHttp,
                ReplayEntryWsFullSessionBaseReplaySessionWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplayEntryWsFullSessionBaseCatchAll,
    ]

    class Meta:
        """Meta class for ReplayEntryWsFull"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryHttpFull on ReplayEntryHttp {\n  __typename\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplayEntryWsFull on ReplayEntryWs {\n  __typename\n  createdAt\n  error\n  id\n  http {\n    ...ReplayEntryHttpFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n}"
        name = "ReplayEntryWsFull"
        type = "ReplayEntryWs"


class ReplayEntryFullBase(Model):
    """No documentation"""


class ReplayEntryFullCatch(ReplayEntryFullBase):
    """Catch all class for ReplayEntryFullBase"""

    typename: str = Field(alias="__typename")
    "No documentation"


class ReplayEntryFullReplayEntryHttp(ReplayEntryHttpFull, ReplayEntryFullBase, Model):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplayEntryFullReplayEntryWs(ReplayEntryWsFull, ReplayEntryFullBase, Model):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class GetCertificateRuntimeCertificate(Model):
    """No documentation"""

    typename: Literal["Certificate"] = Field(alias="__typename", default="Certificate")
    p12: str


class GetCertificateRuntime(Model):
    """No documentation"""

    typename: Literal["Runtime"] = Field(alias="__typename", default="Runtime")
    certificate: GetCertificateRuntimeCertificate


class GetCertificate(Model):
    """No documentation found for this operation."""

    runtime: GetCertificateRuntime

    class Arguments(Model):
        """Arguments for GetCertificate"""

        password: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for GetCertificate"""

        document = "query GetCertificate($password: Sensitive) {\n  runtime {\n    certificate {\n      p12(password: $password)\n      __typename\n    }\n    __typename\n  }\n}"


class ImportCertificateImportcertificateCertificateUserErrorInlineFragment(
    CertificateUserErrorFull, Model
):
    pass


class ImportCertificateImportcertificateOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class ImportCertificateImportcertificate(Model):
    """No documentation"""

    typename: Literal["ImportCertificatePayload"] = Field(
        alias="__typename", default="ImportCertificatePayload"
    )
    error: Optional[
        Union[
            ImportCertificateImportcertificateCertificateUserErrorInlineFragment,
            ImportCertificateImportcertificateOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class ImportCertificate(Model):
    """No documentation found for this operation."""

    importCertificate: ImportCertificateImportcertificate

    class Arguments(Model):
        """Arguments for ImportCertificate"""

        input: ImportCertificateInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ImportCertificate"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CertificateUserErrorFull on CertificateUserError {\n  ...UserErrorFull\n  reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nmutation ImportCertificate($input: ImportCertificateInput!) {\n  importCertificate(input: $input) {\n    error {\n      __typename\n      ... on CertificateUserError {\n        ...CertificateUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class RegenerateCertificateRegeneratecertificate(Model):
    """No documentation"""

    typename: Literal["RegenerateCertificatePayload"] = Field(
        alias="__typename", default="RegenerateCertificatePayload"
    )
    success: bool


class RegenerateCertificate(Model):
    """No documentation found for this operation."""

    regenerateCertificate: RegenerateCertificateRegeneratecertificate

    class Arguments(Model):
        """Arguments for RegenerateCertificate"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RegenerateCertificate"""

        document = "mutation RegenerateCertificate {\n  regenerateCertificate {\n    success\n    __typename\n  }\n}"


class CreateDnsRewriteCreatednsrewriteOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class CreateDnsRewriteCreatednsrewriteUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class CreateDnsRewriteCreatednsrewrite(Model):
    """No documentation"""

    typename: Literal["CreateDNSRewritePayload"] = Field(
        alias="__typename", default="CreateDNSRewritePayload"
    )
    error: Optional[
        Union[
            CreateDnsRewriteCreatednsrewriteOtherUserErrorInlineFragment,
            CreateDnsRewriteCreatednsrewriteUnknownIdUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    rewrite: Optional[DnsRewriteFull] = Field(default=None)


class CreateDnsRewrite(Model):
    """No documentation found for this operation."""

    createDnsRewrite: CreateDnsRewriteCreatednsrewrite

    class Arguments(Model):
        """Arguments for CreateDnsRewrite"""

        input: CreateDNSRewriteInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateDnsRewrite"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment DnsRewriteFull on DNSRewrite {\n  id\n  allowlist\n  denylist\n  enabled\n  rank\n  resolution {\n    __typename\n    ... on DNSIpResolver {\n      ip\n    }\n    ... on DNSUpstreamResolver {\n      id\n    }\n  }\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation CreateDnsRewrite($input: CreateDNSRewriteInput!) {\n  createDnsRewrite(input: $input) {\n    error {\n      __typename\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n    }\n    rewrite {\n      ...DnsRewriteFull\n      __typename\n    }\n    __typename\n  }\n}"


class DnsUpstreams(Model):
    """No documentation found for this operation."""

    dnsUpstreams: List[DnsUpstreamFull]

    class Arguments(Model):
        """Arguments for DnsUpstreams"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DnsUpstreams"""

        document = "fragment DnsUpstreamFull on DNSUpstream {\n  id\n  ip\n  name\n  __typename\n}\n\nquery DnsUpstreams {\n  dnsUpstreams {\n    ...DnsUpstreamFull\n    __typename\n  }\n}"


class CreateDnsUpstreamCreatednsupstream(Model):
    """No documentation"""

    typename: Literal["CreateDNSUpstreamPayload"] = Field(
        alias="__typename", default="CreateDNSUpstreamPayload"
    )
    upstream: DnsUpstreamFull


class CreateDnsUpstream(Model):
    """No documentation found for this operation."""

    createDnsUpstream: CreateDnsUpstreamCreatednsupstream

    class Arguments(Model):
        """Arguments for CreateDnsUpstream"""

        input: CreateDNSUpstreamInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateDnsUpstream"""

        document = "fragment DnsUpstreamFull on DNSUpstream {\n  id\n  ip\n  name\n  __typename\n}\n\nmutation CreateDnsUpstream($input: CreateDNSUpstreamInput!) {\n  createDnsUpstream(input: $input) {\n    upstream {\n      ...DnsUpstreamFull\n      __typename\n    }\n    __typename\n  }\n}"


class Environments(Model):
    """No documentation found for this operation."""

    environments: List[EnvironmentFull]

    class Arguments(Model):
        """Arguments for Environments"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Environments"""

        document = "fragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nquery Environments {\n  environments {\n    ...EnvironmentFull\n    __typename\n  }\n}"


class EnvironmentQuery(Model):
    """No documentation found for this operation."""

    environment: Optional[EnvironmentFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for EnvironmentQuery"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for EnvironmentQuery"""

        document = "fragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nquery EnvironmentQuery($id: ID!) {\n  environment(id: $id) {\n    ...EnvironmentFull\n    __typename\n  }\n}"


class CreateEnvironmentCreateenvironmentNameTakenUserErrorInlineFragment(
    NameTakenUserErrorFull, Model
):
    pass


class CreateEnvironmentCreateenvironmentPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class CreateEnvironmentCreateenvironmentCloudUserErrorInlineFragment(
    CloudUserErrorFull, Model
):
    pass


class CreateEnvironmentCreateenvironmentOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class CreateEnvironmentCreateenvironment(Model):
    """No documentation"""

    typename: Literal["CreateEnvironmentPayload"] = Field(
        alias="__typename", default="CreateEnvironmentPayload"
    )
    error: Optional[
        Union[
            CreateEnvironmentCreateenvironmentNameTakenUserErrorInlineFragment,
            CreateEnvironmentCreateenvironmentPermissionDeniedUserErrorInlineFragment,
            CreateEnvironmentCreateenvironmentCloudUserErrorInlineFragment,
            CreateEnvironmentCreateenvironmentOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    environment: Optional[EnvironmentFull] = Field(default=None)


class CreateEnvironment(Model):
    """No documentation found for this operation."""

    createEnvironment: CreateEnvironmentCreateenvironment

    class Arguments(Model):
        """Arguments for CreateEnvironment"""

        input: CreateEnvironmentInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateEnvironment"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nmutation CreateEnvironment($input: CreateEnvironmentInput!) {\n  createEnvironment(input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    environment {\n      ...EnvironmentFull\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateEnvironmentUpdateenvironmentUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class UpdateEnvironmentUpdateenvironmentNameTakenUserErrorInlineFragment(
    NameTakenUserErrorFull, Model
):
    pass


class UpdateEnvironmentUpdateenvironmentNewerVersionUserErrorInlineFragment(
    NewerVersionUserErrorFull, Model
):
    pass


class UpdateEnvironmentUpdateenvironmentPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class UpdateEnvironmentUpdateenvironmentOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class UpdateEnvironmentUpdateenvironment(Model):
    """No documentation"""

    typename: Literal["UpdateEnvironmentPayload"] = Field(
        alias="__typename", default="UpdateEnvironmentPayload"
    )
    error: Optional[
        Union[
            UpdateEnvironmentUpdateenvironmentUnknownIdUserErrorInlineFragment,
            UpdateEnvironmentUpdateenvironmentNameTakenUserErrorInlineFragment,
            UpdateEnvironmentUpdateenvironmentNewerVersionUserErrorInlineFragment,
            UpdateEnvironmentUpdateenvironmentPermissionDeniedUserErrorInlineFragment,
            UpdateEnvironmentUpdateenvironmentOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    environment: Optional[EnvironmentFull] = Field(default=None)


class UpdateEnvironment(Model):
    """No documentation found for this operation."""

    updateEnvironment: UpdateEnvironmentUpdateenvironment

    class Arguments(Model):
        """Arguments for UpdateEnvironment"""

        id: str
        input: UpdateEnvironmentInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateEnvironment"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment NewerVersionUserErrorFull on NewerVersionUserError {\n  ...UserErrorFull\n  version\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation UpdateEnvironment($id: ID!, $input: UpdateEnvironmentInput!) {\n  updateEnvironment(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on NewerVersionUserError {\n        ...NewerVersionUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    environment {\n      ...EnvironmentFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteEnvironmentDeleteenvironmentUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class DeleteEnvironmentDeleteenvironmentOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class DeleteEnvironmentDeleteenvironment(Model):
    """No documentation"""

    typename: Literal["DeleteEnvironmentPayload"] = Field(
        alias="__typename", default="DeleteEnvironmentPayload"
    )
    deletedId: Optional[str] = Field(default=None)
    error: Optional[
        Union[
            DeleteEnvironmentDeleteenvironmentUnknownIdUserErrorInlineFragment,
            DeleteEnvironmentDeleteenvironmentOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class DeleteEnvironment(Model):
    """No documentation found for this operation."""

    deleteEnvironment: DeleteEnvironmentDeleteenvironment

    class Arguments(Model):
        """Arguments for DeleteEnvironment"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteEnvironment"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation DeleteEnvironment($id: ID!) {\n  deleteEnvironment(id: $id) {\n    deletedId\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class SelectEnvironmentSelectenvironmentUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class SelectEnvironmentSelectenvironmentOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class SelectEnvironmentSelectenvironmentEnvironmentVariables(Model):
    """No documentation"""

    typename: Literal["EnvironmentVariable"] = Field(
        alias="__typename", default="EnvironmentVariable"
    )
    name: str
    value: str
    kind: EnvironmentVariableKind


class SelectEnvironmentSelectenvironmentEnvironment(Model):
    """No documentation"""

    typename: Literal["Environment"] = Field(alias="__typename", default="Environment")
    id: str
    name: str
    variables: List[SelectEnvironmentSelectenvironmentEnvironmentVariables]
    version: int


class SelectEnvironmentSelectenvironment(Model):
    """No documentation"""

    typename: Literal["SelectEnvironmentPayload"] = Field(
        alias="__typename", default="SelectEnvironmentPayload"
    )
    error: Optional[
        Union[
            SelectEnvironmentSelectenvironmentUnknownIdUserErrorInlineFragment,
            SelectEnvironmentSelectenvironmentOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    environment: Optional[SelectEnvironmentSelectenvironmentEnvironment] = Field(
        default=None
    )


class SelectEnvironment(Model):
    """No documentation found for this operation."""

    selectEnvironment: SelectEnvironmentSelectenvironment

    class Arguments(Model):
        """Arguments for SelectEnvironment"""

        id: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SelectEnvironment"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation SelectEnvironment($id: ID) {\n  selectEnvironment(id: $id) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    environment {\n      id\n      name\n      variables {\n        name\n        value\n        kind\n        __typename\n      }\n      version\n      __typename\n    }\n    __typename\n  }\n}"


class FilterPresets(Model):
    """No documentation found for this operation."""

    filterPresets: List[FilterPresetFull]

    class Arguments(Model):
        """Arguments for FilterPresets"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for FilterPresets"""

        document = "fragment HTTPQLQueryFull on HTTPQL {\n  __typename\n  code\n}\n\nfragment StreamQLQueryFull on StreamQL {\n  __typename\n  code\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause {\n    ... on HTTPQL {\n      ...HTTPQLQueryFull\n    }\n    ... on StreamQL {\n      ...StreamQLQueryFull\n    }\n    __typename\n  }\n  __typename\n}\n\nquery FilterPresets {\n  filterPresets {\n    ...FilterPresetFull\n    __typename\n  }\n}"


class FilterPreset(Model):
    """No documentation found for this operation."""

    filterPreset: Optional[FilterPresetFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for FilterPreset"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for FilterPreset"""

        document = "fragment HTTPQLQueryFull on HTTPQL {\n  __typename\n  code\n}\n\nfragment StreamQLQueryFull on StreamQL {\n  __typename\n  code\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause {\n    ... on HTTPQL {\n      ...HTTPQLQueryFull\n    }\n    ... on StreamQL {\n      ...StreamQLQueryFull\n    }\n    __typename\n  }\n  __typename\n}\n\nquery FilterPreset($id: ID!) {\n  filterPreset(id: $id) {\n    ...FilterPresetFull\n    __typename\n  }\n}"


class CreateFilterPresetCreatefilterpresetNameTakenUserErrorInlineFragment(
    NameTakenUserErrorFull, Model
):
    pass


class CreateFilterPresetCreatefilterpresetAliasTakenUserErrorInlineFragment(
    AliasTakenUserErrorFull, Model
):
    pass


class CreateFilterPresetCreatefilterpresetPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class CreateFilterPresetCreatefilterpresetCloudUserErrorInlineFragment(
    CloudUserErrorFull, Model
):
    pass


class CreateFilterPresetCreatefilterpresetOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class CreateFilterPresetCreatefilterpreset(Model):
    """No documentation"""

    typename: Literal["CreateFilterPresetPayload"] = Field(
        alias="__typename", default="CreateFilterPresetPayload"
    )
    error: Optional[
        Union[
            CreateFilterPresetCreatefilterpresetNameTakenUserErrorInlineFragment,
            CreateFilterPresetCreatefilterpresetAliasTakenUserErrorInlineFragment,
            CreateFilterPresetCreatefilterpresetPermissionDeniedUserErrorInlineFragment,
            CreateFilterPresetCreatefilterpresetCloudUserErrorInlineFragment,
            CreateFilterPresetCreatefilterpresetOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    filter: Optional[FilterPresetFull] = Field(default=None)


class CreateFilterPreset(Model):
    """No documentation found for this operation."""

    createFilterPreset: CreateFilterPresetCreatefilterpreset

    class Arguments(Model):
        """Arguments for CreateFilterPreset"""

        input: CreateFilterPresetInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateFilterPreset"""

        document = "fragment HTTPQLQueryFull on HTTPQL {\n  __typename\n  code\n}\n\nfragment StreamQLQueryFull on StreamQL {\n  __typename\n  code\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment AliasTakenUserErrorFull on AliasTakenUserError {\n  ...UserErrorFull\n  alias\n  __typename\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause {\n    ... on HTTPQL {\n      ...HTTPQLQueryFull\n    }\n    ... on StreamQL {\n      ...StreamQLQueryFull\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nmutation CreateFilterPreset($input: CreateFilterPresetInput!) {\n  createFilterPreset(input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on AliasTakenUserError {\n        ...AliasTakenUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    filter {\n      ...FilterPresetFull\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateFilterPresetUpdatefilterpresetNameTakenUserErrorInlineFragment(
    NameTakenUserErrorFull, Model
):
    pass


class UpdateFilterPresetUpdatefilterpresetAliasTakenUserErrorInlineFragment(
    AliasTakenUserErrorFull, Model
):
    pass


class UpdateFilterPresetUpdatefilterpresetOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class UpdateFilterPresetUpdatefilterpreset(Model):
    """No documentation"""

    typename: Literal["UpdateFilterPresetPayload"] = Field(
        alias="__typename", default="UpdateFilterPresetPayload"
    )
    error: Optional[
        Union[
            UpdateFilterPresetUpdatefilterpresetNameTakenUserErrorInlineFragment,
            UpdateFilterPresetUpdatefilterpresetAliasTakenUserErrorInlineFragment,
            UpdateFilterPresetUpdatefilterpresetOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    filter: Optional[FilterPresetFull] = Field(default=None)


class UpdateFilterPreset(Model):
    """No documentation found for this operation."""

    updateFilterPreset: UpdateFilterPresetUpdatefilterpreset

    class Arguments(Model):
        """Arguments for UpdateFilterPreset"""

        id: str
        input: UpdateFilterPresetInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateFilterPreset"""

        document = "fragment HTTPQLQueryFull on HTTPQL {\n  __typename\n  code\n}\n\nfragment StreamQLQueryFull on StreamQL {\n  __typename\n  code\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment AliasTakenUserErrorFull on AliasTakenUserError {\n  ...UserErrorFull\n  alias\n  __typename\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause {\n    ... on HTTPQL {\n      ...HTTPQLQueryFull\n    }\n    ... on StreamQL {\n      ...StreamQLQueryFull\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nmutation UpdateFilterPreset($id: ID!, $input: UpdateFilterPresetInput!) {\n  updateFilterPreset(id: $id, input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on AliasTakenUserError {\n        ...AliasTakenUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    filter {\n      ...FilterPresetFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteFilterPresetDeletefilterpreset(Model):
    """No documentation"""

    typename: Literal["DeleteFilterPresetPayload"] = Field(
        alias="__typename", default="DeleteFilterPresetPayload"
    )
    deletedId: Optional[str] = Field(default=None)


class DeleteFilterPreset(Model):
    """No documentation found for this operation."""

    deleteFilterPreset: DeleteFilterPresetDeletefilterpreset

    class Arguments(Model):
        """Arguments for DeleteFilterPreset"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteFilterPreset"""

        document = "mutation DeleteFilterPreset($id: ID!) {\n  deleteFilterPreset(id: $id) {\n    deletedId\n    __typename\n  }\n}"


class Finding(Model):
    """No documentation found for this operation."""

    finding: Optional[FindingFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Finding"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Finding"""

        document = "fragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nquery Finding($id: ID!) {\n  finding(id: $id) {\n    ...FindingFull\n    __typename\n  }\n}"


class FindingsFindingsEdges(Model):
    """An edge in a connection."""

    typename: Literal["FindingEdge"] = Field(alias="__typename", default="FindingEdge")
    cursor: str
    "A cursor for use in pagination"
    node: FindingFull
    "The item at the end of the edge"


class FindingsFindingsPageinfo(Model):
    """Information about pagination in a connection"""

    typename: Literal["PageInfo"] = Field(alias="__typename", default="PageInfo")
    hasNextPage: bool
    "When paginating forwards, are there more items?"
    hasPreviousPage: bool
    "When paginating backwards, are there more items?"
    startCursor: Optional[str] = Field(default=None)
    "When paginating backwards, the cursor to continue."
    endCursor: Optional[str] = Field(default=None)
    "When paginating forwards, the cursor to continue."


class FindingsFindings(Model):
    """No documentation"""

    typename: Literal["FindingConnection"] = Field(
        alias="__typename", default="FindingConnection"
    )
    edges: List[FindingsFindingsEdges]
    "A list of edges."
    pageInfo: FindingsFindingsPageinfo
    "Information to aid in pagination."


class Findings(Model):
    """No documentation found for this operation."""

    findings: FindingsFindings

    class Arguments(Model):
        """Arguments for Findings"""

        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        filter: Optional[FilterClauseFindingInput] = Field(default=None)
        order: Optional[FindingOrderInput] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Findings"""

        document = "fragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nquery Findings($first: Int, $after: String, $last: Int, $before: String, $filter: FilterClauseFindingInput, $order: FindingOrderInput) {\n  findings(\n    first: $first\n    after: $after\n    last: $last\n    before: $before\n    filter: $filter\n    order: $order\n  ) {\n    edges {\n      cursor\n      node {\n        ...FindingFull\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}"


class CreateFindingCreatefindingOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class CreateFindingCreatefindingUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class CreateFindingCreatefinding(Model):
    """No documentation"""

    typename: Literal["CreateFindingPayload"] = Field(
        alias="__typename", default="CreateFindingPayload"
    )
    error: Optional[
        Union[
            CreateFindingCreatefindingOtherUserErrorInlineFragment,
            CreateFindingCreatefindingUnknownIdUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    finding: Optional[FindingFull] = Field(default=None)


class CreateFinding(Model):
    """No documentation found for this operation."""

    createFinding: CreateFindingCreatefinding

    class Arguments(Model):
        """Arguments for CreateFinding"""

        requestId: str
        input: CreateFindingInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateFinding"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation CreateFinding($requestId: ID!, $input: CreateFindingInput!) {\n  createFinding(requestId: $requestId, input: $input) {\n    error {\n      __typename\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n    }\n    finding {\n      ...FindingFull\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateFindingUpdatefindingUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class UpdateFindingUpdatefindingOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class UpdateFindingUpdatefinding(Model):
    """No documentation"""

    typename: Literal["UpdateFindingPayload"] = Field(
        alias="__typename", default="UpdateFindingPayload"
    )
    error: Optional[
        Union[
            UpdateFindingUpdatefindingUnknownIdUserErrorInlineFragment,
            UpdateFindingUpdatefindingOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    finding: Optional[FindingFull] = Field(default=None)


class UpdateFinding(Model):
    """No documentation found for this operation."""

    updateFinding: UpdateFindingUpdatefinding

    class Arguments(Model):
        """Arguments for UpdateFinding"""

        id: str
        input: UpdateFindingInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateFinding"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation UpdateFinding($id: ID!, $input: UpdateFindingInput!) {\n  updateFinding(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    finding {\n      ...FindingFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteFindingsDeletefindings(Model):
    """No documentation"""

    typename: Literal["DeleteFindingsPayload"] = Field(
        alias="__typename", default="DeleteFindingsPayload"
    )
    deletedIds: Optional[List[str]] = Field(default=None)


class DeleteFindings(Model):
    """No documentation found for this operation."""

    deleteFindings: DeleteFindingsDeletefindings

    class Arguments(Model):
        """Arguments for DeleteFindings"""

        input: Optional[DeleteFindingsInput] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteFindings"""

        document = "mutation DeleteFindings($input: DeleteFindingsInput) {\n  deleteFindings(input: $input) {\n    deletedIds\n    __typename\n  }\n}"


class HostedFiles(Model):
    """No documentation found for this operation."""

    hostedFiles: List[HostedFileFull]

    class Arguments(Model):
        """Arguments for HostedFiles"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for HostedFiles"""

        document = "fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}\n\nquery HostedFiles {\n  hostedFiles {\n    ...HostedFileFull\n    __typename\n  }\n}"


class UploadHostedFileUploadhostedfile(Model):
    """No documentation"""

    typename: Literal["UploadHostedFilePayload"] = Field(
        alias="__typename", default="UploadHostedFilePayload"
    )
    hostedFile: Optional[HostedFileFull] = Field(default=None)


class UploadHostedFile(Model):
    """No documentation found for this operation."""

    uploadHostedFile: UploadHostedFileUploadhostedfile

    class Arguments(Model):
        """Arguments for UploadHostedFile"""

        input: UploadHostedFileInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UploadHostedFile"""

        document = "fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}\n\nmutation UploadHostedFile($input: UploadHostedFileInput!) {\n  uploadHostedFile(input: $input) {\n    hostedFile {\n      ...HostedFileFull\n      __typename\n    }\n    __typename\n  }\n}"


class RenameHostedFileRenamehostedfile(Model):
    """No documentation"""

    typename: Literal["RenameHostedFilePayload"] = Field(
        alias="__typename", default="RenameHostedFilePayload"
    )
    hostedFile: Optional[HostedFileFull] = Field(default=None)


class RenameHostedFile(Model):
    """No documentation found for this operation."""

    renameHostedFile: RenameHostedFileRenamehostedfile

    class Arguments(Model):
        """Arguments for RenameHostedFile"""

        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameHostedFile"""

        document = "fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}\n\nmutation RenameHostedFile($id: ID!, $name: String!) {\n  renameHostedFile(id: $id, name: $name) {\n    hostedFile {\n      ...HostedFileFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteHostedFileDeletehostedfile(Model):
    """No documentation"""

    typename: Literal["DeleteHostedFilePayload"] = Field(
        alias="__typename", default="DeleteHostedFilePayload"
    )
    deletedId: Optional[str] = Field(default=None)


class DeleteHostedFile(Model):
    """No documentation found for this operation."""

    deleteHostedFile: DeleteHostedFileDeletehostedfile

    class Arguments(Model):
        """Arguments for DeleteHostedFile"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteHostedFile"""

        document = "mutation DeleteHostedFile($id: ID!) {\n  deleteHostedFile(id: $id) {\n    deletedId\n    __typename\n  }\n}"


class InstanceSettings(Model):
    """No documentation found for this operation."""

    instanceSettings: InstanceSettingsFull

    class Arguments(Model):
        """Arguments for InstanceSettings"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for InstanceSettings"""

        document = "fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}\n\nfragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}\n\nfragment InstanceSettingsFull on InstanceSettings {\n  aiProviders {\n    anthropic {\n      ...InstanceAIProviderAnthropicFull\n      __typename\n    }\n    google {\n      ...InstanceAIProviderGoogleFull\n      __typename\n    }\n    openai {\n      ...InstanceAIProviderOpenAIFull\n      __typename\n    }\n    openrouter {\n      ...InstanceAIProviderOpenRouterFull\n      __typename\n    }\n    __typename\n  }\n  analytic {\n    enabled\n    cloud\n    local\n    __typename\n  }\n  onboarding {\n    analytic\n    __typename\n  }\n  __typename\n}\n\nquery InstanceSettings {\n  instanceSettings {\n    ...InstanceSettingsFull\n    __typename\n  }\n}"


class SetInstanceSettingsSetinstancesettings(Model):
    """No documentation"""

    typename: Literal["SetInstanceSettingsPayload"] = Field(
        alias="__typename", default="SetInstanceSettingsPayload"
    )
    settings: InstanceSettingsFull


class SetInstanceSettings(Model):
    """No documentation found for this operation."""

    setInstanceSettings: SetInstanceSettingsSetinstancesettings

    class Arguments(Model):
        """Arguments for SetInstanceSettings"""

        input: SetInstanceSettingsInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SetInstanceSettings"""

        document = "fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}\n\nfragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}\n\nfragment InstanceSettingsFull on InstanceSettings {\n  aiProviders {\n    anthropic {\n      ...InstanceAIProviderAnthropicFull\n      __typename\n    }\n    google {\n      ...InstanceAIProviderGoogleFull\n      __typename\n    }\n    openai {\n      ...InstanceAIProviderOpenAIFull\n      __typename\n    }\n    openrouter {\n      ...InstanceAIProviderOpenRouterFull\n      __typename\n    }\n    __typename\n  }\n  analytic {\n    enabled\n    cloud\n    local\n    __typename\n  }\n  onboarding {\n    analytic\n    __typename\n  }\n  __typename\n}\n\nmutation SetInstanceSettings($input: SetInstanceSettingsInput!) {\n  setInstanceSettings(input: $input) {\n    settings {\n      ...InstanceSettingsFull\n      __typename\n    }\n    __typename\n  }\n}"


class PluginPackages(Model):
    """No documentation found for this operation."""

    pluginPackages: List[PluginPackageMeta]

    class Arguments(Model):
        """Arguments for PluginPackages"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for PluginPackages"""

        document = "fragment PluginPackageMeta on PluginPackage {\n  id\n  manifestId\n  plugins {\n    __typename\n    id\n    manifestId\n    enabled\n  }\n  __typename\n}\n\nquery PluginPackages {\n  pluginPackages {\n    ...PluginPackageMeta\n    __typename\n  }\n}"


class InstallPluginPackageInstallpluginpackagePluginUserErrorInlineFragment(
    PluginUserErrorFull, Model
):
    pass


class InstallPluginPackageInstallpluginpackageStoreUserErrorInlineFragment(
    StoreUserErrorFull, Model
):
    pass


class InstallPluginPackageInstallpluginpackageCloudUserErrorInlineFragment(
    CloudUserErrorFull, Model
):
    pass


class InstallPluginPackageInstallpluginpackageOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class InstallPluginPackageInstallpluginpackage(Model):
    """No documentation"""

    typename: Literal["InstallPluginPackagePayload"] = Field(
        alias="__typename", default="InstallPluginPackagePayload"
    )
    package: Optional[PluginPackageMeta] = Field(default=None)
    error: Optional[
        Union[
            InstallPluginPackageInstallpluginpackagePluginUserErrorInlineFragment,
            InstallPluginPackageInstallpluginpackageStoreUserErrorInlineFragment,
            InstallPluginPackageInstallpluginpackageCloudUserErrorInlineFragment,
            InstallPluginPackageInstallpluginpackageOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class InstallPluginPackage(Model):
    """No documentation found for this operation."""

    installPluginPackage: InstallPluginPackageInstallpluginpackage

    class Arguments(Model):
        """Arguments for InstallPluginPackage"""

        input: InstallPluginPackageInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for InstallPluginPackage"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PluginPackageMeta on PluginPackage {\n  id\n  manifestId\n  plugins {\n    __typename\n    id\n    manifestId\n    enabled\n  }\n  __typename\n}\n\nfragment PluginUserErrorFull on PluginUserError {\n  ...UserErrorFull\n  reason\n  __typename\n}\n\nfragment StoreUserErrorFull on StoreUserError {\n  ...UserErrorFull\n  storeReason: reason\n  __typename\n}\n\nmutation InstallPluginPackage($input: InstallPluginPackageInput!) {\n  installPluginPackage(input: $input) {\n    package {\n      ...PluginPackageMeta\n      __typename\n    }\n    error {\n      __typename\n      ... on PluginUserError {\n        ...PluginUserErrorFull\n      }\n      ... on StoreUserError {\n        ...StoreUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class Projects(Model):
    """No documentation found for this operation."""

    projects: List[ProjectFull]

    class Arguments(Model):
        """Arguments for Projects"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Projects"""

        document = "fragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nquery Projects {\n  projects {\n    ...ProjectFull\n    __typename\n  }\n}"


class CreateProjectCreateprojectNameTakenUserErrorInlineFragment(
    NameTakenUserErrorFull, Model
):
    pass


class CreateProjectCreateprojectPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class CreateProjectCreateprojectCloudUserErrorInlineFragment(CloudUserErrorFull, Model):
    pass


class CreateProjectCreateprojectOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class CreateProjectCreateproject(Model):
    """No documentation"""

    typename: Literal["CreateProjectPayload"] = Field(
        alias="__typename", default="CreateProjectPayload"
    )
    error: Optional[
        Union[
            CreateProjectCreateprojectNameTakenUserErrorInlineFragment,
            CreateProjectCreateprojectPermissionDeniedUserErrorInlineFragment,
            CreateProjectCreateprojectCloudUserErrorInlineFragment,
            CreateProjectCreateprojectOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    project: Optional[ProjectFull] = Field(default=None)


class CreateProject(Model):
    """No documentation found for this operation."""

    createProject: CreateProjectCreateproject

    class Arguments(Model):
        """Arguments for CreateProject"""

        input: CreateProjectInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateProject"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nmutation CreateProject($input: CreateProjectInput!) {\n  createProject(input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    project {\n      ...ProjectFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteProjectDeleteprojectProjectUserErrorInlineFragment(
    ProjectUserErrorFull, Model
):
    pass


class DeleteProjectDeleteprojectUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class DeleteProjectDeleteprojectOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class DeleteProjectDeleteproject(Model):
    """No documentation"""

    typename: Literal["DeleteProjectPayload"] = Field(
        alias="__typename", default="DeleteProjectPayload"
    )
    deletedId: Optional[str] = Field(default=None)
    error: Optional[
        Union[
            DeleteProjectDeleteprojectProjectUserErrorInlineFragment,
            DeleteProjectDeleteprojectUnknownIdUserErrorInlineFragment,
            DeleteProjectDeleteprojectOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class DeleteProject(Model):
    """No documentation found for this operation."""

    deleteProject: DeleteProjectDeleteproject

    class Arguments(Model):
        """Arguments for DeleteProject"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteProject"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ProjectUserErrorFull on ProjectUserError {\n  ...UserErrorFull\n  projectReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation DeleteProject($id: ID!) {\n  deleteProject(id: $id) {\n    deletedId\n    error {\n      __typename\n      ... on ProjectUserError {\n        ...ProjectUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class RenameProjectRenameprojectNameTakenUserErrorInlineFragment(Model):
    typename: Literal["NameTakenUserError"] = Field(
        alias="__typename", default="NameTakenUserError"
    )
    code: str
    name: str


class RenameProjectRenameprojectUnknownIdUserErrorInlineFragment(Model):
    typename: Literal["UnknownIdUserError"] = Field(
        alias="__typename", default="UnknownIdUserError"
    )
    code: str
    id: str


class RenameProjectRenameprojectOtherUserErrorInlineFragment(Model):
    typename: Literal["OtherUserError"] = Field(
        alias="__typename", default="OtherUserError"
    )
    code: str


class RenameProjectRenameproject(Model):
    """No documentation"""

    typename: Literal["RenameProjectPayload"] = Field(
        alias="__typename", default="RenameProjectPayload"
    )
    error: Optional[
        Union[
            RenameProjectRenameprojectNameTakenUserErrorInlineFragment,
            RenameProjectRenameprojectUnknownIdUserErrorInlineFragment,
            RenameProjectRenameprojectOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    project: Optional[ProjectFull] = Field(default=None)


class RenameProject(Model):
    """No documentation found for this operation."""

    renameProject: RenameProjectRenameproject

    class Arguments(Model):
        """Arguments for RenameProject"""

        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameProject"""

        document = "fragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nmutation RenameProject($id: ID!, $name: String!) {\n  renameProject(id: $id, name: $name) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        code\n        name\n      }\n      ... on UnknownIdUserError {\n        code\n        id\n      }\n      ... on OtherUserError {\n        code\n      }\n    }\n    project {\n      ...ProjectFull\n      __typename\n    }\n    __typename\n  }\n}"


class SelectProjectSelectprojectCurrentproject(Model):
    """No documentation"""

    typename: Literal["CurrentProject"] = Field(
        alias="__typename", default="CurrentProject"
    )
    project: ProjectFull


class SelectProjectSelectprojectProjectUserErrorInlineFragment(
    ProjectUserErrorFull, Model
):
    pass


class SelectProjectSelectprojectUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class SelectProjectSelectprojectOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class SelectProjectSelectproject(Model):
    """No documentation"""

    typename: Literal["SelectProjectPayload"] = Field(
        alias="__typename", default="SelectProjectPayload"
    )
    currentProject: Optional[SelectProjectSelectprojectCurrentproject] = Field(
        default=None
    )
    error: Optional[
        Union[
            SelectProjectSelectprojectProjectUserErrorInlineFragment,
            SelectProjectSelectprojectUnknownIdUserErrorInlineFragment,
            SelectProjectSelectprojectOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class SelectProject(Model):
    """No documentation found for this operation."""

    selectProject: SelectProjectSelectproject

    class Arguments(Model):
        """Arguments for SelectProject"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SelectProject"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nfragment ProjectUserErrorFull on ProjectUserError {\n  ...UserErrorFull\n  projectReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation SelectProject($id: ID!) {\n  selectProject(id: $id) {\n    currentProject {\n      project {\n        ...ProjectFull\n        __typename\n      }\n      __typename\n    }\n    error {\n      __typename\n      ... on ProjectUserError {\n        ...ProjectUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class ReplayEntryReplayentryBase(Model):
    """No documentation"""


class ReplayEntryReplayentryBaseReplayEntryHttp(
    ReplayEntryFullReplayEntryHttp, ReplayEntryReplayentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplayEntryReplayentryBaseReplayEntryWs(
    ReplayEntryFullReplayEntryWs, ReplayEntryReplayentryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplayEntryReplayentryBaseCatchAll(ReplayEntryReplayentryBase, Model):
    """Catch all class for ReplayEntryReplayentryBase"""

    typename: str = Field(alias="__typename")


class ReplayEntry(Model):
    """No documentation found for this operation."""

    replayEntry: Optional[
        Union[
            Annotated[
                Union[
                    ReplayEntryReplayentryBaseReplayEntryHttp,
                    ReplayEntryReplayentryBaseReplayEntryWs,
                ],
                Field(discriminator="typename"),
            ],
            ReplayEntryReplayentryBaseCatchAll,
        ]
    ] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplayEntry"""

        id: str
        sessionKind: ReplaySessionKind
        includeReplayRaw: bool
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplayEntry"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryHttpFull on ReplayEntryHttp {\n  __typename\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplayEntryWsFull on ReplayEntryWs {\n  __typename\n  createdAt\n  error\n  id\n  http {\n    ...ReplayEntryHttpFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  ... on ReplayEntryHttp {\n    ...ReplayEntryHttpFull\n  }\n  ... on ReplayEntryWs {\n    ...ReplayEntryWsFull\n  }\n  __typename\n}\n\nquery ReplayEntry($id: ID!, $sessionKind: ReplaySessionKind!, $includeReplayRaw: Boolean!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  replayEntry(id: $id, sessionKind: $sessionKind) {\n    ...ReplayEntryFull\n    __typename\n  }\n}"


class ReplaySessionsReplaysessionsEdgesNodeBase(Model):
    """No documentation"""


class ReplaySessionsReplaysessionsEdgesNodeBaseReplaySessionHttp(
    ReplaySessionMetaReplaySessionHttp, ReplaySessionsReplaysessionsEdgesNodeBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class ReplaySessionsReplaysessionsEdgesNodeBaseReplaySessionWs(
    ReplaySessionMetaReplaySessionWs, ReplaySessionsReplaysessionsEdgesNodeBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class ReplaySessionsReplaysessionsEdgesNodeBaseCatchAll(
    ReplaySessionsReplaysessionsEdgesNodeBase, Model
):
    """Catch all class for ReplaySessionsReplaysessionsEdgesNodeBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionsReplaysessionsEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplaySessionEdge"] = Field(
        alias="__typename", default="ReplaySessionEdge"
    )
    cursor: str
    "A cursor for use in pagination"
    node: Union[
        Annotated[
            Union[
                ReplaySessionsReplaysessionsEdgesNodeBaseReplaySessionHttp,
                ReplaySessionsReplaysessionsEdgesNodeBaseReplaySessionWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplaySessionsReplaysessionsEdgesNodeBaseCatchAll,
    ]
    "The item at the end of the edge"


class ReplaySessionsReplaysessionsPageinfo(Model):
    """Information about pagination in a connection"""

    typename: Literal["PageInfo"] = Field(alias="__typename", default="PageInfo")
    hasNextPage: bool
    "When paginating forwards, are there more items?"
    hasPreviousPage: bool
    "When paginating backwards, are there more items?"
    startCursor: Optional[str] = Field(default=None)
    "When paginating backwards, the cursor to continue."
    endCursor: Optional[str] = Field(default=None)
    "When paginating forwards, the cursor to continue."


class ReplaySessionsReplaysessions(Model):
    """No documentation"""

    typename: Literal["ReplaySessionConnection"] = Field(
        alias="__typename", default="ReplaySessionConnection"
    )
    edges: List[ReplaySessionsReplaysessionsEdges]
    "A list of edges."
    pageInfo: ReplaySessionsReplaysessionsPageinfo
    "Information to aid in pagination."


class ReplaySessions(Model):
    """No documentation found for this operation."""

    replaySessions: ReplaySessionsReplaysessions

    class Arguments(Model):
        """Arguments for ReplaySessions"""

        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySessions"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}\n\nfragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplaySessionMeta on ReplaySession {\n  ... on ReplaySessionHttp {\n    ...ReplaySessionHttpMeta\n  }\n  ... on ReplaySessionWs {\n    ...ReplaySessionWsMeta\n  }\n  __typename\n}\n\nquery ReplaySessions($first: Int, $after: String, $last: Int, $before: String) {\n  replaySessions(first: $first, after: $after, last: $last, before: $before) {\n    edges {\n      cursor\n      node {\n        ...ReplaySessionMeta\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}"


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase(Model):
    """No documentation"""


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryHttp(
    ReplayEntryFullReplayEntryHttp,
    ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryWs(
    ReplayEntryFullReplayEntryWs,
    ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseCatchAll(
    ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase, Model
):
    """Catch all class for ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionEntriesReplaysessionEntriesEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplayEntryEdge"] = Field(
        alias="__typename", default="ReplayEntryEdge"
    )
    cursor: str
    "A cursor for use in pagination"
    node: Union[
        Annotated[
            Union[
                ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryHttp,
                ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseCatchAll,
    ]
    "The item at the end of the edge"


class ReplaySessionEntriesReplaysessionEntriesPageinfo(Model):
    """Information about pagination in a connection"""

    typename: Literal["PageInfo"] = Field(alias="__typename", default="PageInfo")
    hasNextPage: bool
    "When paginating forwards, are there more items?"
    hasPreviousPage: bool
    "When paginating backwards, are there more items?"
    startCursor: Optional[str] = Field(default=None)
    "When paginating backwards, the cursor to continue."
    endCursor: Optional[str] = Field(default=None)
    "When paginating forwards, the cursor to continue."


class ReplaySessionEntriesReplaysessionEntries(Model):
    """No documentation"""

    typename: Literal["ReplayEntryConnection"] = Field(
        alias="__typename", default="ReplayEntryConnection"
    )
    edges: List[ReplaySessionEntriesReplaysessionEntriesEdges]
    "A list of edges."
    pageInfo: ReplaySessionEntriesReplaysessionEntriesPageinfo
    "Information to aid in pagination."


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase(Model):
    """No documentation"""


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryHttp(
    ReplayEntryFullReplayEntryHttp,
    ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryWs(
    ReplayEntryFullReplayEntryWs,
    ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseCatchAll(
    ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase, Model
):
    """Catch all class for ReplaySessionEntriesReplaysessionEntriesEdgesNodeBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionEntriesReplaysessionEntriesEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplayEntryEdge"] = Field(
        alias="__typename", default="ReplayEntryEdge"
    )
    cursor: str
    "A cursor for use in pagination"
    node: Union[
        Annotated[
            Union[
                ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryHttp,
                ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseReplayEntryWs,
            ],
            Field(discriminator="typename"),
        ],
        ReplaySessionEntriesReplaysessionEntriesEdgesNodeBaseCatchAll,
    ]
    "The item at the end of the edge"


class ReplaySessionEntriesReplaysessionEntriesPageinfo(Model):
    """Information about pagination in a connection"""

    typename: Literal["PageInfo"] = Field(alias="__typename", default="PageInfo")
    hasNextPage: bool
    "When paginating forwards, are there more items?"
    hasPreviousPage: bool
    "When paginating backwards, are there more items?"
    startCursor: Optional[str] = Field(default=None)
    "When paginating backwards, the cursor to continue."
    endCursor: Optional[str] = Field(default=None)
    "When paginating forwards, the cursor to continue."


class ReplaySessionEntriesReplaysessionEntries(Model):
    """No documentation"""

    typename: Literal["ReplayEntryConnection"] = Field(
        alias="__typename", default="ReplayEntryConnection"
    )
    edges: List[ReplaySessionEntriesReplaysessionEntriesEdges]
    "A list of edges."
    pageInfo: ReplaySessionEntriesReplaysessionEntriesPageinfo
    "Information to aid in pagination."


class ReplaySessionEntriesReplaysessionBase(Model):
    """No documentation"""


class ReplaySessionEntriesReplaysessionBaseReplaySessionHttp(
    ReplaySessionEntriesReplaysessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )
    entries: ReplaySessionEntriesReplaysessionEntries


class ReplaySessionEntriesReplaysessionBaseReplaySessionWs(
    ReplaySessionEntriesReplaysessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )
    entries: ReplaySessionEntriesReplaysessionEntries


class ReplaySessionEntriesReplaysessionBaseCatchAll(
    ReplaySessionEntriesReplaysessionBase, Model
):
    """Catch all class for ReplaySessionEntriesReplaysessionBase"""

    typename: str = Field(alias="__typename")


class ReplaySessionEntries(Model):
    """No documentation found for this operation."""

    replaySession: Optional[
        Union[
            Annotated[
                Union[
                    ReplaySessionEntriesReplaysessionBaseReplaySessionHttp,
                    ReplaySessionEntriesReplaysessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            ReplaySessionEntriesReplaysessionBaseCatchAll,
        ]
    ] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplaySessionEntries"""

        id: str
        after: Optional[str] = Field(default=None)
        before: Optional[str] = Field(default=None)
        first: Optional[int] = Field(default=None)
        last: Optional[int] = Field(default=None)
        includeReplayRaw: bool
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySessionEntries"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryHttpFull on ReplayEntryHttp {\n  __typename\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplayEntryWsFull on ReplayEntryWs {\n  __typename\n  createdAt\n  error\n  id\n  http {\n    ...ReplayEntryHttpFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  ... on ReplayEntryHttp {\n    ...ReplayEntryHttpFull\n  }\n  ... on ReplayEntryWs {\n    ...ReplayEntryWsFull\n  }\n  __typename\n}\n\nquery ReplaySessionEntries($id: ID!, $after: String, $before: String, $first: Int, $last: Int, $includeReplayRaw: Boolean!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  replaySession(id: $id) {\n    ... on ReplaySessionHttp {\n      entries(after: $after, before: $before, first: $first, last: $last) {\n        edges {\n          cursor\n          node {\n            ...ReplayEntryFull\n          }\n        }\n        pageInfo {\n          hasNextPage\n          hasPreviousPage\n          startCursor\n          endCursor\n        }\n      }\n    }\n    ... on ReplaySessionWs {\n      entries(after: $after, before: $before, first: $first, last: $last) {\n        edges {\n          cursor\n          node {\n            ...ReplayEntryFull\n          }\n        }\n        pageInfo {\n          hasNextPage\n          hasPreviousPage\n          startCursor\n          endCursor\n        }\n      }\n    }\n    __typename\n  }\n}"


class ReplaySessionReplaysessionBase(Model):
    """No documentation"""


class ReplaySessionReplaysessionBaseReplaySessionHttp(
    ReplaySessionMetaReplaySessionHttp, ReplaySessionReplaysessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class ReplaySessionReplaysessionBaseReplaySessionWs(
    ReplaySessionMetaReplaySessionWs, ReplaySessionReplaysessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class ReplaySessionReplaysessionBaseCatchAll(ReplaySessionReplaysessionBase, Model):
    """Catch all class for ReplaySessionReplaysessionBase"""

    typename: str = Field(alias="__typename")


class ReplaySession(Model):
    """No documentation found for this operation."""

    replaySession: Optional[
        Union[
            Annotated[
                Union[
                    ReplaySessionReplaysessionBaseReplaySessionHttp,
                    ReplaySessionReplaysessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            ReplaySessionReplaysessionBaseCatchAll,
        ]
    ] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplaySession"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySession"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}\n\nfragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplaySessionMeta on ReplaySession {\n  ... on ReplaySessionHttp {\n    ...ReplaySessionHttpMeta\n  }\n  ... on ReplaySessionWs {\n    ...ReplaySessionWsMeta\n  }\n  __typename\n}\n\nquery ReplaySession($id: ID!) {\n  replaySession(id: $id) {\n    ...ReplaySessionMeta\n    __typename\n  }\n}"


class ReplaySessionCollectionsReplaysessioncollectionsEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplaySessionCollectionEdge"] = Field(
        alias="__typename", default="ReplaySessionCollectionEdge"
    )
    cursor: str
    "A cursor for use in pagination"
    node: ReplaySessionCollectionMeta
    "The item at the end of the edge"


class ReplaySessionCollectionsReplaysessioncollectionsPageinfo(Model):
    """Information about pagination in a connection"""

    typename: Literal["PageInfo"] = Field(alias="__typename", default="PageInfo")
    hasNextPage: bool
    "When paginating forwards, are there more items?"
    hasPreviousPage: bool
    "When paginating backwards, are there more items?"
    startCursor: Optional[str] = Field(default=None)
    "When paginating backwards, the cursor to continue."
    endCursor: Optional[str] = Field(default=None)
    "When paginating forwards, the cursor to continue."


class ReplaySessionCollectionsReplaysessioncollections(Model):
    """No documentation"""

    typename: Literal["ReplaySessionCollectionConnection"] = Field(
        alias="__typename", default="ReplaySessionCollectionConnection"
    )
    edges: List[ReplaySessionCollectionsReplaysessioncollectionsEdges]
    "A list of edges."
    pageInfo: ReplaySessionCollectionsReplaysessioncollectionsPageinfo
    "Information to aid in pagination."


class ReplaySessionCollections(Model):
    """No documentation found for this operation."""

    replaySessionCollections: ReplaySessionCollectionsReplaysessioncollections

    class Arguments(Model):
        """Arguments for ReplaySessionCollections"""

        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySessionCollections"""

        document = "fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}\n\nquery ReplaySessionCollections($first: Int, $after: String, $last: Int, $before: String) {\n  replaySessionCollections(\n    first: $first\n    after: $after\n    last: $last\n    before: $before\n  ) {\n    edges {\n      cursor\n      node {\n        ...ReplaySessionCollectionMeta\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}"


class CreateReplaySessionCreatereplaysessionPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class CreateReplaySessionCreatereplaysessionCloudUserErrorInlineFragment(
    CloudUserErrorFull, Model
):
    pass


class CreateReplaySessionCreatereplaysessionOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class CreateReplaySessionCreatereplaysessionSessionBase(Model):
    """No documentation"""


class CreateReplaySessionCreatereplaysessionSessionBaseReplaySessionHttp(
    ReplaySessionMetaReplaySessionHttp,
    CreateReplaySessionCreatereplaysessionSessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class CreateReplaySessionCreatereplaysessionSessionBaseReplaySessionWs(
    ReplaySessionMetaReplaySessionWs,
    CreateReplaySessionCreatereplaysessionSessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class CreateReplaySessionCreatereplaysessionSessionBaseCatchAll(
    CreateReplaySessionCreatereplaysessionSessionBase, Model
):
    """Catch all class for CreateReplaySessionCreatereplaysessionSessionBase"""

    typename: str = Field(alias="__typename")


class CreateReplaySessionCreatereplaysession(Model):
    """No documentation"""

    typename: Literal["CreateReplaySessionPayload"] = Field(
        alias="__typename", default="CreateReplaySessionPayload"
    )
    error: Optional[
        Union[
            CreateReplaySessionCreatereplaysessionPermissionDeniedUserErrorInlineFragment,
            CreateReplaySessionCreatereplaysessionCloudUserErrorInlineFragment,
            CreateReplaySessionCreatereplaysessionOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    session: Optional[
        Union[
            Annotated[
                Union[
                    CreateReplaySessionCreatereplaysessionSessionBaseReplaySessionHttp,
                    CreateReplaySessionCreatereplaysessionSessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            CreateReplaySessionCreatereplaysessionSessionBaseCatchAll,
        ]
    ] = Field(default=None)


class CreateReplaySession(Model):
    """No documentation found for this operation."""

    createReplaySession: CreateReplaySessionCreatereplaysession

    class Arguments(Model):
        """Arguments for CreateReplaySession"""

        input: CreateReplaySessionInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateReplaySession"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}\n\nfragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment ReplaySessionMeta on ReplaySession {\n  ... on ReplaySessionHttp {\n    ...ReplaySessionHttpMeta\n  }\n  ... on ReplaySessionWs {\n    ...ReplaySessionWsMeta\n  }\n  __typename\n}\n\nmutation CreateReplaySession($input: CreateReplaySessionInput!) {\n  createReplaySession(input: $input) {\n    error {\n      __typename\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class CreateReplaySessionCollectionCreatereplaysessioncollection(Model):
    """No documentation"""

    typename: Literal["CreateReplaySessionCollectionPayload"] = Field(
        alias="__typename", default="CreateReplaySessionCollectionPayload"
    )
    collection: Optional[ReplaySessionCollectionMeta] = Field(default=None)


class CreateReplaySessionCollection(Model):
    """No documentation found for this operation."""

    createReplaySessionCollection: (
        CreateReplaySessionCollectionCreatereplaysessioncollection
    )

    class Arguments(Model):
        """Arguments for CreateReplaySessionCollection"""

        input: CreateReplaySessionCollectionInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateReplaySessionCollection"""

        document = "fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}\n\nmutation CreateReplaySessionCollection($input: CreateReplaySessionCollectionInput!) {\n  createReplaySessionCollection(input: $input) {\n    collection {\n      ...ReplaySessionCollectionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteReplaySessionsDeletereplaysessions(Model):
    """No documentation"""

    typename: Literal["DeleteReplaySessionsPayload"] = Field(
        alias="__typename", default="DeleteReplaySessionsPayload"
    )
    deletedIds: Optional[List[str]] = Field(default=None)


class DeleteReplaySessions(Model):
    """No documentation found for this operation."""

    deleteReplaySessions: DeleteReplaySessionsDeletereplaysessions

    class Arguments(Model):
        """Arguments for DeleteReplaySessions"""

        ids: List[str]
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteReplaySessions"""

        document = "mutation DeleteReplaySessions($ids: [ID!]!) {\n  deleteReplaySessions(ids: $ids) {\n    deletedIds\n    __typename\n  }\n}"


class DeleteReplaySessionCollectionDeletereplaysessioncollection(Model):
    """No documentation"""

    typename: Literal["DeleteReplaySessionCollectionPayload"] = Field(
        alias="__typename", default="DeleteReplaySessionCollectionPayload"
    )
    deletedId: Optional[str] = Field(default=None)


class DeleteReplaySessionCollection(Model):
    """No documentation found for this operation."""

    deleteReplaySessionCollection: (
        DeleteReplaySessionCollectionDeletereplaysessioncollection
    )

    class Arguments(Model):
        """Arguments for DeleteReplaySessionCollection"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteReplaySessionCollection"""

        document = "mutation DeleteReplaySessionCollection($id: ID!) {\n  deleteReplaySessionCollection(id: $id) {\n    deletedId\n    __typename\n  }\n}"


class MoveReplaySessionMovereplaysessionSessionBase(Model):
    """No documentation"""


class MoveReplaySessionMovereplaysessionSessionBaseReplaySessionHttp(
    ReplaySessionMetaReplaySessionHttp,
    MoveReplaySessionMovereplaysessionSessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class MoveReplaySessionMovereplaysessionSessionBaseReplaySessionWs(
    ReplaySessionMetaReplaySessionWs,
    MoveReplaySessionMovereplaysessionSessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class MoveReplaySessionMovereplaysessionSessionBaseCatchAll(
    MoveReplaySessionMovereplaysessionSessionBase, Model
):
    """Catch all class for MoveReplaySessionMovereplaysessionSessionBase"""

    typename: str = Field(alias="__typename")


class MoveReplaySessionMovereplaysession(Model):
    """No documentation"""

    typename: Literal["MoveReplaySessionPayload"] = Field(
        alias="__typename", default="MoveReplaySessionPayload"
    )
    session: Optional[
        Union[
            Annotated[
                Union[
                    MoveReplaySessionMovereplaysessionSessionBaseReplaySessionHttp,
                    MoveReplaySessionMovereplaysessionSessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            MoveReplaySessionMovereplaysessionSessionBaseCatchAll,
        ]
    ] = Field(default=None)


class MoveReplaySession(Model):
    """No documentation found for this operation."""

    moveReplaySession: MoveReplaySessionMovereplaysession

    class Arguments(Model):
        """Arguments for MoveReplaySession"""

        id: str
        collectionId: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for MoveReplaySession"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}\n\nfragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplaySessionMeta on ReplaySession {\n  ... on ReplaySessionHttp {\n    ...ReplaySessionHttpMeta\n  }\n  ... on ReplaySessionWs {\n    ...ReplaySessionWsMeta\n  }\n  __typename\n}\n\nmutation MoveReplaySession($id: ID!, $collectionId: ID!) {\n  moveReplaySession(id: $id, collectionId: $collectionId) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class RenameReplaySessionRenamereplaysessionSessionBase(Model):
    """No documentation"""


class RenameReplaySessionRenamereplaysessionSessionBaseReplaySessionHttp(
    ReplaySessionMetaReplaySessionHttp,
    RenameReplaySessionRenamereplaysessionSessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class RenameReplaySessionRenamereplaysessionSessionBaseReplaySessionWs(
    ReplaySessionMetaReplaySessionWs,
    RenameReplaySessionRenamereplaysessionSessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class RenameReplaySessionRenamereplaysessionSessionBaseCatchAll(
    RenameReplaySessionRenamereplaysessionSessionBase, Model
):
    """Catch all class for RenameReplaySessionRenamereplaysessionSessionBase"""

    typename: str = Field(alias="__typename")


class RenameReplaySessionRenamereplaysession(Model):
    """No documentation"""

    typename: Literal["RenameReplaySessionPayload"] = Field(
        alias="__typename", default="RenameReplaySessionPayload"
    )
    session: Optional[
        Union[
            Annotated[
                Union[
                    RenameReplaySessionRenamereplaysessionSessionBaseReplaySessionHttp,
                    RenameReplaySessionRenamereplaysessionSessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            RenameReplaySessionRenamereplaysessionSessionBaseCatchAll,
        ]
    ] = Field(default=None)


class RenameReplaySession(Model):
    """No documentation found for this operation."""

    renameReplaySession: RenameReplaySessionRenamereplaysession

    class Arguments(Model):
        """Arguments for RenameReplaySession"""

        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameReplaySession"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}\n\nfragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplaySessionMeta on ReplaySession {\n  ... on ReplaySessionHttp {\n    ...ReplaySessionHttpMeta\n  }\n  ... on ReplaySessionWs {\n    ...ReplaySessionWsMeta\n  }\n  __typename\n}\n\nmutation RenameReplaySession($id: ID!, $name: String!) {\n  renameReplaySession(id: $id, name: $name) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class RenameReplaySessionCollectionRenamereplaysessioncollection(Model):
    """No documentation"""

    typename: Literal["RenameReplaySessionCollectionPayload"] = Field(
        alias="__typename", default="RenameReplaySessionCollectionPayload"
    )
    collection: Optional[ReplaySessionCollectionMeta] = Field(default=None)


class RenameReplaySessionCollection(Model):
    """No documentation found for this operation."""

    renameReplaySessionCollection: (
        RenameReplaySessionCollectionRenamereplaysessioncollection
    )

    class Arguments(Model):
        """Arguments for RenameReplaySessionCollection"""

        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameReplaySessionCollection"""

        document = "fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}\n\nmutation RenameReplaySessionCollection($id: ID!, $name: String!) {\n  renameReplaySessionCollection(id: $id, name: $name) {\n    collection {\n      ...ReplaySessionCollectionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBase(Model):
    """No documentation"""


class SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBaseReplaySessionHttp(
    ReplaySessionMetaReplaySessionHttp,
    SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBaseReplaySessionWs(
    ReplaySessionMetaReplaySessionWs,
    SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBase,
    Model,
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBaseCatchAll(
    SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBase, Model
):
    """Catch all class for SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBase"""

    typename: str = Field(alias="__typename")


class SetActiveReplaySessionEntrySetactivereplaysessionentry(Model):
    """No documentation"""

    typename: Literal["SetActiveReplaySessionEntryPayload"] = Field(
        alias="__typename", default="SetActiveReplaySessionEntryPayload"
    )
    session: Optional[
        Union[
            Annotated[
                Union[
                    SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBaseReplaySessionHttp,
                    SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            SetActiveReplaySessionEntrySetactivereplaysessionentrySessionBaseCatchAll,
        ]
    ] = Field(default=None)


class SetActiveReplaySessionEntry(Model):
    """No documentation found for this operation."""

    setActiveReplaySessionEntry: Annotated[
        SetActiveReplaySessionEntrySetactivereplaysessionentry,
        Deprecated("Remove usage, no replacement"),
    ]
    "DEPRECATED: Remove usage, no replacement"

    class Arguments(Model):
        """Arguments for SetActiveReplaySessionEntry"""

        id: str
        entryId: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SetActiveReplaySessionEntry"""

        document = "fragment ReplaySessionHttpMeta on ReplaySessionHttp {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  settings {\n    connectionClose\n    updateContentLength\n    __typename\n  }\n}\n\nfragment ReplaySessionWsMeta on ReplaySessionWs {\n  __typename\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  entries(last: 1) {\n    edges {\n      node {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplaySessionMeta on ReplaySession {\n  ... on ReplaySessionHttp {\n    ...ReplaySessionHttpMeta\n  }\n  ... on ReplaySessionWs {\n    ...ReplaySessionWsMeta\n  }\n  __typename\n}\n\nmutation SetActiveReplaySessionEntry($id: ID!, $entryId: ID!) {\n  setActiveReplaySessionEntry(id: $id, entryId: $entryId) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateReplayEntryDraftUpdatereplayentrydraftEntryBase(Model):
    """No documentation"""

    id: str


class UpdateReplayEntryDraftUpdatereplayentrydraftEntryBaseReplayEntryHttp(
    UpdateReplayEntryDraftUpdatereplayentrydraftEntryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryHttp"] = Field(
        alias="__typename", default="ReplayEntryHttp"
    )


class UpdateReplayEntryDraftUpdatereplayentrydraftEntryBaseReplayEntryWs(
    UpdateReplayEntryDraftUpdatereplayentrydraftEntryBase, Model
):
    """No documentation"""

    typename: Literal["ReplayEntryWs"] = Field(
        alias="__typename", default="ReplayEntryWs"
    )


class UpdateReplayEntryDraftUpdatereplayentrydraftEntryBaseCatchAll(
    UpdateReplayEntryDraftUpdatereplayentrydraftEntryBase, Model
):
    """Catch all class for UpdateReplayEntryDraftUpdatereplayentrydraftEntryBase"""

    typename: str = Field(alias="__typename")


class UpdateReplayEntryDraftUpdatereplayentrydraft(Model):
    """No documentation"""

    typename: Literal["UpdateReplayEntryDraftPayload"] = Field(
        alias="__typename", default="UpdateReplayEntryDraftPayload"
    )
    entry: Optional[
        Union[
            Annotated[
                Union[
                    UpdateReplayEntryDraftUpdatereplayentrydraftEntryBaseReplayEntryHttp,
                    UpdateReplayEntryDraftUpdatereplayentrydraftEntryBaseReplayEntryWs,
                ],
                Field(discriminator="typename"),
            ],
            UpdateReplayEntryDraftUpdatereplayentrydraftEntryBaseCatchAll,
        ]
    ] = Field(default=None)


class UpdateReplayEntryDraft(Model):
    """No documentation found for this operation."""

    updateReplayEntryDraft: UpdateReplayEntryDraftUpdatereplayentrydraft

    class Arguments(Model):
        """Arguments for UpdateReplayEntryDraft"""

        id: str
        input: UpdateReplayEntryDraftInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateReplayEntryDraft"""

        document = "mutation UpdateReplayEntryDraft($id: ID!, $input: UpdateReplayEntryDraftInput!) {\n  updateReplayEntryDraft(id: $id, input: $input) {\n    entry {\n      id\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBase(Model):
    """No documentation"""

    id: str


class UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBaseReplaySessionHttp(
    UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionHttp"] = Field(
        alias="__typename", default="ReplaySessionHttp"
    )


class UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBaseReplaySessionWs(
    UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBase, Model
):
    """No documentation"""

    typename: Literal["ReplaySessionWs"] = Field(
        alias="__typename", default="ReplaySessionWs"
    )


class UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBaseCatchAll(
    UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBase, Model
):
    """Catch all class for UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBase"""

    typename: str = Field(alias="__typename")


class UpdateReplaySessionSettingsUpdatereplaysessionsettings(Model):
    """No documentation"""

    typename: Literal["UpdateReplaySessionSettingsPayload"] = Field(
        alias="__typename", default="UpdateReplaySessionSettingsPayload"
    )
    session: Optional[
        Union[
            Annotated[
                Union[
                    UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBaseReplaySessionHttp,
                    UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBaseReplaySessionWs,
                ],
                Field(discriminator="typename"),
            ],
            UpdateReplaySessionSettingsUpdatereplaysessionsettingsSessionBaseCatchAll,
        ]
    ] = Field(default=None)


class UpdateReplaySessionSettings(Model):
    """No documentation found for this operation."""

    updateReplaySessionSettings: UpdateReplaySessionSettingsUpdatereplaysessionsettings

    class Arguments(Model):
        """Arguments for UpdateReplaySessionSettings"""

        id: str
        input: ReplaySessionSettingsInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateReplaySessionSettings"""

        document = "mutation UpdateReplaySessionSettings($id: ID!, $input: ReplaySessionSettingsInput!) {\n  updateReplaySessionSettings(id: $id, input: $input) {\n    session {\n      id\n      __typename\n    }\n    __typename\n  }\n}"


class StartReplayTaskStartreplaytaskCloudUserErrorInlineFragment(
    CloudUserErrorFull, Model
):
    pass


class StartReplayTaskStartreplaytaskPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class StartReplayTaskStartreplaytaskTaskInProgressUserErrorInlineFragment(
    TaskInProgressUserErrorFull, Model
):
    pass


class StartReplayTaskStartreplaytaskUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class StartReplayTaskStartreplaytaskOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class StartReplayTaskStartreplaytask(Model):
    """No documentation"""

    typename: Literal["StartReplayTaskPayload"] = Field(
        alias="__typename", default="StartReplayTaskPayload"
    )
    error: Optional[
        Union[
            StartReplayTaskStartreplaytaskCloudUserErrorInlineFragment,
            StartReplayTaskStartreplaytaskPermissionDeniedUserErrorInlineFragment,
            StartReplayTaskStartreplaytaskTaskInProgressUserErrorInlineFragment,
            StartReplayTaskStartreplaytaskUnknownIdUserErrorInlineFragment,
            StartReplayTaskStartreplaytaskOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    task: Optional[ReplayTaskMeta] = Field(default=None)


class StartReplayTask(Model):
    """No documentation found for this operation."""

    startReplayTask: StartReplayTaskStartreplaytask

    class Arguments(Model):
        """Arguments for StartReplayTask"""

        sessionId: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for StartReplayTask"""

        document = "fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskInProgressUserErrorFull on TaskInProgressUserError {\n  ...UserErrorFull\n  taskId\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation StartReplayTask($sessionId: ID!) {\n  startReplayTask(sessionId: $sessionId) {\n    error {\n      __typename\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on TaskInProgressUserError {\n        ...TaskInProgressUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    task {\n      ...ReplayTaskMeta\n      __typename\n    }\n    __typename\n  }\n}"


class Request(Model):
    """No documentation found for this operation."""

    request: Optional[RequestFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Request"""

        id: str
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Request"""

        document = "fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nquery Request($id: ID!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  request(id: $id) {\n    ...RequestFull\n    __typename\n  }\n}"


class Response(Model):
    """No documentation found for this operation."""

    response: Optional[ResponseFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Response"""

        id: str
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Response"""

        document = "fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nquery Response($id: ID!, $includeResponseRaw: Boolean!) {\n  response(id: $id) {\n    ...ResponseFull\n    __typename\n  }\n}"


class RequestsRequestsEdges(Model):
    """An edge in a connection."""

    typename: Literal["RequestEdge"] = Field(alias="__typename", default="RequestEdge")
    cursor: str
    "A cursor for use in pagination"
    node: RequestFull
    "The item at the end of the edge"


class RequestsRequestsPageinfo(Model):
    """Information about pagination in a connection"""

    typename: Literal["PageInfo"] = Field(alias="__typename", default="PageInfo")
    hasNextPage: bool
    "When paginating forwards, are there more items?"
    hasPreviousPage: bool
    "When paginating backwards, are there more items?"
    startCursor: Optional[str] = Field(default=None)
    "When paginating backwards, the cursor to continue."
    endCursor: Optional[str] = Field(default=None)
    "When paginating forwards, the cursor to continue."


class RequestsRequests(Model):
    """No documentation"""

    typename: Literal["RequestConnection"] = Field(
        alias="__typename", default="RequestConnection"
    )
    edges: List[RequestsRequestsEdges]
    "A list of edges."
    pageInfo: RequestsRequestsPageinfo
    "Information to aid in pagination."


class Requests(Model):
    """No documentation found for this operation."""

    requests: RequestsRequests

    class Arguments(Model):
        """Arguments for Requests"""

        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        filter: Optional[HTTPQLInput] = Field(default=None)
        order: Optional[RequestResponseOrderInput] = Field(default=None)
        scopeId: Optional[str] = Field(default=None)
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Requests"""

        document = "fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nquery Requests($first: Int, $after: String, $last: Int, $before: String, $filter: HTTPQLInput, $order: RequestResponseOrderInput, $scopeId: ID, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  requests(\n    first: $first\n    after: $after\n    last: $last\n    before: $before\n    filter: $filter\n    order: $order\n    scopeId: $scopeId\n  ) {\n    edges {\n      cursor\n      node {\n        ...RequestFull\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}"


class Scopes(Model):
    """No documentation found for this operation."""

    scopes: List[ScopeFull]

    class Arguments(Model):
        """Arguments for Scopes"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Scopes"""

        document = "fragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nquery Scopes {\n  scopes {\n    ...ScopeFull\n    __typename\n  }\n}"


class Scope(Model):
    """No documentation found for this operation."""

    scope: Optional[ScopeFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Scope"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Scope"""

        document = "fragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nquery Scope($id: ID!) {\n  scope(id: $id) {\n    ...ScopeFull\n    __typename\n  }\n}"


class CreateScopeCreatescopeInvalidGlobTermsUserErrorInlineFragment(
    InvalidGlobTermsUserErrorFull, Model
):
    pass


class CreateScopeCreatescopeOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class CreateScopeCreatescope(Model):
    """No documentation"""

    typename: Literal["CreateScopePayload"] = Field(
        alias="__typename", default="CreateScopePayload"
    )
    error: Optional[
        Union[
            CreateScopeCreatescopeInvalidGlobTermsUserErrorInlineFragment,
            CreateScopeCreatescopeOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    scope: Optional[ScopeFull] = Field(default=None)


class CreateScope(Model):
    """No documentation found for this operation."""

    createScope: CreateScopeCreatescope

    class Arguments(Model):
        """Arguments for CreateScope"""

        input: CreateScopeInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateScope"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment InvalidGlobTermsUserErrorFull on InvalidGlobTermsUserError {\n  ...UserErrorFull\n  terms\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nmutation CreateScope($input: CreateScopeInput!) {\n  createScope(input: $input) {\n    error {\n      __typename\n      ... on InvalidGlobTermsUserError {\n        ...InvalidGlobTermsUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    scope {\n      ...ScopeFull\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateScopeUpdatescopeInvalidGlobTermsUserErrorInlineFragment(
    InvalidGlobTermsUserErrorFull, Model
):
    pass


class UpdateScopeUpdatescopeOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class UpdateScopeUpdatescope(Model):
    """No documentation"""

    typename: Literal["UpdateScopePayload"] = Field(
        alias="__typename", default="UpdateScopePayload"
    )
    error: Optional[
        Union[
            UpdateScopeUpdatescopeInvalidGlobTermsUserErrorInlineFragment,
            UpdateScopeUpdatescopeOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    scope: Optional[ScopeFull] = Field(default=None)


class UpdateScope(Model):
    """No documentation found for this operation."""

    updateScope: UpdateScopeUpdatescope

    class Arguments(Model):
        """Arguments for UpdateScope"""

        id: str
        input: UpdateScopeInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateScope"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment InvalidGlobTermsUserErrorFull on InvalidGlobTermsUserError {\n  ...UserErrorFull\n  terms\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nmutation UpdateScope($id: ID!, $input: UpdateScopeInput!) {\n  updateScope(id: $id, input: $input) {\n    error {\n      __typename\n      ... on InvalidGlobTermsUserError {\n        ...InvalidGlobTermsUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    scope {\n      ...ScopeFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteScopeDeletescope(Model):
    """No documentation"""

    typename: Literal["DeleteScopePayload"] = Field(
        alias="__typename", default="DeleteScopePayload"
    )
    deletedId: str


class DeleteScope(Model):
    """No documentation found for this operation."""

    deleteScope: DeleteScopeDeletescope

    class Arguments(Model):
        """Arguments for DeleteScope"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteScope"""

        document = "mutation DeleteScope($id: ID!) {\n  deleteScope(id: $id) {\n    deletedId\n    __typename\n  }\n}"


class TasksTasksBase(Model):
    """No documentation"""


class TasksTasksBaseDataExportTask(TaskMetaDataExportTask, TasksTasksBase, Model):
    """No documentation"""

    typename: Literal["DataExportTask"] = Field(
        alias="__typename", default="DataExportTask"
    )


class TasksTasksBaseDeleteStreamWsMessageTask(
    TaskMetaDeleteStreamWsMessageTask, TasksTasksBase, Model
):
    """No documentation"""

    typename: Literal["DeleteStreamWsMessageTask"] = Field(
        alias="__typename", default="DeleteStreamWsMessageTask"
    )


class TasksTasksBaseReplayTask(ReplayTaskMeta, TasksTasksBase, Model):
    """No documentation"""

    typename: Literal["ReplayTask"] = Field(alias="__typename", default="ReplayTask")


class TasksTasksBaseWorkflowTask(TaskMetaWorkflowTask, TasksTasksBase, Model):
    """No documentation"""

    typename: Literal["WorkflowTask"] = Field(
        alias="__typename", default="WorkflowTask"
    )


class TasksTasksBaseCatchAll(TasksTasksBase, Model):
    """Catch all class for TasksTasksBase"""

    typename: str = Field(alias="__typename")


class Tasks(Model):
    """No documentation found for this operation."""

    tasks: List[
        Union[
            Annotated[
                Union[
                    TasksTasksBaseDataExportTask,
                    TasksTasksBaseDeleteStreamWsMessageTask,
                    TasksTasksBaseReplayTask,
                    TasksTasksBaseWorkflowTask,
                ],
                Field(discriminator="typename"),
            ],
            TasksTasksBaseCatchAll,
        ]
    ]

    class Arguments(Model):
        """Arguments for Tasks"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Tasks"""

        document = "fragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nquery Tasks {\n  tasks {\n    ...TaskMeta\n    ... on ReplayTask {\n      ...ReplayTaskMeta\n    }\n    __typename\n  }\n}"


class cancelTaskCanceltaskUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class cancelTaskCanceltaskOtherUserErrorInlineFragment(OtherUserErrorFull, Model):
    pass


class cancelTaskCanceltask(Model):
    """No documentation"""

    typename: Literal["CancelTaskPayload"] = Field(
        alias="__typename", default="CancelTaskPayload"
    )
    cancelledId: Optional[str] = Field(default=None)
    error: Optional[
        Union[
            cancelTaskCanceltaskUnknownIdUserErrorInlineFragment,
            cancelTaskCanceltaskOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class cancelTask(Model):
    """No documentation found for this operation."""

    cancelTask: cancelTaskCanceltask

    class Arguments(Model):
        """Arguments for cancelTask"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for cancelTask"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation cancelTask($id: ID!) {\n  cancelTask(id: $id) {\n    cancelledId\n    error {\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      __typename\n    }\n    __typename\n  }\n}"


class FinishedTaskFinishedtaskTaskBase(Model):
    """No documentation"""


class FinishedTaskFinishedtaskTaskBaseDataExportTask(
    TaskMetaDataExportTask, FinishedTaskFinishedtaskTaskBase, Model
):
    """No documentation"""

    typename: Literal["DataExportTask"] = Field(
        alias="__typename", default="DataExportTask"
    )


class FinishedTaskFinishedtaskTaskBaseDeleteStreamWsMessageTask(
    TaskMetaDeleteStreamWsMessageTask, FinishedTaskFinishedtaskTaskBase, Model
):
    """No documentation"""

    typename: Literal["DeleteStreamWsMessageTask"] = Field(
        alias="__typename", default="DeleteStreamWsMessageTask"
    )


class FinishedTaskFinishedtaskTaskBaseReplayTask(
    ReplayTaskMeta, FinishedTaskFinishedtaskTaskBase, Model
):
    """No documentation"""

    typename: Literal["ReplayTask"] = Field(alias="__typename", default="ReplayTask")


class FinishedTaskFinishedtaskTaskBaseWorkflowTask(
    TaskMetaWorkflowTask, FinishedTaskFinishedtaskTaskBase, Model
):
    """No documentation"""

    typename: Literal["WorkflowTask"] = Field(
        alias="__typename", default="WorkflowTask"
    )


class FinishedTaskFinishedtaskTaskBaseCatchAll(FinishedTaskFinishedtaskTaskBase, Model):
    """Catch all class for FinishedTaskFinishedtaskTaskBase"""

    typename: str = Field(alias="__typename")


class FinishedTaskFinishedtaskErrorBase(Model):
    """No documentation"""

    code: str


class FinishedTaskFinishedtaskErrorBaseAIUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["AIUserError"] = Field(alias="__typename", default="AIUserError")


class FinishedTaskFinishedtaskErrorBaseAliasTakenUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["AliasTakenUserError"] = Field(
        alias="__typename", default="AliasTakenUserError"
    )


class FinishedTaskFinishedtaskErrorBaseAssistantUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["AssistantUserError"] = Field(
        alias="__typename", default="AssistantUserError"
    )


class FinishedTaskFinishedtaskErrorBaseAuthenticationUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["AuthenticationUserError"] = Field(
        alias="__typename", default="AuthenticationUserError"
    )


class FinishedTaskFinishedtaskErrorBaseAuthorizationUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["AuthorizationUserError"] = Field(
        alias="__typename", default="AuthorizationUserError"
    )


class FinishedTaskFinishedtaskErrorBaseAutomateTaskUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["AutomateTaskUserError"] = Field(
        alias="__typename", default="AutomateTaskUserError"
    )


class FinishedTaskFinishedtaskErrorBaseBackupUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["BackupUserError"] = Field(
        alias="__typename", default="BackupUserError"
    )


class FinishedTaskFinishedtaskErrorBaseCertificateUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["CertificateUserError"] = Field(
        alias="__typename", default="CertificateUserError"
    )


class FinishedTaskFinishedtaskErrorBaseCloudUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["CloudUserError"] = Field(
        alias="__typename", default="CloudUserError"
    )


class FinishedTaskFinishedtaskErrorBaseInternalUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InternalUserError"] = Field(
        alias="__typename", default="InternalUserError"
    )


class FinishedTaskFinishedtaskErrorBaseInvalidGlobTermsUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InvalidGlobTermsUserError"] = Field(
        alias="__typename", default="InvalidGlobTermsUserError"
    )


class FinishedTaskFinishedtaskErrorBaseInvalidHTTPQLUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InvalidHTTPQLUserError"] = Field(
        alias="__typename", default="InvalidHTTPQLUserError"
    )


class FinishedTaskFinishedtaskErrorBaseInvalidRangeUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InvalidRangeUserError"] = Field(
        alias="__typename", default="InvalidRangeUserError"
    )


class FinishedTaskFinishedtaskErrorBaseInvalidRegexUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InvalidRegexUserError"] = Field(
        alias="__typename", default="InvalidRegexUserError"
    )


class FinishedTaskFinishedtaskErrorBaseInvalidStreamQLUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InvalidStreamQLUserError"] = Field(
        alias="__typename", default="InvalidStreamQLUserError"
    )


class FinishedTaskFinishedtaskErrorBaseNameTakenUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["NameTakenUserError"] = Field(
        alias="__typename", default="NameTakenUserError"
    )


class FinishedTaskFinishedtaskErrorBaseNewerVersionUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["NewerVersionUserError"] = Field(
        alias="__typename", default="NewerVersionUserError"
    )


class FinishedTaskFinishedtaskErrorBaseOtherUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["OtherUserError"] = Field(
        alias="__typename", default="OtherUserError"
    )


class FinishedTaskFinishedtaskErrorBasePermissionDeniedUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["PermissionDeniedUserError"] = Field(
        alias="__typename", default="PermissionDeniedUserError"
    )


class FinishedTaskFinishedtaskErrorBasePluginUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["PluginUserError"] = Field(
        alias="__typename", default="PluginUserError"
    )


class FinishedTaskFinishedtaskErrorBaseProjectUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["ProjectUserError"] = Field(
        alias="__typename", default="ProjectUserError"
    )


class FinishedTaskFinishedtaskErrorBaseRankUserError(
    RankUserErrorFull, FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["RankUserError"] = Field(
        alias="__typename", default="RankUserError"
    )


class FinishedTaskFinishedtaskErrorBaseReadOnlyUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["ReadOnlyUserError"] = Field(
        alias="__typename", default="ReadOnlyUserError"
    )


class FinishedTaskFinishedtaskErrorBaseRenderFailedUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["RenderFailedUserError"] = Field(
        alias="__typename", default="RenderFailedUserError"
    )


class FinishedTaskFinishedtaskErrorBaseStoreUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["StoreUserError"] = Field(
        alias="__typename", default="StoreUserError"
    )


class FinishedTaskFinishedtaskErrorBaseTaskInProgressUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["TaskInProgressUserError"] = Field(
        alias="__typename", default="TaskInProgressUserError"
    )


class FinishedTaskFinishedtaskErrorBaseUnknownIdUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["UnknownIdUserError"] = Field(
        alias="__typename", default="UnknownIdUserError"
    )


class FinishedTaskFinishedtaskErrorBaseUnsupportedPlatformUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["UnsupportedPlatformUserError"] = Field(
        alias="__typename", default="UnsupportedPlatformUserError"
    )


class FinishedTaskFinishedtaskErrorBaseWSUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["WSUserError"] = Field(alias="__typename", default="WSUserError")


class FinishedTaskFinishedtaskErrorBaseWorkflowUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["WorkflowUserError"] = Field(
        alias="__typename", default="WorkflowUserError"
    )


class FinishedTaskFinishedtaskErrorBaseCatchAll(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """Catch all class for FinishedTaskFinishedtaskErrorBase"""

    typename: str = Field(alias="__typename")


class FinishedTaskFinishedtask(Model):
    """No documentation"""

    typename: Literal["FinishedTaskPayload"] = Field(
        alias="__typename", default="FinishedTaskPayload"
    )
    task: Union[
        Annotated[
            Union[
                FinishedTaskFinishedtaskTaskBaseDataExportTask,
                FinishedTaskFinishedtaskTaskBaseDeleteStreamWsMessageTask,
                FinishedTaskFinishedtaskTaskBaseReplayTask,
                FinishedTaskFinishedtaskTaskBaseWorkflowTask,
            ],
            Field(discriminator="typename"),
        ],
        FinishedTaskFinishedtaskTaskBaseCatchAll,
    ]
    status: TaskStatus
    error: Optional[
        Union[
            Annotated[
                Union[
                    FinishedTaskFinishedtaskErrorBaseAIUserError,
                    FinishedTaskFinishedtaskErrorBaseAliasTakenUserError,
                    FinishedTaskFinishedtaskErrorBaseAssistantUserError,
                    FinishedTaskFinishedtaskErrorBaseAuthenticationUserError,
                    FinishedTaskFinishedtaskErrorBaseAuthorizationUserError,
                    FinishedTaskFinishedtaskErrorBaseAutomateTaskUserError,
                    FinishedTaskFinishedtaskErrorBaseBackupUserError,
                    FinishedTaskFinishedtaskErrorBaseCertificateUserError,
                    FinishedTaskFinishedtaskErrorBaseCloudUserError,
                    FinishedTaskFinishedtaskErrorBaseInternalUserError,
                    FinishedTaskFinishedtaskErrorBaseInvalidGlobTermsUserError,
                    FinishedTaskFinishedtaskErrorBaseInvalidHTTPQLUserError,
                    FinishedTaskFinishedtaskErrorBaseInvalidRangeUserError,
                    FinishedTaskFinishedtaskErrorBaseInvalidRegexUserError,
                    FinishedTaskFinishedtaskErrorBaseInvalidStreamQLUserError,
                    FinishedTaskFinishedtaskErrorBaseNameTakenUserError,
                    FinishedTaskFinishedtaskErrorBaseNewerVersionUserError,
                    FinishedTaskFinishedtaskErrorBaseOtherUserError,
                    FinishedTaskFinishedtaskErrorBasePermissionDeniedUserError,
                    FinishedTaskFinishedtaskErrorBasePluginUserError,
                    FinishedTaskFinishedtaskErrorBaseProjectUserError,
                    FinishedTaskFinishedtaskErrorBaseRankUserError,
                    FinishedTaskFinishedtaskErrorBaseReadOnlyUserError,
                    FinishedTaskFinishedtaskErrorBaseRenderFailedUserError,
                    FinishedTaskFinishedtaskErrorBaseStoreUserError,
                    FinishedTaskFinishedtaskErrorBaseTaskInProgressUserError,
                    FinishedTaskFinishedtaskErrorBaseUnknownIdUserError,
                    FinishedTaskFinishedtaskErrorBaseUnsupportedPlatformUserError,
                    FinishedTaskFinishedtaskErrorBaseWSUserError,
                    FinishedTaskFinishedtaskErrorBaseWorkflowUserError,
                ],
                Field(discriminator="typename"),
            ],
            FinishedTaskFinishedtaskErrorBaseCatchAll,
        ]
    ] = Field(default=None)


class FinishedTask(Model):
    """No documentation found for this operation."""

    finishedTask: FinishedTaskFinishedtask

    class Arguments(Model):
        """Arguments for FinishedTask"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for FinishedTask"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment RankUserErrorFull on RankUserError {\n  ...UserErrorFull\n  rankReason: reason\n  __typename\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nsubscription FinishedTask {\n  finishedTask {\n    task {\n      ...TaskMeta\n      ... on ReplayTask {\n        ...ReplayTaskMeta\n      }\n      __typename\n    }\n    status\n    error {\n      __typename\n      code\n      ... on RankUserError {\n        ...RankUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class ViewerCloudUserInlineFragmentProfileIdentity(Model):
    """No documentation"""

    typename: Literal["UserIdentity"] = Field(
        alias="__typename", default="UserIdentity"
    )
    email: str
    name: str


class ViewerCloudUserInlineFragmentProfileSubscriptionPlan(Model):
    """No documentation"""

    typename: Literal["UserSubscriptionPlan"] = Field(
        alias="__typename", default="UserSubscriptionPlan"
    )
    name: str


class ViewerCloudUserInlineFragmentProfileSubscriptionEntitlements(Model):
    """No documentation"""

    typename: Literal["UserEntitlement"] = Field(
        alias="__typename", default="UserEntitlement"
    )
    name: str


class ViewerCloudUserInlineFragmentProfileSubscription(Model):
    """No documentation"""

    typename: Literal["UserSubscription"] = Field(
        alias="__typename", default="UserSubscription"
    )
    plan: ViewerCloudUserInlineFragmentProfileSubscriptionPlan
    entitlements: List[ViewerCloudUserInlineFragmentProfileSubscriptionEntitlements]


class ViewerCloudUserInlineFragmentProfile(Model):
    """No documentation"""

    typename: Literal["UserProfile"] = Field(alias="__typename", default="UserProfile")
    identity: ViewerCloudUserInlineFragmentProfileIdentity
    subscription: ViewerCloudUserInlineFragmentProfileSubscription


class ViewerCloudUserInlineFragment(Model):
    typename: Literal["CloudUser"] = Field(alias="__typename", default="CloudUser")
    id: str
    profile: ViewerCloudUserInlineFragmentProfile


class ViewerGuestUserInlineFragment(Model):
    typename: Literal["GuestUser"] = Field(alias="__typename", default="GuestUser")
    id: str


class ViewerScriptUserInlineFragment(Model):
    typename: Literal["ScriptUser"] = Field(alias="__typename", default="ScriptUser")
    id: str


class Viewer(Model):
    """No documentation found for this operation."""

    viewer: Union[
        ViewerCloudUserInlineFragment,
        ViewerGuestUserInlineFragment,
        ViewerScriptUserInlineFragment,
    ]

    class Arguments(Model):
        """Arguments for Viewer"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Viewer"""

        document = "query Viewer {\n  viewer {\n    ... on CloudUser {\n      __typename\n      id\n      profile {\n        identity {\n          email\n          name\n        }\n        subscription {\n          plan {\n            name\n          }\n          entitlements {\n            name\n          }\n        }\n      }\n    }\n    ... on GuestUser {\n      __typename\n      id\n    }\n    ... on ScriptUser {\n      __typename\n      id\n    }\n    __typename\n  }\n}"


class Workflows(Model):
    """No documentation found for this operation."""

    workflows: List[WorkflowFull]

    class Arguments(Model):
        """Arguments for Workflows"""

        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Workflows"""

        document = "fragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nquery Workflows {\n  workflows {\n    ...WorkflowFull\n    __typename\n  }\n}"


class Workflow(Model):
    """No documentation found for this operation."""

    workflow: Optional[WorkflowFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Workflow"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Workflow"""

        document = "fragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nquery Workflow($id: ID!) {\n  workflow(id: $id) {\n    ...WorkflowFull\n    __typename\n  }\n}"


class CreateWorkflowCreateworkflowWorkflowUserErrorInlineFragment(
    WorkflowUserErrorFull, Model
):
    pass


class CreateWorkflowCreateworkflowOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class CreateWorkflowCreateworkflowPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class CreateWorkflowCreateworkflow(Model):
    """No documentation"""

    typename: Literal["CreateWorkflowPayload"] = Field(
        alias="__typename", default="CreateWorkflowPayload"
    )
    error: Optional[
        Union[
            CreateWorkflowCreateworkflowWorkflowUserErrorInlineFragment,
            CreateWorkflowCreateworkflowOtherUserErrorInlineFragment,
            CreateWorkflowCreateworkflowPermissionDeniedUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    workflow: Optional[WorkflowFull] = Field(default=None)


class CreateWorkflow(Model):
    """No documentation found for this operation."""

    createWorkflow: CreateWorkflowCreateworkflow

    class Arguments(Model):
        """Arguments for CreateWorkflow"""

        input: CreateWorkflowInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateWorkflow"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation CreateWorkflow($input: CreateWorkflowInput!) {\n  createWorkflow(input: $input) {\n    error {\n      __typename\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n    }\n    workflow {\n      ...WorkflowFull\n      __typename\n    }\n    __typename\n  }\n}"


class UpdateWorkflowUpdateworkflowUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class UpdateWorkflowUpdateworkflowWorkflowUserErrorInlineFragment(
    WorkflowUserErrorFull, Model
):
    pass


class UpdateWorkflowUpdateworkflowOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class UpdateWorkflowUpdateworkflowReadOnlyUserErrorInlineFragment(
    ReadOnlyUserErrorFull, Model
):
    pass


class UpdateWorkflowUpdateworkflow(Model):
    """No documentation"""

    typename: Literal["UpdateWorkflowPayload"] = Field(
        alias="__typename", default="UpdateWorkflowPayload"
    )
    error: Optional[
        Union[
            UpdateWorkflowUpdateworkflowUnknownIdUserErrorInlineFragment,
            UpdateWorkflowUpdateworkflowWorkflowUserErrorInlineFragment,
            UpdateWorkflowUpdateworkflowOtherUserErrorInlineFragment,
            UpdateWorkflowUpdateworkflowReadOnlyUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    workflow: Optional[WorkflowFull] = Field(default=None)


class UpdateWorkflow(Model):
    """No documentation found for this operation."""

    updateWorkflow: UpdateWorkflowUpdateworkflow

    class Arguments(Model):
        """Arguments for UpdateWorkflow"""

        id: str
        input: UpdateWorkflowInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateWorkflow"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ReadOnlyUserErrorFull on ReadOnlyUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nfragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation UpdateWorkflow($id: ID!, $input: UpdateWorkflowInput!) {\n  updateWorkflow(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on ReadOnlyUserError {\n        ...ReadOnlyUserErrorFull\n      }\n    }\n    workflow {\n      ...WorkflowFull\n      __typename\n    }\n    __typename\n  }\n}"


class DeleteWorkflowDeleteworkflowUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class DeleteWorkflowDeleteworkflowReadOnlyUserErrorInlineFragment(
    ReadOnlyUserErrorFull, Model
):
    pass


class DeleteWorkflowDeleteworkflowOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class DeleteWorkflowDeleteworkflow(Model):
    """No documentation"""

    typename: Literal["DeleteWorkflowPayload"] = Field(
        alias="__typename", default="DeleteWorkflowPayload"
    )
    deletedId: Optional[str] = Field(default=None)
    error: Optional[
        Union[
            DeleteWorkflowDeleteworkflowUnknownIdUserErrorInlineFragment,
            DeleteWorkflowDeleteworkflowReadOnlyUserErrorInlineFragment,
            DeleteWorkflowDeleteworkflowOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)


class DeleteWorkflow(Model):
    """No documentation found for this operation."""

    deleteWorkflow: DeleteWorkflowDeleteworkflow

    class Arguments(Model):
        """Arguments for DeleteWorkflow"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteWorkflow"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ReadOnlyUserErrorFull on ReadOnlyUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation DeleteWorkflow($id: ID!) {\n  deleteWorkflow(id: $id) {\n    deletedId\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on ReadOnlyUserError {\n        ...ReadOnlyUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}"


class TestWorkflowConvertTestworkflowconvertWorkflowUserErrorInlineFragment(
    WorkflowUserErrorFull, Model
):
    pass


class TestWorkflowConvertTestworkflowconvertPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class TestWorkflowConvertTestworkflowconvertOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class TestWorkflowConvertTestworkflowconvert(Model):
    """No documentation"""

    typename: Literal["TestWorkflowConvertPayload"] = Field(
        alias="__typename", default="TestWorkflowConvertPayload"
    )
    error: Optional[
        Union[
            TestWorkflowConvertTestworkflowconvertWorkflowUserErrorInlineFragment,
            TestWorkflowConvertTestworkflowconvertPermissionDeniedUserErrorInlineFragment,
            TestWorkflowConvertTestworkflowconvertOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    output: Optional[str] = Field(default=None)
    runState: Optional[dict] = Field(default=None)


class TestWorkflowConvert(Model):
    """No documentation found for this operation."""

    testWorkflowConvert: TestWorkflowConvertTestworkflowconvert

    class Arguments(Model):
        """Arguments for TestWorkflowConvert"""

        input: TestWorkflowConvertInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for TestWorkflowConvert"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation TestWorkflowConvert($input: TestWorkflowConvertInput!) {\n  testWorkflowConvert(input: $input) {\n    error {\n      __typename\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    output\n    runState\n    __typename\n  }\n}"


class TestWorkflowPassiveTestworkflowpassiveWorkflowUserErrorInlineFragment(
    WorkflowUserErrorFull, Model
):
    pass


class TestWorkflowPassiveTestworkflowpassivePermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class TestWorkflowPassiveTestworkflowpassiveOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class TestWorkflowPassiveTestworkflowpassive(Model):
    """No documentation"""

    typename: Literal["TestWorkflowPassivePayload"] = Field(
        alias="__typename", default="TestWorkflowPassivePayload"
    )
    error: Optional[
        Union[
            TestWorkflowPassiveTestworkflowpassiveWorkflowUserErrorInlineFragment,
            TestWorkflowPassiveTestworkflowpassivePermissionDeniedUserErrorInlineFragment,
            TestWorkflowPassiveTestworkflowpassiveOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    runState: Optional[dict] = Field(default=None)


class TestWorkflowPassive(Model):
    """No documentation found for this operation."""

    testWorkflowPassive: TestWorkflowPassiveTestworkflowpassive

    class Arguments(Model):
        """Arguments for TestWorkflowPassive"""

        input: TestWorkflowPassiveInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for TestWorkflowPassive"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation TestWorkflowPassive($input: TestWorkflowPassiveInput!) {\n  testWorkflowPassive(input: $input) {\n    error {\n      __typename\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    runState\n    __typename\n  }\n}"


class TestWorkflowActiveTestworkflowactiveWorkflowUserErrorInlineFragment(
    WorkflowUserErrorFull, Model
):
    pass


class TestWorkflowActiveTestworkflowactivePermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class TestWorkflowActiveTestworkflowactiveOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class TestWorkflowActiveTestworkflowactive(Model):
    """No documentation"""

    typename: Literal["TestWorkflowActivePayload"] = Field(
        alias="__typename", default="TestWorkflowActivePayload"
    )
    error: Optional[
        Union[
            TestWorkflowActiveTestworkflowactiveWorkflowUserErrorInlineFragment,
            TestWorkflowActiveTestworkflowactivePermissionDeniedUserErrorInlineFragment,
            TestWorkflowActiveTestworkflowactiveOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    runState: Optional[dict] = Field(default=None)


class TestWorkflowActive(Model):
    """No documentation found for this operation."""

    testWorkflowActive: TestWorkflowActiveTestworkflowactive

    class Arguments(Model):
        """Arguments for TestWorkflowActive"""

        input: TestWorkflowActiveInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for TestWorkflowActive"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation TestWorkflowActive($input: TestWorkflowActiveInput!) {\n  testWorkflowActive(input: $input) {\n    error {\n      __typename\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    runState\n    __typename\n  }\n}"


class ToggleWorkflowToggleworkflowUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class ToggleWorkflowToggleworkflowOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class ToggleWorkflowToggleworkflow(Model):
    """No documentation"""

    typename: Literal["ToggleWorkflowPayload"] = Field(
        alias="__typename", default="ToggleWorkflowPayload"
    )
    error: Optional[
        Union[
            ToggleWorkflowToggleworkflowUnknownIdUserErrorInlineFragment,
            ToggleWorkflowToggleworkflowOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    workflow: Optional[WorkflowFull] = Field(default=None)


class ToggleWorkflow(Model):
    """No documentation found for this operation."""

    toggleWorkflow: ToggleWorkflowToggleworkflow

    class Arguments(Model):
        """Arguments for ToggleWorkflow"""

        id: str
        enabled: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ToggleWorkflow"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nfragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nmutation ToggleWorkflow($id: ID!, $enabled: Boolean!) {\n  toggleWorkflow(id: $id, enabled: $enabled) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    workflow {\n      ...WorkflowFull\n      __typename\n    }\n    __typename\n  }\n}"


class RunConvertWorkflowRunconvertworkflowWorkflowUserErrorInlineFragment(
    WorkflowUserErrorFull, Model
):
    pass


class RunConvertWorkflowRunconvertworkflowPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class RunConvertWorkflowRunconvertworkflowOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class RunConvertWorkflowRunconvertworkflow(Model):
    """No documentation"""

    typename: Literal["RunConvertWorkflowPayload"] = Field(
        alias="__typename", default="RunConvertWorkflowPayload"
    )
    error: Optional[
        Union[
            RunConvertWorkflowRunconvertworkflowWorkflowUserErrorInlineFragment,
            RunConvertWorkflowRunconvertworkflowPermissionDeniedUserErrorInlineFragment,
            RunConvertWorkflowRunconvertworkflowOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    output: Optional[str] = Field(default=None)


class RunConvertWorkflow(Model):
    """No documentation found for this operation."""

    runConvertWorkflow: RunConvertWorkflowRunconvertworkflow

    class Arguments(Model):
        """Arguments for RunConvertWorkflow"""

        id: str
        input: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RunConvertWorkflow"""

        document = "fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation RunConvertWorkflow($id: ID!, $input: Blob!) {\n  runConvertWorkflow(id: $id, input: $input) {\n    error {\n      __typename\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    output\n    __typename\n  }\n}"


class RunActiveWorkflowRunactiveworkflowUnknownIdUserErrorInlineFragment(
    UnknownIdUserErrorFull, Model
):
    pass


class RunActiveWorkflowRunactiveworkflowPermissionDeniedUserErrorInlineFragment(
    PermissionDeniedUserErrorFull, Model
):
    pass


class RunActiveWorkflowRunactiveworkflowOtherUserErrorInlineFragment(
    OtherUserErrorFull, Model
):
    pass


class RunActiveWorkflowRunactiveworkflow(Model):
    """No documentation"""

    typename: Literal["RunActiveWorkflowPayload"] = Field(
        alias="__typename", default="RunActiveWorkflowPayload"
    )
    error: Optional[
        Union[
            RunActiveWorkflowRunactiveworkflowUnknownIdUserErrorInlineFragment,
            RunActiveWorkflowRunactiveworkflowPermissionDeniedUserErrorInlineFragment,
            RunActiveWorkflowRunactiveworkflowOtherUserErrorInlineFragment,
        ]
    ] = Field(default=None)
    task: Optional[WorkflowTaskMeta] = Field(default=None)


class RunActiveWorkflow(Model):
    """No documentation found for this operation."""

    runActiveWorkflow: RunActiveWorkflowRunactiveworkflow

    class Arguments(Model):
        """Arguments for RunActiveWorkflow"""

        id: str
        input: RunActiveWorkflowInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RunActiveWorkflow"""

        document = "fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nfragment WorkflowTaskMeta on WorkflowTask {\n  ...TaskMeta\n  workflow {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation RunActiveWorkflow($id: ID!, $input: RunActiveWorkflowInput!) {\n  runActiveWorkflow(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    task {\n      ...WorkflowTaskMeta\n      __typename\n    }\n    __typename\n  }\n}"


CertificateInput.model_rebuild()
CreateDNSRewriteInput.model_rebuild()
CreateEnvironmentInput.model_rebuild()
CreateFilterPresetInput.model_rebuild()
CreateReplaySessionInput.model_rebuild()
DNSResolverInput.model_rebuild()
InstallPluginPackageInput.model_rebuild()
QueryInput.model_rebuild()
ReplayEntryHttpSettingsInput.model_rebuild()
ReplayPlaceholderInput.model_rebuild()
ReplayPreprocessorInput.model_rebuild()
ReplayPreprocessorOptionsInput.model_rebuild()
SetInstanceSettingsInput.model_rebuild()
UpdateReplayEntryDraftInput.model_rebuild()
