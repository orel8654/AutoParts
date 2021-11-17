from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_count = KeyboardButton('Сделать расчет!')
btn_subs = KeyboardButton('Оформить подписку!')
start_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_count, btn_subs)

subs_profile = KeyboardButton('ПОДПИСКА')
subs_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(subs_profile)