
from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from aiogram.enums.chat_action import ChatAction
from aiogram.fsm.context import FSMContext

from markups.reply import main_menu

from data.database import Database
from midlewares.check_sub import check_user_subscription
from markups.inline import get_channels_markup

from utils.states import Survey

from config import config as cfg
from data.create_link import create_link

router = Router()
db = Database()


@router.callback_query(F.data == "check_subscription")
async def recheck_subscription(callback: CallbackQuery):
    not_subscribed = await check_user_subscription(callback.bot, callback.from_user.id)

    if not_subscribed:
        await callback.message.edit_text(
            "Hali ham barcha kanallarga obuna bo'lmagansiz.",
            reply_markup=get_channels_markup(not_subscribed)
        )
    else:
        await callback.message.edit_text("✅ Obuna tasdiqlandi!")
        await callback.message.answer("Botdan foydalanishingiz mumkin.", reply_markup=main_menu())
        # тут можно вызвать следующее действие (например, отправить меню или т.д.)


@router.callback_query(F.data.startswith("lesson_"))
async def handle_lesson_selection(callback: CallbackQuery):
    lesson_type = callback.data.split("_")[1]
    await callback.message.delete()
    
    await callback.answer(f"Siz {lesson_type} darslikni tanladingiz.")
    if lesson_type == "online":
        await callback.message.answer("Online darsliklar mavjud. Batafsil ma'lumot admindan olsangiz bo'ladi\n@sbgroup0712", reply_markup=main_menu())
    elif lesson_type == "offline":
        await callback.message.answer("🔧 Offline darsliklar bo'limi hali tayyorlanmoqda", reply_markup=main_menu())


@router.callback_query(F.data.startswith("experience_"))
async def handle_experience_selection(callback: CallbackQuery, state: FSMContext):
    experience_level = callback.data.split("experience_")[1]
    await callback.message.delete()
    
    await state.set_state(Survey.expirience)
    await state.update_data(experience=experience_level)
    await callback.message.answer("Savdo sistemasida qanday muammolaringiz bor?\nShu bo'yicha qisqacha malumot bering.\n\n<i>Text yoki golosovoy tashlang</i>",)


@router.callback_query(F.data.startswith("admin_confirm_"))
async def handle_admin_confirmation(callback: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = callback.data.split("admin_confirm_")[1].split("_")[0]

    await callback.message.edit_reply_markup(reply_markup=None)
    
    if callback.data.endswith("yes"):
        invite = await create_link(user_id, bot)
        if  invite is None:
            return
        await bot.send_message(
            chat_id=int(user_id),
            text=f"Tabriklaymiz, siz guruhga qabul qilindingiz. Shu link orqali qo'shilsangiz bo'ladi: {invite.invite_link}",
            reply_markup=main_menu()
        )
    elif callback.data.endswith("no"):
        await bot.send_message(
            chat_id=int(user_id),
            text="Sizga guruhga qo'shilish uchun admin tomonidan ruxsat berilmadi. @sbgroup0712 ga yozing.",
            reply_markup=main_menu()
        )