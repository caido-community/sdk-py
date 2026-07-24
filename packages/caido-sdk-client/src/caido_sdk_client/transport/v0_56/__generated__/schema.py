from enum import Enum
from typing import Annotated, List, Literal, Optional, Union

from caido_sdk_client.utils.pydantic import Model
from pydantic import ConfigDict, Field


class Deprecated:
    """Marks a field as deprecated, carrying the GraphQL deprecation reason."""

    def __init__(self, reason=None):
        self.reason = reason

    def __repr__(self):
        return "Deprecated(" + repr(self.reason) + ")"


class CloudErrorReason(str, Enum):
    """No documentation"""

    UNAVAILABLE = "UNAVAILABLE"
    UNEXPECTED = "UNEXPECTED"


class Ordering(str, Enum):
    """No documentation"""

    ASC = "ASC"
    DESC = "DESC"


class PermissionDeniedErrorReason(str, Enum):
    """No documentation"""

    ENTITLEMENT = "ENTITLEMENT"
    GUEST_USER = "GUEST_USER"
    SCRIPT_USER = "SCRIPT_USER"


class RankErrorReason(str, Enum):
    """No documentation"""

    CONCURRENT_UPDATE = "CONCURRENT_UPDATE"
    INVALID_AFTER_BEFORE = "INVALID_AFTER_BEFORE"
    NOT_ENABLED = "NOT_ENABLED"


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


class TaskStatus(str, Enum):
    """No documentation"""

    CANCELLED = "CANCELLED"
    DONE = "DONE"
    ERROR = "ERROR"


class ConnectionInfoInput(Model):
    """No documentation"""

    SNI: Optional[str] = None
    host: str
    isTLS: bool
    port: int


class CreateReplaySessionCollectionInput(Model):
    """No documentation"""

    name: str


class CreateReplaySessionInput(Model):
    """No documentation"""

    collectionId: Optional[str] = None
    requestSource: Optional["RequestSourceInput"] = None


class HTTPQLInput(Model):
    """No documentation"""

    code: str


class RangeInput(Model):
    """No documentation"""

    end: int
    start: int


class ReplayEntrySettingsInput(Model):
    """No documentation"""

    connectionClose: bool
    placeholders: List["ReplayPlaceholderInput"]
    updateContentLength: bool


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


class StartReplayTaskInput(Model):
    """No documentation"""

    connection: ConnectionInfoInput
    raw: str
    settings: ReplayEntrySettingsInput


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


class UserErrorFullInvalidRegexUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["InvalidRegexUserError"] = Field(
        alias="__typename", default="InvalidRegexUserError"
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


class UserErrorFullWorkflowUserError(UserErrorFullBase, Model):
    """No documentation"""

    typename: Literal["WorkflowUserError"] = Field(
        alias="__typename", default="WorkflowUserError"
    )


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


class ReplaySessionMetaCollection(Model):
    """No documentation"""

    typename: Literal["ReplaySessionCollection"] = Field(
        alias="__typename", default="ReplaySessionCollection"
    )
    id: str


class ReplaySessionMetaActiveentry(Model):
    """No documentation"""

    typename: Literal["ReplayEntry"] = Field(alias="__typename", default="ReplayEntry")
    id: str


class ReplaySessionMeta(Model):
    """No documentation"""

    typename: Literal["ReplaySession"] = Field(
        alias="__typename", default="ReplaySession"
    )
    id: str
    name: str
    collection: ReplaySessionMetaCollection
    activeEntry: Optional[ReplaySessionMetaActiveentry] = Field(default=None)

    class Meta:
        """Meta class for ReplaySessionMeta"""

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}"
        name = "ReplaySessionMeta"
        type = "ReplaySession"


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


class ReplayTaskMetaReplayentry(Model):
    """No documentation"""

    typename: Literal["ReplayEntry"] = Field(alias="__typename", default="ReplayEntry")
    id: str


class ReplayTaskMeta(TaskMetaReplayTask, Model):
    """No documentation"""

    typename: Literal["ReplayTask"] = Field(alias="__typename", default="ReplayTask")
    replayEntry: ReplayTaskMetaReplayentry

    class Meta:
        """Meta class for ReplayTaskMeta"""

        document = "fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}"
        name = "ReplayTaskMeta"
        type = "ReplayTask"


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


class ReplayEntryFullSession(Model):
    """No documentation"""

    typename: Literal["ReplaySession"] = Field(
        alias="__typename", default="ReplaySession"
    )
    id: str


class ReplayEntryFullSettings(Model):
    """No documentation"""

    typename: Literal["ReplayEntrySettings"] = Field(
        alias="__typename", default="ReplayEntrySettings"
    )
    placeholders: List[ReplayPlaceholderFull]


