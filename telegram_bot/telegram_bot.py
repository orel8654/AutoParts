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
            if db.user_id_check(message.from_user.id) == False:
                await bot.send_message(message.from_user.id, 'Вы новый пользователь! Хотите оформить подписку или вернутся?', reply_markup=markups.subs_btn)
            else:
                if db.check_days_subs(message.from_user.id) == False:
                    await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.continue_subs_btn)
                else:
                    await bot.send_message(message.from_user.id, 'Допуск получен!')
        elif message.text == 'Оформить подписку!':
            #-----------------------------------------------ЗДЕСЬ МЕТОД ДОБАВЛЕНИЯ ПОДПИСКИ
            #-----------------------------------------------ЕСЛИ ТРАНЗАКЦИЯ УСПЕШНА
            if db.user_add(message.from_user.id) == True:
                await bot.send_message(message.from_user.id, 'Подписка успешна добавлена!', reply_markup=markups.start_btn)
            else:
                await bot.send_message(message.from_user.id, 'Произошла ошибка! Напишите пожалуйста, администратору для решения проблемы!')
        elif message.text == 'Продлить подписку!':
            #-----------------------------------------------ЗДЕСЬ МЕТОД ПРОДЛЕНИЯ ПОДПИСКИ
            #-----------------------------------------------ЕСЛИ ТРАНЗАКЦИЯ УСПЕШНА
            if db.user_update(message.from_user.id) == True:
                await bot.send_message(message.from_user.id, 'Ваша подписка успешна продлена!', reply_markup=markups.start_btn)
            else:
                await bot.send_message(message.from_user.id, 'Произошла ошибка! Напишите пожалуйста, администратору для решения проблемы!')
        elif message.text == 'Главная':
            await bot.send_message(message.from_user.id, 'Какие действия сделать?', reply_markup=markups.start_btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
