"""Optional/nullable utility helpers."""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")

type Maybe[T] = T | None


def is_absent(argument: T | None) -> bool:
    return argument is None


def is_present(argument: T | None) -> bool:
    return argument is not None
