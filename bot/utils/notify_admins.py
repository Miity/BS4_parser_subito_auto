import logging
from aiogram import Dispatcher
from bot.loader import bot
from bot.data.config import admins_id

logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


async def on_start_notify(dp:Dispatcher):
    for admin in admins_id:
        try:
            await dp.bot.send_message(chat_id=admin, text='бот запущен')
        except Exception as e:
            print('error in "on_start_notify" \n', e)
            

from app.models import Car
async def send_info(dp:Dispatcher, car:Car):
    for admin in admins_id:
        try:
            await dp.bot.send_message(chat_id=admin, text=car.print_info())
        except Exception as e:
            print('error in "on_start_notify" \n', e)