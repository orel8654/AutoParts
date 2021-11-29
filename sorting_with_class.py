"""
Сортировка - вывод(отправка в телеграм)
"""

import json
import re
import emex_parser
import asyncio

class SortedParts:


    def read_file_for_hood(self, data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('кузов', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('hood|капот', k['name'].lower()):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price


    def read_file_for_fenders(self, data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('кузов', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('крыло|fender', k['name'].lower()):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price


    def read_file_for_electric(self, data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('электрика', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('фара|headlamp|lamp|head lamp', k['name']):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price


    def read_file_for_bumpers(self, data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('кузов', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('бампер|bumper', k['name'].lower()):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price


    def read_file_for_doors(self,data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('кузов', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('дверь|door|багажник', k['name'].lower()):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price


    def read_file_for_glasses(self,data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            for i in data:
                if re.search('кузов', i['title'].lower()):
                    for j in i['all_parts']:
                        for k in j['title']['attr']:
                            try:
                                if re.search('стекло|glass', k['name'].lower()):
                                    ama_price.append(k)
                            except:
                                continue
            if len(ama_price) > 0:
                for i in ama_price:
                    try:
                        emex = emex_parser.main(i['number'], car_mark)
                        emex_price.append({
                            'number': i['number'],
                            'max_prices': emex,
                        })
                    except:
                        continue
            else:
                emex_price = []
            return ama_price, emex_price


    def read_file_for_engine(self, data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('двигатель', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('двигатель|engine|block', k['name'].lower()):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price

    def read_file_for_srs(self, data, car_mark):
        ama_price = []
        emex_price = []
        for i in data:
            if re.search('кузов', i['title'].lower()):
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        try:
                            if re.search('подушка|airbag|air bag|безопастност', k['name'].lower()):
                                ama_price.append(k)
                        except:
                            continue
        if len(ama_price) > 0:
            for i in ama_price:
                try:
                    emex = emex_parser.main(i['number'], car_mark)
                    emex_price.append({
                        'number': i['number'],
                        'max_prices': emex,
                    })
                except:
                    continue
        else:
            emex_price = []
        return ama_price, emex_price




#-----------------------------------------------------------------------------------------------------------------------Start def sorted HOOD
def start_sorted_hood(data, mark):
    class_hood = SortedParts()
    ama_price_dict, emex_price_dict = class_hood.read_file_for_hood(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted FENDERS
def start_sorted_fenders(data, mark):
    class_front_fender = SortedParts()
    ama_price_dict, emex_price_dict = class_front_fender.read_file_for_fenders(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted HEADLIGHTS
def start_sorted_headlights(data, mark):
    class_headlights = SortedParts()
    ama_price_dict, emex_price_dict = class_headlights.read_file_for_electric(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted BUMPERS
def start_sorted_bumpers(data, mark):
    class_front_bumper = SortedParts()
    ama_price_dict, emex_price_dict = class_front_bumper.read_file_for_bumpers(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted DOORS
def start_sorted_doors(data, mark):
    class_rear_hood = SortedParts()
    ama_price_dict, emex_price_dict = class_rear_hood.read_file_for_doors(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted GLASSES
def start_sorted_glasses(data, mark):
    class_glasses = SortedParts()
    ama_price_dict, emex_price_dict = class_glasses.read_file_for_glasses(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted ENGINE
def start_sorted_engine(data, mark):
    class_engine = SortedParts()
    ama_price_dict, emex_price_dict = class_engine.read_file_for_engine(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Start def sorted SRS
def start_sorted_srs(data, mark):
    class_engine = SortedParts()
    ama_price_dict, emex_price_dict = class_engine.read_file_for_srs(data, mark)
    return ama_price_dict, emex_price_dict


#-----------------------------------------------------------------------------------------------------------------------Def input and sorted with class part
def start_main(mark_m, model_m, year_m, sort_category):
    car_mark = mark_m
    car_model = model_m
    file_year = year_m
    with open(f'models/{car_mark}/{car_model}/{file_year}') as file:
        data_file = json.load(file)
    if sort_category == 'Капот':
        return start_sorted_hood(data_file, car_mark)
    elif sort_category == 'Крылья':
        return start_sorted_fenders(data_file, car_mark)
    elif sort_category == 'Фары':
        return start_sorted_headlights(data_file, car_mark)
    elif sort_category == 'Бамперы':
        return start_sorted_bumpers(data_file, car_mark)
    elif sort_category == 'Стекла':
        return start_sorted_glasses(data_file, car_mark)
    elif sort_category == 'Двигатель':
        return start_sorted_engine(data_file, car_mark)
    elif sort_category == 'Двери':
        return start_sorted_doors(data_file, car_mark)
    elif sort_category == 'SRS':
        return start_sorted_srs(data_file, car_mark)

#
# if __name__ == '__main__':
#     check = start_main('toyota', 'allex', '1-hatchback-right-e120-2001-3071.json', 'Капот')
#     print(check[0])
#     print(check[-1])
'''
Передается из файла treat_send маркаа машины, модель машины, год машины(название файла) и список запчастей по которым нужно предоставить данные по ценам, если передается не спиок а строка и равна 'all', то производтся подсчет по все категориям запчастей.
Отсюда же должен вызываться метод отправки в телеграм клиенту. 
'''