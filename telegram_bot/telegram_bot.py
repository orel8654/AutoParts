import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import emex_parser_most_bigger_cost
import report_file_rsa_by_multiproc
import treat_send
import write_pdf
import z_sort_write
from config import TELEGRAM_TOKEN_BOT_GENERAL, QIWI_SECRET_KEY
import asyncio
import markups
from aiogram.types.message import ContentTypes
import db
import recaptcha_treat
import debug.write_function as write
from pyqiwip2p import QiwiP2P
import random
from concurrent.futures.thread import ThreadPoolExecutor


logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(token=TELEGRAM_TOKEN_BOT_GENERAL)
dp = Dispatcher(bot, storage=MemoryStorage())
p2p = QiwiP2P(auth_key=QIWI_SECRET_KEY, default_amount=345)
sem = asyncio.Semaphore(25)
# executor = ThreadPoolExecutor(5)

'''----------------------------Машина состояния----------------------------'''
class Form(StatesGroup):
    general = State()
    category = State()

class Big(StatesGroup):
    car_mark = State()

class RCA(StatesGroup):
    car_mark = State()
    part_number = State()

class Pay(StatesGroup):
    data = State()

class Report(StatesGroup):
    vin = State()
    data = State()
    mark = State()

class Executor:
    """In most cases, you can just use the 'execute' instance as a
    function, i.e. y = await execute(f, a, b, k=c) => run f(a, b, k=c) in
    the executor, assign result to y. The defaults can be changed, though,
    with your own instantiation of Executor, i.e. execute =
    Executor(nthreads=4)"""
    def __init__(self, loop=loop, nthreads=1):
        from concurrent.futures import ThreadPoolExecutor
        self._ex = ThreadPoolExecutor(nthreads)
        self._loop = loop
    def __call__(self, f, *args, **kw):
        from functools import partial
        return self._loop.run_in_executor(self._ex, partial(f, *args, **kw))
# execute = Executor()

'''----------------------------Рабочая информация----------------------------'''
async def on_startup(_):
    print('Bot is online!')

async def check_pay(bill):
    check = p2p.check(bill_id=bill.bill_id).status
    return check

'''----------------------------Команды /----------------------------'''
@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Привет, {0.first_name}!\n\nБот предоставляет актуальные цены на запчасти из открытых источников AMAYAMA, EMEX и РСА\n\n/help - инструкция по использованию бота!\n/info - дополнительная информация!\n/supmod - каталог моделей!\n/pay - информация об оплате!'.format(message.from_user), reply_markup=markups.start_btn)

@dp.message_handler(commands=['help'])
async def command_help(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_HELP}')

@dp.message_handler(commands=['info'])
async def command_info(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_INFO}')

@dp.message_handler(commands=['supmod'])
async def command_info(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_SUPMOD}')

@dp.message_handler(commands=['pay'])
async def command_pay(message:types.Message):
    await bot.send_message(message.from_user.id, f'{markups.CMD_PAY}')

'''----------------------------Для DEBUG, тесты, проверки----------------------------'''
@dp.message_handler(commands=['admintest'])
async def command_admin(message:types.Message):
    await bot.send_message(message.from_user.id, 'Метод для администратора! Нажмите кнопку!', reply_markup=markups.btn_admin_admin)


