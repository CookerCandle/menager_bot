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
                InlineKeyboardButton(text="❌ Bu brokerda yangiman ❌", callback_data="exness_profile_no")
                
            ],
            [
                InlineKeyboardButton(text="✅ Bu brokerdan ro'yxatdan o'tganman ✅", callback_data="exness_profile_yes")
            ]
        ]
    )
    return exness_profile


def admin_confirm_markup(id):
    admin_confirm = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash ✅", callback_data=f"admin_confirm_{id}_yes"),
                InlineKeyboardButton(text="❌ habar yozish ❌", callback_data=f"admin_confirm_{id}_no")
            ]
        ]
    )
    return admin_confirm