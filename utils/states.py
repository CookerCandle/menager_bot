from aiogram.fsm.state import StatesGroup, State


class Survey(StatesGroup):
    expirience = State()
    problems = State()
    confirm = State()
    
class ChannelAdd(StatesGroup):
    name = State()
    link = State()
    member = State()

class ChannelDelete(StatesGroup):
    name = State()

class SendMessage(StatesGroup):
    message = State()