'''----------------------------Обработчик кнопок----------------------------'''
@dp.message_handler()
async def echo_send(message: types.Message):
    if message.chat.type == 'private':

        if message.text == 'Выбор функций':
            if db.user_id_check(message.from_user.id) == False:
                await bot.send_message(message.from_user.id, 'Вы новый пользователь! Оформите подписку!', reply_markup=markups.subs_btn)
            else:
                if db.check_days_subs(message.from_user.id) == False:
                    await bot.send_message(message.from_user.id, 'У вас закончилась подписка! продлите подписку!', reply_markup=markups.continue_subs_btn)
                else:
                    await bot.send_message(message.from_user.id, 'Аутентификация пройдена!', reply_markup=markups.activate_program)


        elif message.text == 'Оформить подписку':
            if message.chat.type == 'private':
                new_bill = p2p.bill(bill_id=message.from_user.id + random.randint(1000, 9999), lifetime=2, comment='APT')
                await bot.send_message(message.from_user.id, f'Стоимость подписки 345 рублей!\nВаша ссылка на оплату:\n{new_bill.pay_url}\n\nСсылка активна 2 минуты!')
                await asyncio.sleep(120)
                check = await check_pay(new_bill)
                if check != 'WAITING':
                    if db.user_add(message.from_user.id) == True:
                        await bot.send_message(message.from_user.id, 'Подписка успешна оформлена!', reply_markup=markups.start_btn)
                    else:
                        await bot.send_message(message.from_user.id, 'Произошла ошибка! Напишите пожалуйста, администратору для решения проблемы!')
                else:
                    await bot.send_message(message.from_user.id, 'Ваш счет оплаты закрыт! Повторите попытку!')
                    p2p.reject(bill_id=new_bill.bill_id)


        elif message.text == 'Продлить подписку':
            if message.chat.type == 'private':
                new_bill = p2p.bill(bill_id=message.from_user.id + random.randint(1000, 9999), lifetime=2, comment='APT')
                await bot.send_message(message.from_user.id, f'Стоимость подписки 345 рублей!\nВаша ссылка на оплату:\n\n{new_bill.pay_url}\n\nСсылка активна 2 минуты!')
                await asyncio.sleep(120)
                check = await check_pay(new_bill)
                if check != 'WAITING':
                    if db.user_update(message.from_user.id) == True:
                        await bot.send_message(message.from_user.id, 'Ваша подписка успешна оформлена!', reply_markup=markups.start_btn)
                    else:
                        await bot.send_message(message.from_user.id, 'Произошла ошибка! Напишите пожалуйста, администратору для решения проблемы!')
                else:
                    await bot.send_message(message.from_user.id, 'Ваш счет оплаты закрыт! Повторите попытку!')
                    p2p.reject(bill_id=new_bill.bill_id)

        elif message.text == 'Главная':
            await bot.send_message(message.from_user.id, 'Выберите функцию?', reply_markup=markups.activate_program)


        elif message.text == 'Выборка по модели':
            if db.user_id_check(message.from_user.id) == True:
                if db.check_days_subs(message.from_user.id) == True:
                    await bot.send_message(message.from_user.id, 'Введите марку, модель, год начала производства автомобиля через запятую. Пример - toyota, allex, 2001', reply_markup=markups.input_btn)
                    await Form.general.set()
                else:
                    await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.btn_continue_subs)
            else:
                await bot.send_message(message.from_user.id, 'Вы новый пользователь, оформите подписку!', reply_markup=markups.subs_btn)


        elif message.text == 'Выборка по цене':
            await bot.send_message(message.from_user.id, 'Выберите марку автомобиля, чтобы вывести максимальную цену запчасти!', reply_markup=markups.btn_marks_category)
            await Big.car_mark.set()


        elif message.text == 'Расчет РСА':
            if db.user_id_check(message.from_user.id) == True:
                if db.check_days_subs(message.from_user.id) == True:
                    await bot.send_message(message.from_user.id, 'Введите марку авто, номер детали через запятую. Пример - toyota, 52119-13340-A0. Расчте может занять от 30 до 120 секунд!')
                    await RCA.car_mark.set()
                else:
                    await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.btn_continue_subs)
            else:
                await bot.send_message(message.from_user.id, 'Вы новый пользователь, оформите подписку!', reply_markup=markups.subs_btn)

        elif message.text == 'Админ':
            if db.admin_add(message.from_user.id) == True:
                await bot.send_message(message.from_user.id, 'Режим администратора активирован!', reply_markup=markups.start_btn)


        elif message.text == 'Сделать отчет':
            if db.user_id_check(message.from_user.id) == True:
                if db.check_days_subs(message.from_user.id) == True:
                    await bot.send_message(message.from_user.id, 'Отправьте номер кузова авто!')
                    await Report.vin.set()
                else:
                    await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.btn_continue_subs)
            else:
                await bot.send_message(message.from_user.id, 'Вы новый пользователь, оформите подписку!', reply_markup=markups.subs_btn)


