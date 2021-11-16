import requests
from config import TELEGRAM_TOKEN_SEND_PROCESSING
def send_message(text):

    api_token = TELEGRAM_TOKEN_SEND_PROCESSING

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        chat_id='@sendprocessing',
        text=text,
    ))

if __name__ == '__main__':
    text = 'Процесс на компьютере закончился!'
    send_message(text)
