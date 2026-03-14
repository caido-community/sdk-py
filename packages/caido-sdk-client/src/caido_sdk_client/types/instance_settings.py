"""Instance settings-related user-facing types."""

from __future__ import annotations

from dataclasses import dataclass

# --- Current settings (output) ---


@dataclass(frozen=True)
class AnthropicAISetting:
    """Provider settings for Anthropic."""

    api_key: str


@dataclass(frozen=True)
class GoogleAISetting:
    """Provider settings for Google."""

    api_key: str


@dataclass(frozen=True)
class OpenAIAISetting:
    """Provider settings for OpenAI."""

    api_key: str
    url: str | None = None


@dataclass(frozen=True)
class OpenRouterAISetting:
    """Provider settings for OpenRouter."""

    api_key: str


@dataclass(frozen=True)
class AISettings:
    """Current AI provider settings."""

    anthropic: AnthropicAISetting | None = None
    google: GoogleAISetting | None = None
    openai: OpenAIAISetting | None = None
    openrouter: OpenRouterAISetting | None = None


@dataclass(frozen=True)
class AnalyticsSettings:
    """Current analytics settings."""

    enabled: bool
    cloud: bool
    local: bool


@dataclass(frozen=True)
class OnboardingSettings:
    """Current onboarding settings."""

    analytic: bool


@dataclass(frozen=True)
class InstanceSettings:
    """Current instance settings."""

    ai: AISettings
    analytics: AnalyticsSettings
    onboarding: OnboardingSettings


# --- Input types for setting values ---

# Allow string (api key only) or full setting object for each provider.
SetAnthropicAISettingInput = str | AnthropicAISetting
SetGoogleAISettingInput = str | GoogleAISetting
SetOpenAIAISettingInput = str | OpenAIAISetting
SetOpenRouterAISettingInput = str | OpenRouterAISetting


@dataclass(frozen=True)
class SetAnalyticsSettingsInput:
    """Input for setting analytics settings."""

    enabled: bool


@dataclass(frozen=True)
class SetOnboardingSettingsInput:
    """Input for setting onboarding settings."""

    analytic: bool


@dataclass(frozen=True)
class SetAISettingsInput:
    """Input for setting AI provider settings. Exactly one provider must be set."""

    anthropic: SetAnthropicAISettingInput | None = None
    google: SetGoogleAISettingInput | None = None
    openai: SetOpenAIAISettingInput | None = None
    openrouter: SetOpenRouterAISettingInput | None = None


@dataclass(frozen=True)
class SetInstanceSettingsInput:
    """Input for setting instance settings. Exactly one setting group must be set."""

    ai: SetAISettingsInput | None = None
    analytics: SetAnalyticsSettingsInput | None = None
    onboarding: SetOnboardingSettingsInput | None = None
