from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

def inline_number():
    btn1 = InlineKeyboardButton(text=' ', url='https://t.me/Absaitov_Dilshod')
    desing = [
        [btn1]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=desing)
    return ikm




