"""Project-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import ProjectErrorReason


class ProjectUserError(BaseError):
    reason: ProjectErrorReason

    def __init__(self, reason: ProjectErrorReason) -> None:
        match reason:
            case ProjectErrorReason.DELETING:
                super().__init__("Project is currently being deleted.")
                self.reason = reason
            case ProjectErrorReason.EXPORTING:
                super().__init__("Project is currently being exported.")
                self.reason = reason
            case ProjectErrorReason.INVALID_VERSION:
                super().__init__("Project doesn't have a valid version.")
                self.reason = reason
            case ProjectErrorReason.NOT_READY:
                super().__init__("Project is not ready yet.")
                self.reason = reason
            case ProjectErrorReason.TOO_RECENT:
                super().__init__(
                    "The project was created with a newer version of Caido."
                )
                self.reason = reason
