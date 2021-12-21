import asyncio
import report_file_rsa
import aiohttp


DATA = []
CAR_MARK = ''

async def get_html(link):
    import requests
    import config

    res = requests.get(link, headers=config.HEADERS)
    return res.text

async def check_price(link):
    from bs4 import BeautifulSoup

    cost = 0
    data = []
    response = await get_html(link)
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find('tr', class_='parts-in-stock-widget_part-row')
    try:
        price = items.find('td', class_='priceRangeContainer').find_next('strong').get_text(strip=True)
        try:
            price = price.replace('руб.', '').strip()
            price = price.replace('\xa0', '').strip()
            price = price.split('до')[-1]
            try:
                price = int(price)
            except Exception as ex:
                print(ex)
                price = 0
        except:
            price = 0
    except Exception as ex:
        price = 0

    try:
        name = soup.find('tr', class_='top').find_next('h4').get_text(strip=True)
        name = name.split(':')[-1]
    except:
        name = 'Не найдено'

    if price > cost:
        cost = price
        data = {
            'name': name,
            'number': items.find('b', class_='parts-in-stock-widget_part-oem').find_next('strong').get_text(strip=True),
            'price': price,
            'link': link,
        }
        print(data)


    DATA.append(data)


async def get_list_parts(html):
    from bs4 import BeautifulSoup
    import config

    tasks = []
    data = []
    cost = 0
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('td', class_='ama-schema-td detail_list')
    for i in items:
        links = i.find_all('a')
        for j in links:
            link = j.get('href')
            task = asyncio.create_task(check_price(link))
            tasks.append(task)
    await asyncio.gather(*tasks)
        #     response = await get_html(link)
        #     soup = BeautifulSoup(response, 'lxml')
        #     items = soup.find('tr', class_='parts-in-stock-widget_part-row')
        #     try:
        #         price = items.find('td', class_='priceRangeContainer').find_next('strong').get_text(strip=True)
        #         try:
        #             price = price.replace('руб.', '').strip()
        #             price = price.replace('\xa0', '').strip()
        #             price = price.split('до')[-1]
        #             try:
        #                 price = int(price)
        #             except Exception as ex:
        #                 print(ex)
        #                 price = 0
        #         except:
        #             price = 0
        #     except Exception as ex:
        #         price = 0
        #
        #     try:
        #         name = soup.find('tr', class_='top').find_next('h4').get_text(strip=True)
        #         name = name.split(':')[-1]
        #     except:
        #         name = 'Не найдено'
        #
        #     if price > cost:
        #         cost = price
        #         data = {
        #             'name': name,
        #             'number': items.find('b', class_='parts-in-stock-widget_part-oem').find_next('strong').get_text(strip=True),
        #             'price': price,
        #             'link': link,
        #         }
        #         print(data)
        #     else:
        #         continue

        # DATA.append(data)


'''СОЗДАЕМ асинхронный список gather для парсинга всего остального'''
async def get_gather(html):
    from bs4 import BeautifulSoup
    import config

    all_links = []
    data = []
    tasks = []

    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('map', class_='detail-list')
    for i in items:
        links = i.find_all('a')
        for j in links:
            link = j.get('href')
            all_links.append(link)

    for i in all_links:
        response = await get_html(i)
        try:
            task = asyncio.create_task(get_list_parts(response))
            tasks.append(task)
        except Exception as ex:
            print(ex)
            continue
    await asyncio.gather(*tasks)



'''ПОСЛЕ ФУНКЦИИ main проходится по ссылкам кузова и электрике'''
async def parse_data(body_link, electric_link, car_link):

    data = []
    tasks = []

    car_mark = car_link.split('/')[-4]
    CAR_MARK = car_mark.split('-')[0]

    urls = [body_link, electric_link]


    for i in urls:

        task = asyncio.create_task(get_gather(await get_html(i)))
        tasks.append(task)

    await asyncio.gather(*tasks)

    # return data, car_mark


'''ПРИНИМАЕТ НОМЕР КУЗОВА'''
async def main(vin):
    from selenium import webdriver
    import config


    vin = vin['vin']
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')
    options.add_argument('--disable-notifications')
    options.add_argument("--mute-audio")
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path='/Users/egororlov/Desktop/autoparts/webdriver/chromedriver',
        options=options,
    )

    try:
        URL = config.LIST_MODEL1
        car_mark = ''
        category_body = ''
        category_electric = ''

        for i in URL:

            driver.get(i)
            await asyncio.sleep(1)
            input_data = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/form/input')
            input_data.send_keys(vin)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/form/button').click()
            await asyncio.sleep(1)
            try:
                category_body = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/h3[2]/a').get_attribute('href')
                category_electric = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/h3[4]/a').get_attribute('href')
                car_link = driver.current_url
            except:
                continue

        driver.quit()
        if category_body != '' and category_electric != '':
            await parse_data(category_body, category_electric, car_link)
            return DATA, CAR_MARK
        else:
            return '', ''

    except Exception as ex:
        print(f'Ошибка в report_file_rsa_with_parse\n{ex}')
        driver.quit()
        return '', ''


if __name__ == '__main__':
    asyncio.run(main('ENY34250622'))