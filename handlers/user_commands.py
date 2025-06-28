from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeAllPrivateChats
from aiogram.fsm.context import FSMContext

from config import config as cfg
from data.database import Database

from markups.reply import main_menu, remove_keyboard


db = Database()
router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.clear()

    commands = [BotCommand(command="start", description="start")]
    
    await bot.set_my_commands(commands, scope=BotCommandScopeAllPrivateChats())

    if not await db.user_exists(message.from_user.id):
        await db.add_user(message.from_user.id)
        await message.answer("Salom, botga xush kelibsiz!", reply_markup=main_menu())
    else:
        await message.answer("Qanday yordam bera olaman!", reply_markup=main_menu())