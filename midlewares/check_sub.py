from typing import Callable, Awaitable,Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from data.database import Database
from markups.inline import get_channels_markup


db = Database()


class CheckSubscription(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        channels = await db.get_chanels()

        not_subscribed = []
        if channels:
            for name, link, member in channels:
                try:
                    chat_member = await event.bot.get_chat_member(chat_id=member, user_id=event.from_user.id)
                    if chat_member.status not in ['member', 'administrator', 'creator']:
                        not_subscribed.append((name, link))
                except:
                    print(f"Error checking subscription for {name} ({link})")
        
        if not_subscribed:
            await event.answer("Botdan foydalanish uchunkanallarga obuna bo'lishingiz kerak", reply_markup=get_channels_markup(not_subscribed))
            return
        return await handler(event, data)