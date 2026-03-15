from enum import Enum
from typing import Annotated, List, Literal, Optional, Union

from caido_sdk_client.utils.pydantic import Model
from gql import FileVar
from pydantic import ConfigDict, Field


class CloudErrorReason(str, Enum):
    """No documentation"""
    UNAVAILABLE = 'UNAVAILABLE'
    UNEXPECTED = 'UNEXPECTED'

class EnvironmentVariableKind(str, Enum):
    """No documentation"""
    PLAIN = 'PLAIN'
    SECRET = 'SECRET'

class FindingOrderBy(str, Enum):
    """No documentation"""
    CREATED_AT = 'CREATED_AT'
    HOST = 'HOST'
    ID = 'ID'
    PATH = 'PATH'
    REPORTER = 'REPORTER'
    TITLE = 'TITLE'

class HostedFileStatus(str, Enum):
    """No documentation"""
    ERROR = 'ERROR'
    READY = 'READY'

class Ordering(str, Enum):
    """No documentation"""
    ASC = 'ASC'
    DESC = 'DESC'

class PermissionDeniedErrorReason(str, Enum):
    """No documentation"""
    ENTITLEMENT = 'ENTITLEMENT'
    GUEST_USER = 'GUEST_USER'
    SCRIPT_USER = 'SCRIPT_USER'

class PluginErrorReason(str, Enum):
    """No documentation"""
    ALREADY_INSTALLED = 'ALREADY_INSTALLED'
    INVALID_MANIFEST = 'INVALID_MANIFEST'
    INVALID_OPERATION = 'INVALID_OPERATION'
    INVALID_PACKAGE = 'INVALID_PACKAGE'
    MISSING_FILE = 'MISSING_FILE'

class ProjectErrorReason(str, Enum):
    """No documentation"""
    DELETING = 'DELETING'
    EXPORTING = 'EXPORTING'
    INVALID_VERSION = 'INVALID_VERSION'
    NOT_READY = 'NOT_READY'
    TOO_RECENT = 'TOO_RECENT'

class ProjectStatus(str, Enum):
    """No documentation"""
    ERROR = 'ERROR'
    READY = 'READY'
    RESTORING = 'RESTORING'

class RankErrorReason(str, Enum):
    """No documentation"""
    CONCURRENT_UPDATE = 'CONCURRENT_UPDATE'
    INVALID_AFTER_BEFORE = 'INVALID_AFTER_BEFORE'
    NOT_ENABLED = 'NOT_ENABLED'

class RequestResponseOrderBy(str, Enum):
    """No documentation"""
    CREATED_AT = 'CREATED_AT'
    FILE_EXTENSION = 'FILE_EXTENSION'
    HOST = 'HOST'
    ID = 'ID'
    METHOD = 'METHOD'
    PATH = 'PATH'
    QUERY = 'QUERY'
    RESP_LENGTH = 'RESP_LENGTH'
    RESP_ROUNDTRIP_TIME = 'RESP_ROUNDTRIP_TIME'
    RESP_STATUS_CODE = 'RESP_STATUS_CODE'
    SOURCE = 'SOURCE'

class StoreErrorReason(str, Enum):
    """No documentation"""
    FILE_UNAVAILABLE = 'FILE_UNAVAILABLE'
    INVALID_PUBLIC_KEY = 'INVALID_PUBLIC_KEY'
    INVALID_SIGNATURE = 'INVALID_SIGNATURE'
    PACKAGE_TOO_LARGE = 'PACKAGE_TOO_LARGE'
    PACKAGE_UNKNOWN = 'PACKAGE_UNKNOWN'

class TaskStatus(str, Enum):
    """No documentation"""
    CANCELLED = 'CANCELLED'
    DONE = 'DONE'
    ERROR = 'ERROR'

class WorkflowErrorReason(str, Enum):
    """No documentation"""
    EXECUTION_ERROR = 'EXECUTION_ERROR'
    INVALID_INPUT = 'INVALID_INPUT'
    INVALID_PROPERTY = 'INVALID_PROPERTY'
    INVALID_TRIGGER = 'INVALID_TRIGGER'
    INVALID_WORKFLOW = 'INVALID_WORKFLOW'

class WorkflowKind(str, Enum):
    """No documentation"""
    ACTIVE = 'ACTIVE'
    CONVERT = 'CONVERT'
    PASSIVE = 'PASSIVE'

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

class ConnectionInfoInput(Model):
    """No documentation"""
    SNI: Optional[str] = None
    host: str
    isTLS: bool
    port: int

class CreateEnvironmentInput(Model):
    """No documentation"""
    name: str
    variables: List['EnvironmentVariableInput']

class CreateFilterPresetInput(Model):
    """No documentation"""
    alias: str
    clause: str
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
    requestSource: Optional['RequestSourceInput'] = None

class CreateScopeInput(Model):
    """No documentation"""
    allowlist: List[str]
    denylist: List[str]
    name: str

class CreateWorkflowInput(Model):
    """No documentation"""
    definition: dict
    global_: bool = Field(alias='global')

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

class InstallPluginPackageInput(Model):
    """No documentation"""
    force: Optional[bool] = None
    source: 'PluginPackageSource'

class PluginPackageSource(Model):
    """No documentation"""
    file: Optional[FileVar] = None
    manifestId: Optional[str] = None
    url: Optional[str] = None

class RangeInput(Model):
    """No documentation"""
    end: int
    start: int

class ReplayEntrySettingsInput(Model):
    """No documentation"""
    connectionClose: bool
    placeholders: List['ReplayPlaceholderInput']
    updateContentLength: bool

class ReplayEnvironmentPreprocessorInput(Model):
    """No documentation"""
    variableName: str

class ReplayPlaceholderInput(Model):
    """No documentation"""
    inputRange: RangeInput
    outputRange: RangeInput
    preprocessors: List['ReplayPreprocessorInput']

class ReplayPrefixPreprocessorInput(Model):
    """No documentation"""
    value: str

class ReplayPreprocessorInput(Model):
    """No documentation"""
    options: 'ReplayPreprocessorOptionsInput'

class ReplayPreprocessorOptionsInput(Model):
    """No documentation"""
    environment: Optional[ReplayEnvironmentPreprocessorInput] = None
    prefix: Optional[ReplayPrefixPreprocessorInput] = None
    suffix: Optional['ReplaySuffixPreprocessorInput'] = None
    urlEncode: Optional['ReplayUrlEncodePreprocessorInput'] = None
    workflow: Optional['ReplayWorkflowPreprocessorInput'] = None

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

class SetInstanceSettingsInput(Model):
    """No documentation"""
    aiProvider: Optional['SettingsAIProviderInput'] = None
    analytics: Optional['SettingsAnalyticInput'] = None
    onboarding: Optional['SettingsOnboardingInput'] = None

class SettingsAIProviderInput(Model):
    """No documentation"""
    anthropic: Optional[AIProviderAnthropicInput] = None
    google: Optional[AIProviderGoogleInput] = None
    openai: Optional[AIProviderOpenAIInput] = None
    openrouter: Optional[AIProviderOpenRouterInput] = None

class SettingsAnalyticInput(Model):
    """No documentation"""
    enabled: bool

class SettingsOnboardingInput(Model):
    """No documentation"""
    analytic: bool

class StartReplayTaskInput(Model):
    """No documentation"""
    connection: ConnectionInfoInput
    raw: str
    settings: ReplayEntrySettingsInput

class UpdateEnvironmentInput(Model):
    """No documentation"""
    name: str
    variables: List[EnvironmentVariableInput]
    version: int

class UpdateFilterPresetInput(Model):
    """No documentation"""
    alias: str
    clause: str
    name: str

class UpdateFindingInput(Model):
    """No documentation"""
    description: Optional[str] = None
    hidden: Optional[bool] = None
    title: Optional[str] = None

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
    typename: Literal['ConnectionInfo'] = Field(alias='__typename', default='ConnectionInfo')
    host: str
    port: int
    isTLS: bool
    SNI: Optional[str] = Field(default=None)

    class Meta:
        """Meta class for ConnectionInfoFull"""
        document = 'fragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}'
        name = 'ConnectionInfoFull'
        type = 'ConnectionInfo'

class EnvironmentFullVariables(Model):
    """No documentation"""
    typename: Literal['EnvironmentVariable'] = Field(alias='__typename', default='EnvironmentVariable')
    name: str
    value: str
    kind: EnvironmentVariableKind

class EnvironmentFull(Model):
    """No documentation"""
    typename: Literal['Environment'] = Field(alias='__typename', default='Environment')
    id: str
    name: str
    variables: List[EnvironmentFullVariables]
    version: int

    class Meta:
        """Meta class for EnvironmentFull"""
        document = 'fragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}'
        name = 'EnvironmentFull'
        type = 'Environment'

class UserErrorFullBase(Model):
    """No documentation"""
    code: str

class UserErrorFullCatch(UserErrorFullBase):
    """Catch all class for UserErrorFullBase"""
    typename: str = Field(alias='__typename')
    'No documentation'
    code: str

class UserErrorFullAIUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['AIUserError'] = Field(alias='__typename', default='AIUserError')

class UserErrorFullAliasTakenUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['AliasTakenUserError'] = Field(alias='__typename', default='AliasTakenUserError')

class UserErrorFullAssistantUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['AssistantUserError'] = Field(alias='__typename', default='AssistantUserError')

class UserErrorFullAuthenticationUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['AuthenticationUserError'] = Field(alias='__typename', default='AuthenticationUserError')

class UserErrorFullAuthorizationUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['AuthorizationUserError'] = Field(alias='__typename', default='AuthorizationUserError')

class UserErrorFullAutomateTaskUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['AutomateTaskUserError'] = Field(alias='__typename', default='AutomateTaskUserError')

class UserErrorFullBackupUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['BackupUserError'] = Field(alias='__typename', default='BackupUserError')

class UserErrorFullCertificateUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['CertificateUserError'] = Field(alias='__typename', default='CertificateUserError')

class UserErrorFullCloudUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class UserErrorFullInternalUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['InternalUserError'] = Field(alias='__typename', default='InternalUserError')

class UserErrorFullInvalidGlobTermsUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['InvalidGlobTermsUserError'] = Field(alias='__typename', default='InvalidGlobTermsUserError')

class UserErrorFullInvalidHTTPQLUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['InvalidHTTPQLUserError'] = Field(alias='__typename', default='InvalidHTTPQLUserError')

class UserErrorFullInvalidRegexUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['InvalidRegexUserError'] = Field(alias='__typename', default='InvalidRegexUserError')

class UserErrorFullNameTakenUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class UserErrorFullNewerVersionUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['NewerVersionUserError'] = Field(alias='__typename', default='NewerVersionUserError')

class UserErrorFullOtherUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class UserErrorFullPermissionDeniedUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class UserErrorFullPluginUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['PluginUserError'] = Field(alias='__typename', default='PluginUserError')

class UserErrorFullProjectUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['ProjectUserError'] = Field(alias='__typename', default='ProjectUserError')

class UserErrorFullRankUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['RankUserError'] = Field(alias='__typename', default='RankUserError')

class UserErrorFullReadOnlyUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['ReadOnlyUserError'] = Field(alias='__typename', default='ReadOnlyUserError')

class UserErrorFullRenderFailedUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['RenderFailedUserError'] = Field(alias='__typename', default='RenderFailedUserError')

class UserErrorFullStoreUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['StoreUserError'] = Field(alias='__typename', default='StoreUserError')

class UserErrorFullTaskInProgressUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['TaskInProgressUserError'] = Field(alias='__typename', default='TaskInProgressUserError')

class UserErrorFullUnknownIdUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class UserErrorFullUnsupportedPlatformUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['UnsupportedPlatformUserError'] = Field(alias='__typename', default='UnsupportedPlatformUserError')

class UserErrorFullWorkflowUserError(UserErrorFullBase, Model):
    """No documentation"""
    typename: Literal['WorkflowUserError'] = Field(alias='__typename', default='WorkflowUserError')

class FilterPresetFull(Model):
    """No documentation"""
    typename: Literal['FilterPreset'] = Field(alias='__typename', default='FilterPreset')
    id: str
    name: str
    alias: str
    clause: str

    class Meta:
        """Meta class for FilterPresetFull"""
        document = 'fragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause\n  __typename\n}'
        name = 'FilterPresetFull'
        type = 'FilterPreset'

class FindingFullRequest(Model):
    """No documentation"""
    typename: Literal['Request'] = Field(alias='__typename', default='Request')
    id: str

class FindingFull(Model):
    """No documentation"""
    typename: Literal['Finding'] = Field(alias='__typename', default='Finding')
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
        document = 'fragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}'
        name = 'FindingFull'
        type = 'Finding'

class HostedFileFull(Model):
    """No documentation"""
    typename: Literal['HostedFile'] = Field(alias='__typename', default='HostedFile')
    id: str
    name: str
    path: str
    size: int
    status: HostedFileStatus
    createdAt: str
    updatedAt: str

    class Meta:
        """Meta class for HostedFileFull"""
        document = 'fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}'
        name = 'HostedFileFull'
        type = 'HostedFile'

class InstanceAIProviderAnthropicFull(Model):
    """No documentation"""
    typename: Literal['AIProviderAnthropic'] = Field(alias='__typename', default='AIProviderAnthropic')
    apiKey: str

    class Meta:
        """Meta class for InstanceAIProviderAnthropicFull"""
        document = 'fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}'
        name = 'InstanceAIProviderAnthropicFull'
        type = 'AIProviderAnthropic'

class InstanceAIProviderGoogleFull(Model):
    """No documentation"""
    typename: Literal['AIProviderGoogle'] = Field(alias='__typename', default='AIProviderGoogle')
    apiKey: str

    class Meta:
        """Meta class for InstanceAIProviderGoogleFull"""
        document = 'fragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}'
        name = 'InstanceAIProviderGoogleFull'
        type = 'AIProviderGoogle'

