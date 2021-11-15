import requests
from config import TELEGRAM_TOKEN
def send_message(text):

    api_token = TELEGRAM_TOKEN

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        chat_id='@sendprocessing',
        text=text,
    ))

if __name__ == '__main__':
    text = 'Процесс на компьютере закончился!'
    send_message(text)
