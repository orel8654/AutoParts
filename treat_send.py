import json
import time
import re
from pathlib import Path
import sorting_with_class

def valid_folder(car_mark, car_model): #-------------------------------------------HAVE OR NOT FILE IN DIRECTORY
    path = Path(f'models/{car_mark}/{car_model}')
    subdirs = []
    files = []
    for i in path.iterdir():
        if i.is_dir():
            subdirs.append(i)
        else:
            files.append(i)
    return files

def recompile_file(folder, year): #------------------------------------RETURN ONE FILE
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

#---------------------------------------------------------------------------------------------CALL IN SORTED_WITH_CLASS
    sorting_with_class.start_main(car_mark, car_model, one_file)

#---------------------------------------------------------------------------------------------NOTES
'''
Note
'''