import requests

def send_message(text):

    api_token = '2076509234:AAEx0X5agqD1rkJxiOK8rFVIZbC4dWaNsHc'

    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        chat_id='@sendprocessing',
        text=text,
    ))

if __name__ == '__main__':
    text = 'Процесс на компьютере закончился!'
    send_message(text)
