import requests
from bs4 import BeautifulSoup
import json
from config import *
import time
import os.path
from os import path
from telegram_send import send_message

#---------------------------------------------------------------------------------------------BASE HTML(don't delete!!!)
def get_html(url):
    s = requests.Session()
    r = s.get(url, headers=HEADERS)
    return r

#---------------------------------------------------------------------------------------------WORKED SET
def get_attr(link):
    attr = []
    html = get_html(link).text
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('tr', class_='map-item link')
    for i in items:
        try:
            name = i.find('td', class_='name').get_text(strip=True)
        except:
            name = None
        try:
            number = i.find('td', class_='number').find_next('a').get_text(strip=True)
        except:
            number = None
        try:
            price = i.find('td', class_='price').get_text(strip=True)
        except:
            price = None
        try:
            link = 'https://www.amayama.com' + i.find('td', class_='number').find_next('a').get('href')
        except:
            link = None
        try:
            count = i.find('td', class_='count').get_text(strip=True)
        except:
            count = None
        attr.append({
            'link' : link,
            'name' : name,
            'number' : number,
            'price' : price,
            'count' : count,
        })
    return attr

def get_title(link):
    parts = []
    html = get_html(link).text
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='schemas-list-item')
    for i in items:
        try:
            try:
                href = i.find('a').get('href')
            except:
                href = 'None'

            try:
                name = i.find('a').get_text(strip=True)
            except:
                name = None

            parts.append({
                'link' : 'https://www.amayama.com' + href,
                'title' : {
                    'attr': get_attr('https://www.amayama.com' + href),
                },
            })
        except Exception as ex:
            print(ex)
            continue
    return parts
#---------------------------------------------------------------------------------------------SAVE JSON WORKED
def save_json(data, file_name):
    mark_car = file_name.split('/')[-3]
    model_car = file_name.split('/')[-2]
    spec_car = file_name.split('/')[-1]
    try:
        with open(f"models/{mark_car}/{model_car}/{spec_car}.json", "w") as file:
            json.dump(data, file)
        send_message(f'Файл: {mark_car}/{model_car}/{spec_car} записан успешно!')
    except Exception as ex:
        print(f'Save error! Folder {mark_car}/{model_car}/{spec_car}')
        send_message(f'При сохранении произошла ошибка -- {ex}')

def valid_writer(link):
    if RULES_WRITER == False:
        mark_car = link.split('/')[-3].strip()
        model_car = link.split('/')[-2].strip()
        spec_car = link.split('/')[-1].strip()
        ret = path.exists(f'models/{mark_car}/{model_car}/{spec_car}.json')
        return ret
    else:
        return True

def check(all_link):
    rules = valid_writer(all_link)
    if rules == False:
        try:
            all_parts = []
            html = get_html(all_link).text
            soup = BeautifulSoup(html, 'lxml')
            items = soup.find('div', class_='list')
            hrefs = items.find_all('a')
            for i in hrefs:
                href = i.get('href')
                title = i.find('div', class_='name').get_text(strip=True)
                all_parts.append({
                    'title' : title,
                    'all_parts' : get_title('https://www.amayama.com' + href),
                    'link' : 'https://www.amayama.com' + href,
                })
                print(all_parts)
            save_json(all_parts, all_link)
        except Exception as ex:
            print(ex)
            save_json(all_parts, all_link)
    else:
        send_message(f'Ссылка {all_link} уже записана в json!')

if __name__ == '__main__':

    def get_list_models_links(link):
        html = get_html(link).text
        soup = BeautifulSoup(html, 'lxml')
        try:
            items = soup.find('div', class_='list')
            hrefs = items.find_all('a')
            for href in hrefs:
                check('https://www.amayama.com' + href.get('href'))
                send_message(f'Ссылка {href} парсинг закончен!')
        except:
            try:
                items = soup.find('table')
                colom = items.find_all('tr')
                try:
                    for i in colom:
                        check('https://www.amayama.com' + i.find('td').find_next('a').get('href'))
                        send_message(f'Ссылка {i} парсинг закончен!')
                except:
                    send_message(f'Ошибка с табличными данными!')
            except:
                send_message(f'Ошибка в получении html!')

    def get_list_group_items(html):
        try:
            soup = BeautifulSoup(html, 'lxml')
            items = soup.find_all('a', class_='list-group-item')
            for item in items:
                get_list_models_links(item.get('href'))
        except Exception as ex:
            send_message(f'Произошла ошибка {ex} в получении спецификаций моделей!')
            return

#---------------------------------------------------------------------------------------------START LIST MODEL1
    for i in LIST_MODEL1:
        try:
            html = get_html(i).text
            get_list_group_items(html)
        except Exception as ex:
            send_message(f'Произошла ошибка {ex} в основном цикле!')
            continue

# ---------------------------------------------------------------------------------------------START LIST MODEL2
#     for i in LIST_MODEL2:
#         try:
#             html = get_html(i).text
#             get_list_group_items(html)
#         except Exception as ex:
#             send_message(f'Произошла ошибка {ex} в основном цикле!')
#             continue


#---------------------------------------------------------------------------------------------NOTES
'''
Загрузка памяти
Разобраться с табличными значениями
'''