import json
import requests
import emex_parser
from config import LIST_HOOD, LIST_FRONT_FENDER, LIST_HEADLIGHTS, LIST_FRONT_BUMPER, LIST_REAR_BUMPER, LIST_REAR_HOOD, LIST_REAR_FENDER, LIST_GLASSES_WINDSHIELD, LIST_GLASSES_DOORS, LIST_GLASSES_BACK, LIST_SRS_SECURITY, LIST_ENGINE, LIST_DOORS, CATEGORY_ENGINE, CATEGORY_BODY, CATEGORY_ELECTRIC, CATEGORY_TRANSMISSION
from functools import reduce


#-----------------------------------------------------------------------------------------------------------------------TEST MOST BIGGER COST PART
list_cars = ['3-suv-left-n180-1999-r-3210.json', '4-suv-left-n210-2002-3211.json', '4-suv-left-n210-2005-r-3207.json']

for item in list_cars:
    with open(f'models/toyota/4runner/{item}', 'r') as file:
        data = json.load(file)
    max_cost = []
    for i in data:
        if i['title'] == CATEGORY_BODY:
            for j in i['all_parts']:
                for k in j['title']['attr']:
                    try:
                        if k['name'].lower() in LIST_HOOD:
                            try:
                                price = int(k['price'])
                                max_dict = {
                                    'link': k['link'],
                                    'number': k['number'],
                                    'price': price,
                                }
                                max_cost.append(max_dict)
                            except:
                                price = int(k['price'].replace('\xa0', ''))
                                max_dict = {
                                    'link': k['link'],
                                    'number': k['number'],
                                    'price': price,
                                }
                                max_cost.append(max_dict)
                    except:
                        continue
