"""SDK for instance settings."""

from __future__ import annotations

from caido_sdk_client.convert.instance_settings import map_to_instance_settings
from caido_sdk_client.graphql import GraphQLClient
from caido_sdk_client.graphql.__generated__.schema import (
    InstanceSettings as InstanceSettingsOp,
)
from caido_sdk_client.graphql.__generated__.schema import (
    SetInstanceSettings,
)
from caido_sdk_client.types.instance_settings import (
    AnthropicAISetting,
    GoogleAISetting,
    InstanceSettings,
    OpenAIAISetting,
    OpenRouterAISetting,
    SetAISettingsInput,
    SetAnalyticsSettingsInput,
    SetInstanceSettingsInput,
    SetOnboardingSettingsInput,
)


def _normalize_anthropic(value: str | AnthropicAISetting) -> dict[str, str]:
    if isinstance(value, str):
        return {"apiKey": value}
    return {"apiKey": value.api_key}


def _normalize_google(value: str | GoogleAISetting) -> dict[str, str]:
    if isinstance(value, str):
        return {"apiKey": value}
    return {"apiKey": value.api_key}


def _normalize_openai(value: str | OpenAIAISetting) -> dict[str, str | None]:
    if isinstance(value, str):
        return {"apiKey": value}
    return {"apiKey": value.api_key, "url": value.url}


def _normalize_openrouter(value: str | OpenRouterAISetting) -> dict[str, str]:
    if isinstance(value, str):
        return {"apiKey": value}
    return {"apiKey": value.api_key}


def _normalize_ai_input(input: SetAISettingsInput) -> dict[str, dict]:
    """Build SettingsAIProviderInput dict (one provider)."""
    if input.anthropic is not None:
        return {"anthropic": _normalize_anthropic(input.anthropic)}
    if input.google is not None:
        return {"google": _normalize_google(input.google)}
    if input.openai is not None:
        return {"openai": _normalize_openai(input.openai)}
    if input.openrouter is not None:
        return {"openrouter": _normalize_openrouter(input.openrouter)}
    raise ValueError("Invalid AI settings input: exactly one provider must be set")


def _build_raw_input(input: SetInstanceSettingsInput) -> dict:
    """Build GraphQL SetInstanceSettingsInput dict (camelCase keys)."""
    if input.ai is not None:
        return {"aiProvider": _normalize_ai_input(input.ai)}
    if input.analytics is not None:
        return {"analytics": {"enabled": input.analytics.enabled}}
    if input.onboarding is not None:
        return {"onboarding": {"analytic": input.onboarding.analytic}}
    raise ValueError("Invalid instance settings input: exactly one group must be set")


class InstanceSettingsSDK:
    """SDK for instance settings."""

    def __init__(self, graphql: GraphQLClient) -> None:
        self._graphql = graphql

    async def get(self) -> InstanceSettings:
        """Get current instance settings."""
        result = await self._graphql.query(InstanceSettingsOp.Meta.document)
        model = InstanceSettingsOp.model_validate(result)
        return map_to_instance_settings(model.instanceSettings)

    async def set(self, input: SetInstanceSettingsInput) -> InstanceSettings:
        """Set an instance setting group."""
        raw = _build_raw_input(input)
        result = await self._graphql.mutation(
            SetInstanceSettings.Meta.document,
            variables={"input": raw},
        )
        model = SetInstanceSettings.model_validate(result)
        return map_to_instance_settings(model.setInstanceSettings.settings)

    async def set_ai(self, input: SetAISettingsInput) -> InstanceSettings:
        """Set AI settings for one provider."""
        return await self.set(SetInstanceSettingsInput(ai=input))

    async def set_analytics(
        self,
        input: SetAnalyticsSettingsInput,
    ) -> InstanceSettings:
        """Set analytics settings."""
        return await self.set(SetInstanceSettingsInput(analytics=input))

    async def set_onboarding(
        self,
        input: SetOnboardingSettingsInput,
    ) -> InstanceSettings:
        """Set onboarding settings."""
        return await self.set(SetInstanceSettingsInput(onboarding=input))