class InstanceAIProviderOpenAIFull(Model):
    """No documentation"""
    typename: Literal['AIProviderOpenAI'] = Field(alias='__typename', default='AIProviderOpenAI')
    apiKey: str
    url: Optional[str] = Field(default=None)

    class Meta:
        """Meta class for InstanceAIProviderOpenAIFull"""
        document = 'fragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}'
        name = 'InstanceAIProviderOpenAIFull'
        type = 'AIProviderOpenAI'

class InstanceAIProviderOpenRouterFull(Model):
    """No documentation"""
    typename: Literal['AIProviderOpenRouter'] = Field(alias='__typename', default='AIProviderOpenRouter')
    apiKey: str

    class Meta:
        """Meta class for InstanceAIProviderOpenRouterFull"""
        document = 'fragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}'
        name = 'InstanceAIProviderOpenRouterFull'
        type = 'AIProviderOpenRouter'

class PluginPackageMetaPluginsBase(Model):
    """No documentation"""
    id: str
    manifestId: str
    enabled: bool

class PluginPackageMetaPluginsBasePluginBackend(PluginPackageMetaPluginsBase, Model):
    """No documentation"""
    typename: Literal['PluginBackend'] = Field(alias='__typename', default='PluginBackend')

class PluginPackageMetaPluginsBasePluginFrontend(PluginPackageMetaPluginsBase, Model):
    """No documentation"""
    typename: Literal['PluginFrontend'] = Field(alias='__typename', default='PluginFrontend')

class PluginPackageMetaPluginsBasePluginWorkflow(PluginPackageMetaPluginsBase, Model):
    """No documentation"""
    typename: Literal['PluginWorkflow'] = Field(alias='__typename', default='PluginWorkflow')

class PluginPackageMetaPluginsBaseCatchAll(PluginPackageMetaPluginsBase, Model):
    """Catch all class for PluginPackageMetaPluginsBase"""
    typename: str = Field(alias='__typename')

class PluginPackageMeta(Model):
    """No documentation"""
    typename: Literal['PluginPackage'] = Field(alias='__typename', default='PluginPackage')
    id: str
    manifestId: str
    plugins: List[Union[Annotated[Union[PluginPackageMetaPluginsBasePluginBackend, PluginPackageMetaPluginsBasePluginFrontend, PluginPackageMetaPluginsBasePluginWorkflow], Field(discriminator='typename')], PluginPackageMetaPluginsBaseCatchAll]]

    class Meta:
        """Meta class for PluginPackageMeta"""
        document = 'fragment PluginPackageMeta on PluginPackage {\n  id\n  manifestId\n  plugins {\n    __typename\n    id\n    manifestId\n    enabled\n  }\n  __typename\n}'
        name = 'PluginPackageMeta'
        type = 'PluginPackage'

class ProjectFull(Model):
    """No documentation"""
    typename: Literal['Project'] = Field(alias='__typename', default='Project')
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
    'Defines if the project would be read-only if selected by the caller'

    class Meta:
        """Meta class for ProjectFull"""
        document = 'fragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}'
        name = 'ProjectFull'
        type = 'Project'

class RangeFull(Model):
    """No documentation"""
    typename: Literal['Range'] = Field(alias='__typename', default='Range')
    start: int
    end: int

    class Meta:
        """Meta class for RangeFull"""
        document = 'fragment RangeFull on Range {\n  start\n  end\n  __typename\n}'
        name = 'RangeFull'
        type = 'Range'

class ReplayPrefixPreprocessorFull(Model):
    """No documentation"""
    typename: Literal['ReplayPrefixPreprocessor'] = Field(alias='__typename', default='ReplayPrefixPreprocessor')
    value: str

    class Meta:
        """Meta class for ReplayPrefixPreprocessorFull"""
        document = 'fragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}'
        name = 'ReplayPrefixPreprocessorFull'
        type = 'ReplayPrefixPreprocessor'

class ReplaySuffixPreprocessorFull(Model):
    """No documentation"""
    typename: Literal['ReplaySuffixPreprocessor'] = Field(alias='__typename', default='ReplaySuffixPreprocessor')
    value: str

    class Meta:
        """Meta class for ReplaySuffixPreprocessorFull"""
        document = 'fragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}'
        name = 'ReplaySuffixPreprocessorFull'
        type = 'ReplaySuffixPreprocessor'

class ReplayUrlEncodePreprocessorFull(Model):
    """No documentation"""
    typename: Literal['ReplayUrlEncodePreprocessor'] = Field(alias='__typename', default='ReplayUrlEncodePreprocessor')
    charset: Optional[str] = Field(default=None)
    nonAscii: bool

    class Meta:
        """Meta class for ReplayUrlEncodePreprocessorFull"""
        document = 'fragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}'
        name = 'ReplayUrlEncodePreprocessorFull'
        type = 'ReplayUrlEncodePreprocessor'

class ReplayWorkflowPreprocessorFull(Model):
    """No documentation"""
    typename: Literal['ReplayWorkflowPreprocessor'] = Field(alias='__typename', default='ReplayWorkflowPreprocessor')
    id: str

    class Meta:
        """Meta class for ReplayWorkflowPreprocessorFull"""
        document = 'fragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}'
        name = 'ReplayWorkflowPreprocessorFull'
        type = 'ReplayWorkflowPreprocessor'

class ReplayEnvironmentPreprocessorFull(Model):
    """No documentation"""
    typename: Literal['ReplayEnvironmentPreprocessor'] = Field(alias='__typename', default='ReplayEnvironmentPreprocessor')
    variableName: str

    class Meta:
        """Meta class for ReplayEnvironmentPreprocessorFull"""
        document = 'fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}'
        name = 'ReplayEnvironmentPreprocessorFull'
        type = 'ReplayEnvironmentPreprocessor'

class ReplayPreprocessorFullReplayPrefixPreprocessorInlineFragment(Model):
    typename: Literal['ReplayPrefixPreprocessor'] = Field(alias='__typename', default='ReplayPrefixPreprocessor')

class ReplayPreprocessorFullReplaySuffixPreprocessorInlineFragment(Model):
    typename: Literal['ReplaySuffixPreprocessor'] = Field(alias='__typename', default='ReplaySuffixPreprocessor')

class ReplayPreprocessorFullReplayUrlEncodePreprocessorInlineFragment(Model):
    typename: Literal['ReplayUrlEncodePreprocessor'] = Field(alias='__typename', default='ReplayUrlEncodePreprocessor')

class ReplayPreprocessorFullReplayWorkflowPreprocessorInlineFragment(Model):
    typename: Literal['ReplayWorkflowPreprocessor'] = Field(alias='__typename', default='ReplayWorkflowPreprocessor')

class ReplayPreprocessorFullReplayEnvironmentPreprocessorInlineFragment(Model):
    typename: Literal['ReplayEnvironmentPreprocessor'] = Field(alias='__typename', default='ReplayEnvironmentPreprocessor')

class ReplayPreprocessorFull(Model):
    """No documentation"""
    typename: Literal['ReplayPreprocessor'] = Field(alias='__typename', default='ReplayPreprocessor')
    options: Union[ReplayPreprocessorFullReplayPrefixPreprocessorInlineFragment, ReplayPreprocessorFullReplaySuffixPreprocessorInlineFragment, ReplayPreprocessorFullReplayUrlEncodePreprocessorInlineFragment, ReplayPreprocessorFullReplayWorkflowPreprocessorInlineFragment, ReplayPreprocessorFullReplayEnvironmentPreprocessorInlineFragment]

    class Meta:
        """Meta class for ReplayPreprocessorFull"""
        document = 'fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}'
        name = 'ReplayPreprocessorFull'
        type = 'ReplayPreprocessor'

class ReplaySessionMetaCollection(Model):
    """No documentation"""
    typename: Literal['ReplaySessionCollection'] = Field(alias='__typename', default='ReplaySessionCollection')
    id: str

class ReplaySessionMetaActiveentry(Model):
    """No documentation"""
    typename: Literal['ReplayEntry'] = Field(alias='__typename', default='ReplayEntry')
    id: str

class ReplaySessionMeta(Model):
    """No documentation"""
    typename: Literal['ReplaySession'] = Field(alias='__typename', default='ReplaySession')
    id: str
    name: str
    collection: ReplaySessionMetaCollection
    activeEntry: Optional[ReplaySessionMetaActiveentry] = Field(default=None)

    class Meta:
        """Meta class for ReplaySessionMeta"""
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}'
        name = 'ReplaySessionMeta'
        type = 'ReplaySession'

class ReplaySessionCollectionMeta(Model):
    """No documentation"""
    typename: Literal['ReplaySessionCollection'] = Field(alias='__typename', default='ReplaySessionCollection')
    id: str
    name: str

    class Meta:
        """Meta class for ReplaySessionCollectionMeta"""
        document = 'fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}'
        name = 'ReplaySessionCollectionMeta'
        type = 'ReplaySessionCollection'

class ResponseFull(Model):
    """No documentation"""
    typename: Literal['Response'] = Field(alias='__typename', default='Response')
    id: str
    statusCode: int
    roundtripTime: int
    length: int
    createdAt: int
    raw: str

    class Meta:
        """Meta class for ResponseFull"""
        document = 'fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}'
        name = 'ResponseFull'
        type = 'Response'

class ScopeFull(Model):
    """No documentation"""
    typename: Literal['Scope'] = Field(alias='__typename', default='Scope')
    id: str
    name: str
    allowlist: List[str]
    denylist: List[str]
    indexed: bool

    class Meta:
        """Meta class for ScopeFull"""
        document = 'fragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}'
        name = 'ScopeFull'
        type = 'Scope'

class TaskMetaBase(Model):
    """No documentation"""
    id: str
    createdAt: str

class TaskMetaCatch(TaskMetaBase):
    """Catch all class for TaskMetaBase"""
    typename: str = Field(alias='__typename')
    'No documentation'
    id: str
    createdAt: str

class TaskMetaDataExportTask(TaskMetaBase, Model):
    """No documentation"""
    typename: Literal['DataExportTask'] = Field(alias='__typename', default='DataExportTask')

class TaskMetaReplayTask(TaskMetaBase, Model):
    """No documentation"""
    typename: Literal['ReplayTask'] = Field(alias='__typename', default='ReplayTask')

class TaskMetaWorkflowTask(TaskMetaBase, Model):
    """No documentation"""
    typename: Literal['WorkflowTask'] = Field(alias='__typename', default='WorkflowTask')

class WorkflowFull(Model):
    """No documentation"""
    typename: Literal['Workflow'] = Field(alias='__typename', default='Workflow')
    id: str
    name: str
    kind: WorkflowKind
    definition: dict
    enabled: bool
    global_: bool = Field(alias='global')
    readOnly: bool
    createdAt: str
    updatedAt: str

    class Meta:
        """Meta class for WorkflowFull"""
        document = 'fragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}'
        name = 'WorkflowFull'
        type = 'Workflow'

class CloudUserErrorFull(UserErrorFullCloudUserError, Model):
    """No documentation"""
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')
    cloudReason: CloudErrorReason

    class Meta:
        """Meta class for CloudUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}'
        name = 'CloudUserErrorFull'
        type = 'CloudUserError'

class NameTakenUserErrorFull(UserErrorFullNameTakenUserError, Model):
    """No documentation"""
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')
    name: str

    class Meta:
        """Meta class for NameTakenUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}'
        name = 'NameTakenUserErrorFull'
        type = 'NameTakenUserError'

class UnknownIdUserErrorFull(UserErrorFullUnknownIdUserError, Model):
    """No documentation"""
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')
    id: str

    class Meta:
        """Meta class for UnknownIdUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}'
        name = 'UnknownIdUserErrorFull'
        type = 'UnknownIdUserError'

class PermissionDeniedUserErrorFull(UserErrorFullPermissionDeniedUserError, Model):
    """No documentation"""
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')
    permissionReason: PermissionDeniedErrorReason

    class Meta:
        """Meta class for PermissionDeniedUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}'
        name = 'PermissionDeniedUserErrorFull'
        type = 'PermissionDeniedUserError'

class ProjectUserErrorFull(UserErrorFullProjectUserError, Model):
    """No documentation"""
    typename: Literal['ProjectUserError'] = Field(alias='__typename', default='ProjectUserError')
    projectReason: ProjectErrorReason

    class Meta:
        """Meta class for ProjectUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment ProjectUserErrorFull on ProjectUserError {\n  ...UserErrorFull\n  projectReason: reason\n  __typename\n}'
        name = 'ProjectUserErrorFull'
        type = 'ProjectUserError'

class OtherUserErrorFull(UserErrorFullOtherUserError, Model):
    """No documentation"""
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

    class Meta:
        """Meta class for OtherUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}'
        name = 'OtherUserErrorFull'
        type = 'OtherUserError'

class ReadOnlyUserErrorFull(UserErrorFullReadOnlyUserError, Model):
    """No documentation"""
    typename: Literal['ReadOnlyUserError'] = Field(alias='__typename', default='ReadOnlyUserError')

    class Meta:
        """Meta class for ReadOnlyUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment ReadOnlyUserErrorFull on ReadOnlyUserError {\n  ...UserErrorFull\n  __typename\n}'
        name = 'ReadOnlyUserErrorFull'
        type = 'ReadOnlyUserError'

class InvalidGlobTermsUserErrorFull(UserErrorFullInvalidGlobTermsUserError, Model):
    """No documentation"""
    typename: Literal['InvalidGlobTermsUserError'] = Field(alias='__typename', default='InvalidGlobTermsUserError')
    terms: List[str]

    class Meta:
        """Meta class for InvalidGlobTermsUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment InvalidGlobTermsUserErrorFull on InvalidGlobTermsUserError {\n  ...UserErrorFull\n  terms\n  __typename\n}'
        name = 'InvalidGlobTermsUserErrorFull'
        type = 'InvalidGlobTermsUserError'

