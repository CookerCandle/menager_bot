from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import Survey

from markups.inline import exness_profile_markup


db = Database()
router = Router()


@router.message(Survey.expirience, F.text)
async def handle_experience(message: Message, state: FSMContext):
    await state.update_data(problems=message.text)

    data = await state.get_data()
    await message.answer("Guruxga qo'shilish uchun, biz hamkor brockerimizga bizning havolamiz orqali ro'yxatdan o'tishingiz kerak.\n\n")
    await message.answer("<a href='https://one.exnesstrack.org/a/zmhzwlylc9'>EXNESS</a>", reply_markup=exness_profile_markup())
    await state.clear()
    