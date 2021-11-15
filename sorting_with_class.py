"""
Сортировка - Капот, крыло, фары, задняя часть,
"""

import json

import emex_parser


class SortedParts:

    engine = 'Двигатель, топливная система и инструменты'
    transmission = 'Трансмиссия и шасси'
    body = 'Кузов и салон'
    electric = 'Электрика'

    def __init__(self):
        self.parts_front_hood = ['Капот', 'Hood', 'капот', 'hood', 'hood sub-assy', 'Hood Sub-Assy', 'HOOD SUB-ASSY']
        self.parts_front_fender = ['Крыло', 'Wing', 'Fender', 'Подкрылок', 'крыло', 'wing', 'fender', 'подкрылок', 'fender sub-assy, front rh', 'Fender Sub-Assy, Front Rh', 'fender sub-assy, front lh', 'Fender Sub-Assy, Front Lh', 'shield sub-assy, front fender splash, rh', 'shield sub-assy, front fender splash, lh', 'Shield Sub-Assy, Front Fender Splash, Rh', 'Shield Sub-Assy, Front Fender Splash, Lh']
        self.parts_headlights = ['Фара', 'фара', 'Head Lamp Assembly,Rh', 'Head Lamp Assembly,Lh', 'Кронштейн Фары', 'кронштейн фары', 'head lamp assembly,rh', 'head lamp assembly,lh', 'lamp assembly-head left', 'lamp assembly-head right', 'Lamp Assembly-Head Left', 'Lamp Assembly-Head Right', 'headlamp assy, rh', 'headlamp assy, lh', 'Headlamp Assy, Rh', 'Headlamp Assy, Lh']
        self.parts_front_bumper = ['бампер', 'Бампер', 'bumper', 'Bumper', 'cover, front bumper', 'Cover, Front Bumper', 'front bumper', 'Front Bumper']
        self.parts_rear_bumper = ['бампер', 'bumper', 'Bumper', 'cover, rear bumper', 'Cover, Rear Bumper', 'rear bumper', 'Rear Bumper']
        self.parts_rear_hood = ['back door', 'Back door', 'Back Door', 'багажник', 'Багажник', 'assembly back door', 'Assembly back door', 'задняя дверь', 'Задняя дверь', 'panel sub-assy, luggage compartment door', 'крышка багажника', 'Крышка багажника', 'Luggage compartment door', 'luggage compartment door', 'Panel sub-assy', 'panel sub-assy, back door', 'Panel sub-assy, back door']
        self.parts_rear_fender = []
        self.parts_glasses = []
        self.parts_srs_security = []
        self.parts_engine = []
        self.parts_number = []

    def read_file_for_hood(self, data, car_mark):
        average_price = []
        emex_prises = []
        for i in data:
            if i['title'] == SortedParts.body:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['name'] in self.parts_front_hood:
                            emex_prises.extend(emex_parser.main(k['number'], car_mark))
                            try:
                                price = int(k['price'])
                                name = k['name']
                                number = k['number']
                                average_price.append({
                                    'name': name,
                                    'price': price,
                                    'number': number,
                                })
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                name = k['name']
                                number = k['number']
                                average_price.append({
                                    'name': name,
                                    'price': price,
                                    'number': number,
                                })
        average_sum = 0
        if len(average_price) > 0:
            for i in average_price:
                price = i['price']
                average_sum += price
            average_sum = int(average_sum / len(average_price))
        elif len(average_price) == 0:
            average_sum = 0
        return average_sum, emex_prises

    def read_file_for_front_fender(self, data, car_mark):
        average_price_fender = []
        average_price_underfender = []
        emex_price_fender = []
        emex_price_underfender = []
        for i in data:
            if i['title'] == SortedParts.body:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['name'] in self.parts_front_fender:
                            try:
                                price = int(k['price'])
                                if k['name'] == 'подкрылок':
                                    emex_price_underfender.extend(emex_parser.main(k['number'], car_mark))
                                    average_price_underfender.append(price)
                                elif k['name'] == 'крыло':
                                    emex_price_fender.extend(emex_parser.main(k['number'], car_mark))
                                    average_price_fender.append(price)
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                if k['name'] == 'подкрылок':
                                    emex_price_fender.extend(emex_parser.main(k['number'], car_mark))
                                    average_price_underfender.append(price)
                                elif k['name'] == 'крыло':
                                    emex_price_fender.extend(emex_parser.main(k['number'], car_mark))
                                    average_price_fender.append(price)
        average_price_underfender_sum = 0
        average_price_fender_sum = 0
        if len(average_price_fender) > 0:
            for i in average_price_fender:
                average_price_fender_sum += i
            average_price_fender_sum = int(average_price_fender_sum / len(average_price_fender))
        elif len(average_price_fender) == 0:
            average_price_fender_sum = 'Не найдено'

        if len(average_price_underfender) > 0:
            for i in average_price_underfender:
                average_price_underfender_sum += i
            try:
                average_price_underfender_sum = int(average_price_underfender_sum / len(average_price_fender))
            except:
                average_price_underfender_sum = 'Не найдено'
        elif len(average_price_underfender) == 0:
            average_price_underfender_sum = 'Не найдено'
        return average_price_underfender_sum, average_price_fender_sum, emex_price_fender, emex_price_underfender

    def read_file_for_electric(self, data, car_mark):
        average_price_headlights = []
        emex_parts = []
        for i in data:
            if i['title'] == SortedParts.electric:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['name'] in self.parts_headlights:
                            emex_parts.extend(emex_parser.main(k['number'], car_mark))
                            try:
                                price = int(k['price'])
                                average_price_headlights.append(price)
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                average_price_headlights.append(price)
        average_price_headlights_sum = 0
        if len(average_price_headlights) > 0:
            for i in average_price_headlights:
                average_price_headlights_sum += i
            average_price_headlights_sum = int(average_price_headlights_sum / len(average_price_headlights))
        elif len(average_price_headlights) == 0:
            average_price_headlights_sum = 'Не найдено'
        return average_price_headlights_sum, emex_parts

    def read_file_for_front_bumper(self, data, car_mark):
        average_price_bumper = []
        emex_parts = []
        for i in data:
            if i['title'] == SortedParts.body:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['name'] in self.parts_front_bumper:
                            emex_parts.extend(emex_parser.main(k['number'], car_mark))
                            try:
                                price = int(k['price'])
                                average_price_bumper.append(price)
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                average_price_bumper.append(price)
        average_price_bumper_sum = 0
        if len(average_price_bumper) > 0:
            for i in average_price_bumper:
                average_price_bumper_sum += i
            average_price_bumper_sum = int(average_price_bumper_sum / len(average_price_bumper))
        elif len(average_price_bumper) == 0:
            average_price_bumper_sum = 'Не найдено'
        return average_price_bumper_sum, emex_parts

    def read_file_for_rear_bumper(self, data, car_mark):
        average_price_bumper = []
        emex_parts = []
        for i in data:
            if i['title'] == SortedParts.body:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['name'] in self.parts_rear_bumper:
                            emex_parts.extend(emex_parser.main(k['number'], car_mark))
                            try:
                                price = int(k['price'])
                                average_price_bumper.append(price)
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                average_price_bumper.append(price)
        average_price_bumper_sum = 0
        if len(average_price_bumper) > 0:
            for i in average_price_bumper:
                average_price_bumper_sum += i
            average_price_bumper_sum = int(average_price_bumper_sum / len(average_price_bumper))
        elif len(average_price_bumper) == 0:
            average_price_bumper_sum = 'Не найдено'
        return average_price_bumper_sum, emex_parts

    def read_file_for_rear_hood(self,data, car_mark):
        average_price_hood = []
        emex_parts = []
        for i in data:
            if i['title'] == SortedParts.body:
                for j in i['all_parts']:
                    for k in j['title']['attr']:
                        if k['name'] in self.parts_rear_hood:
                            emex_parts.extend(emex_parser.main(k['number'], car_mark))
                            try:
                                price = int(k['price'])
                                average_price_hood.append(price)
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                average_price_hood.append(price)
        average_price_hood_sum = 0
        if len(average_price_hood) > 0:
            for i in average_price_hood:
                average_price_hood_sum += i
            average_price_hood_sum = int(average_price_hood_sum / len(average_price_hood))
        elif len(average_price_hood) == 0:
            average_price_hood_sum = 'Не найдено'
        return average_price_hood_sum, emex_parts

    def read_file_for_rear_fender(self, data):
        pass

    def read_file_for_glasses(self,data):
        pass

    def read_file_for_srs_security(self, data):
        pass

    def read_file_for_engine(self, data):
        pass

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



