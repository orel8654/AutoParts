from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_count = KeyboardButton('Выбор функций')
btn_subs = KeyboardButton('Оформить подписку')
btn_back = KeyboardButton('Главная')
btn_back_back = KeyboardButton('Назад')
btn_continue_subs = KeyboardButton('Продлить подписку')
btn_admin = KeyboardButton('Админ')
btn_pay = KeyboardButton('Купить')

btn_model_car = KeyboardButton('Выборка по модели')
btn_most_cost = KeyboardButton('Выборка по цене')
btn_rca = KeyboardButton('Расчет РСА')
btn_report = KeyboardButton('Сделать отчет')

cat_hood = KeyboardButton('Капот')
cat_fender = KeyboardButton('Крылья')
cat_headlights = KeyboardButton('Фары')
cat_glasses = KeyboardButton('Стекла')
cat_bumper = KeyboardButton('Бамперы')
cat_engine = KeyboardButton('Двигатель')
cat_doors = KeyboardButton('Двери')
cat_srs = KeyboardButton('SRS')

mark_subaru = KeyboardButton('Subaru')
mark_toyota = KeyboardButton('Toyota')
mark_suzuki = KeyboardButton('Suzuki')
mark_nissan = KeyboardButton('Nissan')
mark_mitsubishi = KeyboardButton('Mitsubishi')
mark_mazda = KeyboardButton('Mazda')
mark_honda = KeyboardButton('Honda')
mark_all = KeyboardButton('Максимум из всех')

start_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_count)
subs_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_subs, btn_back)
continue_subs_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_continue_subs, btn_back)
activate_program = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_model_car, btn_rca, btn_report, btn_back)
input_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_count, btn_back)
category_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(cat_hood, cat_fender, cat_headlights, cat_glasses, cat_bumper, cat_doors, cat_srs, cat_engine, btn_back)
btn_marks_category = ReplyKeyboardMarkup(resize_keyboard=True).add(mark_subaru, mark_toyota, mark_suzuki, mark_nissan, mark_mitsubishi, mark_mazda, mark_honda, mark_all, btn_back)
back_back_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back_back)
back_back_btn2= ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back)
btn_admin_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_admin)
btn_pay_report = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_pay, btn_back)

CMD_HELP = '📍 Бот работает по подписке (подробная информация /pay)\n\n♻️ Функция "Выборка по модели":\nВведите сообщение в формате: марка, модель, год начала производства. Пример - subaru, legacy b4, 2003\nДалее посредством кнопок выберите категорию\n\n♻️ Функция "Расчет РСА":\nВведите данные в формате: марка, номер запчасти. Пример - subaru, 64010CA030VL\n⚠️ Эта категория расчета требует больше времени и может занять от 30 до 120 секунд\nНомера запчастей вы можете получить в функции "Выборка по модели"\n\nВы можете не дожидаться ответа и отправить новый запрос!\n\n♻️ Функция "Сделать отчет":\nВведите ⚠️ номер кузова, бот проверит информацию в базе, оплатите отчет, после успешной оплаты в течении ⚠️ 30 минут бот отправит вам отчет в формате - TXT!'

CMD_INFO = '⚠️ Вся информация взята из открытых источников и предоставлена в ознакомительных целях\n\n⚠️ Обратите внимание, что цены на запчасти из источников AMAYAMA, EMEX, РСА отличаются\n\n⚠️ Расчет отчета производится по категориям: "Кузов", "Электрика", "Аксессуары"\n\n⚠️ Если при расчете цена не найдена, значит информация о запчасти отсутствует в каталогах\n\n⚠️ Мы не храним и не передаем 3-м лицам данные введенные пользователем, по вопросам связанным с работой бота напишите администратору:\n@geoo001'

CMD_SUPMOD = '♻️ Выборка по модели:\n\nHONDA\nMAZDA\nMITSUBISHI\nNISSAN\nSUBARU\nSUZUKI\nTOYOTA\n\n♻️ Расчет РСА:\n\nSUBARU\nNISSAN\nTOYOTA\nHONDA\nMAZDA\nMITSUBISHI\nSUZUKI\nACURA\nAUDI\nBMW\nCADILLAC\nCHERY\nCHEVROLET\nFORD\nHYUNDAI\nINFINITI\nKIA\nLEXUS\nPORSCHE\nVOLKSWAGEN\n\n⚠️ В дальнейшем будут добавлены другие марки!\n\n♻️ Сделать отчет:\n\n⚠️ На данный момент поддерживается только номер кузова!'

CMD_PAY = '📍 Стоимость подписки - 345 рублей\n\n📍 Подписка действует 30 дней\n\n📍 Оплата производится через платежную систему QIWI\n\n📍 При нажатии "Оформить подписку" формируется счет оплаты, который действует 2 минуты\n\n📍 После оплаты дождитесь проверки вашего платежа. Вам будет отправлено сообщение "Подписка успешно оформлена!"\n\n📍 После проверки платежа вам предоставляется доступ ко всем функциям бота!\n\n📍 Стоисоть отчета - 945 рублей\n\n📍 После оплаты дождитесь дождитесь проверки вашего платежа. Вам будет отправлено подтверждение!'