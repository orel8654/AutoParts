import json
import time
import re
from pathlib import Path
import sorting_with_class

def test(data, num): #-------------------------------------------------------------------------worked test(eject data) on number
    for i in data:
        all_parts = i['all_parts']
        for j in all_parts:
            title = j['title']['attr']
            for k in title:
                try:
                    if k['number'] == num:
                        return k['price'], k['name'], k['link'], k['number']
                except:
                    return None

def valid_folder(car_mark, car_model): #-------------------------------------------worked test have or not file in folder
    path = Path(f'models/{car_mark}/{car_model}')
    subdirs = []
    files = []
    for i in path.iterdir():
        if i.is_dir():
            subdirs.append(i)
        else:
            files.append(i)
    return files

def recompile_file(folder, year): #------------------------------------worked test
    file = 'no'
    for i in folder:
        spec = str(i)
        spec = spec.split('-')
        try:
            spec = int(spec[-2])
            if str(spec) == str(year):
                file = i
                break
            else:
                continue
        except:
            spec = int(spec[-3])
            if str(spec) == str(year):
                file = i
                break
            else:
                continue
    if file != 'no':
        file = str(file)
        file = file.split('/')[-1]
        return file
    else:
        check = str(folder[-1]).split('/')[-1]
        return check


if __name__ == '__main__':
#---------------------------------------------------------------------------------------------INPUT DATA
    # car_mark = input('Введите марку машины: ').lower()
    # car_model = input('Введите название машины: ').replace(' ', '-').lower()
    # car_spec = input('Введите год производства: ').lower()
    car_mark = 'toyota'.lower()
    car_model = 'allex'.replace(' ', '-').lower()
    car_spec = '2004'.lower()

#---------------------------------------------------------------------------------------------SORTED DATA IN FILE (don't delete!)
    files = valid_folder(car_mark, car_model) #Get PATH FOLDER
    one_file = recompile_file(files, car_spec) #Get FILE NAME

#---------------------------------------------------------------------------------------------OPEN FILE and GET DATA (CALL IN SORTED CLASS)
    with open(f'models/{car_mark}/{car_model}/{one_file}', 'r') as file:
        data = json.load(file)

#---------------------------------------------------------------------------------------------ADD PARTS NUMBERS
    # num = []
    # while True:
    #     try:
    #         part_number = input('Введите номер детали, по одному за раз, если больше не хотите добавлять введите цифру - 1: ')
    #         if part_number != '1':
    #             num.append(part_number)
    #         else:
    #             break
    #     except Exception as ex:
    #         break

#---------------------------------------------------------------------------------------------SENDING INFO IN TELEGRAM
    # sum = 0
    # all_sum = []
    # all_name = []
    # all_links = []
    # all_numbers = []
    # for i in num:
    #     price_cost, name, link, number = test(data, i)
    #     try:
    #         sum += int(price_cost)
    #         all_sum.append(int(price_cost))
    #         all_links.append(link)
    #         all_name.append(name)
    #         all_numbers.append(number)
    #     except Exception as ex:
    #         if price_cost == None or price_cost == 'null' or price_cost == 'Нет в наличии':
    #             sum += 0
    #             all_sum.append('Нет в наличии')
    #             all_name.append(name)
    #             all_links.append(link)
    #             all_numbers.append(number)
    #         else:
    #             sum += int(price_cost.replace('\xa0', ''))
    #             all_sum.append(int(price_cost.replace('\xa0', '')))
    #             all_name.append(name)
    #             all_links.append(link)
    #             all_numbers.append(number)
    #
    # print(f'Сумма запчастей = {sum}')
    # print(f'Наименования деталей {all_name}\nСтоимость {all_sum}\nСсылки {all_links}\nНомера деталей {all_numbers}')

#---------------------------------------------------------------------------------------------NOTES
'''
Note
'''