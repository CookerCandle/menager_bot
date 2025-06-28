from aiogram import Bot

from config import config as cfg


async def create_link(user_id: int, bot: Bot):
    try:
        invite = await bot.create_chat_invite_link(
            chat_id=cfg.private_group,
            member_limit=1,
            name=f"Invite for {user_id}"
        )
        return invite
    except Exception as e:
        await bot.send_message(
            chat_id=cfg.log_group,
            text=f"Foydalanuvchiga link yaratilmadi --{user_id}--: {e}"
        )
        return None