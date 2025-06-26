from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import config as cfg
from data.database import Database

from markups.reply import admin_menu


db = Database()
router = Router()


@router.message(Command("admin"), F.from_user.id.in_(cfg.admins))
async def admin_start(message: Message):
    await message.answer("Admin panelga xush kelibs!", reply_markup=admin_menu())