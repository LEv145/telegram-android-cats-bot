from __future__ import annotations

import typing as t

from pydantic import (
    BaseModel,
    BaseSettings,
)


class BotModel(BaseModel):
    token: str


class LoggingModel(BaseModel):
    level: str | None
    format: str | None


class Settings(BaseSettings):
    bot: BotModel
    log: LoggingModel | None

    class Config():
        env_prefix = "TACB__"
        env_nested_delimiter = "__"
