from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import SendMessage

from markups.reply import admin_menu


router = Router()
db = Database()


@router.callback_query(SendMessage.check, F.data.startswith("ad_"))
async def send_ad_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    data = await state.get_data()
    lang = await db.get_lang(callback.from_user.id)
    users = await db.get_users() 
    for user in users:
        try:
            await callback.bot.copy_message(user[0], callback.from_user.id, data["ad"])
        except:
            pass
    await state.clear()
    await callback.message.answer("Реклама отправлена", lang)


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