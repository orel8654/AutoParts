import json
import emex_parser
from config import LIST_HOOD, LIST_FRONT_FENDER, LIST_HEADLIGHTS, LIST_FRONT_BUMPER, LIST_REAR_BUMPER, LIST_REAR_HOOD, LIST_GLASSES_WINDSHIELD, LIST_GLASSES_DOORS, LIST_GLASSES_BACK, LIST_SRS_SECURITY, LIST_ENGINE, LIST_DOORS, CATEGORY_ENGINE, CATEGORY_BODY, CATEGORY_ELECTRIC, CATEGORY_TRANSMISSION
import os
from os import path
import time
from heapq import nlargest
import recaptcha

def sorted_max_price_all_items(data): #---------------------------------------------------------------------------------СОРТИРОВКА МАКСИМАЛЬНОЙ ЦЕНЫ ЗАПЧАСТИ
    max_item = 0
    lst = ''
    for i in data:
        if i['title'] == CATEGORY_BODY:
            for j in i['all_parts']:
                for k in j['title']['attr']:
                    if k['price'] > max_item:
                        if k['name'] in LIST_HOOD or k['name'] in LIST_REAR_HOOD or k['name'] in LIST_DOORS or k['name'] in LIST_GLASSES_WINDSHIELD or k['name'] in LIST_HEADLIGHTS or k['name'] in LIST_FRONT_BUMPER or k['name'] in LIST_GLASSES_DOORS or k['name'] in LIST_GLASSES_BACK or k['name'] in LIST_SRS_SECURITY or k['name'] in LIST_FRONT_BUMPER:
                            if 'seat' not in k['name'].lower() or 'exaust' not in k['name'].lower():
                                max_item = k['price']
                                lst = k
    return lst

def read_all_files(car_mark): #-------------------------------------------------------------------------------------------------ПОЛУЧЕНИЕ ВСЕХ ДАННЫХ ИЗ ФАЙЛОВ (МОЖНО СОРТИРОВАТЬ ПО МАРКЕ)
    max_cost = []
    path = 'models/'
    folderlist = os.listdir(path)
    for i in folderlist:
        if car_mark.lower() == 'максимум из всех':
            try:
                car_model_list = os.listdir(path + i + '/')
                for j in car_model_list:
                    try:
                        all_files = os.listdir(path + i + '/' + j)
                        for k in all_files:
                            with open(f'{path}{i}/{j}/{k}', 'r') as file:
                                data_file = json.load(file)
                            max_price = sorted_max_price_all_items(data_file)
                            max_cost.append({
                                'car_name': f'{i} {j}',
                                'max_part': max_price,
                            })
                    except:
                        continue
            except:
                continue
        else:
            if car_mark.lower() == i:
                try:
                    car_model_list = os.listdir(path + i + '/')
                    for j in car_model_list:
                        try:
                            all_files = os.listdir(path + i + '/' + j)
                            for k in all_files:
                                with open(f'{path}{i}/{j}/{k}', 'r') as file:
                                    data_file = json.load(file)
                                max_price = sorted_max_price_all_items(data_file)
                                max_cost.append({
                                    'car_name': f'{i} {j}',
                                    'max_part': max_price,
                                })
                        except:
                            continue
                except:
                    continue
    return max_cost

def input_main(car_mark): #-----------------------------------------------------------------------------------------------------ВЫВОД МАКСИМАЛЬНОЙ ЦЕНЫ ЗАПЧАСТИ ВМЕСТЕ С МОДЕЛЬЮ
    car_mark = car_mark['car_mark']
    check_lst = ''
    check_max = 0
    check_mark = ''
    lst = read_all_files(car_mark)
    for i in lst:
        try:
            lst_parts = i['max_part']
            if lst_parts['price'] > check_max:
                check_max = lst_parts['price']
                check_lst = lst_parts
                check_mark = i['car_name']
        except:
            continue
    emex_mark = check_mark.split(' ')[0].strip()
    emex_price = []
    emex_price.extend(emex_parser.main(check_lst["number"], emex_mark))
    try:
        return f'Название машины: {check_mark}\nНаименование детали: {check_lst["name"]}\nСсылка: {check_lst["link"]}\nНомер детали: {check_lst["number"]}\nМаксимальная цена по AMAYAMA: {check_lst["price"]} RUB\nМаксимальная цена по EMEX: {max(emex_price)} RUB\n\n{recaptcha.find_past(check_lst["number"], car_mark)}'
    except:
        return f'Название машины: {check_mark}\nНаименование детали: {check_lst["name"]}\nСсылка: {check_lst["link"]}\nНомер детали: {check_lst["number"]}\nМаксимальная цена по AMAYAMA: {check_lst["price"]} RUB\nМаксимальная цена по EMEX не найдена!\n\n{recaptcha.find_past(check_lst["number"], car_mark)}'


# def input_tg(data):
#     # print(data)
#     print(input_main('Subaru'))