from aiogram import Bot

from config import config as cfg
from markups.reply import main_menu

async def create_link(user_id: int, bot: Bot):
    try:
        invite = await bot.create_chat_invite_link(
            chat_id=cfg.private_group,
            member_limit=1,
            name=f"Invite for {user_id}"
        )
        await bot.send_message(
            chat_id=int(user_id),
            text=f"Tabriklaymiz, siz guruhga qabul qilindingiz. Shu link orqali qo'shilsangiz bo'ladi: {invite.invite_link}",
            reply_markup=main_menu()
        )
    except Exception as e:
        await bot.send_message(
            chat_id=cfg.log_group,
            text=f"Foydalanuvchiga link yaratilmadi --{user_id}--: {e}"
        )