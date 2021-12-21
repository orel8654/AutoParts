import asyncio
import datetime
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures

lst_data_dict = []
sem = asyncio.Semaphore(8)
sem1 = asyncio.Semaphore(5)
executor = ThreadPoolExecutor(5)

'''----------------Принимает марку машины, VIN/кузов, номер детали, название деталии считает в РСА иожно передать ID из телеги--------------'''
async def parsing_data(car_mark, vin, number, part_name, link):
    import recaptcha

    async with sem:
        print(f'Отправка в RECAPTCHA {vin.upper()}')
        await asyncio.sleep(0.1)
        res_captcha = await recaptcha.find_past(number, car_mark)
        await asyncio.sleep(0.1)
        res = (f'Ссылка = {link}\nНазвание запчасти = {part_name}\n{res_captcha}\n\n')
    print(res)

    with open(f'reports_rsa/{vin.upper()}.txt', 'a+') as file:
        file.write(res)
    file.close()


'''---------------------------------Принимает отсортированный список, марку машины и VIN/кузов (ПОКА ЧТО ПРОПУСКАЕМ)---------------------------------'''
async def callback_pars(data, car_mark='subaru', vin=datetime.datetime.now()):
    tasks = []
    lst = []
    for i in data:
        if i['number'] != '':
            try:
                if int(i['price']) > 5000:
                    task = asyncio.create_task(parsing_data(car_mark, vin, i["number"], i["name"], i["link"]))
                    tasks.append(task)
            except:
                continue

    await asyncio.gather(*tasks)


'''---------------------------------Принимает и сортирует кузов и электрику---------------------------------'''
async def sorting_data(data):
    import re

    lst = []
    for i in data:
        '''
        ДОБАВЛЕНА КАТЕГОРИЯ "АКСЕССУАРЫ" ДЛЯ ПОДСЧЕТА
        '''
        if re.search('кузов', i['title'].lower()) or re.search('электрика', i['title'].lower()) or re.search('аксессуары', i['title'].lower()):
            for j in i['all_parts']:
                for k in j['title']['attr']:
                    lst.append(k)
    return lst


'''---------------------------------Принимает ссылку на AMAYAMA---------------------------------'''
async def find_and_read_file(link):
    import json
    car_mark = ''
    try:
        car_mark = link.split('/')[-3].strip()
        car_model = link.split('/')[-2].strip()
        car_spec = link.split('/')[-1].strip()
        with open(f'models/{car_mark}/{car_model}/{car_spec}.json', 'r') as file:
            data = json.load(file)
        data_sort = await sorting_data(data)
        return data_sort, car_mark

    except:
        return ''



'''---------------------------------Принимает марку машины, спецификацию, год для моделей JAPAN---------------------------------'''
async def find_and_read_file_japan(car_mark, car_spec, year):

    async def sorting_data_japan():
        pass

    import json
    import os

    spec = ''
    data = []
    data2 = []
    try:
        directory = f'models/{car_mark}/{car_spec}'
        files = os.listdir(directory)
        for i in files:
            try:
                file = i.split('-')[-3]
                file = int(file)
                count = int(year) - file
                if count > 0:
                    data.append({
                        'diff': count,
                        'spec': i,
                    })
                    data2.append(count)
            except:
                file = i.split('-')[-2]
                file = int(file)
                count = int(year) - file
                if count > 0:
                    data.append({
                        'diff': count,
                        'spec': i,
                    })
                    data2.append(count)
        count = 0
        min_diff = min(data2)
        for i in data:
            if i['diff'] == min_diff:
                spec = i['spec']
        with open(f'models/{car_mark}/{car_spec}/{spec}', 'r') as file:
            data = json.load(file)
        data_sort = await sorting_data(data)

        return data_sort, car_mark

    except:
        return ''


'''---------------------------------Принимает VIN или номер кузова с маркой машины---------------------------------'''
async def main(vin):
    from selenium import webdriver
    import time
    import config
    import aiohttp

    vin = vin['vin']
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')
    options.add_argument('--disable-notifications')
    options.add_argument("--mute-audio")
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path='webdriver/chromedriver',
        options=options,
    )

    try:
        URL = config.LIST_MODEL1
        car_name = ''
        for i in URL:

            driver.get(i)
            await asyncio.sleep(1)
            input_data = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/form/input')
            input_data.send_keys(vin)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/form/button').click()
            await asyncio.sleep(1)
            try:
                if driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/a[1]/div'):
                    car_name = driver.current_url
                    driver.quit()
                    return await find_and_read_file(car_name)
            except:
                '''
                НОВАЯ ОБРАБОТКА С JAPAN
                '''
                try:
                    if driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/h3[2]/a'):
                        link = driver.current_url
                        car_name = link.split('/')[-4]
                        car_name = car_name.split('-')[0]
                        car_spec = link.split('/')[-3]
                        car_spec = car_spec.split('_')[0]
                        year = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]').text
                        year = year.split('.')[-1]
                        return await find_and_read_file_japan(car_name, car_spec, year)
                except:
                    continue
        driver.quit()

        return await find_and_read_file(car_name)

    except Exception as ex:
        print(f'Ошибка в report_file_rsa\n{ex}')
        driver.quit()
        return '', ''


# if __name__ == '__main__':
#     data, car_mark = asyncio.run(main('bl5013130'))
#     print('HERE')
#     asyncio.run(callback_pars(data, car_mark, 'bl5013130'))
    # data, car_mark = loop.run_until_complete(main('bl5013130'))
    # print('HERE')
    # loop.run_until_complete(callback_pars(data, car_mark, 'bl5013130'))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    '''Передается ТОЛЬКО ВИН'''
    try:
        '''Передается ТОЛЬКО ВИН'''
        data, car_mark = loop.run_until_complete(main('eny34250622'))
        '''Второй запрос передает сортированный список запчастей, марка машины и вин для записи в файл'''
        # loop.run_until_complete(callback_pars(data, car_mark, 'bl5013130'))
        '''Третий открывает и отправляет файл пользователю'''
        print(data)
    except:
        print('Авто нет в базе!')
    # sorting_lst = loop.run_until_complete(sorting_data(data))
    # asyncio.run(callback_pars(data, 'bl5013130'))
    # print(lst_data_dict)
