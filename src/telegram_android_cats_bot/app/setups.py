from __future__ import annotations

import typing as t

import colorlog
from pymaybe import maybe

from telegram_android_cats_bot.config import Settings


def setup_logging(settings: Settings) -> None:
    logger_config: dict[str, t.Any] = {}

    if maybe(settings).log.level:
        logger_config["level"] = settings.log.level  # type: ignore
    if maybe(settings).log.format:
        logger_config["format"] = settings.log.format  # type: ignore

    colorlog.basicConfig(**logger_config)
