from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def started_handler():
    n1 = KeyboardButton(text="Filial 📍")
    n2 = KeyboardButton(text="Start ✅")
    n3 = KeyboardButton(text="Admin 👨🏻‍💻")

    design = [
        [n1, n2],
        [n3]
    ]

    tkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return tkm

def start1_handler():
    r1 = KeyboardButton(text="Woman 🧍‍♀️")
    r2 = KeyboardButton(text="Men 🧍‍♂️")
    r3 = KeyboardButton(text="🔙 back")
    design = [
        [r1 , r2],
        [r3]
    ]
    stm = ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True, one_time_keyboard=True)
    return stm


def oy_handler():
    n1 = KeyboardButton(text="1-oy")
    n2 = KeyboardButton(text="2-oy")
    n3 = KeyboardButton(text="3-oy")
    n4 = KeyboardButton(text="4-oy")
    n5 = KeyboardButton(text="🔙 back")

    design1 = [
        [n1 , n2],
        [n3, n4],
        [n5]

    ]

    tkm1 = ReplyKeyboardMarkup(keyboard=design1, resize_keyboard=True, one_time_keyboard=True)
    return tkm1

def hafta_handler():
    t1 = KeyboardButton(text="Dushanba")
    t2 = KeyboardButton(text="Seshanba")
    t3 = KeyboardButton(text="Chorshanba")
    t4 = KeyboardButton(text="Payshanba")
    t5 = KeyboardButton(text="Juma")
    t6 = KeyboardButton(text="Shanba")
    t7 = KeyboardButton(text="🔙 back")

    design1 = [
        [t1 , t2 , t3],
        [t4, t5 , t6],
        [t7]

    ]

    tkm1 = ReplyKeyboardMarkup(keyboard=design1, resize_keyboard=True, one_time_keyboard=True)
    return tkm1