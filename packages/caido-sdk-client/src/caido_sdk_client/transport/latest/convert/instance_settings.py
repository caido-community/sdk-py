"""Conversion helpers for instance-settings GraphQL fragments."""

from __future__ import annotations

from caido_sdk_client.graphql.__generated__.schema import InstanceSettingsFull
from caido_sdk_client.types.instance_settings import (
    AISettings,
    AnalyticsSettings,
    AnthropicAISetting,
    GoogleAISetting,
    InstanceSettings,
    OnboardingSettings,
    OpenAIAISetting,
    OpenRouterAISetting,
)


def map_to_instance_settings(data: InstanceSettingsFull) -> InstanceSettings:
    """Convert an InstanceSettingsFull fragment into the public InstanceSettings type."""
    return InstanceSettings(
        ai=_map_to_ai_settings(data),
        analytics=_map_to_analytics_settings(data),
        onboarding=_map_to_onboarding_settings(data),
    )


def _map_to_ai_settings(data: InstanceSettingsFull) -> AISettings:
    providers = data.aiProviders
    anthropic = providers.anthropic
    google = providers.google
    openai = providers.openai
    openrouter = providers.openrouter

    return AISettings(
        anthropic=AnthropicAISetting(api_key=anthropic.apiKey)
        if anthropic is not None
        else None,
        google=GoogleAISetting(api_key=google.apiKey) if google is not None else None,
        openai=OpenAIAISetting(
            api_key=openai.apiKey,
            url=openai.url if openai.url is not None else None,
        )
        if openai is not None
        else None,
        openrouter=OpenRouterAISetting(api_key=openrouter.apiKey)
        if openrouter is not None
        else None,
    )


def _map_to_analytics_settings(data: InstanceSettingsFull) -> AnalyticsSettings:
    a = data.analytic
    return AnalyticsSettings(enabled=a.enabled, cloud=a.cloud, local=a.local)


def _map_to_onboarding_settings(data: InstanceSettingsFull) -> OnboardingSettings:
    o = data.onboarding
    return OnboardingSettings(analytic=o.analytic)
