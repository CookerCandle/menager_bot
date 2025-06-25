from aiogram.fsm.state import StatesGroup, State


class Survey(StatesGroup):
    expirience = State()
    problems = State()
    