class AliasTakenUserErrorFull(UserErrorFullAliasTakenUserError, Model):
    """No documentation"""
    typename: Literal['AliasTakenUserError'] = Field(alias='__typename', default='AliasTakenUserError')
    alias: str

    class Meta:
        """Meta class for AliasTakenUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment AliasTakenUserErrorFull on AliasTakenUserError {\n  ...UserErrorFull\n  alias\n  __typename\n}'
        name = 'AliasTakenUserErrorFull'
        type = 'AliasTakenUserError'

class NewerVersionUserErrorFull(UserErrorFullNewerVersionUserError, Model):
    """No documentation"""
    typename: Literal['NewerVersionUserError'] = Field(alias='__typename', default='NewerVersionUserError')
    version: int

    class Meta:
        """Meta class for NewerVersionUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment NewerVersionUserErrorFull on NewerVersionUserError {\n  ...UserErrorFull\n  version\n  __typename\n}'
        name = 'NewerVersionUserErrorFull'
        type = 'NewerVersionUserError'

class PluginUserErrorFull(UserErrorFullPluginUserError, Model):
    """No documentation"""
    typename: Literal['PluginUserError'] = Field(alias='__typename', default='PluginUserError')
    reason: PluginErrorReason

    class Meta:
        """Meta class for PluginUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment PluginUserErrorFull on PluginUserError {\n  ...UserErrorFull\n  reason\n  __typename\n}'
        name = 'PluginUserErrorFull'
        type = 'PluginUserError'

class StoreUserErrorFull(UserErrorFullStoreUserError, Model):
    """No documentation"""
    typename: Literal['StoreUserError'] = Field(alias='__typename', default='StoreUserError')
    storeReason: StoreErrorReason

    class Meta:
        """Meta class for StoreUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment StoreUserErrorFull on StoreUserError {\n  ...UserErrorFull\n  storeReason: reason\n  __typename\n}'
        name = 'StoreUserErrorFull'
        type = 'StoreUserError'

class RankUserErrorFull(UserErrorFullRankUserError, Model):
    """No documentation"""
    typename: Literal['RankUserError'] = Field(alias='__typename', default='RankUserError')
    rankReason: RankErrorReason

    class Meta:
        """Meta class for RankUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment RankUserErrorFull on RankUserError {\n  ...UserErrorFull\n  rankReason: reason\n  __typename\n}'
        name = 'RankUserErrorFull'
        type = 'RankUserError'

class TaskInProgressUserErrorFull(UserErrorFullTaskInProgressUserError, Model):
    """No documentation"""
    typename: Literal['TaskInProgressUserError'] = Field(alias='__typename', default='TaskInProgressUserError')
    taskId: str

    class Meta:
        """Meta class for TaskInProgressUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment TaskInProgressUserErrorFull on TaskInProgressUserError {\n  ...UserErrorFull\n  taskId\n  __typename\n}'
        name = 'TaskInProgressUserErrorFull'
        type = 'TaskInProgressUserError'

class WorkflowUserErrorFull(UserErrorFullWorkflowUserError, Model):
    """No documentation"""
    typename: Literal['WorkflowUserError'] = Field(alias='__typename', default='WorkflowUserError')
    node: Optional[str] = Field(default=None)
    message: str
    reason: WorkflowErrorReason

    class Meta:
        """Meta class for WorkflowUserErrorFull"""
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}'
        name = 'WorkflowUserErrorFull'
        type = 'WorkflowUserError'

class InstanceSettingsFullAiproviders(Model):
    """No documentation"""
    typename: Literal['AIProviders'] = Field(alias='__typename', default='AIProviders')
    anthropic: Optional[InstanceAIProviderAnthropicFull] = Field(default=None)
    google: Optional[InstanceAIProviderGoogleFull] = Field(default=None)
    openai: Optional[InstanceAIProviderOpenAIFull] = Field(default=None)
    openrouter: Optional[InstanceAIProviderOpenRouterFull] = Field(default=None)

class InstanceSettingsFullAnalytic(Model):
    """No documentation"""
    typename: Literal['AnalyticStatus'] = Field(alias='__typename', default='AnalyticStatus')
    enabled: bool
    cloud: bool
    local: bool

class InstanceSettingsFullOnboarding(Model):
    """No documentation"""
    typename: Literal['OnboardingState'] = Field(alias='__typename', default='OnboardingState')
    analytic: bool

class InstanceSettingsFull(Model):
    """No documentation"""
    typename: Literal['InstanceSettings'] = Field(alias='__typename', default='InstanceSettings')
    aiProviders: InstanceSettingsFullAiproviders
    analytic: InstanceSettingsFullAnalytic
    onboarding: InstanceSettingsFullOnboarding

    class Meta:
        """Meta class for InstanceSettingsFull"""
        document = 'fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}\n\nfragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}\n\nfragment InstanceSettingsFull on InstanceSettings {\n  aiProviders {\n    anthropic {\n      ...InstanceAIProviderAnthropicFull\n      __typename\n    }\n    google {\n      ...InstanceAIProviderGoogleFull\n      __typename\n    }\n    openai {\n      ...InstanceAIProviderOpenAIFull\n      __typename\n    }\n    openrouter {\n      ...InstanceAIProviderOpenRouterFull\n      __typename\n    }\n    __typename\n  }\n  analytic {\n    enabled\n    cloud\n    local\n    __typename\n  }\n  onboarding {\n    analytic\n    __typename\n  }\n  __typename\n}'
        name = 'InstanceSettingsFull'
        type = 'InstanceSettings'

class ReplayPlaceholderFull(Model):
    """No documentation"""
    typename: Literal['ReplayPlaceholder'] = Field(alias='__typename', default='ReplayPlaceholder')
    inputRange: RangeFull
    outputRange: RangeFull
    preprocessors: List[ReplayPreprocessorFull]

    class Meta:
        """Meta class for ReplayPlaceholderFull"""
        document = 'fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}'
        name = 'ReplayPlaceholderFull'
        type = 'ReplayPlaceholder'

class RequestFullMetadata(Model):
    """No documentation"""
    typename: Literal['RequestMetadata'] = Field(alias='__typename', default='RequestMetadata')
    id: str
    color: Optional[str] = Field(default=None)

class RequestFull(Model):
    """No documentation"""
    typename: Literal['Request'] = Field(alias='__typename', default='Request')
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
        document = 'fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}'
        name = 'RequestFull'
        type = 'Request'

class ReplayTaskMetaReplayentry(Model):
    """No documentation"""
    typename: Literal['ReplayEntry'] = Field(alias='__typename', default='ReplayEntry')
    id: str

class ReplayTaskMeta(TaskMetaReplayTask, Model):
    """No documentation"""
    typename: Literal['ReplayTask'] = Field(alias='__typename', default='ReplayTask')
    replayEntry: ReplayTaskMetaReplayentry

    class Meta:
        """Meta class for ReplayTaskMeta"""
        document = 'fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}'
        name = 'ReplayTaskMeta'
        type = 'ReplayTask'

class ReplayEntryFullSession(Model):
    """No documentation"""
    typename: Literal['ReplaySession'] = Field(alias='__typename', default='ReplaySession')
    id: str

class ReplayEntryFullSettings(Model):
    """No documentation"""
    typename: Literal['ReplayEntrySettings'] = Field(alias='__typename', default='ReplayEntrySettings')
    placeholders: List[ReplayPlaceholderFull]

class ReplayEntryFull(Model):
    """No documentation"""
    typename: Literal['ReplayEntry'] = Field(alias='__typename', default='ReplayEntry')
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
        document = 'fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n  __typename\n}'
        name = 'ReplayEntryFull'
        type = 'ReplayEntry'

class Environments(Model):
    """No documentation found for this operation."""
    environments: List[EnvironmentFull]

    class Arguments(Model):
        """Arguments for Environments """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Environments """
        document = 'fragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nquery Environments {\n  environments {\n    ...EnvironmentFull\n    __typename\n  }\n}'

class EnvironmentQuery(Model):
    """No documentation found for this operation."""
    environment: Optional[EnvironmentFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for EnvironmentQuery """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for EnvironmentQuery """
        document = 'fragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nquery EnvironmentQuery($id: ID!) {\n  environment(id: $id) {\n    ...EnvironmentFull\n    __typename\n  }\n}'

class CreateEnvironmentCreateenvironmentNameTakenUserErrorInlineFragment(Model):
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class CreateEnvironmentCreateenvironmentPermissionDeniedUserErrorInlineFragment(Model):
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class CreateEnvironmentCreateenvironmentCloudUserErrorInlineFragment(Model):
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class CreateEnvironmentCreateenvironmentOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class CreateEnvironmentCreateenvironment(Model):
    """No documentation"""
    typename: Literal['CreateEnvironmentPayload'] = Field(alias='__typename', default='CreateEnvironmentPayload')
    error: Optional[Union[CreateEnvironmentCreateenvironmentNameTakenUserErrorInlineFragment, CreateEnvironmentCreateenvironmentPermissionDeniedUserErrorInlineFragment, CreateEnvironmentCreateenvironmentCloudUserErrorInlineFragment, CreateEnvironmentCreateenvironmentOtherUserErrorInlineFragment]] = Field(default=None)
    environment: Optional[EnvironmentFull] = Field(default=None)

class CreateEnvironment(Model):
    """No documentation found for this operation."""
    createEnvironment: CreateEnvironmentCreateenvironment

    class Arguments(Model):
        """Arguments for CreateEnvironment """
        input: CreateEnvironmentInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateEnvironment """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nmutation CreateEnvironment($input: CreateEnvironmentInput!) {\n  createEnvironment(input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    environment {\n      ...EnvironmentFull\n      __typename\n    }\n    __typename\n  }\n}'

class UpdateEnvironmentUpdateenvironmentUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class UpdateEnvironmentUpdateenvironmentNameTakenUserErrorInlineFragment(Model):
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class UpdateEnvironmentUpdateenvironmentNewerVersionUserErrorInlineFragment(Model):
    typename: Literal['NewerVersionUserError'] = Field(alias='__typename', default='NewerVersionUserError')

class UpdateEnvironmentUpdateenvironmentPermissionDeniedUserErrorInlineFragment(Model):
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class UpdateEnvironmentUpdateenvironmentOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class UpdateEnvironmentUpdateenvironment(Model):
    """No documentation"""
    typename: Literal['UpdateEnvironmentPayload'] = Field(alias='__typename', default='UpdateEnvironmentPayload')
    error: Optional[Union[UpdateEnvironmentUpdateenvironmentUnknownIdUserErrorInlineFragment, UpdateEnvironmentUpdateenvironmentNameTakenUserErrorInlineFragment, UpdateEnvironmentUpdateenvironmentNewerVersionUserErrorInlineFragment, UpdateEnvironmentUpdateenvironmentPermissionDeniedUserErrorInlineFragment, UpdateEnvironmentUpdateenvironmentOtherUserErrorInlineFragment]] = Field(default=None)
    environment: Optional[EnvironmentFull] = Field(default=None)

