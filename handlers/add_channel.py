from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import ChannelAdd

from markups.reply import admin_menu

router = Router()
db = Database()


@router.message(ChannelAdd.name)
async def sponsor_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ChannelAdd.link)
    await message.answer("Kanal linkini yuboring",)


@router.message(ChannelAdd.link)
async def sponsor_link(message: Message, state: FSMContext):
    await state.update_data(link=message.text) 
    await state.set_state(ChannelAdd.member)
    await message.answer("Kanal IDsini yuboring\n\n(<i>ID -100 dan boshlanadi</i>)")


@router.message(ChannelAdd.member, F.text.lstrip('-').isdigit(), F.text.startswith('-100'))
async def sponsor_member(message: Message, state: FSMContext):
    await state.update_data(member=int(message.text))
    data = await state.get_data()
    await state.clear()
    await db.add_channel(data["name"], data["link"], data["member"])

    await message.answer("Kanal qo'shildi!")
    await message.answer("<b>Botni kanalga admin qilib qo'shing</b>", reply_markup=admin_menu())
    

@router.message(ChannelAdd.member)
async def sponsor_member_incorrect(message: Message, state: FSMContext):
    await message.answer("Sonli ID yuboring!\n\n(<i>ID -100 dan boshlanadi</i>)")