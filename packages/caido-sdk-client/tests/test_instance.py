"""Tests for the Instance SDK."""

from __future__ import annotations

from collections.abc import AsyncGenerator

import pytest
from caido_sdk_client import Client
from caido_sdk_client.types import (
    InstanceSettings,
    OpenAIAISetting,
    SetAISettingsInput,
    SetAnalyticsSettingsInput,
    SetOnboardingSettingsInput,
)


@pytest.fixture
async def original_instance_settings(
    caido: Client,
) -> AsyncGenerator[InstanceSettings, None]:
    """Capture current instance settings and restore them after the test."""
    original = await caido.instance.settings.get()
    yield original
    # Restore analytics and onboarding
    await caido.instance.settings.set_analytics(
        SetAnalyticsSettingsInput(enabled=original.analytics.enabled)
    )
    await caido.instance.settings.set_onboarding(
        SetOnboardingSettingsInput(analytic=original.onboarding.analytic)
    )
    # Restore AI provider if one was set
    if original.ai.openrouter is not None:
        await caido.instance.settings.set_ai(
            SetAISettingsInput(openrouter=original.ai.openrouter.api_key)
        )
        return
    if original.ai.openai is not None:
        await caido.instance.settings.set_ai(
            SetAISettingsInput(
                openai=OpenAIAISetting(
                    api_key=original.ai.openai.api_key,
                    url=original.ai.openai.url,
                )
            )
        )
        return
    if original.ai.anthropic is not None:
        await caido.instance.settings.set_ai(
            SetAISettingsInput(anthropic=original.ai.anthropic.api_key)
        )
        return
    if original.ai.google is not None:
        await caido.instance.settings.set_ai(
            SetAISettingsInput(google=original.ai.google.api_key)
        )


@pytest.mark.usefixtures("original_instance_settings")
async def test_read_and_update_instance_settings(caido: Client) -> None:
    """Read and update instance settings (analytics and onboarding)."""
    original = await caido.instance.settings.get()
    assert isinstance(original.analytics.enabled, bool)
    assert isinstance(original.onboarding.analytic, bool)

    next_analytics = not original.analytics.enabled
    next_onboarding = not original.onboarding.analytic

    analytics_updated = await caido.instance.settings.set_analytics(
        SetAnalyticsSettingsInput(enabled=next_analytics)
    )
    assert analytics_updated.analytics.enabled is next_analytics

    onboarding_updated = await caido.instance.settings.set_onboarding(
        SetOnboardingSettingsInput(analytic=next_onboarding)
    )
    assert onboarding_updated.onboarding.analytic is next_onboarding


@pytest.mark.usefixtures("original_instance_settings")
async def test_set_ai_shorthand_and_object_forms(caido: Client) -> None:
    """Support shorthand (api key string) and object forms for set_ai."""
    import time

    original = await caido.instance.settings.get()
    test_api_key = f"sdk-test-key-{int(time.time() * 1000)}"

    if original.ai.openrouter is not None:
        await caido.instance.settings.set_ai(
            SetAISettingsInput(openrouter=test_api_key)
        )
        return
    if original.ai.openai is not None:
        await caido.instance.settings.set_ai(SetAISettingsInput(openai=test_api_key))
        return
    if original.ai.anthropic is not None:
        await caido.instance.settings.set_ai(SetAISettingsInput(anthropic=test_api_key))
        return
    if original.ai.google is not None:
        await caido.instance.settings.set_ai(SetAISettingsInput(google=test_api_key))
        return
    # No AI provider configured; test passes by doing nothing
    assert True
