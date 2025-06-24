from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def main_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="knopka1"),
                KeyboardButton(text="knopka1")
            ],
            [
                KeyboardButton(text="knopka2"),
                KeyboardButton(text="knopka3")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Berilgan tugmalardan bittasini tanlang",
        one_time_keyboard=True,
        selective=True
    )
    return menu


def remove_keyboard():
    return ReplyKeyboardRemove(
        remove_keyboard=True,
        selective=True
    )

