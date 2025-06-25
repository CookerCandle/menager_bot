import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import user_commands, user_messages
from callbacks import user_call

from midlewares.check_sub import CheckSubscription

from config import config as cfg
from data.database import Database


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=cfg.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    db = Database()

    dp.message.middleware(CheckSubscription())

    dp.include_routers(
        user_commands.router,
        user_call.router,
        user_messages.router,
    )

    await db.initialize()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())