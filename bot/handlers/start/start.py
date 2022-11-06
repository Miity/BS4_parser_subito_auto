from aiogram import types
from bot.loader import dp
import time


@dp.message_handler(commands=['start'])
async def left_to_wait(message: types.Message):
    from app import main 

    for n in range(365, 0, -1):
        time.sleep(86400)
        await message.answer(text=f'Осталось {n} дней')