"""
ТРЕБУЕТСЯ НАСТРОЙКА АСИНХРОННОГО ИСПОЛНЕНИЯ
"""
'''----------------------------Обработчик машины состояния для Сделать отчет----------------------------'''
@dp.message_handler(state=Report.vin)
async def RSA_report(message: types.Message, state: FSMContext):
    import report_file_rsa
    import report_file_rsa_with_parse
    import threading

    if db.check_days_subs(message.from_user.id) == True:
        async with state.proxy() as proxy:
            if message.text != 'Главная':
                await write.write_request_from_user(message.from_user.id, message.text, 'ОТЧЕТ')
                proxy['vin'] = message.text
                try:
                    data, car_mark = await report_file_rsa.main(proxy)
                except:
                    car_mark = ''
                if car_mark != '':
                    check = 'PAY' #
                    # new_bill_report = p2p.bill(bill_id=message.from_user.id + random.randint(1000, 9999), amount=20, lifetime=2, comment='APTreport')
                    # await bot.send_message(message.from_user.id, f'Мы собрали информацию по автомобилю:\n\n{car_mark.upper()}\n\n№{message.text.upper()}\n\nКоличество запчастей: {len(data)}\n\nКупить отчет по ссылке: {new_bill_report.pay_url}\nСылка активна 2 минуты! После проверки оплаты мы пришлем вам отчет!', reply_markup=markups.back_back_btn2)
                    # await asyncio.sleep(120)
                    # check = await check_pay(new_bill_report)
                    if check != 'WAITING':
                        await bot.send_message(message.from_user.id, 'Оплата прошла успешно! Ожидайте!', reply_markup=markups.back_back_btn2)
                        try:
                            await message.answer_document(open(f'reports_rsa/{message.text.upper()}.txt', 'rb'))
                            await bot.send_message(message.from_user.id, 'Пожалуйста, проверьте те позиции, у которых не найдена цена!\nВозможно бот не смог собрать данные!')
                        except Exception:
                            '''
                            НОВЫЙ МЕТОД МУЛЬТИПРОЦЕССОРА
                            '''
                            await report_file_rsa_by_multiproc.create_process(data, message.text, car_mark)
                            await asyncio.sleep(0.1)
                            await z_sort_write.re_write(message.text.upper())
                            await asyncio.sleep(0.1)
                            await message.answer_document(open(f'reports_rsa/{message.text.upper()}.txt', 'rb'))
                            await bot.send_message(message.from_user.id, 'Пожалуйста, проверьте те позиции, у которых не найдена цена!\nВозможно бот не смог собрать данные!')
                    else:
                        await bot.send_message(message.from_user.id, f'Счет оплаты {message.text.upper()} истек! Повторите попытку!', reply_markup=markups.back_back_btn2)
                        # p2p.reject(bill_id=new_bill_report.bill_id)
                else:
                    '''
                    Здесь добавить парсинг не найденных файлов автомобилей таких как Nissan-europe, Nissan-japan, Toyota-europe, Toyota-japan
                    (ПОКА НЕ ОСНОВНАЯ ЗАДАЧА)
                    '''
                    await bot.send_message(message.from_user.id, f'Информации по номеру\n{message.text.upper()}\nНе найдено!',reply_markup=markups.back_back_btn2)
            else:
                await bot.send_message(message.from_user.id, 'Подтвердите!', reply_markup=markups.back_back_btn2)
                await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.btn_continue_subs)
        await state.finish()



"""
РАБОЧИЙ МЕТОД!
НЕ ИЗМЕНЯТЬ!
"""

