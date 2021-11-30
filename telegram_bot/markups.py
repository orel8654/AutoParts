from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_count = KeyboardButton('Выбор функций')
btn_subs = KeyboardButton('Оформить подписку')
btn_back = KeyboardButton('Главная')
btn_back_back = KeyboardButton('Назад')
btn_continue_subs = KeyboardButton('Продлить подписку')
btn_admin = KeyboardButton('Админ')

btn_model_car = KeyboardButton('Выборка по модели')
btn_most_cost = KeyboardButton('Выборка по цене')
btn_rca = KeyboardButton('Расчет РСА')

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
activate_program = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_model_car, btn_rca, btn_back)
input_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_count, btn_back)
category_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(cat_hood, cat_fender, cat_headlights, cat_glasses, cat_bumper, cat_doors, cat_srs, cat_engine, btn_back)
btn_marks_category = ReplyKeyboardMarkup(resize_keyboard=True).add(mark_subaru, mark_toyota, mark_suzuki, mark_nissan, mark_mitsubishi, mark_mazda, mark_honda, mark_all, btn_back)
back_back_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back_back)
back_back_btn2= ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back)
btn_admin_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_admin)

CMD_HELP = 'Бот предоставляет актуальные цены на запчасти японских марок автомобилей!\n\n♻️ Функция "Выборка по модели":\nБот принимает сообщение с маркой, моделью, годом начала производства в формате (subaru, legacy b4, 2003)\nДалее посредством кнопок производится ввод категорий запчастей\n\n♻️ Функция "Выборка по цене":\nВыберите марку автомобиля и бот предоставит самую дорогую деталь это марки каталога AMAYAMA и EMEX!\n⚠️ Всегда проверяйте актуальную цену в РСА, так как цены могут различаться вдвое!\n\n♻️ Функция "Расчет РСА":\n\nВведите данные в формате (subaru, 64010CA030VL) и отправьте боту!\n⚠️ Эта категория расчета требует больше времени и может длиться до 1 минуты\nВы можете дождаться выполнения запроса или отправить новый, сообщения автоматически отправятся вам!'
CMD_INFO = '‼ ️Это пробная версия бота, мы собираем информацию об ошибках взаимодействия с пользователем для улучшения интеграции.\n⚠️ Мы не храним и не передаем 3-м лицам данные введенные пользователем.\n\n⚠️ ️Вся информация о ценах предоставлена в ознакомительных целях и взята с открытых источников.\n\nДля пользования ботом будет введена подписка, для поддержания разработки.\n\n❔ По всем вопросам связанным с работой бота пишите администратору: @geoo001'
CMD_SUPMOD = 'Поддерживаемые модели:\n♻️ Выборка по модели и ♻️ Выборка по цене\n\nHONDA\nMAZDA\nMITSUBISHI\nNISSAN\nSUBARU\nSUZUKI\nTOYOTA\n\n♻️ Расчет РСА:\n\nSUBARU\nNISSAN\nTOYOTA\nHONDA\nMAZDA\nMITSUBISHI\nSUZUKI\nACURA\nAUDI\nBMW\nCADILLAC\nCHERY\nCHEVROLET\nFORD\nHYUNDAI\nINFINITI\nKIA\nLEXUS\nPORSCHE\nVOLKSWAGEN\n\n⚠️ В дальнейшем будут добавлены другие марки!'