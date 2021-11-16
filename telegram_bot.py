from aiogram import Bot, types, executor, Dispatcher
from config import TELEGRAM_TOKEN_BOT_GENERAL

BOT = Bot(token=TELEGRAM_TOKEN_BOT_GENERAL)
dp = Dispatcher(BOT)

async def start_bot(_):
    print('Bot is online')

@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    await BOT.send_message(message.from_user.id, 'Hello, {0.first_name}'.format(message.from_user))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
