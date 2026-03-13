"""Logger interface and console implementation."""

from __future__ import annotations

import logging
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Logger(Protocol):
    def debug(self, message: str, *args: Any) -> None: ...
    def info(self, message: str, *args: Any) -> None: ...
    def warn(self, message: str, *args: Any) -> None: ...
    def error(self, message: str, *args: Any) -> None: ...


class ConsoleLogger:
    def __init__(self) -> None:
        self._logger = logging.getLogger("caido")

    def debug(self, message: str, *args: Any) -> None:
        self._logger.debug("[caido] %s", message, *args)

    def info(self, message: str, *args: Any) -> None:
        self._logger.info("[caido] %s", message, *args)

    def warn(self, message: str, *args: Any) -> None:
        self._logger.warning("[caido] %s", message, *args)

    def error(self, message: str, *args: Any) -> None:
        self._logger.error("[caido] %s", message, *args)
