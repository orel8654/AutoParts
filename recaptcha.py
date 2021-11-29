import asyncio

async def get_response(iframe):
    from config import RUCAPTCHA_API_TOKEN
    import requests
    import time

    r = requests.get(f'http://rucaptcha.com/in.php?key={RUCAPTCHA_API_TOKEN}&method=userrecaptcha&googlekey={iframe}&pageurl=https://prices.autoins.ru/priceAutoParts')
    id_res = r.text.split('|')[-1]
    cnt = 0
    delay = 30
    while True:
        # time.sleep(delay)
        await asyncio.sleep(delay)
        res = requests.get(f'http://rucaptcha.com/res.php?key={RUCAPTCHA_API_TOKEN}&action=get&id={id_res}')
        if cnt !=9:
            if res.text == 'CAPCHA_NOT_READY':
                # time.sleep(5)
                await asyncio.sleep(5)
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


async def find_past(part_number, car_mark):
    import time
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')
    options.add_argument('--disable-notifications')
    options.add_argument("--mute-audio")
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path='/Users/egororlov/Desktop/autoparts/webdriver/chromedriver',
        options=options,
    )
    try:

        #---------------------------------------------------------------------------------------------------------------ENTER TO SITE
        driver.get('https://prices.autoins.ru/priceAutoParts')
        # time.sleep(2)
        await asyncio.sleep(2)


        #---------------------------------------------------------------------------------------------------------------INPUT DATE
        driver.find_element_by_xpath('//*[@id="versionDate"]').click()
        # time.sleep(1)
        await asyncio.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[5]").click()


        #---------------------------------------------------------------------------------------------------------------INPUT REGION
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[3]/div/div[2]/b').click()
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[3]/div/div[3]/div/ul/li[10]').click()
        # time.sleep(1)


        #---------------------------------------------------------------------------------------------------------------INPUT CAR MARK
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[2]/b').click()
        if car_mark.lower() == 'subaru':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[53]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'nissan':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[42]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'toyota':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[55]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'honda':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[23]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'mazda':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[36]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'mitsubishi':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[41]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'suzuki':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[54]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'acura':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[2]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'audi':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[3]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'bmw':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[4]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'cadillac':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[6]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'chery':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[7]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'chevrolet':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[8]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'ford':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[18]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'hyundai':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[24]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'infiniti':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[25]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'kia':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[30]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'lexus':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[33]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'porsche':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[45]').click()
            # time.sleep(1)
            await asyncio.sleep(1)
        elif car_mark.lower() == 'volkswagen':
            driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[57]').click()
            # time.sleep(1)
            await asyncio.sleep(1)


        #---------------------------------------------------------------------------------------------------------------INPUT PART NUMBER
        class_part = driver.find_element_by_xpath('//*[@id="article1"]')
        class_part.send_keys(part_number)


        #---------------------------------------------------------------------------------------------------------------TEXT AREA AND INPUT RECAPTCHA
        iframes = driver.find_element_by_class_name('g-recaptcha').get_attribute('data-sitekey')
        element = driver.find_element_by_css_selector('#g-recaptcha-response[style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"]')
        driver.execute_script('arguments[0].setAttribute("style","width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 100px 25px; padding: 0px; resize: none;")', element)
        element2 = driver.find_element_by_xpath('//*[@id="g-recaptcha-response"]')
        res = await get_response(iframes)
        element2.send_keys(res)
        # time.sleep(1)


        #---------------------------------------------------------------------------------------------------------------INPUT REQUEST PAT NUMBER
        driver.find_element_by_css_selector('body > div.page-wrapper > section > div > div:nth-child(8) > input:nth-child(3)').click()
        # time.sleep(1)
        await asyncio.sleep(1)


        #---------------------------------------------------------------------------------------------------------------SCRAPE DATA
        try:
            number = driver.find_element_by_xpath('//*[@id="resultTableOfOnlyOriginSpares"]/tbody/tr[2]/td[1]').text
        except:
            number = part_number
        try:
            part_name = driver.find_element_by_xpath('//*[@id="resultTableOfOnlyOriginSpares"]/tbody/tr[2]/td[2]').text
            if part_name == '':
                part_name = 'Не указано'
        except:
            part_name = 'Не указано'
        try:
            price = driver.find_element_by_xpath('//*[@id="resultTableOfOnlyOriginSpares"]/tbody/tr[2]/td[3]').text
            try:
                price = int(price)
            except:
                price = price
        except:
            price = 'Цена не указана'
        driver.quit()


        return f'Номер детали: {number}\nЦена по РСА: {price}\nНаименование запчасти: {part_name}'
    except Exception as ex:
        print(f'recaptcha\ngeneral_loop\n{ex}')
        driver.quit()
        return f'Что-то пошло не так, пожалуйста повторите попытку позже, либо измените параметры!'

# if __name__ == '__main__':
#     find_past('21460-VG100', 'nissan')