# if __name__ == '__main__':
#-----------------------------------------------------------------------------------------------------------------------Start def sorted HOOD
def start_sorted_hood(data, mark):
    class_hood = SortedParts()
    epc_average_price_hood, emex_price_hood = class_hood.read_file_for_hood(data, mark)
    try:
        print(f'Средняя цена капота по AMAYAMA: {epc_average_price_hood} RUB\nМаксимальная цена капота по EMEX: {max(emex_price_hood)} RUB')
    except:
        print('Произошла ошибка, цены по капотам не найдены!')

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
    average_price_underfender, average_price_fender, max_price_fender_emex, max_price_underfender_emex = class_front_fender.read_file_for_front_fender(data, mark)
    try:
        print(f'Средняя цена крыла: {average_price_fender} RUB\nСредняя цена подкрылка: {average_price_underfender} RUB\nМаксимальная цена крыла по EMEX {max(max_price_fender_emex)} RUB\nМаксимальная цена подкрылка по EMEX {max(max_price_underfender_emex)} RUB')
    except ValueError:
        print(f'Произошла ошибка, цены по крыльям не найдены!')
#-----------------------------------------------------------------------------------------------------------------------Start def sorted REAR FENDER
def start_sorted_rear_fender(data):
    pass

#-----------------------------------------------------------------------------------------------------------------------Start def sorted HEADLIGHTS
def start_sorted_headlights(data, mark):
    class_headlights = SortedParts()
    average_price_headlights, emex_max_price_headlights = class_headlights.read_file_for_electric(data, mark)
    try:
        print(f'Средняя цена фары по AMAYAMA: {average_price_headlights} RUB\nМаксимальная цена фары по EMEX: {max(emex_max_price_headlights)}')
    except ValueError:
        print('Произошла ошибка, цены по фарам не найдены!')
