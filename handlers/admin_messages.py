from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import ChannelAdd, ChannelDelete


from config import config as cfg
from markups.reply import remove_keyboard as rmk
from markups.reply import admin_menu


router = Router()
db = Database()


@router.message(F.text.in_(["Kanal qo'shish", "Kanalni o'chirish", "Kanallar ro'yxatini ko'rish"]), F.from_user.id.in_(cfg.admins))
async def admin_messages(message: Message, state: FSMContext):
    await state.clear()

    if message.text == "Kanal qo'shish":
        await state.set_state(ChannelAdd.name)
        await message.answer("Kanal nomini kiriting:", reply_markup=rmk())
    elif message.text == "Kanalni o'chirish":
        await state.set_state(ChannelDelete.name)
        channels = await db.get_channels() 
        if not channels:
            await message.answer("Kanallar mavjud emas!", reply_markup=admin_menu())
            await state.clear()
            return
        formated_channels = "\n".join(f"{index + 1}) {channel[0]} {channel[1]}" for index, channel in enumerate(channels))
        await message.answer(f"O'chirmoqchi bo'lgan kanalingizni tanlang:\n{formated_channels}")
    elif message.text == "Kanallar ro'yxatini ko'rish":
        channels = await db.get_channels()
        if channels:
            formated_channels = "\n".join(f"{index + 1}) {channel[0]} {channel[1]}" for index, channel in enumerate(channels))
            await message.answer(f"Kanallar ro'yxati:\n{formated_channels}", reply_markup=admin_menu())
        else:
            await message.answer("Kanallar mavjud emas!", reply_markup=admin_menu())  