import asyncio
import logging
import sys
from aiogram import F

from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
# from aiogram.utils.markdown import hbold
from fitnise_bot.button import started_handler, start1_handler,oy_handler,hafta_handler
# from fitnise_bot.inline_button import inline_number


TOKEN = '6631400339:AAGF3VX86JigeR8zYpbVyUUWROEkU8hA5Tw'
dp = Dispatcher()


@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer("photo handler successful ")
    await message.answer(f"{message.photo[0].file_id}")


# @dp.message(CommandStart())
# async def start_handler(message: Message):
#     image_url = 'AgACAgIAAxkBAAMCZXGeSsdYTVcVogABcRmYjZyTnx07AAIr0zEba-OQS-DL2PNyzPaQAQADAgADcwADMwQ'
#     await message.answer(f"""Assalomu alaykum !
# Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi""")
#     media = types.InputMediaPhoto(media=image_url)
#     await message.answer_media_group([media])
#     await message.answer(text="Hi", reply_markup= start_handler())

@dp.message(Command('start'))
async def start_handler(msg: Message) -> None:
    await msg.answer(text="Hi", reply_markup=started_handler())


@dp.message(lambda msg: msg.text == 'Filial 📍')
async def lacation_hander(msg: Message):
    await msg.answer_location(41.30465070299682, 69.25317846453066)

@dp.message(lambda msg: msg.text == 'Admin 👨🏻‍💻')
async def lacation_hander(msg: Message):
    await msg.answer(text="https://t.me/Absaitov_Dilshod" )


# """ ---------------------------------- start ---------------------------------------------- """


@dp.message(lambda msg: msg.text == 'Start ✅')
async def start_handler(msg: Message):
    await msg.answer(text="Quydagilardan birontasini tanlang 👇🏿", reply_markup=start1_handler())

# """ ---------------------------------- Woman ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Woman 🧍‍♀️')
async def start_handler(msg: Message):
    await msg.answer(text="Quydagilarni birontasini tanlang 👇🏿", reply_markup=oy_handler())



# """ ---------------------------------- 1-oy ---------------------------------------------- """

@dp.message(lambda msg: msg.text == '1-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())

# """ -------------------------------------------------------------------------------- """



@dp.message(lambda msg: msg.text == '2-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """


@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())



# """ -------------------------------------------------------------------------------- """

@dp.message(lambda msg: msg.text == '3-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())


# """ -------------------------------------------------------------------------------- """


@dp.message(lambda msg: msg.text == '4-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Quydagilarni birontasini tanlang 👇🏿", reply_markup=started_handler())





# """ ---------------------------------- Men 🧍‍♂️ ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Men 🧍‍♂️')
async def start_handler(msg: Message):
    await msg.answer(text="Quydagilarni birontasini tanlang 👇🏿", reply_markup=oy_handler())



# """ ---------------------------------- 1-oy ---------------------------------------------- """

@dp.message(lambda msg: msg.text == '1-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())

@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())

# """ -------------------------------------------------------------------------------- """



@dp.message(lambda msg: msg.text == '2-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """


@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())



# """ -------------------------------------------------------------------------------- """

@dp.message(lambda msg: msg.text == '3-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())


# """ -------------------------------------------------------------------------------- """


@dp.message(lambda msg: msg.text == '4-oy')
async def start_handler(msg: Message):
    await msg.answer(text="Hafta kunlaridan birontasini tanlang", reply_markup=hafta_handler())

# """ ---------------------------------- hafta_kunlari ---------------------------------------------- """

@dp.message(lambda msg: msg.text == 'Dushanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Seshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Chorshanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Juma')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == 'Shanba')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=hafta_handler())


@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Gazini bosing", reply_markup=start1_handler())

@dp.message(lambda msg: msg.text == '🔙 back')
async def start_handler(msg: Message):
    await msg.answer(text="Quydagilarni birontasini tanlang 👇🏿", reply_markup=started_handler())







# @dp.message(lambda msg: msg.text == 'Start ✅')
# async def start_handler(msg: Message):
#     await msg.answer(text="Hi", reply_markup=start1_handler())
#




async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
