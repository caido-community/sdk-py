"""User-facing types for viewer-related models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


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
    id: str
    profile: UserProfile


@dataclass(frozen=True)
class GuestUser:
    kind: Literal["GuestUser"]
    id: str


@dataclass(frozen=True)
class ScriptUser:
    kind: Literal["ScriptUser"]
    id: str


User = CloudUser | GuestUser | ScriptUser