class UpdateEnvironment(Model):
    """No documentation found for this operation."""
    updateEnvironment: UpdateEnvironmentUpdateenvironment

    class Arguments(Model):
        """Arguments for UpdateEnvironment """
        id: str
        input: UpdateEnvironmentInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateEnvironment """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment EnvironmentFull on Environment {\n  id\n  name\n  variables {\n    name\n    value\n    kind\n    __typename\n  }\n  version\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment NewerVersionUserErrorFull on NewerVersionUserError {\n  ...UserErrorFull\n  version\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation UpdateEnvironment($id: ID!, $input: UpdateEnvironmentInput!) {\n  updateEnvironment(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on NewerVersionUserError {\n        ...NewerVersionUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    environment {\n      ...EnvironmentFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteEnvironmentDeleteenvironmentUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class DeleteEnvironmentDeleteenvironmentOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class DeleteEnvironmentDeleteenvironment(Model):
    """No documentation"""
    typename: Literal['DeleteEnvironmentPayload'] = Field(alias='__typename', default='DeleteEnvironmentPayload')
    deletedId: Optional[str] = Field(default=None)
    error: Optional[Union[DeleteEnvironmentDeleteenvironmentUnknownIdUserErrorInlineFragment, DeleteEnvironmentDeleteenvironmentOtherUserErrorInlineFragment]] = Field(default=None)

class DeleteEnvironment(Model):
    """No documentation found for this operation."""
    deleteEnvironment: DeleteEnvironmentDeleteenvironment

    class Arguments(Model):
        """Arguments for DeleteEnvironment """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteEnvironment """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation DeleteEnvironment($id: ID!) {\n  deleteEnvironment(id: $id) {\n    deletedId\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}'

class SelectEnvironmentSelectenvironmentUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class SelectEnvironmentSelectenvironmentOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class SelectEnvironmentSelectenvironmentEnvironmentVariables(Model):
    """No documentation"""
    typename: Literal['EnvironmentVariable'] = Field(alias='__typename', default='EnvironmentVariable')
    name: str
    value: str
    kind: EnvironmentVariableKind

class SelectEnvironmentSelectenvironmentEnvironment(Model):
    """No documentation"""
    typename: Literal['Environment'] = Field(alias='__typename', default='Environment')
    id: str
    name: str
    variables: List[SelectEnvironmentSelectenvironmentEnvironmentVariables]
    version: int

class SelectEnvironmentSelectenvironment(Model):
    """No documentation"""
    typename: Literal['SelectEnvironmentPayload'] = Field(alias='__typename', default='SelectEnvironmentPayload')
    error: Optional[Union[SelectEnvironmentSelectenvironmentUnknownIdUserErrorInlineFragment, SelectEnvironmentSelectenvironmentOtherUserErrorInlineFragment]] = Field(default=None)
    environment: Optional[SelectEnvironmentSelectenvironmentEnvironment] = Field(default=None)

class SelectEnvironment(Model):
    """No documentation found for this operation."""
    selectEnvironment: SelectEnvironmentSelectenvironment

    class Arguments(Model):
        """Arguments for SelectEnvironment """
        id: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SelectEnvironment """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation SelectEnvironment($id: ID) {\n  selectEnvironment(id: $id) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    environment {\n      id\n      name\n      variables {\n        name\n        value\n        kind\n        __typename\n      }\n      version\n      __typename\n    }\n    __typename\n  }\n}'

class FilterPresets(Model):
    """No documentation found for this operation."""
    filterPresets: List[FilterPresetFull]

    class Arguments(Model):
        """Arguments for FilterPresets """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for FilterPresets """
        document = 'fragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause\n  __typename\n}\n\nquery FilterPresets {\n  filterPresets {\n    ...FilterPresetFull\n    __typename\n  }\n}'

class FilterPreset(Model):
    """No documentation found for this operation."""
    filterPreset: Optional[FilterPresetFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for FilterPreset """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for FilterPreset """
        document = 'fragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause\n  __typename\n}\n\nquery FilterPreset($id: ID!) {\n  filterPreset(id: $id) {\n    ...FilterPresetFull\n    __typename\n  }\n}'

class CreateFilterPresetCreatefilterpresetNameTakenUserErrorInlineFragment(Model):
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class CreateFilterPresetCreatefilterpresetAliasTakenUserErrorInlineFragment(Model):
    typename: Literal['AliasTakenUserError'] = Field(alias='__typename', default='AliasTakenUserError')

class CreateFilterPresetCreatefilterpresetPermissionDeniedUserErrorInlineFragment(Model):
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class CreateFilterPresetCreatefilterpresetCloudUserErrorInlineFragment(Model):
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class CreateFilterPresetCreatefilterpresetOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class CreateFilterPresetCreatefilterpreset(Model):
    """No documentation"""
    typename: Literal['CreateFilterPresetPayload'] = Field(alias='__typename', default='CreateFilterPresetPayload')
    error: Optional[Union[CreateFilterPresetCreatefilterpresetNameTakenUserErrorInlineFragment, CreateFilterPresetCreatefilterpresetAliasTakenUserErrorInlineFragment, CreateFilterPresetCreatefilterpresetPermissionDeniedUserErrorInlineFragment, CreateFilterPresetCreatefilterpresetCloudUserErrorInlineFragment, CreateFilterPresetCreatefilterpresetOtherUserErrorInlineFragment]] = Field(default=None)
    filter: Optional[FilterPresetFull] = Field(default=None)

class CreateFilterPreset(Model):
    """No documentation found for this operation."""
    createFilterPreset: CreateFilterPresetCreatefilterpreset

    class Arguments(Model):
        """Arguments for CreateFilterPreset """
        input: CreateFilterPresetInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateFilterPreset """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment AliasTakenUserErrorFull on AliasTakenUserError {\n  ...UserErrorFull\n  alias\n  __typename\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nmutation CreateFilterPreset($input: CreateFilterPresetInput!) {\n  createFilterPreset(input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on AliasTakenUserError {\n        ...AliasTakenUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    filter {\n      ...FilterPresetFull\n      __typename\n    }\n    __typename\n  }\n}'

class UpdateFilterPresetUpdatefilterpresetNameTakenUserErrorInlineFragment(Model):
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class UpdateFilterPresetUpdatefilterpresetAliasTakenUserErrorInlineFragment(Model):
    typename: Literal['AliasTakenUserError'] = Field(alias='__typename', default='AliasTakenUserError')

class UpdateFilterPresetUpdatefilterpresetOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class UpdateFilterPresetUpdatefilterpreset(Model):
    """No documentation"""
    typename: Literal['UpdateFilterPresetPayload'] = Field(alias='__typename', default='UpdateFilterPresetPayload')
    error: Optional[Union[UpdateFilterPresetUpdatefilterpresetNameTakenUserErrorInlineFragment, UpdateFilterPresetUpdatefilterpresetAliasTakenUserErrorInlineFragment, UpdateFilterPresetUpdatefilterpresetOtherUserErrorInlineFragment]] = Field(default=None)
    filter: Optional[FilterPresetFull] = Field(default=None)

class UpdateFilterPreset(Model):
    """No documentation found for this operation."""
    updateFilterPreset: UpdateFilterPresetUpdatefilterpreset

    class Arguments(Model):
        """Arguments for UpdateFilterPreset """
        id: str
        input: UpdateFilterPresetInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateFilterPreset """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment AliasTakenUserErrorFull on AliasTakenUserError {\n  ...UserErrorFull\n  alias\n  __typename\n}\n\nfragment FilterPresetFull on FilterPreset {\n  id\n  name\n  alias\n  clause\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nmutation UpdateFilterPreset($id: ID!, $input: UpdateFilterPresetInput!) {\n  updateFilterPreset(id: $id, input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on AliasTakenUserError {\n        ...AliasTakenUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    filter {\n      ...FilterPresetFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteFilterPresetDeletefilterpreset(Model):
    """No documentation"""
    typename: Literal['DeleteFilterPresetPayload'] = Field(alias='__typename', default='DeleteFilterPresetPayload')
    deletedId: Optional[str] = Field(default=None)

class DeleteFilterPreset(Model):
    """No documentation found for this operation."""
    deleteFilterPreset: DeleteFilterPresetDeletefilterpreset

    class Arguments(Model):
        """Arguments for DeleteFilterPreset """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteFilterPreset """
        document = 'mutation DeleteFilterPreset($id: ID!) {\n  deleteFilterPreset(id: $id) {\n    deletedId\n    __typename\n  }\n}'

class Finding(Model):
    """No documentation found for this operation."""
    finding: Optional[FindingFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Finding """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Finding """
        document = 'fragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nquery Finding($id: ID!) {\n  finding(id: $id) {\n    ...FindingFull\n    __typename\n  }\n}'

class FindingsFindingsEdges(Model):
    """An edge in a connection."""
    typename: Literal['FindingEdge'] = Field(alias='__typename', default='FindingEdge')
    cursor: str
    'A cursor for use in pagination'
    node: FindingFull
    'The item at the end of the edge'

class FindingsFindingsPageinfo(Model):
    """Information about pagination in a connection"""
    typename: Literal['PageInfo'] = Field(alias='__typename', default='PageInfo')
    hasNextPage: bool
    'When paginating forwards, are there more items?'
    hasPreviousPage: bool
    'When paginating backwards, are there more items?'
    startCursor: Optional[str] = Field(default=None)
    'When paginating backwards, the cursor to continue.'
    endCursor: Optional[str] = Field(default=None)
    'When paginating forwards, the cursor to continue.'

class FindingsFindings(Model):
    """No documentation"""
    typename: Literal['FindingConnection'] = Field(alias='__typename', default='FindingConnection')
    edges: List[FindingsFindingsEdges]
    'A list of edges.'
    pageInfo: FindingsFindingsPageinfo
    'Information to aid in pagination.'

class Findings(Model):
    """No documentation found for this operation."""
    findings: FindingsFindings

    class Arguments(Model):
        """Arguments for Findings """
        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        filter: Optional[FilterClauseFindingInput] = Field(default=None)
        order: Optional[FindingOrderInput] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Findings """
        document = 'fragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nquery Findings($first: Int, $after: String, $last: Int, $before: String, $filter: FilterClauseFindingInput, $order: FindingOrderInput) {\n  findings(\n    first: $first\n    after: $after\n    last: $last\n    before: $before\n    filter: $filter\n    order: $order\n  ) {\n    edges {\n      cursor\n      node {\n        ...FindingFull\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}'

class CreateFindingCreatefindingOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class CreateFindingCreatefindingUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class CreateFindingCreatefinding(Model):
    """No documentation"""
    typename: Literal['CreateFindingPayload'] = Field(alias='__typename', default='CreateFindingPayload')
    error: Optional[Union[CreateFindingCreatefindingOtherUserErrorInlineFragment, CreateFindingCreatefindingUnknownIdUserErrorInlineFragment]] = Field(default=None)
    finding: Optional[FindingFull] = Field(default=None)

class CreateFinding(Model):
    """No documentation found for this operation."""
    createFinding: CreateFindingCreatefinding

    class Arguments(Model):
        """Arguments for CreateFinding """
        requestId: str
        input: CreateFindingInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateFinding """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation CreateFinding($requestId: ID!, $input: CreateFindingInput!) {\n  createFinding(requestId: $requestId, input: $input) {\n    error {\n      __typename\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n    }\n    finding {\n      ...FindingFull\n      __typename\n    }\n    __typename\n  }\n}'

class UpdateFindingUpdatefindingUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class UpdateFindingUpdatefindingOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class UpdateFindingUpdatefinding(Model):
    """No documentation"""
    typename: Literal['UpdateFindingPayload'] = Field(alias='__typename', default='UpdateFindingPayload')
    error: Optional[Union[UpdateFindingUpdatefindingUnknownIdUserErrorInlineFragment, UpdateFindingUpdatefindingOtherUserErrorInlineFragment]] = Field(default=None)
    finding: Optional[FindingFull] = Field(default=None)

class UpdateFinding(Model):
    """No documentation found for this operation."""
    updateFinding: UpdateFindingUpdatefinding

    class Arguments(Model):
        """Arguments for UpdateFinding """
        id: str
        input: UpdateFindingInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateFinding """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment FindingFull on Finding {\n  id\n  request {\n    id\n    __typename\n  }\n  title\n  reporter\n  description\n  dedupeKey\n  host\n  path\n  hidden\n  createdAt\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation UpdateFinding($id: ID!, $input: UpdateFindingInput!) {\n  updateFinding(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    finding {\n      ...FindingFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteFindingsDeletefindings(Model):
    """No documentation"""
    typename: Literal['DeleteFindingsPayload'] = Field(alias='__typename', default='DeleteFindingsPayload')
    deletedIds: Optional[List[str]] = Field(default=None)

class DeleteFindings(Model):
    """No documentation found for this operation."""
    deleteFindings: DeleteFindingsDeletefindings

    class Arguments(Model):
        """Arguments for DeleteFindings """
        input: Optional[DeleteFindingsInput] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteFindings """
        document = 'mutation DeleteFindings($input: DeleteFindingsInput) {\n  deleteFindings(input: $input) {\n    deletedIds\n    __typename\n  }\n}'

class HostedFiles(Model):
    """No documentation found for this operation."""
    hostedFiles: List[HostedFileFull]

    class Arguments(Model):
        """Arguments for HostedFiles """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for HostedFiles """
        document = 'fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}\n\nquery HostedFiles {\n  hostedFiles {\n    ...HostedFileFull\n    __typename\n  }\n}'

class UploadHostedFileUploadhostedfile(Model):
    """No documentation"""
    typename: Literal['UploadHostedFilePayload'] = Field(alias='__typename', default='UploadHostedFilePayload')
    hostedFile: Optional[HostedFileFull] = Field(default=None)

class UploadHostedFile(Model):
    """No documentation found for this operation."""
    uploadHostedFile: UploadHostedFileUploadhostedfile

    class Arguments(Model):
        """Arguments for UploadHostedFile """
        input: UploadHostedFileInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UploadHostedFile """
        document = 'fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}\n\nmutation UploadHostedFile($input: UploadHostedFileInput!) {\n  uploadHostedFile(input: $input) {\n    hostedFile {\n      ...HostedFileFull\n      __typename\n    }\n    __typename\n  }\n}'

class RenameHostedFileRenamehostedfile(Model):
    """No documentation"""
    typename: Literal['RenameHostedFilePayload'] = Field(alias='__typename', default='RenameHostedFilePayload')
    hostedFile: Optional[HostedFileFull] = Field(default=None)

class RenameHostedFile(Model):
    """No documentation found for this operation."""
    renameHostedFile: RenameHostedFileRenamehostedfile

    class Arguments(Model):
        """Arguments for RenameHostedFile """
        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameHostedFile """
        document = 'fragment HostedFileFull on HostedFile {\n  id\n  name\n  path\n  size\n  status\n  createdAt\n  updatedAt\n  __typename\n}\n\nmutation RenameHostedFile($id: ID!, $name: String!) {\n  renameHostedFile(id: $id, name: $name) {\n    hostedFile {\n      ...HostedFileFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteHostedFileDeletehostedfile(Model):
    """No documentation"""
    typename: Literal['DeleteHostedFilePayload'] = Field(alias='__typename', default='DeleteHostedFilePayload')
    deletedId: Optional[str] = Field(default=None)

class DeleteHostedFile(Model):
    """No documentation found for this operation."""
    deleteHostedFile: DeleteHostedFileDeletehostedfile

    class Arguments(Model):
        """Arguments for DeleteHostedFile """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteHostedFile """
        document = 'mutation DeleteHostedFile($id: ID!) {\n  deleteHostedFile(id: $id) {\n    deletedId\n    __typename\n  }\n}'

class InstanceSettings(Model):
    """No documentation found for this operation."""
    instanceSettings: InstanceSettingsFull

    class Arguments(Model):
        """Arguments for InstanceSettings """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for InstanceSettings """
        document = 'fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}\n\nfragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}\n\nfragment InstanceSettingsFull on InstanceSettings {\n  aiProviders {\n    anthropic {\n      ...InstanceAIProviderAnthropicFull\n      __typename\n    }\n    google {\n      ...InstanceAIProviderGoogleFull\n      __typename\n    }\n    openai {\n      ...InstanceAIProviderOpenAIFull\n      __typename\n    }\n    openrouter {\n      ...InstanceAIProviderOpenRouterFull\n      __typename\n    }\n    __typename\n  }\n  analytic {\n    enabled\n    cloud\n    local\n    __typename\n  }\n  onboarding {\n    analytic\n    __typename\n  }\n  __typename\n}\n\nquery InstanceSettings {\n  instanceSettings {\n    ...InstanceSettingsFull\n    __typename\n  }\n}'

class SetInstanceSettingsSetinstancesettings(Model):
    """No documentation"""
    typename: Literal['SetInstanceSettingsPayload'] = Field(alias='__typename', default='SetInstanceSettingsPayload')
    settings: InstanceSettingsFull

class SetInstanceSettings(Model):
    """No documentation found for this operation."""
    setInstanceSettings: SetInstanceSettingsSetinstancesettings

    class Arguments(Model):
        """Arguments for SetInstanceSettings """
        input: SetInstanceSettingsInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SetInstanceSettings """
        document = 'fragment InstanceAIProviderAnthropicFull on AIProviderAnthropic {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderGoogleFull on AIProviderGoogle {\n  apiKey\n  __typename\n}\n\nfragment InstanceAIProviderOpenAIFull on AIProviderOpenAI {\n  apiKey\n  url\n  __typename\n}\n\nfragment InstanceAIProviderOpenRouterFull on AIProviderOpenRouter {\n  apiKey\n  __typename\n}\n\nfragment InstanceSettingsFull on InstanceSettings {\n  aiProviders {\n    anthropic {\n      ...InstanceAIProviderAnthropicFull\n      __typename\n    }\n    google {\n      ...InstanceAIProviderGoogleFull\n      __typename\n    }\n    openai {\n      ...InstanceAIProviderOpenAIFull\n      __typename\n    }\n    openrouter {\n      ...InstanceAIProviderOpenRouterFull\n      __typename\n    }\n    __typename\n  }\n  analytic {\n    enabled\n    cloud\n    local\n    __typename\n  }\n  onboarding {\n    analytic\n    __typename\n  }\n  __typename\n}\n\nmutation SetInstanceSettings($input: SetInstanceSettingsInput!) {\n  setInstanceSettings(input: $input) {\n    settings {\n      ...InstanceSettingsFull\n      __typename\n    }\n    __typename\n  }\n}'

class PluginPackages(Model):
    """No documentation found for this operation."""
    pluginPackages: List[PluginPackageMeta]

    class Arguments(Model):
        """Arguments for PluginPackages """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for PluginPackages """
        document = 'fragment PluginPackageMeta on PluginPackage {\n  id\n  manifestId\n  plugins {\n    __typename\n    id\n    manifestId\n    enabled\n  }\n  __typename\n}\n\nquery PluginPackages {\n  pluginPackages {\n    ...PluginPackageMeta\n    __typename\n  }\n}'

class InstallPluginPackageInstallpluginpackagePluginUserErrorInlineFragment(Model):
    typename: Literal['PluginUserError'] = Field(alias='__typename', default='PluginUserError')

class InstallPluginPackageInstallpluginpackageStoreUserErrorInlineFragment(Model):
    typename: Literal['StoreUserError'] = Field(alias='__typename', default='StoreUserError')

class InstallPluginPackageInstallpluginpackageCloudUserErrorInlineFragment(Model):
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class InstallPluginPackageInstallpluginpackageOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class InstallPluginPackageInstallpluginpackage(Model):
    """No documentation"""
    typename: Literal['InstallPluginPackagePayload'] = Field(alias='__typename', default='InstallPluginPackagePayload')
    package: Optional[PluginPackageMeta] = Field(default=None)
    error: Optional[Union[InstallPluginPackageInstallpluginpackagePluginUserErrorInlineFragment, InstallPluginPackageInstallpluginpackageStoreUserErrorInlineFragment, InstallPluginPackageInstallpluginpackageCloudUserErrorInlineFragment, InstallPluginPackageInstallpluginpackageOtherUserErrorInlineFragment]] = Field(default=None)

class InstallPluginPackage(Model):
    """No documentation found for this operation."""
    installPluginPackage: InstallPluginPackageInstallpluginpackage

    class Arguments(Model):
        """Arguments for InstallPluginPackage """
        input: InstallPluginPackageInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for InstallPluginPackage """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PluginPackageMeta on PluginPackage {\n  id\n  manifestId\n  plugins {\n    __typename\n    id\n    manifestId\n    enabled\n  }\n  __typename\n}\n\nfragment PluginUserErrorFull on PluginUserError {\n  ...UserErrorFull\n  reason\n  __typename\n}\n\nfragment StoreUserErrorFull on StoreUserError {\n  ...UserErrorFull\n  storeReason: reason\n  __typename\n}\n\nmutation InstallPluginPackage($input: InstallPluginPackageInput!) {\n  installPluginPackage(input: $input) {\n    package {\n      ...PluginPackageMeta\n      __typename\n    }\n    error {\n      __typename\n      ... on PluginUserError {\n        ...PluginUserErrorFull\n      }\n      ... on StoreUserError {\n        ...StoreUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}'

class Projects(Model):
    """No documentation found for this operation."""
    projects: List[ProjectFull]

    class Arguments(Model):
        """Arguments for Projects """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Projects """
        document = 'fragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nquery Projects {\n  projects {\n    ...ProjectFull\n    __typename\n  }\n}'

class CreateProjectCreateprojectNameTakenUserErrorInlineFragment(Model):
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class CreateProjectCreateprojectPermissionDeniedUserErrorInlineFragment(Model):
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class CreateProjectCreateprojectCloudUserErrorInlineFragment(Model):
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class CreateProjectCreateprojectOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class CreateProjectCreateproject(Model):
    """No documentation"""
    typename: Literal['CreateProjectPayload'] = Field(alias='__typename', default='CreateProjectPayload')
    error: Optional[Union[CreateProjectCreateprojectNameTakenUserErrorInlineFragment, CreateProjectCreateprojectPermissionDeniedUserErrorInlineFragment, CreateProjectCreateprojectCloudUserErrorInlineFragment, CreateProjectCreateprojectOtherUserErrorInlineFragment]] = Field(default=None)
    project: Optional[ProjectFull] = Field(default=None)

class CreateProject(Model):
    """No documentation found for this operation."""
    createProject: CreateProjectCreateproject

    class Arguments(Model):
        """Arguments for CreateProject """
        input: CreateProjectInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateProject """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment NameTakenUserErrorFull on NameTakenUserError {\n  ...UserErrorFull\n  name\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nmutation CreateProject($input: CreateProjectInput!) {\n  createProject(input: $input) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        ...NameTakenUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    project {\n      ...ProjectFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteProjectDeleteprojectProjectUserErrorInlineFragment(Model):
    typename: Literal['ProjectUserError'] = Field(alias='__typename', default='ProjectUserError')

class DeleteProjectDeleteprojectUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class DeleteProjectDeleteprojectOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class DeleteProjectDeleteproject(Model):
    """No documentation"""
    typename: Literal['DeleteProjectPayload'] = Field(alias='__typename', default='DeleteProjectPayload')
    deletedId: Optional[str] = Field(default=None)
    error: Optional[Union[DeleteProjectDeleteprojectProjectUserErrorInlineFragment, DeleteProjectDeleteprojectUnknownIdUserErrorInlineFragment, DeleteProjectDeleteprojectOtherUserErrorInlineFragment]] = Field(default=None)

class DeleteProject(Model):
    """No documentation found for this operation."""
    deleteProject: DeleteProjectDeleteproject

    class Arguments(Model):
        """Arguments for DeleteProject """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteProject """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ProjectUserErrorFull on ProjectUserError {\n  ...UserErrorFull\n  projectReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation DeleteProject($id: ID!) {\n  deleteProject(id: $id) {\n    deletedId\n    error {\n      __typename\n      ... on ProjectUserError {\n        ...ProjectUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}'

class RenameProjectRenameprojectNameTakenUserErrorInlineFragment(Model):
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')
    code: str
    name: str

class RenameProjectRenameprojectUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')
    code: str
    id: str

class RenameProjectRenameprojectOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')
    code: str

class RenameProjectRenameproject(Model):
    """No documentation"""
    typename: Literal['RenameProjectPayload'] = Field(alias='__typename', default='RenameProjectPayload')
    error: Optional[Union[RenameProjectRenameprojectNameTakenUserErrorInlineFragment, RenameProjectRenameprojectUnknownIdUserErrorInlineFragment, RenameProjectRenameprojectOtherUserErrorInlineFragment]] = Field(default=None)
    project: Optional[ProjectFull] = Field(default=None)

class RenameProject(Model):
    """No documentation found for this operation."""
    renameProject: RenameProjectRenameproject

    class Arguments(Model):
        """Arguments for RenameProject """
        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameProject """
        document = 'fragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nmutation RenameProject($id: ID!, $name: String!) {\n  renameProject(id: $id, name: $name) {\n    error {\n      __typename\n      ... on NameTakenUserError {\n        code\n        name\n      }\n      ... on UnknownIdUserError {\n        code\n        id\n      }\n      ... on OtherUserError {\n        code\n      }\n    }\n    project {\n      ...ProjectFull\n      __typename\n    }\n    __typename\n  }\n}'

class SelectProjectSelectprojectCurrentproject(Model):
    """No documentation"""
    typename: Literal['CurrentProject'] = Field(alias='__typename', default='CurrentProject')
    project: ProjectFull

class SelectProjectSelectprojectProjectUserErrorInlineFragment(Model):
    typename: Literal['ProjectUserError'] = Field(alias='__typename', default='ProjectUserError')

class SelectProjectSelectprojectUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class SelectProjectSelectprojectOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class SelectProjectSelectproject(Model):
    """No documentation"""
    typename: Literal['SelectProjectPayload'] = Field(alias='__typename', default='SelectProjectPayload')
    currentProject: Optional[SelectProjectSelectprojectCurrentproject] = Field(default=None)
    error: Optional[Union[SelectProjectSelectprojectProjectUserErrorInlineFragment, SelectProjectSelectprojectUnknownIdUserErrorInlineFragment, SelectProjectSelectprojectOtherUserErrorInlineFragment]] = Field(default=None)

class SelectProject(Model):
    """No documentation found for this operation."""
    selectProject: SelectProjectSelectproject

    class Arguments(Model):
        """Arguments for SelectProject """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SelectProject """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ProjectFull on Project {\n  id\n  name\n  path\n  status\n  temporary\n  createdAt\n  updatedAt\n  version\n  size\n  readOnly\n  __typename\n}\n\nfragment ProjectUserErrorFull on ProjectUserError {\n  ...UserErrorFull\n  projectReason: reason\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation SelectProject($id: ID!) {\n  selectProject(id: $id) {\n    currentProject {\n      project {\n        ...ProjectFull\n        __typename\n      }\n      __typename\n    }\n    error {\n      __typename\n      ... on ProjectUserError {\n        ...ProjectUserErrorFull\n      }\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}'

class ReplayEntry(Model):
    """No documentation found for this operation."""
    replayEntry: Optional[ReplayEntryFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplayEntry """
        id: str
        includeReplayRaw: bool
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplayEntry """
        document = 'fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery ReplayEntry($id: ID!, $includeReplayRaw: Boolean!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  replayEntry(id: $id) {\n    ...ReplayEntryFull\n    __typename\n  }\n}'

class ReplaySessionsReplaysessionsEdges(Model):
    """An edge in a connection."""
    typename: Literal['ReplaySessionEdge'] = Field(alias='__typename', default='ReplaySessionEdge')
    cursor: str
    'A cursor for use in pagination'
    node: ReplaySessionMeta
    'The item at the end of the edge'

class ReplaySessionsReplaysessionsPageinfo(Model):
    """Information about pagination in a connection"""
    typename: Literal['PageInfo'] = Field(alias='__typename', default='PageInfo')
    hasNextPage: bool
    'When paginating forwards, are there more items?'
    hasPreviousPage: bool
    'When paginating backwards, are there more items?'
    startCursor: Optional[str] = Field(default=None)
    'When paginating backwards, the cursor to continue.'
    endCursor: Optional[str] = Field(default=None)
    'When paginating forwards, the cursor to continue.'

class ReplaySessionsReplaysessions(Model):
    """No documentation"""
    typename: Literal['ReplaySessionConnection'] = Field(alias='__typename', default='ReplaySessionConnection')
    edges: List[ReplaySessionsReplaysessionsEdges]
    'A list of edges.'
    pageInfo: ReplaySessionsReplaysessionsPageinfo
    'Information to aid in pagination.'

class ReplaySessions(Model):
    """No documentation found for this operation."""
    replaySessions: ReplaySessionsReplaysessions

    class Arguments(Model):
        """Arguments for ReplaySessions """
        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySessions """
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nquery ReplaySessions($first: Int, $after: String, $last: Int, $before: String) {\n  replaySessions(first: $first, after: $after, last: $last, before: $before) {\n    edges {\n      cursor\n      node {\n        ...ReplaySessionMeta\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}'

class ReplaySessionEntriesReplaysessionEntriesEdges(Model):
    """An edge in a connection."""
    typename: Literal['ReplayEntryEdge'] = Field(alias='__typename', default='ReplayEntryEdge')
    cursor: str
    'A cursor for use in pagination'
    node: ReplayEntryFull
    'The item at the end of the edge'

class ReplaySessionEntriesReplaysessionEntriesPageinfo(Model):
    """Information about pagination in a connection"""
    typename: Literal['PageInfo'] = Field(alias='__typename', default='PageInfo')
    hasNextPage: bool
    'When paginating forwards, are there more items?'
    hasPreviousPage: bool
    'When paginating backwards, are there more items?'
    startCursor: Optional[str] = Field(default=None)
    'When paginating backwards, the cursor to continue.'
    endCursor: Optional[str] = Field(default=None)
    'When paginating forwards, the cursor to continue.'

class ReplaySessionEntriesReplaysessionEntries(Model):
    """No documentation"""
    typename: Literal['ReplayEntryConnection'] = Field(alias='__typename', default='ReplayEntryConnection')
    edges: List[ReplaySessionEntriesReplaysessionEntriesEdges]
    'A list of edges.'
    pageInfo: ReplaySessionEntriesReplaysessionEntriesPageinfo
    'Information to aid in pagination.'

class ReplaySessionEntriesReplaysession(Model):
    """No documentation"""
    typename: Literal['ReplaySession'] = Field(alias='__typename', default='ReplaySession')
    entries: ReplaySessionEntriesReplaysessionEntries

class ReplaySessionEntries(Model):
    """No documentation found for this operation."""
    replaySession: Optional[ReplaySessionEntriesReplaysession] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplaySessionEntries """
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
        """Meta class for ReplaySessionEntries """
        document = 'fragment ReplayEnvironmentPreprocessorFull on ReplayEnvironmentPreprocessor {\n  __typename\n  variableName\n}\n\nfragment ReplayPrefixPreprocessorFull on ReplayPrefixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplaySuffixPreprocessorFull on ReplaySuffixPreprocessor {\n  __typename\n  value\n}\n\nfragment ReplayUrlEncodePreprocessorFull on ReplayUrlEncodePreprocessor {\n  __typename\n  charset\n  nonAscii\n}\n\nfragment ReplayWorkflowPreprocessorFull on ReplayWorkflowPreprocessor {\n  __typename\n  id\n}\n\nfragment RangeFull on Range {\n  start\n  end\n  __typename\n}\n\nfragment ReplayPreprocessorFull on ReplayPreprocessor {\n  __typename\n  options {\n    ... on ReplayPrefixPreprocessor {\n      ...ReplayPrefixPreprocessorFull\n    }\n    ... on ReplaySuffixPreprocessor {\n      ...ReplaySuffixPreprocessorFull\n    }\n    ... on ReplayUrlEncodePreprocessor {\n      ...ReplayUrlEncodePreprocessorFull\n    }\n    ... on ReplayWorkflowPreprocessor {\n      ...ReplayWorkflowPreprocessorFull\n    }\n    ... on ReplayEnvironmentPreprocessor {\n      ...ReplayEnvironmentPreprocessorFull\n    }\n    __typename\n  }\n}\n\nfragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment ConnectionInfoFull on ConnectionInfo {\n  __typename\n  host\n  port\n  isTLS\n  SNI\n}\n\nfragment ReplayPlaceholderFull on ReplayPlaceholder {\n  __typename\n  inputRange {\n    ...RangeFull\n    __typename\n  }\n  outputRange {\n    ...RangeFull\n    __typename\n  }\n  preprocessors {\n    ...ReplayPreprocessorFull\n    __typename\n  }\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nfragment ReplayEntryFull on ReplayEntry {\n  connection {\n    ...ConnectionInfoFull\n    __typename\n  }\n  createdAt\n  error\n  id\n  raw @include(if: $includeReplayRaw)\n  request {\n    ...RequestFull\n    __typename\n  }\n  session {\n    id\n    __typename\n  }\n  settings {\n    placeholders {\n      ...ReplayPlaceholderFull\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery ReplaySessionEntries($id: ID!, $after: String, $before: String, $first: Int, $last: Int, $includeReplayRaw: Boolean!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  replaySession(id: $id) {\n    entries(after: $after, before: $before, first: $first, last: $last) {\n      edges {\n        cursor\n        node {\n          ...ReplayEntryFull\n          __typename\n        }\n        __typename\n      }\n      pageInfo {\n        hasNextPage\n        hasPreviousPage\n        startCursor\n        endCursor\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}'

class ReplaySession(Model):
    """No documentation found for this operation."""
    replaySession: Optional[ReplaySessionMeta] = Field(default=None)

    class Arguments(Model):
        """Arguments for ReplaySession """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySession """
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nquery ReplaySession($id: ID!) {\n  replaySession(id: $id) {\n    ...ReplaySessionMeta\n    __typename\n  }\n}'

class ReplaySessionCollectionsReplaysessioncollectionsEdges(Model):
    """An edge in a connection."""
    typename: Literal['ReplaySessionCollectionEdge'] = Field(alias='__typename', default='ReplaySessionCollectionEdge')
    cursor: str
    'A cursor for use in pagination'
    node: ReplaySessionCollectionMeta
    'The item at the end of the edge'

class ReplaySessionCollectionsReplaysessioncollectionsPageinfo(Model):
    """Information about pagination in a connection"""
    typename: Literal['PageInfo'] = Field(alias='__typename', default='PageInfo')
    hasNextPage: bool
    'When paginating forwards, are there more items?'
    hasPreviousPage: bool
    'When paginating backwards, are there more items?'
    startCursor: Optional[str] = Field(default=None)
    'When paginating backwards, the cursor to continue.'
    endCursor: Optional[str] = Field(default=None)
    'When paginating forwards, the cursor to continue.'

class ReplaySessionCollectionsReplaysessioncollections(Model):
    """No documentation"""
    typename: Literal['ReplaySessionCollectionConnection'] = Field(alias='__typename', default='ReplaySessionCollectionConnection')
    edges: List[ReplaySessionCollectionsReplaysessioncollectionsEdges]
    'A list of edges.'
    pageInfo: ReplaySessionCollectionsReplaysessioncollectionsPageinfo
    'Information to aid in pagination.'

class ReplaySessionCollections(Model):
    """No documentation found for this operation."""
    replaySessionCollections: ReplaySessionCollectionsReplaysessioncollections

    class Arguments(Model):
        """Arguments for ReplaySessionCollections """
        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for ReplaySessionCollections """
        document = 'fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}\n\nquery ReplaySessionCollections($first: Int, $after: String, $last: Int, $before: String) {\n  replaySessionCollections(\n    first: $first\n    after: $after\n    last: $last\n    before: $before\n  ) {\n    edges {\n      cursor\n      node {\n        ...ReplaySessionCollectionMeta\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}'

class CreateReplaySessionCreatereplaysession(Model):
    """No documentation"""
    typename: Literal['CreateReplaySessionPayload'] = Field(alias='__typename', default='CreateReplaySessionPayload')
    session: Optional[ReplaySessionMeta] = Field(default=None)

class CreateReplaySession(Model):
    """No documentation found for this operation."""
    createReplaySession: CreateReplaySessionCreatereplaysession

    class Arguments(Model):
        """Arguments for CreateReplaySession """
        input: CreateReplaySessionInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateReplaySession """
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation CreateReplaySession($input: CreateReplaySessionInput!) {\n  createReplaySession(input: $input) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}'

class CreateReplaySessionCollectionCreatereplaysessioncollection(Model):
    """No documentation"""
    typename: Literal['CreateReplaySessionCollectionPayload'] = Field(alias='__typename', default='CreateReplaySessionCollectionPayload')
    collection: Optional[ReplaySessionCollectionMeta] = Field(default=None)

class CreateReplaySessionCollection(Model):
    """No documentation found for this operation."""
    createReplaySessionCollection: CreateReplaySessionCollectionCreatereplaysessioncollection

    class Arguments(Model):
        """Arguments for CreateReplaySessionCollection """
        input: CreateReplaySessionCollectionInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateReplaySessionCollection """
        document = 'fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}\n\nmutation CreateReplaySessionCollection($input: CreateReplaySessionCollectionInput!) {\n  createReplaySessionCollection(input: $input) {\n    collection {\n      ...ReplaySessionCollectionMeta\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteReplaySessionsDeletereplaysessions(Model):
    """No documentation"""
    typename: Literal['DeleteReplaySessionsPayload'] = Field(alias='__typename', default='DeleteReplaySessionsPayload')
    deletedIds: Optional[List[str]] = Field(default=None)

class DeleteReplaySessions(Model):
    """No documentation found for this operation."""
    deleteReplaySessions: DeleteReplaySessionsDeletereplaysessions

    class Arguments(Model):
        """Arguments for DeleteReplaySessions """
        ids: List[str]
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteReplaySessions """
        document = 'mutation DeleteReplaySessions($ids: [ID!]!) {\n  deleteReplaySessions(ids: $ids) {\n    deletedIds\n    __typename\n  }\n}'

class DeleteReplaySessionCollectionDeletereplaysessioncollection(Model):
    """No documentation"""
    typename: Literal['DeleteReplaySessionCollectionPayload'] = Field(alias='__typename', default='DeleteReplaySessionCollectionPayload')
    deletedId: Optional[str] = Field(default=None)

class DeleteReplaySessionCollection(Model):
    """No documentation found for this operation."""
    deleteReplaySessionCollection: DeleteReplaySessionCollectionDeletereplaysessioncollection

    class Arguments(Model):
        """Arguments for DeleteReplaySessionCollection """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteReplaySessionCollection """
        document = 'mutation DeleteReplaySessionCollection($id: ID!) {\n  deleteReplaySessionCollection(id: $id) {\n    deletedId\n    __typename\n  }\n}'

class MoveReplaySessionMovereplaysession(Model):
    """No documentation"""
    typename: Literal['MoveReplaySessionPayload'] = Field(alias='__typename', default='MoveReplaySessionPayload')
    session: Optional[ReplaySessionMeta] = Field(default=None)

class MoveReplaySession(Model):
    """No documentation found for this operation."""
    moveReplaySession: MoveReplaySessionMovereplaysession

    class Arguments(Model):
        """Arguments for MoveReplaySession """
        id: str
        collectionId: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for MoveReplaySession """
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation MoveReplaySession($id: ID!, $collectionId: ID!) {\n  moveReplaySession(id: $id, collectionId: $collectionId) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}'

class RenameReplaySessionRenamereplaysession(Model):
    """No documentation"""
    typename: Literal['RenameReplaySessionPayload'] = Field(alias='__typename', default='RenameReplaySessionPayload')
    session: Optional[ReplaySessionMeta] = Field(default=None)

class RenameReplaySession(Model):
    """No documentation found for this operation."""
    renameReplaySession: RenameReplaySessionRenamereplaysession

    class Arguments(Model):
        """Arguments for RenameReplaySession """
        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameReplaySession """
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation RenameReplaySession($id: ID!, $name: String!) {\n  renameReplaySession(id: $id, name: $name) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}'

class RenameReplaySessionCollectionRenamereplaysessioncollection(Model):
    """No documentation"""
    typename: Literal['RenameReplaySessionCollectionPayload'] = Field(alias='__typename', default='RenameReplaySessionCollectionPayload')
    collection: Optional[ReplaySessionCollectionMeta] = Field(default=None)

class RenameReplaySessionCollection(Model):
    """No documentation found for this operation."""
    renameReplaySessionCollection: RenameReplaySessionCollectionRenamereplaysessioncollection

    class Arguments(Model):
        """Arguments for RenameReplaySessionCollection """
        id: str
        name: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for RenameReplaySessionCollection """
        document = 'fragment ReplaySessionCollectionMeta on ReplaySessionCollection {\n  id\n  name\n  __typename\n}\n\nmutation RenameReplaySessionCollection($id: ID!, $name: String!) {\n  renameReplaySessionCollection(id: $id, name: $name) {\n    collection {\n      ...ReplaySessionCollectionMeta\n      __typename\n    }\n    __typename\n  }\n}'

class SetActiveReplaySessionEntrySetactivereplaysessionentry(Model):
    """No documentation"""
    typename: Literal['SetActiveReplaySessionEntryPayload'] = Field(alias='__typename', default='SetActiveReplaySessionEntryPayload')
    session: Optional[ReplaySessionMeta] = Field(default=None)

class SetActiveReplaySessionEntry(Model):
    """No documentation found for this operation."""
    setActiveReplaySessionEntry: SetActiveReplaySessionEntrySetactivereplaysessionentry
    'DEPRECATED Remove usage, no replacement: : None '

    class Arguments(Model):
        """Arguments for SetActiveReplaySessionEntry """
        id: str
        entryId: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for SetActiveReplaySessionEntry """
        document = 'fragment ReplaySessionMeta on ReplaySession {\n  id\n  name\n  collection {\n    id\n    __typename\n  }\n  activeEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nmutation SetActiveReplaySessionEntry($id: ID!, $entryId: ID!) {\n  setActiveReplaySessionEntry(id: $id, entryId: $entryId) {\n    session {\n      ...ReplaySessionMeta\n      __typename\n    }\n    __typename\n  }\n}'

class StartReplayTaskStartreplaytaskCloudUserErrorInlineFragment(Model):
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class StartReplayTaskStartreplaytaskPermissionDeniedUserErrorInlineFragment(Model):
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class StartReplayTaskStartreplaytaskTaskInProgressUserErrorInlineFragment(Model):
    typename: Literal['TaskInProgressUserError'] = Field(alias='__typename', default='TaskInProgressUserError')

class StartReplayTaskStartreplaytaskOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class StartReplayTaskStartreplaytask(Model):
    """No documentation"""
    typename: Literal['StartReplayTaskPayload'] = Field(alias='__typename', default='StartReplayTaskPayload')
    error: Optional[Union[StartReplayTaskStartreplaytaskCloudUserErrorInlineFragment, StartReplayTaskStartreplaytaskPermissionDeniedUserErrorInlineFragment, StartReplayTaskStartreplaytaskTaskInProgressUserErrorInlineFragment, StartReplayTaskStartreplaytaskOtherUserErrorInlineFragment]] = Field(default=None)
    task: Optional[ReplayTaskMeta] = Field(default=None)

class StartReplayTask(Model):
    """No documentation found for this operation."""
    startReplayTask: StartReplayTaskStartreplaytask

    class Arguments(Model):
        """Arguments for StartReplayTask """
        sessionId: str
        input: StartReplayTaskInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for StartReplayTask """
        document = 'fragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nfragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment CloudUserErrorFull on CloudUserError {\n  ...UserErrorFull\n  cloudReason: reason\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskInProgressUserErrorFull on TaskInProgressUserError {\n  ...UserErrorFull\n  taskId\n  __typename\n}\n\nmutation StartReplayTask($sessionId: ID!, $input: StartReplayTaskInput!) {\n  startReplayTask(sessionId: $sessionId, input: $input) {\n    error {\n      __typename\n      ... on CloudUserError {\n        ...CloudUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n      ... on TaskInProgressUserError {\n        ...TaskInProgressUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    task {\n      ...ReplayTaskMeta\n      __typename\n    }\n    __typename\n  }\n}'

class Request(Model):
    """No documentation found for this operation."""
    request: Optional[RequestFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Request """
        id: str
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Request """
        document = 'fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nquery Request($id: ID!, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  request(id: $id) {\n    ...RequestFull\n    __typename\n  }\n}'

class Response(Model):
    """No documentation found for this operation."""
    response: Optional[ResponseFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Response """
        id: str
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Response """
        document = 'fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nquery Response($id: ID!, $includeResponseRaw: Boolean!) {\n  response(id: $id) {\n    ...ResponseFull\n    __typename\n  }\n}'

class RequestsRequestsEdges(Model):
    """An edge in a connection."""
    typename: Literal['RequestEdge'] = Field(alias='__typename', default='RequestEdge')
    cursor: str
    'A cursor for use in pagination'
    node: RequestFull
    'The item at the end of the edge'

class RequestsRequestsPageinfo(Model):
    """Information about pagination in a connection"""
    typename: Literal['PageInfo'] = Field(alias='__typename', default='PageInfo')
    hasNextPage: bool
    'When paginating forwards, are there more items?'
    hasPreviousPage: bool
    'When paginating backwards, are there more items?'
    startCursor: Optional[str] = Field(default=None)
    'When paginating backwards, the cursor to continue.'
    endCursor: Optional[str] = Field(default=None)
    'When paginating forwards, the cursor to continue.'

class RequestsRequests(Model):
    """No documentation"""
    typename: Literal['RequestConnection'] = Field(alias='__typename', default='RequestConnection')
    edges: List[RequestsRequestsEdges]
    'A list of edges.'
    pageInfo: RequestsRequestsPageinfo
    'Information to aid in pagination.'

class Requests(Model):
    """No documentation found for this operation."""
    requests: RequestsRequests

    class Arguments(Model):
        """Arguments for Requests """
        first: Optional[int] = Field(default=None)
        after: Optional[str] = Field(default=None)
        last: Optional[int] = Field(default=None)
        before: Optional[str] = Field(default=None)
        filter: Optional[str] = Field(default=None)
        order: Optional[RequestResponseOrderInput] = Field(default=None)
        scopeId: Optional[str] = Field(default=None)
        includeRequestRaw: bool
        includeResponseRaw: bool
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Requests """
        document = 'fragment ResponseFull on Response {\n  id\n  statusCode\n  roundtripTime\n  length\n  createdAt\n  raw @include(if: $includeResponseRaw)\n  __typename\n}\n\nfragment RequestFull on Request {\n  id\n  host\n  port\n  method\n  path\n  query\n  isTls\n  metadata {\n    id\n    color\n    __typename\n  }\n  createdAt\n  raw @include(if: $includeRequestRaw)\n  response {\n    ...ResponseFull\n    __typename\n  }\n  __typename\n}\n\nquery Requests($first: Int, $after: String, $last: Int, $before: String, $filter: HTTPQL, $order: RequestResponseOrderInput, $scopeId: ID, $includeRequestRaw: Boolean!, $includeResponseRaw: Boolean!) {\n  requests(\n    first: $first\n    after: $after\n    last: $last\n    before: $before\n    filter: $filter\n    order: $order\n    scopeId: $scopeId\n  ) {\n    edges {\n      cursor\n      node {\n        ...RequestFull\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}'

class Scopes(Model):
    """No documentation found for this operation."""
    scopes: List[ScopeFull]

    class Arguments(Model):
        """Arguments for Scopes """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Scopes """
        document = 'fragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nquery Scopes {\n  scopes {\n    ...ScopeFull\n    __typename\n  }\n}'

class Scope(Model):
    """No documentation found for this operation."""
    scope: Optional[ScopeFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Scope """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Scope """
        document = 'fragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nquery Scope($id: ID!) {\n  scope(id: $id) {\n    ...ScopeFull\n    __typename\n  }\n}'

class CreateScopeCreatescopeInvalidGlobTermsUserErrorInlineFragment(Model):
    typename: Literal['InvalidGlobTermsUserError'] = Field(alias='__typename', default='InvalidGlobTermsUserError')

class CreateScopeCreatescopeOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class CreateScopeCreatescope(Model):
    """No documentation"""
    typename: Literal['CreateScopePayload'] = Field(alias='__typename', default='CreateScopePayload')
    error: Optional[Union[CreateScopeCreatescopeInvalidGlobTermsUserErrorInlineFragment, CreateScopeCreatescopeOtherUserErrorInlineFragment]] = Field(default=None)
    scope: Optional[ScopeFull] = Field(default=None)

class CreateScope(Model):
    """No documentation found for this operation."""
    createScope: CreateScopeCreatescope

    class Arguments(Model):
        """Arguments for CreateScope """
        input: CreateScopeInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateScope """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment InvalidGlobTermsUserErrorFull on InvalidGlobTermsUserError {\n  ...UserErrorFull\n  terms\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nmutation CreateScope($input: CreateScopeInput!) {\n  createScope(input: $input) {\n    error {\n      __typename\n      ... on InvalidGlobTermsUserError {\n        ...InvalidGlobTermsUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    scope {\n      ...ScopeFull\n      __typename\n    }\n    __typename\n  }\n}'

class UpdateScopeUpdatescopeInvalidGlobTermsUserErrorInlineFragment(Model):
    typename: Literal['InvalidGlobTermsUserError'] = Field(alias='__typename', default='InvalidGlobTermsUserError')

class UpdateScopeUpdatescopeOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class UpdateScopeUpdatescope(Model):
    """No documentation"""
    typename: Literal['UpdateScopePayload'] = Field(alias='__typename', default='UpdateScopePayload')
    error: Optional[Union[UpdateScopeUpdatescopeInvalidGlobTermsUserErrorInlineFragment, UpdateScopeUpdatescopeOtherUserErrorInlineFragment]] = Field(default=None)
    scope: Optional[ScopeFull] = Field(default=None)

class UpdateScope(Model):
    """No documentation found for this operation."""
    updateScope: UpdateScopeUpdatescope

    class Arguments(Model):
        """Arguments for UpdateScope """
        id: str
        input: UpdateScopeInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateScope """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment InvalidGlobTermsUserErrorFull on InvalidGlobTermsUserError {\n  ...UserErrorFull\n  terms\n  __typename\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ScopeFull on Scope {\n  id\n  name\n  allowlist\n  denylist\n  indexed\n  __typename\n}\n\nmutation UpdateScope($id: ID!, $input: UpdateScopeInput!) {\n  updateScope(id: $id, input: $input) {\n    error {\n      __typename\n      ... on InvalidGlobTermsUserError {\n        ...InvalidGlobTermsUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    scope {\n      ...ScopeFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteScopeDeletescope(Model):
    """No documentation"""
    typename: Literal['DeleteScopePayload'] = Field(alias='__typename', default='DeleteScopePayload')
    deletedId: str

class DeleteScope(Model):
    """No documentation found for this operation."""
    deleteScope: DeleteScopeDeletescope

    class Arguments(Model):
        """Arguments for DeleteScope """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteScope """
        document = 'mutation DeleteScope($id: ID!) {\n  deleteScope(id: $id) {\n    deletedId\n    __typename\n  }\n}'

class TasksTasksBase(Model):
    """No documentation"""

class TasksTasksBaseDataExportTask(TaskMetaDataExportTask, TasksTasksBase, Model):
    """No documentation"""
    typename: Literal['DataExportTask'] = Field(alias='__typename', default='DataExportTask')

class TasksTasksBaseReplayTask(TaskMetaReplayTask, TasksTasksBase, Model):
    """No documentation"""
    typename: Literal['ReplayTask'] = Field(alias='__typename', default='ReplayTask')

class TasksTasksBaseWorkflowTask(TaskMetaWorkflowTask, TasksTasksBase, Model):
    """No documentation"""
    typename: Literal['WorkflowTask'] = Field(alias='__typename', default='WorkflowTask')

class TasksTasksBaseCatchAll(TasksTasksBase, Model):
    """Catch all class for TasksTasksBase"""
    typename: str = Field(alias='__typename')

class Tasks(Model):
    """No documentation found for this operation."""
    tasks: List[Union[Annotated[Union[TasksTasksBaseDataExportTask, TasksTasksBaseReplayTask, TasksTasksBaseWorkflowTask], Field(discriminator='typename')], TasksTasksBaseCatchAll]]

    class Arguments(Model):
        """Arguments for Tasks """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Tasks """
        document = 'fragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nquery Tasks {\n  tasks {\n    ...TaskMeta\n    ... on ReplayTask {\n      ...ReplayTaskMeta\n    }\n    __typename\n  }\n}'

class cancelTaskCanceltaskUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class cancelTaskCanceltaskOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class cancelTaskCanceltask(Model):
    """No documentation"""
    typename: Literal['CancelTaskPayload'] = Field(alias='__typename', default='CancelTaskPayload')
    cancelledId: Optional[str] = Field(default=None)
    error: Optional[Union[cancelTaskCanceltaskUnknownIdUserErrorInlineFragment, cancelTaskCanceltaskOtherUserErrorInlineFragment]] = Field(default=None)

class cancelTask(Model):
    """No documentation found for this operation."""
    cancelTask: cancelTaskCanceltask

    class Arguments(Model):
        """Arguments for cancelTask """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for cancelTask """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation cancelTask($id: ID!) {\n  cancelTask(id: $id) {\n    cancelledId\n    error {\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      __typename\n    }\n    __typename\n  }\n}'

class FinishedTaskFinishedtaskTaskBase(Model):
    """No documentation"""

class FinishedTaskFinishedtaskTaskBaseDataExportTask(TaskMetaDataExportTask, FinishedTaskFinishedtaskTaskBase, Model):
    """No documentation"""
    typename: Literal['DataExportTask'] = Field(alias='__typename', default='DataExportTask')

class FinishedTaskFinishedtaskTaskBaseReplayTask(TaskMetaReplayTask, FinishedTaskFinishedtaskTaskBase, Model):
    """No documentation"""
    typename: Literal['ReplayTask'] = Field(alias='__typename', default='ReplayTask')

class FinishedTaskFinishedtaskTaskBaseWorkflowTask(TaskMetaWorkflowTask, FinishedTaskFinishedtaskTaskBase, Model):
    """No documentation"""
    typename: Literal['WorkflowTask'] = Field(alias='__typename', default='WorkflowTask')

class FinishedTaskFinishedtaskTaskBaseCatchAll(FinishedTaskFinishedtaskTaskBase, Model):
    """Catch all class for FinishedTaskFinishedtaskTaskBase"""
    typename: str = Field(alias='__typename')

class FinishedTaskFinishedtaskErrorBase(Model):
    """No documentation"""
    code: str

class FinishedTaskFinishedtaskErrorBaseAIUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['AIUserError'] = Field(alias='__typename', default='AIUserError')

class FinishedTaskFinishedtaskErrorBaseAliasTakenUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['AliasTakenUserError'] = Field(alias='__typename', default='AliasTakenUserError')

class FinishedTaskFinishedtaskErrorBaseAssistantUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['AssistantUserError'] = Field(alias='__typename', default='AssistantUserError')

class FinishedTaskFinishedtaskErrorBaseAuthenticationUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['AuthenticationUserError'] = Field(alias='__typename', default='AuthenticationUserError')

class FinishedTaskFinishedtaskErrorBaseAuthorizationUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['AuthorizationUserError'] = Field(alias='__typename', default='AuthorizationUserError')

class FinishedTaskFinishedtaskErrorBaseAutomateTaskUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['AutomateTaskUserError'] = Field(alias='__typename', default='AutomateTaskUserError')

class FinishedTaskFinishedtaskErrorBaseBackupUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['BackupUserError'] = Field(alias='__typename', default='BackupUserError')

class FinishedTaskFinishedtaskErrorBaseCertificateUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['CertificateUserError'] = Field(alias='__typename', default='CertificateUserError')

class FinishedTaskFinishedtaskErrorBaseCloudUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['CloudUserError'] = Field(alias='__typename', default='CloudUserError')

class FinishedTaskFinishedtaskErrorBaseInternalUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['InternalUserError'] = Field(alias='__typename', default='InternalUserError')

class FinishedTaskFinishedtaskErrorBaseInvalidGlobTermsUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['InvalidGlobTermsUserError'] = Field(alias='__typename', default='InvalidGlobTermsUserError')

class FinishedTaskFinishedtaskErrorBaseInvalidHTTPQLUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['InvalidHTTPQLUserError'] = Field(alias='__typename', default='InvalidHTTPQLUserError')

class FinishedTaskFinishedtaskErrorBaseInvalidRegexUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['InvalidRegexUserError'] = Field(alias='__typename', default='InvalidRegexUserError')

class FinishedTaskFinishedtaskErrorBaseNameTakenUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['NameTakenUserError'] = Field(alias='__typename', default='NameTakenUserError')

class FinishedTaskFinishedtaskErrorBaseNewerVersionUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['NewerVersionUserError'] = Field(alias='__typename', default='NewerVersionUserError')

class FinishedTaskFinishedtaskErrorBaseOtherUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class FinishedTaskFinishedtaskErrorBasePermissionDeniedUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class FinishedTaskFinishedtaskErrorBasePluginUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['PluginUserError'] = Field(alias='__typename', default='PluginUserError')

class FinishedTaskFinishedtaskErrorBaseProjectUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['ProjectUserError'] = Field(alias='__typename', default='ProjectUserError')

class FinishedTaskFinishedtaskErrorBaseRankUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['RankUserError'] = Field(alias='__typename', default='RankUserError')

class FinishedTaskFinishedtaskErrorBaseReadOnlyUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['ReadOnlyUserError'] = Field(alias='__typename', default='ReadOnlyUserError')

class FinishedTaskFinishedtaskErrorBaseRenderFailedUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['RenderFailedUserError'] = Field(alias='__typename', default='RenderFailedUserError')

class FinishedTaskFinishedtaskErrorBaseStoreUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['StoreUserError'] = Field(alias='__typename', default='StoreUserError')

class FinishedTaskFinishedtaskErrorBaseTaskInProgressUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['TaskInProgressUserError'] = Field(alias='__typename', default='TaskInProgressUserError')

class FinishedTaskFinishedtaskErrorBaseUnknownIdUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class FinishedTaskFinishedtaskErrorBaseUnsupportedPlatformUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['UnsupportedPlatformUserError'] = Field(alias='__typename', default='UnsupportedPlatformUserError')

class FinishedTaskFinishedtaskErrorBaseWorkflowUserError(FinishedTaskFinishedtaskErrorBase, Model):
    """No documentation"""
    typename: Literal['WorkflowUserError'] = Field(alias='__typename', default='WorkflowUserError')

class FinishedTaskFinishedtaskErrorBaseCatchAll(FinishedTaskFinishedtaskErrorBase, Model):
    """Catch all class for FinishedTaskFinishedtaskErrorBase"""
    typename: str = Field(alias='__typename')

class FinishedTaskFinishedtask(Model):
    """No documentation"""
    typename: Literal['FinishedTaskPayload'] = Field(alias='__typename', default='FinishedTaskPayload')
    task: Union[Annotated[Union[FinishedTaskFinishedtaskTaskBaseDataExportTask, FinishedTaskFinishedtaskTaskBaseReplayTask, FinishedTaskFinishedtaskTaskBaseWorkflowTask], Field(discriminator='typename')], FinishedTaskFinishedtaskTaskBaseCatchAll]
    status: TaskStatus
    error: Optional[Union[Annotated[Union[FinishedTaskFinishedtaskErrorBaseAIUserError, FinishedTaskFinishedtaskErrorBaseAliasTakenUserError, FinishedTaskFinishedtaskErrorBaseAssistantUserError, FinishedTaskFinishedtaskErrorBaseAuthenticationUserError, FinishedTaskFinishedtaskErrorBaseAuthorizationUserError, FinishedTaskFinishedtaskErrorBaseAutomateTaskUserError, FinishedTaskFinishedtaskErrorBaseBackupUserError, FinishedTaskFinishedtaskErrorBaseCertificateUserError, FinishedTaskFinishedtaskErrorBaseCloudUserError, FinishedTaskFinishedtaskErrorBaseInternalUserError, FinishedTaskFinishedtaskErrorBaseInvalidGlobTermsUserError, FinishedTaskFinishedtaskErrorBaseInvalidHTTPQLUserError, FinishedTaskFinishedtaskErrorBaseInvalidRegexUserError, FinishedTaskFinishedtaskErrorBaseNameTakenUserError, FinishedTaskFinishedtaskErrorBaseNewerVersionUserError, FinishedTaskFinishedtaskErrorBaseOtherUserError, FinishedTaskFinishedtaskErrorBasePermissionDeniedUserError, FinishedTaskFinishedtaskErrorBasePluginUserError, FinishedTaskFinishedtaskErrorBaseProjectUserError, FinishedTaskFinishedtaskErrorBaseRankUserError, FinishedTaskFinishedtaskErrorBaseReadOnlyUserError, FinishedTaskFinishedtaskErrorBaseRenderFailedUserError, FinishedTaskFinishedtaskErrorBaseStoreUserError, FinishedTaskFinishedtaskErrorBaseTaskInProgressUserError, FinishedTaskFinishedtaskErrorBaseUnknownIdUserError, FinishedTaskFinishedtaskErrorBaseUnsupportedPlatformUserError, FinishedTaskFinishedtaskErrorBaseWorkflowUserError], Field(discriminator='typename')], FinishedTaskFinishedtaskErrorBaseCatchAll]] = Field(default=None)

class FinishedTask(Model):
    """No documentation found for this operation."""
    finishedTask: FinishedTaskFinishedtask

    class Arguments(Model):
        """Arguments for FinishedTask """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for FinishedTask """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment RankUserErrorFull on RankUserError {\n  ...UserErrorFull\n  rankReason: reason\n  __typename\n}\n\nfragment ReplayTaskMeta on ReplayTask {\n  ...TaskMeta\n  replayEntry {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment TaskMeta on Task {\n  __typename\n  id\n  createdAt\n}\n\nsubscription FinishedTask {\n  finishedTask {\n    task {\n      ...TaskMeta\n      ... on ReplayTask {\n        ...ReplayTaskMeta\n      }\n      __typename\n    }\n    status\n    error {\n      __typename\n      code\n      ... on RankUserError {\n        ...RankUserErrorFull\n      }\n    }\n    __typename\n  }\n}'

class ViewerCloudUserInlineFragmentProfileIdentity(Model):
    """No documentation"""
    typename: Literal['UserIdentity'] = Field(alias='__typename', default='UserIdentity')
    email: str
    name: str

class ViewerCloudUserInlineFragmentProfileSubscriptionPlan(Model):
    """No documentation"""
    typename: Literal['UserSubscriptionPlan'] = Field(alias='__typename', default='UserSubscriptionPlan')
    name: str

class ViewerCloudUserInlineFragmentProfileSubscriptionEntitlements(Model):
    """No documentation"""
    typename: Literal['UserEntitlement'] = Field(alias='__typename', default='UserEntitlement')
    name: str

class ViewerCloudUserInlineFragmentProfileSubscription(Model):
    """No documentation"""
    typename: Literal['UserSubscription'] = Field(alias='__typename', default='UserSubscription')
    plan: ViewerCloudUserInlineFragmentProfileSubscriptionPlan
    entitlements: List[ViewerCloudUserInlineFragmentProfileSubscriptionEntitlements]

class ViewerCloudUserInlineFragmentProfile(Model):
    """No documentation"""
    typename: Literal['UserProfile'] = Field(alias='__typename', default='UserProfile')
    identity: ViewerCloudUserInlineFragmentProfileIdentity
    subscription: ViewerCloudUserInlineFragmentProfileSubscription

class ViewerCloudUserInlineFragment(Model):
    typename: Literal['CloudUser'] = Field(alias='__typename', default='CloudUser')
    id: str
    profile: ViewerCloudUserInlineFragmentProfile

class ViewerGuestUserInlineFragment(Model):
    typename: Literal['GuestUser'] = Field(alias='__typename', default='GuestUser')
    id: str

class ViewerScriptUserInlineFragment(Model):
    typename: Literal['ScriptUser'] = Field(alias='__typename', default='ScriptUser')
    id: str

class Viewer(Model):
    """No documentation found for this operation."""
    viewer: Union[ViewerCloudUserInlineFragment, ViewerGuestUserInlineFragment, ViewerScriptUserInlineFragment]

    class Arguments(Model):
        """Arguments for Viewer """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Viewer """
        document = 'query Viewer {\n  viewer {\n    ... on CloudUser {\n      __typename\n      id\n      profile {\n        identity {\n          email\n          name\n        }\n        subscription {\n          plan {\n            name\n          }\n          entitlements {\n            name\n          }\n        }\n      }\n    }\n    ... on GuestUser {\n      __typename\n      id\n    }\n    ... on ScriptUser {\n      __typename\n      id\n    }\n    __typename\n  }\n}'

class Workflows(Model):
    """No documentation found for this operation."""
    workflows: List[WorkflowFull]

    class Arguments(Model):
        """Arguments for Workflows """
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Workflows """
        document = 'fragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nquery Workflows {\n  workflows {\n    ...WorkflowFull\n    __typename\n  }\n}'

class Workflow(Model):
    """No documentation found for this operation."""
    workflow: Optional[WorkflowFull] = Field(default=None)

    class Arguments(Model):
        """Arguments for Workflow """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for Workflow """
        document = 'fragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nquery Workflow($id: ID!) {\n  workflow(id: $id) {\n    ...WorkflowFull\n    __typename\n  }\n}'

class CreateWorkflowCreateworkflowWorkflowUserErrorInlineFragment(Model):
    typename: Literal['WorkflowUserError'] = Field(alias='__typename', default='WorkflowUserError')

class CreateWorkflowCreateworkflowOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class CreateWorkflowCreateworkflowPermissionDeniedUserErrorInlineFragment(Model):
    typename: Literal['PermissionDeniedUserError'] = Field(alias='__typename', default='PermissionDeniedUserError')

class CreateWorkflowCreateworkflow(Model):
    """No documentation"""
    typename: Literal['CreateWorkflowPayload'] = Field(alias='__typename', default='CreateWorkflowPayload')
    error: Optional[Union[CreateWorkflowCreateworkflowWorkflowUserErrorInlineFragment, CreateWorkflowCreateworkflowOtherUserErrorInlineFragment, CreateWorkflowCreateworkflowPermissionDeniedUserErrorInlineFragment]] = Field(default=None)
    workflow: Optional[WorkflowFull] = Field(default=None)

class CreateWorkflow(Model):
    """No documentation found for this operation."""
    createWorkflow: CreateWorkflowCreateworkflow

    class Arguments(Model):
        """Arguments for CreateWorkflow """
        input: CreateWorkflowInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for CreateWorkflow """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment PermissionDeniedUserErrorFull on PermissionDeniedUserError {\n  ...UserErrorFull\n  permissionReason: reason\n  __typename\n}\n\nfragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation CreateWorkflow($input: CreateWorkflowInput!) {\n  createWorkflow(input: $input) {\n    error {\n      __typename\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on PermissionDeniedUserError {\n        ...PermissionDeniedUserErrorFull\n      }\n    }\n    workflow {\n      ...WorkflowFull\n      __typename\n    }\n    __typename\n  }\n}'

class UpdateWorkflowUpdateworkflowUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class UpdateWorkflowUpdateworkflowWorkflowUserErrorInlineFragment(Model):
    typename: Literal['WorkflowUserError'] = Field(alias='__typename', default='WorkflowUserError')

class UpdateWorkflowUpdateworkflowOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class UpdateWorkflowUpdateworkflowReadOnlyUserErrorInlineFragment(Model):
    typename: Literal['ReadOnlyUserError'] = Field(alias='__typename', default='ReadOnlyUserError')

class UpdateWorkflowUpdateworkflow(Model):
    """No documentation"""
    typename: Literal['UpdateWorkflowPayload'] = Field(alias='__typename', default='UpdateWorkflowPayload')
    error: Optional[Union[UpdateWorkflowUpdateworkflowUnknownIdUserErrorInlineFragment, UpdateWorkflowUpdateworkflowWorkflowUserErrorInlineFragment, UpdateWorkflowUpdateworkflowOtherUserErrorInlineFragment, UpdateWorkflowUpdateworkflowReadOnlyUserErrorInlineFragment]] = Field(default=None)
    workflow: Optional[WorkflowFull] = Field(default=None)

class UpdateWorkflow(Model):
    """No documentation found for this operation."""
    updateWorkflow: UpdateWorkflowUpdateworkflow

    class Arguments(Model):
        """Arguments for UpdateWorkflow """
        id: str
        input: UpdateWorkflowInput
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for UpdateWorkflow """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ReadOnlyUserErrorFull on ReadOnlyUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nfragment WorkflowFull on Workflow {\n  id\n  name\n  kind\n  definition\n  enabled\n  global\n  readOnly\n  createdAt\n  updatedAt\n  __typename\n}\n\nfragment WorkflowUserErrorFull on WorkflowUserError {\n  ...UserErrorFull\n  node\n  message\n  reason\n  __typename\n}\n\nmutation UpdateWorkflow($id: ID!, $input: UpdateWorkflowInput!) {\n  updateWorkflow(id: $id, input: $input) {\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on WorkflowUserError {\n        ...WorkflowUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n      ... on ReadOnlyUserError {\n        ...ReadOnlyUserErrorFull\n      }\n    }\n    workflow {\n      ...WorkflowFull\n      __typename\n    }\n    __typename\n  }\n}'

class DeleteWorkflowDeleteworkflowUnknownIdUserErrorInlineFragment(Model):
    typename: Literal['UnknownIdUserError'] = Field(alias='__typename', default='UnknownIdUserError')

class DeleteWorkflowDeleteworkflowReadOnlyUserErrorInlineFragment(Model):
    typename: Literal['ReadOnlyUserError'] = Field(alias='__typename', default='ReadOnlyUserError')

class DeleteWorkflowDeleteworkflowOtherUserErrorInlineFragment(Model):
    typename: Literal['OtherUserError'] = Field(alias='__typename', default='OtherUserError')

class DeleteWorkflowDeleteworkflow(Model):
    """No documentation"""
    typename: Literal['DeleteWorkflowPayload'] = Field(alias='__typename', default='DeleteWorkflowPayload')
    deletedId: Optional[str] = Field(default=None)
    error: Optional[Union[DeleteWorkflowDeleteworkflowUnknownIdUserErrorInlineFragment, DeleteWorkflowDeleteworkflowReadOnlyUserErrorInlineFragment, DeleteWorkflowDeleteworkflowOtherUserErrorInlineFragment]] = Field(default=None)

class DeleteWorkflow(Model):
    """No documentation found for this operation."""
    deleteWorkflow: DeleteWorkflowDeleteworkflow

    class Arguments(Model):
        """Arguments for DeleteWorkflow """
        id: str
        model_config = ConfigDict(populate_by_name=None)

    class Meta:
        """Meta class for DeleteWorkflow """
        document = 'fragment UserErrorFull on UserError {\n  __typename\n  code\n}\n\nfragment OtherUserErrorFull on OtherUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment ReadOnlyUserErrorFull on ReadOnlyUserError {\n  ...UserErrorFull\n  __typename\n}\n\nfragment UnknownIdUserErrorFull on UnknownIdUserError {\n  ...UserErrorFull\n  id\n  __typename\n}\n\nmutation DeleteWorkflow($id: ID!) {\n  deleteWorkflow(id: $id) {\n    deletedId\n    error {\n      __typename\n      ... on UnknownIdUserError {\n        ...UnknownIdUserErrorFull\n      }\n      ... on ReadOnlyUserError {\n        ...ReadOnlyUserErrorFull\n      }\n      ... on OtherUserError {\n        ...OtherUserErrorFull\n      }\n    }\n    __typename\n  }\n}'
CreateEnvironmentInput.model_rebuild()
CreateReplaySessionInput.model_rebuild()
InstallPluginPackageInput.model_rebuild()
ReplayEntrySettingsInput.model_rebuild()
ReplayPlaceholderInput.model_rebuild()
ReplayPreprocessorInput.model_rebuild()
ReplayPreprocessorOptionsInput.model_rebuild()
SetInstanceSettingsInput.model_rebuild()