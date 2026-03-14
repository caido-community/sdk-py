"""Types for replay sessions and send options."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

from caido_sdk_client.types.network import ConnectionInfoInput
from caido_sdk_client.types.replay_entry import ReplayEntry
from caido_sdk_client.types.strings import IdLike


@dataclass(frozen=True, slots=True)
class CreateReplaySessionOptions:
    """Options for creating a replay session."""

    collection_id: IdLike | None = None
    """Create from existing request id or raw input."""
    request_source: CreateReplaySessionFromId | CreateReplaySessionFromRaw | None = None


@dataclass(frozen=True, slots=True)
class CreateReplaySessionFromId:
    """Create replay session from an existing request ID."""

    id: IdLike


@dataclass(frozen=True, slots=True)
class CreateReplaySessionFromRaw:
    """Create replay session from raw request bytes and connection."""

    raw: str | bytes
    connection: ConnectionInfoInput


@dataclass(frozen=True, slots=True)
class ReplaySendOptions:
    """Options for replay.send(): raw request bytes and connection; optional settings."""

    raw: str | bytes
    connection: ConnectionInfoInput
    settings: ReplaySendSettings | None = None


@dataclass(frozen=True, slots=True)
class ReplaySendSettings:
    """Settings for replay send."""

    connection_close: bool = False
    update_content_length: bool = True
    placeholders: list[ReplayPlaceholderInput] | None = None


@dataclass(frozen=True, slots=True)
class ReplayPlaceholderInput:
    """Placeholder input for replay send settings."""

    input_range: RangeInput
    output_range: RangeInput
    preprocessors: list[Any] | None = None  # ReplayPreprocessorInput from schema


@dataclass(frozen=True, slots=True)
class RangeInput:
    """Range (start, end) for placeholders."""

    start: int
    end: int


@dataclass(frozen=True, slots=True)
class ReplaySendResult:
    """Result of replay.send() after task finishes."""

    entry: ReplayEntry
    status: Literal["DONE", "CANCELLED", "ERROR"]
    error: dict[str, str] | None = None
