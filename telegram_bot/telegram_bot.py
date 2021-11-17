import logging
from aiogram import Bot, types, executor, Dispatcher
from config import TELEGRAM_TOKEN_BOT_GENERAL
import asyncio
from aiogram.types.message import ContentTypes

logging.basicConfig(level=logging.DEBUG)
loop = asyncio.get_event_loop()
bot = Bot(token=TELEGRAM_TOKEN_BOT_GENERAL)
dp = Dispatcher(bot)

'''----------------------------Рабочая информация----------------------------'''
async def on_startup(_):
    print('Bot is online!')

'''----------------------------Команды----------------------------'''
@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, 'Привет, {0.first_name}'.format(message.from_user))

@dp.message_handler(commands=['help'])
async def command_help(message:types.Message):
    await bot.send_message(message.from_user.id, 'HELP')

'''----------------------------URL----------------------------'''
@dp.message_handler(commands=['count'])
async def echo_send(message: types.Message):
    await message.answer(text='Собираем информацию! Процесс может занять время, пожалуйста подождите!')
    try:
        # parse(message.text)
        # await message.answer_document(open('cars.csv', 'rb'))
        await message.answer(text='Что то делаю!')
    except:
        await message.answer(text='Oшибка на сервере сайта, либо вы неправильно ввели URL!\nПовторите попытку!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
