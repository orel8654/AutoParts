"""
Сортировка - вывод(отправка в телеграм)
"""

import json
import emex_parser
import recaptcha
from config import LIST_HOOD, LIST_FRONT_FENDER, LIST_HEADLIGHTS, LIST_FRONT_BUMPER, LIST_REAR_BUMPER, LIST_REAR_HOOD, LIST_GLASSES_WINDSHIELD, LIST_GLASSES_DOORS, LIST_GLASSES_BACK, LIST_SRS_SECURITY, LIST_ENGINE, LIST_DOORS, CATEGORY_ENGINE, CATEGORY_BODY, CATEGORY_ELECTRIC, CATEGORY_TRANSMISSION

class SortedParts:

    ENGINE = CATEGORY_ENGINE
    TRANSMISSION = CATEGORY_TRANSMISSION
    BODY = CATEGORY_BODY
    ELECTRIC = CATEGORY_ELECTRIC

    def __init__(self):
        self.parts_front_hood = LIST_HOOD
        self.parts_front_fender = LIST_FRONT_FENDER
        self.parts_headlights = LIST_HEADLIGHTS
        self.parts_front_bumper = LIST_FRONT_BUMPER
        self.parts_rear_bumper = LIST_REAR_BUMPER
        self.parts_rear_hood = LIST_REAR_HOOD
        self.parts_glasses_windshield = LIST_GLASSES_WINDSHIELD
        self.parts_glasses_doors = LIST_GLASSES_DOORS
        self.parts_glasses_back = LIST_GLASSES_BACK
        self.parts_srs_security = LIST_SRS_SECURITY
        self.parts_engine = LIST_ENGINE
        self.parts_doors = LIST_DOORS

    def read_file_for_hood(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_front_hood:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_front_fender(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_front_bumper:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_electric(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.ELECTRIC:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_headlights:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_front_bumper(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_front_bumper:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_rear_hood(self,data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_rear_hood:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_rear_fender(self, data):
        pass

    def read_file_for_glasses_windshield(self,data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_glasses_windshield:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_glasses_doors(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_glasses_doors:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_glasses_back(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_glasses_back:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_engine(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.ENGINE:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_engine:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_doors(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_doors:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_srs(self, data, car_mark):
        ama_price = ''
        emex_price = []
        for i in data:
            if i['title'] == SortedParts.BODY:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if k['name'].lower() in self.parts_srs_security:
                                ama_price = k
                        except:
                            continue
        try:
            emex_price.extend(emex_parser.main(ama_price['number'], car_mark))
        except:
            emex_price.append(None)
        return ama_price, emex_price

    def read_file_for_number(self, data, numbers):
        len_numbers = len(numbers)
        parts_sum = 0
        parts_list = []
        for n in numbers:
            for i in data:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['number'] == n:
                            parts_list.append(k)
        average_list = []
        if len_numbers != 0:
            for i in parts_list:
                try:
                    price = int(i['price'])
                    parts_sum += price
                    average_list.append({
                        'link' : i['link'],
                        'name': i['name'],
                        'number': i['number'],
                        'price': price,
                    })
                except:
                    price = int(i['price'].replace('\xa0', ''))
                    parts_sum += price
                    average_list.append({
                        'link': i['link'],
                        'name': i['name'],
                        'number': i['number'],
                        'price': price,
                    })
            return average_list
        else:
            return None






#-----------------------------------------------------------------------------------------------------------------------Start def sorted HOOD
def start_sorted_hood(data, mark):
    class_hood = SortedParts()
    ama_price_dict, emex_price_list = class_hood.read_file_for_hood(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена капота по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена капота по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена капота по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по капоту не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted NUMBERS PARTS
def start_sorted_numbers(data, mark, numbers=['19000-31330']):
    average_summa = 0
    emex_parts = []
    class_numbers = SortedParts()
    average_price_numbers = class_numbers.read_file_for_number(data, numbers)
    if average_price_numbers != None:
        for i in average_price_numbers:
            emex_parts.extend(emex_parser.main(i['number'], mark))
            average_summa += i['price']
            print(f'Ссылка на деталь: {i["link"]}\nНазвание: {i["name"]}\nНомер запчасти: {i["number"]}\nЦена: {i["price"]} рублей.\n')
        print(f'Общая сумма: {average_summa} RUB!')
        print(f'Максимальная цена на деталь по EMEX: {max(emex_parts)} RUB')
    else:
        print('Информации о деталях не найдено!')

#-----------------------------------------------------------------------------------------------------------------------Start def sorted FRONT FENDER
def start_sorted_front_fender(data, mark):
    class_front_fender = SortedParts()
    ama_price_dict, emex_price_list = class_front_fender.read_file_for_front_fender(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена крыла по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена крыла по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена капота по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по капоту не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted HEADLIGHTS
def start_sorted_headlights(data, mark):
    class_headlights = SortedParts()
    ama_price_dict, emex_price_list = class_headlights.read_file_for_electric(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена фары по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена фары по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена фары по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по фарам не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted FRONT BUMPER
def start_sorted_front_bumper(data, mark):
    class_front_bumper = SortedParts()
    ama_price_dict, emex_price_list = class_front_bumper.read_file_for_front_bumper(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена бампера (перед/зад) по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена бампера (перед/зад) по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена бампера (перед/зад) по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по бамперам (перед/зад) не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted REAR HOOD (BACK DOOR)
def start_sorted_rear_hood(data, mark):
    class_rear_hood = SortedParts()
    ama_price_dict, emex_price_list = class_rear_hood.read_file_for_rear_hood(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена задней двери по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена задней двери по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена задней двери по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по задней двери не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted GLASSES WINDSHIELD
def start_sorted_glasses_windshield(data, mark):
    class_glasses = SortedParts()
    ama_price_dict, emex_price_list = class_glasses.read_file_for_glasses_windshield(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена лобового стекла по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная лобового стекла по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена лобового стекла по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по лобовому стеклу не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted GLASSES DOORS
def start_sorted_glasses_doors(data, mark):
    class_glasses = SortedParts()
    ama_price_dict, emex_price_list = class_glasses.read_file_for_glasses_doors(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена бокового стекла по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена бокового стекла по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена бокового стекла по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по боковым стеклам не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted GLASSES BACK DOOR
def start_sorted_glasses_back_window(data, mark):
    class_glasses = SortedParts()
    ama_price_dict, emex_price_list = class_glasses.read_file_for_glasses_back(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена заднего стекла по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена заднего стекла по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена заднего стекла по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по задним стеклам не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted ENGINE
def start_sorted_engine(data, mark):
    class_engine = SortedParts()
    ama_price_dict, emex_price_list = class_engine.read_file_for_engine(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена двигателя по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена двигателя по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена двигателя по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по двигателю не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted DOORS
def start_sorted_doors(data, mark):
    class_engine = SortedParts()
    ama_price_dict, emex_price_list = class_engine.read_file_for_doors(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена боковой двери по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена боковой двери по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена боковой двери по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по боковым дверям не найдено!'

#-----------------------------------------------------------------------------------------------------------------------Start def sorted SRS
def start_sorted_srs(data, mark):
    class_engine = SortedParts()
    ama_price_dict, emex_price_list = class_engine.read_file_for_srs(data, mark)
    if ama_price_dict != '':
        try:
            return f'Максимальная цена SRS по AMAYAMA: {ama_price_dict["price"]} RUB\nМаксимальная цена SRS по EMEX: {max(emex_price_list)} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
        except:
            return f'Максимальная цена SRS по AMAYAMA: {ama_price_dict["price"]} RUB\nСсылка на деталь: {ama_price_dict["link"]}\nНомер детали: {ama_price_dict["number"]}\nИнформации на EMEX не найдено!\n\n{recaptcha.find_past(ama_price_dict["number"], mark)}'
    else:
        return f'Информации по SRS не найдено!'



#-----------------------------------------------------------------------------------------------------------------------Def input and sorted with class part
def start_main(mark_m, model_m, year_m, sort_category):
    car_mark = mark_m
    car_model = model_m
    file_year = year_m
    with open(f'models/{car_mark}/{car_model}/{file_year}') as file:
        data_file = json.load(file)
    if sort_category == 'Капот':
        return start_sorted_hood(data_file, car_mark)
    elif sort_category == 'Номер':
        return start_sorted_numbers(data_file, car_mark)
    elif sort_category == 'Крыло':
        return start_sorted_front_fender(data_file, car_mark)
    elif sort_category == 'Фара':
        return start_sorted_headlights(data_file, car_mark)
    elif sort_category == 'Бампер':
        return start_sorted_front_bumper(data_file, car_mark)
    elif sort_category == 'Багажник':
        return start_sorted_rear_hood(data_file, car_mark)
    elif sort_category == 'Стекла':
        windshield = start_sorted_glasses_windshield(data_file, car_mark)
        doors = start_sorted_glasses_doors(data_file, car_mark)
        back = start_sorted_glasses_back_window(data_file, car_mark)
        return f'{windshield}\n\n{doors}\n\n{back}'
    elif sort_category == 'Двигатель':
        return start_sorted_engine(data_file, car_mark)
    elif sort_category == 'Двери':
        return start_sorted_doors(data_file, car_mark)
    elif sort_category == 'SRS':
        return start_sorted_srs(data_file, car_mark)
    elif sort_category == 'Все позиции':
        a1 = start_sorted_hood(data_file, car_mark)
        a2 = start_sorted_front_fender(data_file, car_mark)
        a3 = start_sorted_headlights(data_file, car_mark)
        a4 = start_sorted_front_bumper(data_file, car_mark)
        a5 = start_sorted_glasses_windshield(data_file, car_mark)
        a6 = start_sorted_glasses_doors(data_file, car_mark)
        a7 = start_sorted_glasses_back_window(data_file, car_mark)
        a8 = start_sorted_rear_hood(data_file, car_mark)
        a9 = start_sorted_engine(data_file, car_mark)
        a10 = start_sorted_doors(data_file, car_mark)
        a11 = start_sorted_srs(data_file, car_mark)
        return f'{a1}\n\n{a2}\n\n{a3}\n\n{a4}\n\n{a5}\n\n{a6}\n\n{a7}\n\n{a8}\n\n{a9}\n\n{a10}\n\n{a11}'

# print(start_main('toyota', 'auris', '1-hatchback-right-e150-2006-3309.json', 'SRS'))
'''
Передается из файла treat_send маркаа машины, модель машины, год машины(название файла) и список запчастей по которым нужно предоставить данные по ценам, если передается не спиок а строка и равна 'all', то производтся подсчет по все категориям запчастей.
Отсюда же должен вызываться метод отправки в телеграм клиенту. 
'''