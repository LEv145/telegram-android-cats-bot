from __future__ import annotations

import typing as t

from aiogram import (
    Bot,
    Dispatcher,
)

from telegram_android_cats_bot.app.setups import setup_logging
from telegram_android_cats_bot.config import Settings


settings = Settings()  # type: ignore
setup_logging(settings)
dp = Dispatcher()


def main() -> None:
    bot = Bot(token=settings.bot.token)
    context: dict[str, t.Any] = {}
    dp.run_polling(bot, context=context)


if __name__ == "__main__":
    main()