#-----------------------------------------------------------------------------------------------------------------------Start def sorted FRONT BUMPER
def start_sorted_front_bumper(data, mark):
    class_front_bumper = SortedParts()
    average_price_front_bumper, emex_max_price_front_bumper = class_front_bumper.read_file_for_front_bumper(data, mark)
    try:
        print(f'Средняя цена переднего бампера AMAYAMA: {average_price_front_bumper} RUB\nМаксимальная цена переднего бампера по EMEX: {max(emex_max_price_front_bumper)} RUB')
    except ValueError:
        print('Произошла ошибка, цены по бамперам не найдены!')

#-----------------------------------------------------------------------------------------------------------------------Start def sorted REAR BUMPER
def start_sorted_rear_bumper(data, mark):
    class_rear_bumper = SortedParts()
    average_price_rear_bumper, emex_max_price_rear_bumper = class_rear_bumper.read_file_for_rear_bumper(data, mark)
    try:
        print(f'Средняя цена заднего бампера: {average_price_rear_bumper} RUB\nМаксимальная цена переднего бампера по EMEX: {max(emex_max_price_rear_bumper)} RUB')
    except ValueError:
        print('Произошла ошибка, цены по бамперам не найдены!')

#-----------------------------------------------------------------------------------------------------------------------Start def sorted REAR HOOD (BACK DOOR)
def start_sorted_rear_hood(data, mark):
    class_rear_hood = SortedParts()
    average_price_rear_hood, emex_max_price_rear_hood = class_rear_hood.read_file_for_rear_hood(data, mark)
    try:
        print(f'Средняя цена крышки багажника: {average_price_rear_hood} RUB\nМаксимальная цена крышки багажника по EMEX: {max(emex_max_price_rear_hood)}')
    except ValueError:
        print(f'Произошла ошибка, цены по багажникам не найдены!')

#-----------------------------------------------------------------------------------------------------------------------Def input and sorted with class part
def start_main(mark_m, model_m, year_m):
    car_mark = mark_m
    car_model = model_m
    file_year = year_m
    with open(f'models/{car_mark}/{car_model}/{file_year}') as file:
        data_file = json.load(file)
    start_sorted_hood(data_file, car_mark)
    # start_sorted_numbers(data_file, car_mark)
    start_sorted_front_fender(data_file, car_mark)
    start_sorted_headlights(data_file, car_mark)
    start_sorted_front_bumper(data_file, car_mark) #Требует доработки
    start_sorted_rear_bumper(data_file, car_mark) #Требует доработки по сути одинаковы
    start_sorted_rear_hood(data_file, car_mark)