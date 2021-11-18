from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_count = KeyboardButton('Сделать расчет!')
btn_subs = KeyboardButton('Оформить подписку!')
btn_back = KeyboardButton('Главная')
btn_continue_subs = KeyboardButton('Продлить подписку!')
start_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_count)
subs_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_subs, btn_back)
continue_subs_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_continue_subs, btn_back)