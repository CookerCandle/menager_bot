from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.fsm.context import FSMContext

from config import config as cfg


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    ...