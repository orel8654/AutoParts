'''
Прием сообщения и обработка
'''
import json
import time
import re
from pathlib import Path, PurePosixPath
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
    for i in folder:
        file = str(PurePosixPath(i))
        file = file.split('/')
        if file[-1] != '.DS_Store':
            file = file[-1].split('-')
            try:
                file = int(file[-2])
                if file == int(year):
                    file = i
                    break
                else:
                    continue
            except:
                file = int(file[-3])
                if file == int(year):
                    file = i
                    break
                else:
                    continue
    if file != '':
        file = str(PurePosixPath(i))
        file = file.split('/')[-1]
        return file
    else:
        return None

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
    car_mark = model[0].strip().lower().replace(' ', '-')
    car_model = model[1].strip().lower().replace(' ', '-')
    car_spec = model[-1].strip().lower()
    category = data['category']
    try:
        one_file = sorted_data_in_file(car_mark, car_model, car_spec)
        mes_ret = call_in_sorted_with_class(car_mark, car_model, one_file, category)
        return mes_ret
    except Exception as ex:
        print(f'treat_send\ninput_main\n{ex}')
        return 'Неправильно введены данные, либо данные о машине отсутвуют!'

if __name__ == '__main__':
    lst = {'general': 'toyota, allex, 2001', 'category':'Список позиций'}
    # print(input_main(lst))

#-----------------------------------------------------------------------------------------------------------------------NOTES
'''
Из телеграма передается марка машины, модель машины, год начала производства, список запчастей, если списка запчастей не передано, то считается все запчасти в машине
'''