from aiogram import F, Router, Bot
from aiogram.types import Message

from data.database import Database
from markups.reply import remove_keyboard as rmk

db = Database()
router = Router()


@router.message(F.text.in_(["knopka1", "knopka2", "knopka3", "knopka4"]))
async def handle_button_click(message: Message, bot: Bot):
    
    if message.text == "knopka1":
        await message.answer("Siz knopka1 ni tanladingiz", reply_markup=rmk())
    elif message.text == "knopka2":
        await message.answer("Siz knopka2 ni tanladingiz", reply_markup=rmk())
    elif message.text == "knopka3":
        await message.answer("Siz knopka3 ni tanladingiz", reply_markup=rmk())
    elif message.text == "knopka4":
        await message.answer("Siz knopka4 ni tanladingiz", reply_markup=rmk())


@router.message()
async def echo(message: Message):
    await message.answer("Sizni chunmadim")