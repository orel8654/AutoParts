import logging
from aiogram import Bot, types, executor, Dispatcher
from config import TELEGRAM_TOKEN_BOT_GENERAL
import asyncio
import markups
from aiogram.types.message import ContentTypes
import db

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(token=TELEGRAM_TOKEN_BOT_GENERAL)
dp = Dispatcher(bot)

'''----------------------------Рабочая информация----------------------------'''
async def on_startup(_):
    print('Bot is online!')

def check_subscribe():
    pass

'''----------------------------Команды /----------------------------'''
@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markups.start_btn)

@dp.message_handler(commands=['help'])
async def command_help(message:types.Message):
    await bot.send_message(message.from_user.id, 'HELP')

'''----------------------------Обработчик кнопок----------------------------'''
@dp.message_handler()
async def echo_send(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Сделать расчет!':
            await bot.send_message(message.from_user.id, 'Считаем!')
        elif message.text == 'Оформить подписку!':
            await bot.send_message(message.from_user.id, 'Делаем подписку!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
