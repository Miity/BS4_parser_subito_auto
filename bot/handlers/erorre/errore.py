from aiogram import types
from loader import dp


@dp.message_handler()
async def erorre(message: types.Message):
    text = "I don't know what to do"
    await message.answer(text = text)
    print(message.content_type)
