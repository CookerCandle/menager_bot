from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import Survey

from markups.inline import exness_profile_markup, admin_confirm_markup

from config import config as cfg


db = Database()
router = Router()


@router.message(Survey.expirience, F.text)
async def handler_experience(message: Message, state: FSMContext):
    await state.update_data(problems=message.text)
    await state.set_state(Survey.confirm)

    await message.answer("Guruxga qo'shilish uchun, biz hamkor bo'lgan brockerga, bizning havolamiz orqali ro'yxatdan o'tishingiz kerak.\n\n")
    await message.answer("<a href='https://one.exnesstrack.org/a/zmhzwlylc9'>EXNESS</a>", reply_markup=exness_profile_markup())


@router.message(Survey.expirience, F.voice)
async def handler_experience_voice(message: Message, state: FSMContext):
    await state.update_data(problems=message.message_id)
    await state.set_state(Survey.confirm)

    await message.answer("Guruxga qo'shilish uchun, biz hamkor bo'lgan brockerga, bizning havolamiz orqali ro'yxatdan o'tishingiz kerak.\n\n")
    await message.answer("<a href='https://one.exnesstrack.org/a/zmhzwlylc9'>EXNESS</a>", reply_markup=exness_profile_markup())


@router.callback_query(Survey.confirm, F.data.startswith("exness_profile_"))
async def handler_confirm(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("<a href='https://one.exnesstrack.org/a/zmhzwlylc9'>EXNESS</a>")

    exness_profile = callback.data.split("exness_profile_")[1]

    if exness_profile == "yes":
        await callback.message.answer_video(FSInputFile("sources/lesson.mp4"), caption="Shu videodagi ko'rsatmalarga amal qiling va screenshot yuboring.")
    elif exness_profile == "no":
        await callback.message.answer_video(FSInputFile("sources/lesson.mp4"), caption="Shu videodagi ko'rsatmalarga amal qiling va screenshot yuboring.")


@router.message(Survey.confirm, F.photo)
async def handler_confirm_image(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(confirm=message.message_id)
    data = await state.get_data()

    await message.answer("Ma'lumotlar Yubborildi, adminlar ko'rib chiqishadi va siz bilan bog'lanishdi.")

    if isinstance(data["problems"], str):
        await bot.copy_message(cfg.log_group, message.chat.id, data["confirm"], 
                               caption=f"User: {'@' + message.from_user.username if message.from_user.username else message.from_user.id}\n\nMuammolar:\n{data['problems']}\n\nTajriba:\n{data['experience']}", 
                               reply_markup=admin_confirm_markup(message.chat.id))
    else:
        reply = await bot.copy_message(cfg.log_group, message.chat.id, data["problems"])
        await bot.copy_message(cfg.log_group, message.chat.id, data["confirm"], 
                               caption=f"User: {'@' + message.from_user.username if message.from_user.username else message.from_user.id}\n\nTajriba:\n{data['experience']}", 
                               reply_markup=admin_confirm_markup(message.chat.id), 
                               reply_to_message_id=reply.message_id)
    
    await state.clear()