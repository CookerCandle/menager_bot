
from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from aiogram.enums.chat_action import ChatAction

from data.database import Database
from midlewares.check_sub import check_user_subscription
from markups.inline import get_channels_markup


router = Router()
db = Database()


@router.callback_query(F.data == "check_subscription")
async def recheck_subscription(callback: CallbackQuery):
    not_subscribed = await check_user_subscription(callback.bot, callback.from_user.id)

    if not_subscribed:
        await callback.message.edit_text(
            "Hali ham barcha kanallarga obuna bo'lmagansiz.",
            reply_markup=get_channels_markup(not_subscribed)
        )
    else:
        await callback.message.edit_text("✅ Obuna tasdiqlandi! Botdan foydalanishingiz mumkin.")
        # тут можно вызвать следующее действие (например, отправить меню или т.д.)
