"""Higher-level SDK for user-related operations."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Protocol, runtime_checkable

from caido_sdk_client.errors.sdk import (
    NoViewerInResponseError,
    UnsupportedViewerTypeError,
)
from caido_sdk_client.graphql.__generated__.schema import (
    Viewer,
    ViewerCloudUserInlineFragment,
    ViewerGuestUserInlineFragment,
    ViewerScriptUserInlineFragment,
)
from caido_sdk_client.types.strings import Id
from caido_sdk_client.types.user import (
    CloudUser,
    GuestUser,
    ScriptUser,
    SubscriptionEntitlement,
    SubscriptionPlan,
    User,
    UserIdentity,
    UserProfile,
    UserSubscription,
)


@runtime_checkable
class UserGraphQLClient(Protocol):
    """Protocol implemented by GraphQL clients used by UserSDK."""

    async def query(
        self,
        document: str,
        variables: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a GraphQL query."""


class UserSDK:
    """Higher-level SDK for user-related operations."""

    def __init__(self, graphql: UserGraphQLClient) -> None:
        self._graphql = graphql

    async def viewer(self) -> User:
        """Get the currently authenticated user (viewer)."""
        result = await self._graphql.query(Viewer.Meta.document)
        model = Viewer.model_validate(result)
        viewer = model.viewer
        if viewer is None:
            raise NoViewerInResponseError()

        match viewer:
            case ViewerCloudUserInlineFragment():
                return CloudUser(
                    kind="CloudUser",
                    id=Id(viewer.id),
                    profile=UserProfile(
                        identity=UserIdentity(
                            email=viewer.profile.identity.email,
                            name=viewer.profile.identity.name,
                        ),
                        subscription=UserSubscription(
                            plan=SubscriptionPlan(
                                name=viewer.profile.subscription.plan.name,
                            ),
                            entitlements=[
                                SubscriptionEntitlement(name=e.name)
                                for e in viewer.profile.subscription.entitlements
                            ],
                        ),
                    ),
                )
            case ViewerGuestUserInlineFragment():
                return GuestUser(kind="GuestUser", id=Id(viewer.id))
            case ViewerScriptUserInlineFragment():
                return ScriptUser(kind="ScriptUser", id=Id(viewer.id))
            case _:
                typename = getattr(viewer, "typename", None)
                raise UnsupportedViewerTypeError(typename)
