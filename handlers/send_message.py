from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import SendMessage

from markups.reply import admin_menu


router = Router()
db = Database()


@router.message(SendMessage.message)
async def send_ad(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(message=message.message_id)
    data = await state.get_data()
    
    users = await db.get_users()
    counter = 0
    for user in users:
        try:
            await bot.copy_message(user[0], message.chat.id, data["message"])
            counter += 1
        except:
            pass

    await message.answer(f"Hat yuborildi:\n{counter} foydalanuvchilar qabul qilishdi", reply_markup=admin_menu())
    await state.clear()