class ReplayEntryFull(Model):
    """No documentation"""

    typename: Literal["ReplayEntry"] = Field(alias="__typename", default="ReplayEntry")
    connection: ConnectionInfoFull
    createdAt: int
    error: Optional[str] = Field(default=None)
    id: str
    raw: str
    request: Optional[RequestFull] = Field(default=None)
    session: ReplayEntryFullSession
    settings: ReplayEntryFullSettings

    class Meta:
        """Meta class for ReplayEntryFull"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n  __typename\n}"
        name = "ReplayEntryFull"
        type = "ReplayEntry"


class ReplayEntry(Model):
    """No documentation found for this operation."""

    replayEntry: Optional[ReplayEntryFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplayEntry"""

        id: str
        includeReplayRaw: bool
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplayEntry"""

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery ReplayEntry($id: ID!, $includeReplayRaw: Boolean!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  replayEntry(id: $id) {\n    ...ReplayEntryFull\n    __typename\n  }\n}"


class ReplaySessionsReplaysessionsEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplaySessionEdge"] = Field(
        alias="__typename", default="ReplaySessionEdge"
    )
    cursor: str
    "A cursor for use in pagination"
    node: ReplaySessionMeta
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

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nquery ReplaySessions($first: Int, $after: String, $last: Int, $before: String) {\n  replaySessions(first: $first, after: $after, last: $last, before: $before) {\n    edges {\n      cursor\n      node {\n        ...ReplaySessionMeta\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}"


class ReplaySessionEntriesReplaysessionEntriesEdges(Model):
    """An edge in a connection."""

    typename: Literal["ReplayEntryEdge"] = Field(
        alias="__typename", default="ReplayEntryEdge"
    )
    cursor: str
    "A cursor for use in pagination"
    node: ReplayEntryFull
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


class ReplaySessionEntriesReplaysession(Model):
    """No documentation"""

    typename: Literal["ReplaySession"] = Field(
        alias="__typename", default="ReplaySession"
    )
    entries: ReplaySessionEntriesReplaysessionEntries


class ReplaySessionEntries(Model):
    """No documentation found for this operation."""

    replaySession: Optional[ReplaySessionEntriesReplaysession] = Field(default=None)

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

        document = "fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery ReplaySessionEntries($id: ID!, $after: String, $before: String, $first: Int, $last: Int, $includeReplayRaw: Boolean!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  replaySession(id: $id) {\n    entries(after: $after, before: $before, first: $first, last: $last) {\n      edges {\n        cursor\n        node {\n          ...ReplayEntryFull\n          __typename\n        }\n        __typename\n      }\n      pageInfo {\n        hasNextPage\n        hasPreviousPage\n        startCursor\n        endCursor\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"


class ReplaySession(Model):
    """No documentation found for this operation."""

    replaySession: Optional[ReplaySessionMeta] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplaySession"""

        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySession"""

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nquery ReplaySession($id: ID!) {\n  replaySession(id: $id) {\n    ...ReplaySessionMeta\n    __typename\n  }\n}"


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


class CreateReplaySessionCreatereplaysession(Model):
    """No documentation"""

    typename: Literal["CreateReplaySessionPayload"] = Field(
        alias="__typename", default="CreateReplaySessionPayload"
    )
    session: Optional[ReplaySessionMeta] = Field(default=None)


class CreateReplaySession(Model):
    """No documentation found for this operation."""

    createReplaySession: CreateReplaySessionCreatereplaysession

    class Arguments(Model):
        """Arguments for CreateReplaySession"""

        input: CreateReplaySessionInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateReplaySession"""

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation CreateReplaySession($input: CreateReplaySessionInput!) {\n  createReplaySession(input: $input) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


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


class MoveReplaySessionMovereplaysession(Model):
    """No documentation"""

    typename: Literal["MoveReplaySessionPayload"] = Field(
        alias="__typename", default="MoveReplaySessionPayload"
    )
    session: Optional[ReplaySessionMeta] = Field(default=None)


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

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation MoveReplaySession($id: ID!, $collectionId: ID!) {\n  moveReplaySession(id: $id, collectionId: $collectionId) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


class RenameReplaySessionRenamereplaysession(Model):
    """No documentation"""

    typename: Literal["RenameReplaySessionPayload"] = Field(
        alias="__typename", default="RenameReplaySessionPayload"
    )
    session: Optional[ReplaySessionMeta] = Field(default=None)


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

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation RenameReplaySession($id: ID!, $name: String!) {\n  renameReplaySession(id: $id, name: $name) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


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


class SetActiveReplaySessionEntrySetactivereplaysessionentry(Model):
    """No documentation"""

    typename: Literal["SetActiveReplaySessionEntryPayload"] = Field(
        alias="__typename", default="SetActiveReplaySessionEntryPayload"
    )
    session: Optional[ReplaySessionMeta] = Field(default=None)


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

        document = "fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation SetActiveReplaySessionEntry($id: ID!, $entryId: ID!) {\n  setActiveReplaySessionEntry(id: $id, entryId: $entryId) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}"


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
        input: StartReplayTaskInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for StartReplayTask"""

        document = "fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskInProgressUserErrorFull on TaskInProgressUserError {\n  ...UserErrorFull\n  taskId\n  __typename\n}\n\nmutation StartReplayTask($sessionId: ID!, $input: StartReplayTaskInput!) {\n  startReplayTask(sessionId: $sessionId, input: $input) {\n    error {\n      __typename\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on TaskInProgressUserError {\n        ...TaskInProgressUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    task {\n      ...ReplayTaskMeta\n      __typename\n    }\n    __typename\n  }\n}"


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


class FinishedTaskFinishedtaskErrorBaseInvalidRegexUserError(
    FinishedTaskFinishedtaskErrorBase, Model
):
    """No documentation"""

    typename: Literal["InvalidRegexUserError"] = Field(
        alias="__typename", default="InvalidRegexUserError"
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
                    FinishedTaskFinishedtaskErrorBaseInvalidRegexUserError,
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


CreateReplaySessionInput.model_rebuild()
ReplayEntrySettingsInput.model_rebuild()
ReplayPlaceholderInput.model_rebuild()
ReplayPreprocessorInput.model_rebuild()
ReplayPreprocessorOptionsInput.model_rebuild()
