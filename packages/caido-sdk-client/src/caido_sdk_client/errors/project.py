"""Project-related errors."""

from __future__ import annotations

from caido_sdk_client.errors.base import BaseError
from caido_sdk_client.graphql.__generated__.schema import (
    ProjectErrorReason,
    ProjectUserErrorFull,
)


class ProjectUserError(BaseError):
    reason: ProjectErrorReason

    def __init__(self, error: ProjectUserErrorFull) -> None:
        match error.projectReason:
            case ProjectErrorReason.DELETING:
                super().__init__("Project is currently being deleted.")
                self.reason = error.projectReason
            case ProjectErrorReason.EXPORTING:
                super().__init__("Project is currently being exported.")
                self.reason = error.projectReason
            case ProjectErrorReason.INVALID_VERSION:
                super().__init__("Project doesn't have a valid version.")
                self.reason = error.projectReason
            case ProjectErrorReason.NOT_READY:
                super().__init__("Project is not ready yet.")
                self.reason = error.projectReason
            case ProjectErrorReason.TOO_RECENT:
                super().__init__(
                    "The project was created with a newer version of Caido."
                )
                self.reason = error.projectReason
