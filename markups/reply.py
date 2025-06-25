from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def main_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💻 SB Community"),
                KeyboardButton(text="🎥 Instagram")
            ],
            [
                KeyboardButton(text="📚 Darsliklar"),       
                KeyboardButton(text="☎️ Biz bilan aloqa") # https://www.instagram.com/sbtradinguz?igsh=ZHdya3RxajBxa3E4
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Berilgan tugmalardan bittasini tanlang",
        one_time_keyboard=True,
        selective=True
    )
    return menu


def admin_request():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📊 Admin"),
                KeyboardButton(text="📈 SB bilan aloqa")
            ],
            [
                KeyboardButton(text="🔙 Orqaga")
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

