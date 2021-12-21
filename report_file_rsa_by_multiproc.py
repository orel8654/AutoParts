import asyncio
import os
import json
import re
import random

def get_response(iframe):
    from config import RUCAPTCHA_API_TOKEN
    import requests
    import time

    r = requests.get(
        f'http://rucaptcha.com/in.php?key={RUCAPTCHA_API_TOKEN}&method=userrecaptcha&googlekey={iframe}&pageurl=https://prices.autoins.ru/priceAutoParts')
    id_res = r.text.split('|')[-1]
    cnt = 0
    delay = 30
    time.sleep(delay)
    while True:
        res = requests.get(f'http://rucaptcha.com/res.php?key={RUCAPTCHA_API_TOKEN}&action=get&id={id_res}')
        if cnt != 7:
            if res.text == 'CAPCHA_NOT_READY':
                time.sleep(5)
                res = requests.get(f'http://rucaptcha.com/res.php?key={RUCAPTCHA_API_TOKEN}&action=get&id={id_res}')
                res = res.text.split('|')[-1]
                print(res)
                cnt += 1
                delay = 10
                continue
            else:
                res = res.text.split('|')[-1]
                print(res)
                return res
        else:
            return 'CAPCHA_NOT_READY'

def get_and_safe_content(number, car_mark, link, part_name, vin):
    from seleniumwire import webdriver
    from selenium.webdriver.chrome.options import Options
    from config import PROXY_LIST
    import time

    options_proxy = {
        'proxy': {
            'https': random.choice(PROXY_LIST),
        }
    }
    options = Options()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36')
    options.add_argument('--disable-notifications')
    options.add_argument("--mute-audio")
    options.add_argument('--headless')
    options.add_argument("--disable-extensions")
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(
        executable_path='/Users/egororlov/Desktop/autoparts/webdriver/chromedriver',
        options=options,
        seleniumwire_options=options_proxy,
    )
    try:
        # ---------------------------------------------------------------------------------------------------------------ENTER TO SITE
        driver.get('https://prices.autoins.ru/priceAutoParts')
        time.sleep(2)

        # ---------------------------------------------------------------------------------------------------------------INPUT DATE
        driver.find_element_by_xpath('//*[@id="versionDate"]').click()  #
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[4]").click()  #

        # ---------------------------------------------------------------------------------------------------------------INPUT REGION
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[3]/div/div[2]/b').click()  #
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[3]/div/div[3]/div/ul/li[10]').click()  #

        # ---------------------------------------------------------------------------------------------------------------INPUT CAR MARK
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[2]/b').click()  #
        if car_mark.lower() == 'subaru':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[53]').click()  #
            time.sleep(1)
        elif car_mark.lower() == 'nissan':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[42]').click()
            time.sleep(1)
        elif car_mark.lower() == 'toyota':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[55]').click()  #
            time.sleep(1)
        elif car_mark.lower() == 'honda':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[23]').click()
            time.sleep(1)
        elif car_mark.lower() == 'mazda':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[36]').click()
            time.sleep(1)
        elif car_mark.lower() == 'mitsubishi':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[41]').click()
            time.sleep(1)
        elif car_mark.lower() == 'suzuki':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[54]').click()
            time.sleep(1)
        elif car_mark.lower() == 'acura':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[2]').click()
            time.sleep(1)
        elif car_mark.lower() == 'audi':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[3]').click()
            time.sleep(1)
        elif car_mark.lower() == 'bmw':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[4]').click()
            time.sleep(1)
        elif car_mark.lower() == 'cadillac':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[6]').click()
            time.sleep(1)
        elif car_mark.lower() == 'chery':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[7]').click()
            time.sleep(1)
        elif car_mark.lower() == 'chevrolet':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[8]').click()
            time.sleep(1)
        elif car_mark.lower() == 'ford':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[18]').click()
            time.sleep(1)
        elif car_mark.lower() == 'hyundai':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[24]').click()
            time.sleep(1)
        elif car_mark.lower() == 'infiniti':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[25]').click()
            time.sleep(1)
        elif car_mark.lower() == 'kia':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[30]').click()
            time.sleep(1)
        elif car_mark.lower() == 'lexus':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[33]').click()
            time.sleep(1)
        elif car_mark.lower() == 'porsche':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[45]').click()
            time.sleep(1)
        elif car_mark.lower() == 'volkswagen':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[57]').click()
            time.sleep(1)

        # ---------------------------------------------------------------------------------------------------------------INPUT PART NUMBER
        class_part = driver.find_element_by_xpath('//*[@id="article1"]')  #
        class_part.send_keys(number)  #

        # ---------------------------------------------------------------------------------------------------------------TEXT AREA AND INPUT RECAPTCHA
        iframes = driver.find_element_by_class_name('g-recaptcha').get_attribute('data-sitekey')  #
        element = driver.find_element_by_css_selector(
            '#g-recaptcha-response[style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"]')  #
        driver.execute_script(
            'arguments[0].setAttribute("style","width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 100px 25px; padding: 0px; resize: none;")',
            element)
        element2 = driver.find_element_by_xpath('//*[@id="g-recaptcha-response"]')  #
        time.sleep(0.3)
        res = get_response(iframes)
        time.sleep(0.3)
        element2.send_keys(res)  #

        # ---------------------------------------------------------------------------------------------------------------INPUT REQUEST PAT NUMBER
        driver.find_element_by_css_selector(
            'body > div.page-wrapper > section > div > div:nth-child(8) > input:nth-child(3)').click()  #
        time.sleep(2)

        # ---------------------------------------------------------------------------------------------------------------SCRAPE DATA
        number = number
        try:
            '''
            DON'T TOUCH 

            //*[@id="resultTableOfOnlyOriginSpares"]/tbody/tr[2]/td[3]

            '''
            price = driver.find_element_by_xpath('//*[@id="resultTableOfOnlyOriginSpares"]/tbody/tr[2]/td[3]').text  #
        except:
            try:
                price = driver.find_element_by_xpath(
                    '//*[@id="resultTableOfOnlyOriginSpares"]/tbody/tr[4]/td[3]').text  #
            except:
                price = 'Цена не найдена'

        driver.quit()

        with open(f'reports_rsa/{vin.upper()}.txt', 'a+') as file:
            file.write(f'Ссылка: {link},\nНазвание запчасти: {part_name.upper()},\nНомер запчасти: {number.upper()},\nСтоимость РСА: {price}\n\n')
        file.close()

        # return f'Номер детали = {number.upper()}\nЦена по РСА = {price}'

    except Exception as ex:
        print(f'recaptcha\ngeneral_loop\n{ex}')
        driver.quit()
        with open(f'reports_rsa/{vin.upper()}.txt', 'a+') as file:
            file.write(f'Ссылка: {link},\nНазвание запчасти: {part_name.upper()},\nНомер запчасти: {number.upper()},\nСтоимость РСА: Не найдено!\n\n')
        file.close()
        # return f'Что-то пошло не так, пожалуйста повторите попытку позже, либо измените параметры!'


async def create_process(data, vin, car_mark):
    import multiprocessing

    tasks = []
    for i in data:
        if i["number"] != '':
            try:
                if int(i["price"]) > 1000:
                    task = multiprocessing.Process(target=get_and_safe_content, args=(i["number"], car_mark, i["link"], i["name"], vin,))
                    tasks.append(task)
            except:
                continue
    count = 0
    for j in tasks:
        j.start()
        print('new proc')
        if count >= 5:
            count = 0
            await asyncio.sleep(65)
        count += 1

    for j in tasks:
        j.join()

# if __name__ == '__main__':
#     asyncio.run(main('subaru', 'двигатель'))