from typing import Callable, Awaitable,Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from data.database import Database
from markups.inline import get_channels_markup


db = Database()


# check_sub.py
async def check_user_subscription(bot, user_id):
    channels = await db.get_chanels()
    not_subscribed = []

    if channels:
        for name, link, member in channels:
            try:
                chat_member = await bot.get_chat_member(chat_id=member, user_id=user_id)
                if chat_member.status not in ['member', 'administrator', 'creator']:
                    not_subscribed.append((name, link))
            except Exception as e:
                print(f"Error checking subscription for {name} ({link}): {e}")

    return not_subscribed



from .check_sub import check_user_subscription

class CheckSubscription(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        not_subscribed = await check_user_subscription(event.bot, event.from_user.id)

        if not_subscribed:
            await event.answer(
                "Botdan foydalanish uchun kanallarga obuna bo'lishingiz kerak:",
                reply_markup=get_channels_markup(not_subscribed)
            )
            return

        return await handler(event, data)
