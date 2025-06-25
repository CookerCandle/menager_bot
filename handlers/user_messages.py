from aiogram import F, Router, Bot
from aiogram.types import Message, FSInputFile 

from data.database import Database

from markups.reply import remove_keyboard as rmk
from markups.reply import main_menu, admin_request
from markups.inline import lessons_markup, experience_markup

db = Database()
router = Router()


@router.message(F.text.in_(["💻 SB Community", "🎥 Instagram", "📚 Darsliklar", "☎️ Biz bilan aloqa", "🔙 Orqaga"]))
async def handle_button_click(message: Message, bot: Bot):
    
    if message.text == "💻 SB Community":
        await message.answer("SB communityga ulanish uchun so'rovnomadan o'ting:", reply_markup=rmk())
        await message.answer("Trading soxasida qancha tajribaga egasiz?", reply_markup=experience_markup())
    elif message.text == "🎥 Instagram":
        await message.answer_photo(FSInputFile("sources/instagram.jpg"), caption="<a href='https://www.instagram.com/sbtradinguz?igsh=ZHdya3RxajBxa3E4'>⭐️Bizning Instagram⭐️</a>", reply_markup=main_menu())
    elif message.text == "📚 Darsliklar":
        await message.answer("Darslik turini tanlang:", reply_markup=lessons_markup())
    elif message.text == "☎️ Biz bilan aloqa":
        await message.answer("Agar biron-bir savol yoki taklif bo'lsa, bizga aloqaga chiqing", reply_markup=admin_request())

    if message.text == "🔙 Orqaga":
        await message.answer("Bosh sahifa", reply_markup=main_menu())


@router.message(F.text.in_(["📊 Admin", "📈 SB bilan aloqa"]))
async def handle_admin_request(message: Message, bot: Bot):
    if message.text == "📊 Admin":
        await message.answer("📝 Admin profili --> @SbGroup0712", reply_markup=main_menu())
    elif message.text == "📈 SB bilan aloqa":
        await message.answer("+99877-***-**-**", reply_markup=rmk())


@router.message()
async def echo(message: Message):
    await message.answer("Sizni chunmadim")