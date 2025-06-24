from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_channels_markup(data):
    buttons = [
        [InlineKeyboardButton(text=f"{index + 1}) {name}", url=link)]
        for index, (name, link) in enumerate(data)
    ]
    buttons.append([InlineKeyboardButton(text="Obuna bo'ldim ✅", callback_data="check_subscription")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
