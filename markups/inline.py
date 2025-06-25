from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_channels_markup(data):
    buttons = [
        [InlineKeyboardButton(text=f"{index + 1}) {name}", url=link)]
        for index, (name, link) in enumerate(data)
    ]
    buttons.append([InlineKeyboardButton(text="Obuna bo'ldim ✅", callback_data="check_subscription")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def lessons_markup():
    lessons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌐 Online", callback_data="lesson_online"),
                InlineKeyboardButton(text="🧑🏻‍💻 Offline", callback_data="lesson_offline"),
            ]
        ]
    )
    return lessons


def experience_markup():
    experience = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⌛️ 0 < 6 oy", callback_data="experience_6-oygacha"),
            ],
            [
                InlineKeyboardButton(text="⌛️ 6 oy > 12 oy", callback_data="experience_6-oydan-12-oygacha"),
            ],
            [
                InlineKeyboardButton(text="⌛️ 1 yil > 3 yil", callback_data="experience_1-yildan-3-yilgacha"),
            ]
        ]
    )
    return experience


def exness_profile_markup():
    exness_profile = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Bu brockerdan ro'yxatdan o'tganman ✅", callback_data="exness_profile_yes")
            ],
            [
                InlineKeyboardButton(text="❌ Bu brockerdan yangiman ❌", callback_data="exness_profile_no")
            ]
        ]
    )
    return exness_profile