'''----------------------------Обработчик машины состояния для Расчета по РСА----------------------------'''
@dp.message_handler(state=RCA.car_mark)
async def RCA_processing(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text != 'Главная':
            await write.write_request_from_user(message.from_user.id, message.text, 'РСА')
            proxy['car_mark'] = message.text
            ret_message = await recaptcha_treat.input_main(proxy)
            await write.write_answer_from_functions(message.from_user.id, ret_message, 'РСА')
            await bot.send_message(message.from_user.id, ret_message)
        else:
            await bot.send_message(message.from_user.id, 'Подтвердите!', reply_markup=markups.back_back_btn2)
            await state.finish()

"""
ПОКА ЧТО НЕРАБОЧИЙ МЕТОД !!!!!
'''----------------------------Обработчик машины состояния для Выборка по цене----------------------------'''
@dp.message_handler(state=Big.car_mark)
async def processing_car(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text != 'Главная':
            proxy['car_mark'] = message.text
            # ret_message = emex_parser_most_bigger_cost.input_main(proxy)
            await bot.send_message(message.from_user.id, 'ret_message: ЗАГЛУШКА')
        else:
            await state.finish()
"""



"""
РАБОЧИЙ МЕТОД!
ИЗМЕНИТЬ ПРОВЕРКУ ВВОДА АВТОМОБИЛЯ, НЕ ПРОВЕРЯЕТ НА НАЛИЧИЕ МАШИНЫ
"""
'''----------------------------Обработчик машины состояния для Выборка по модели----------------------------'''
@dp.message_handler(state=Form.general)
async def processing_text(message: types.Message, state: FSMContext):
    if db.check_days_subs(message.from_user.id) == True:
        async with state.proxy() as proxy:
            if message.text != 'Главная':
                await write.write_request_from_user(message.from_user.id, message.text, 'КАТЕГОРИИ')
                check_car = treat_send.input_main(message.text)
                '''
                НОВАЯ ПРОВЕРКА! 
                ПРОТЕСТИРОВАТЬ!
                '''
                # if check_car != 'Неправильно введены данные, либо данные о машине отсутвуют!':
                proxy['general'] = message.text
                await Form.next()
                await bot.send_message(message.from_user.id, 'Теперь выберите категорию, чтобы сделать расчет!', reply_markup=markups.category_btn)
                # else:
                #     await bot.send_message(message.from_user.id, 'Неправильно введены данные, либо данные о машине отсутвуют!', reply_markup=markups.back_back_btn2)
            else:
                await bot.send_message(message.from_user.id, 'Подтвердите!', reply_markup=markups.back_back_btn2)
                await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.btn_continue_subs)
        await state.finish()


@dp.message_handler(state=Form.category)
async def processing_text_category(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:
        if message.text == 'Капот':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id, f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}', 'КАТЕГОРИИ')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()


        elif message.text == 'Крылья':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id,f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}', 'КАТЕГОРИИ')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id,
                                                   f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id,
                                                   f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'Фары':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id,f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}', 'КАТЕГОРИИ')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'Стекла':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id, f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}', 'КАТЕГОРИИ')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'Бамперы':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id, f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}', 'КАТЕГОРИИ')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'Двери':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id, f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}', 'КАТЕГОРИИ')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'SRS':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id, f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'Двигатель':
            proxy['category'] = message.text
            if db.check_days_subs(message.from_user.id) == True:
                message_ret = treat_send.input_main(proxy)
                if len(message_ret[0]) != 0:
                    for i in message_ret[0]:
                        await bot.send_message(message.from_user.id, f'AMAYAMA:\nНазвание: {i["name"].upper()}\nНомер: {i["number"].upper()}\nЦена: {i["price"]}\nСсылка: {i["link"]}')
                        await write.write_answer_from_functions(message.from_user.id, f'AMAYAMA&Название={i["name"].upper()}&Номер={i["number"].upper()}&Цена={i["price"]}&Ссылка={i["link"]}')
                    for i in message_ret[-1]:
                        if len(i['max_prices']) != 0:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: {max(i["max_prices"])}')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена={max(i["max_prices"])}', 'КАТЕГОРИИ')
                        else:
                            await bot.send_message(message.from_user.id, f'EMEX:\nНомер детали: {i["number"].upper()}\nМаксимальная цена: Не найдено!')
                            await write.write_answer_from_functions(message.from_user.id, f'EMEX&Номер детали={i["number"].upper()}&Максимальная цена=Не найдено!', 'КАТЕГОРИИ')
                else:
                    await bot.send_message(message.from_user.id, 'Запчастей не найдено!')
                    await write.write_answer_from_functions(message.from_user.id, 'Запчастей не найдено!', 'КАТЕГОРИИ')
            else:
                await bot.send_message(message.from_user.id, 'У вас закончилась подписка! Хотите продлить?', reply_markup=markups.back_back_btn2)
                await state.finish()



        elif message.text == 'Главная':
            await bot.send_message(message.from_user.id, 'Подтвердите', reply_markup=markups.back_back_btn2)
            await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
