import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import emex_parser_most_bigger_cost
import treat_send
from config import TELEGRAM_TOKEN_BOT_GENERAL, LIST_CAR_MARKS
import asyncio
import markups
from aiogram.types.message import ContentTypes
import db
import recaptcha_treat

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(token=TELEGRAM_TOKEN_BOT_GENERAL)
dp = Dispatcher(bot, storage=MemoryStorage())

'''----------------------------Машина состояния----------------------------'''
class Form(StatesGroup):
    general = State()
    category = State()

class Big(StatesGroup):
    car_mark = State()

class RCA(StatesGroup):
    car_mark = State()
    part_number = State()

'''----------------------------Рабочая информация----------------------------'''
async def on_startup(_):
    print('Bot is online!')



'''----------------------------Команды /----------------------------'''
@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Привет, {0.first_name}! Я помогу тебе получить информацию о ценах запчастей!\n/help - инструкция по использованию бота!\n/info - дополнительная информация о проекте!\n/supmod - каталог моделей'.format(message.from_user), reply_markup=markups.start_btn)

@dp.message_handler(commands=['help'])
async def command_help(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_HELP}')

@dp.message_handler(commands=['info'])
async def command_info(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_INFO}')

@dp.message_handler(commands=['supmod'])
async def command_info(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_SUPMOD}')



'''----------------------------Обработчик кнопок----------------------------'''
@dp.message_handler()
async def echo_send(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Выбор функций':
            if db.user_id_check(message.from_user.id) == False:
                await bot.send_message(message.from_user.id, 'Вы новый пользователь! Хотите оформить подписку или вернутся?', reply_markup=markups.subs_btn)
            else:
                if db.check_days_subs(message.from_user.id) == False:
                    await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.continue_subs_btn)
                else:
                    await bot.send_message(message.from_user.id, 'Аутентификация пройдена!', reply_markup=markups.activate_program)
        elif message.text == 'Оформить подписку!':
            #-----------------------------------------------ЕСЛИ ТРАНЗАКЦИЯ УСПЕШНА
            if db.user_add(message.from_user.id) == True:
                await bot.send_message(message.from_user.id, 'Подписка успешна добавлена!', reply_markup=markups.start_btn)
            else:
                await bot.send_message(message.from_user.id, 'Произошла ошибка! Напишите пожалуйста, администратору для решения проблемы!')
        elif message.text == 'Продлить подписку!':
            #-----------------------------------------------ЕСЛИ ТРАНЗАКЦИЯ УСПЕШНА
            if db.user_update(message.from_user.id) == True:
                await bot.send_message(message.from_user.id, 'Ваша подписка успешна продлена!', reply_markup=markups.start_btn)
            else:
                await bot.send_message(message.from_user.id, 'Произошла ошибка! Напишите пожалуйста, администратору для решения проблемы!')
        elif message.text == 'Главная':
            await bot.send_message(message.from_user.id, 'Какие действия сделать?', reply_markup=markups.activate_program)
        elif message.text == 'Выборка по модели':
            await bot.send_message(message.from_user.id, 'Введите марку, модель, год начала производства автомобиля через запятую, например (toyota, allex, 2001)', reply_markup=markups.input_btn)
            await Form.general.set()
        elif message.text == 'Выборка по цене':
            await bot.send_message(message.from_user.id, 'Выберите марку автомобиля, чтобы вывести максимальную цену запчасти!', reply_markup=markups.btn_marks_category)
            await Big.car_mark.set()
        elif message.text == 'Расчет РСА':
            await bot.send_message(message.from_user.id, 'Введите марку авто и номер детали через запятую, например (toyota, 52119-13340-A0). Расчет может занять до 1 минуты!')
            await RCA.car_mark.set()

'''----------------------------Обработчик машины состояния для Расчета по РСА----------------------------'''
@dp.message_handler(state=RCA.car_mark)
async def RCA_processing(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text != 'Главная':
            proxy['car_mark'] = message.text
            ret_message = recaptcha_treat.input_main(proxy)
            await bot.send_message(message.from_user.id, ret_message)
        else:
            await state.finish()

'''----------------------------Обработчик машины состояния для Выборка по цене----------------------------'''
@dp.message_handler(state=Big.car_mark)
async def processing_car(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text != 'Главная':
            proxy['car_mark'] = message.text
            ret_message = emex_parser_most_bigger_cost.input_main(proxy)
            await bot.send_message(message.from_user.id, ret_message)
        else:
            await state.finish()

'''----------------------------Обработчик машины состояния для Выборка по модели----------------------------'''
@dp.message_handler(state=Form.general)
async def processing_text(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text != 'Главная':
            proxy['general'] = message.text
            await Form.next()
            await bot.send_message(message.from_user.id, 'Теперь выберите категорию, чтобы сделать расчет!', reply_markup=markups.category_btn)
        else:
            await state.finish()

@dp.message_handler(state=Form.category)
async def processing_text_category(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text == 'Капот':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Крыло':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Фара':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Стекла':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Бампер':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Багажник':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Двери':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'SRS':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Двигатель':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Все позиции':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                await bot.send_message(message.from_user.id, message_ret)
        elif message.text == 'Главная':
            await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
