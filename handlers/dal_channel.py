from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from data.database import Database
from utils.states import ChannelDelete

from markups.reply import admin_menu

router = Router()
db = Database() 


@router.message(ChannelDelete.name)
async def del_channel(message: Message, state: FSMContext):
    channels = await db.get_channels()
    channel = [channel[0] for channel in channels]
    if message.text in channel:
        await db.delete_channel(message.text)
        await message.answer("Kanal o'chirildi", reply_markup=admin_menu())
        await state.clear()
    else:
        await message.answer("Bunday kanal mavjud emas\n Kanal nomini tekshirib qaytadan kiriting")
    