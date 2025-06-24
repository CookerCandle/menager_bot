from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.fsm.context import FSMContext

from config import Config as cfg
from data.database import Database

from markups.reply import main_menu, remove_keyboard


db = Database()
router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext) -> None:
    await state.clear()

    if not await db.user_exists(message.from_user.id):
        await db.add_user(message.from_user.id)
        await message.answer("Salom, botga xush kelibsiz!", reply_markup=main_menu())
    else:
        await message.answer("Qanday yordam bera olaman!", reply_markup=main_menu())