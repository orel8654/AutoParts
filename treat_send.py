'''
Прием сообщения и обработка
'''
import json
import time
import re
from pathlib import Path
import sorting_with_class

#-----------------------------------------------------------------------------------------------------------------------HAVE OR NOT FILE IN DIRECTORY
def valid_folder(car_mark, car_model):
    path = Path(f'models/{car_mark}/{car_model}')
    subdirs = []
    files = []
    for i in path.iterdir():
        if i.is_dir():
            subdirs.append(i)
        else:
            files.append(i)
    return files

#-----------------------------------------------------------------------------------------------------------------------RETURN ONE FILE
def recompile_file(folder, year):
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

#-----------------------------------------------------------------------------------------------------------------------SORTED DATA IN FILE (don't delete!)
def sorted_data_in_file(car_mark, car_model, car_spec):
    files = valid_folder(car_mark, car_model)  # Get PATH FOLDER
    one_file = recompile_file(files, car_spec)  # Get FILE NAME
    return one_file
#-----------------------------------------------------------------------------------------------------------------------CALL IN SORTED_WITH_CLASS
def call_in_sorted_with_class(car_mark, car_model, one_file, check_sort_category):
    return sorting_with_class.start_main(car_mark, car_model, one_file, check_sort_category)

#-----------------------------------------------------------------------------------------------------------------------INPUT DATA
def input_main(data):
    model = data['general'].split(',')
    car_mark = model[0].strip().lower()
    car_model = model[1].strip().replace(' ', '-').lower()
    car_spec = model[-1].strip()
    category = data['category']
    try:
        one_file = sorted_data_in_file(car_mark, car_model, car_spec)
        mes_ret = call_in_sorted_with_class(car_mark, car_model, one_file, category)
        return mes_ret
    except:
        return 'Неправильно введены данные, либо данные о машине отсутвуют!'

if __name__ == '__main__':
    lst = ['фара']
    input_main(car_mark='toyota', car_model='allex', car_spec='2001', class_sorted_category=lst)

#-----------------------------------------------------------------------------------------------------------------------NOTES
'''
Из телеграма передается марка машины, модель машины, год начала производства, список запчастей, если списка запчастей не передано, то считается все запчасти в машине
'''