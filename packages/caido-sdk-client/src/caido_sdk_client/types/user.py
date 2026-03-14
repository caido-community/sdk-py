"""User-facing types for viewer-related models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from caido_sdk_client.types.strings import Id


@dataclass(frozen=True)
class UserIdentity:
    email: str
    name: str


@dataclass(frozen=True)
class SubscriptionPlan:
    name: str


@dataclass(frozen=True)
class SubscriptionEntitlement:
    name: str


@dataclass(frozen=True)
class UserSubscription:
    plan: SubscriptionPlan
    entitlements: list[SubscriptionEntitlement]


@dataclass(frozen=True)
class UserProfile:
    identity: UserIdentity
    subscription: UserSubscription


@dataclass(frozen=True)
class CloudUser:
    kind: Literal["CloudUser"]
    id: Id
    profile: UserProfile


@dataclass(frozen=True)
class GuestUser:
    kind: Literal["GuestUser"]
    id: Id


@dataclass(frozen=True)
class ScriptUser:
    kind: Literal["ScriptUser"]
    id: Id


User = CloudUser | GuestUser | ScriptUser
