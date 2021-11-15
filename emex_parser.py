from bs4 import BeautifulSoup
import requests
from config import *

def get_html(url):
    s = requests.Session()
    r = s.get(url, headers=HEADERS)
    return r

def get_content(html):
    em_price = []
    soup = BeautifulSoup(html, 'lxml')
    try:
        items = soup.find_all('div', class_='po743by')
        for item in items:
            prices = item.find_all('div', class_='pd8jfdj')
            for price in prices:
                cost = price.find('span', class_='prcggmh').get_text(strip=True)
                cost = cost.replace(' ', '')
                cost = cost.replace('от', '')
                em_price.append(int(cost))
        return em_price
    except:
        return em_price.append('0')

def main(number, mark):
    part_price = []
    url = f'https://emex.ru/products/{number}/{mark}/33271'
    html = get_html(url).text
    part_price.extend(get_content(html))
    return part_price

if __name__ == '__main__':
    main('57229AG0009P', 'subaru')