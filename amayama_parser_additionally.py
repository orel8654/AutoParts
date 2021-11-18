import requests
from config import HEADERS
from bs4 import BeautifulSoup

def get_html(url):
    s = requests.Session()
    r = s.get(url, headers=HEADERS)
    return r

def get_content(html):
    price = 0
    link = ''
    name = ''
    number = ''
    lst_dict = []
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('tr', class_='map-item link')
    for i in items:
        try:
            price_bs = i.find('td', class_='price').get_text(strip=True).replace('\xa0', '')
            if int(price_bs) > price:
                price = int(price_bs)
                link = 'https://www.amayama.com' + i.get('data-url')
                name = i.find('td', class_='name').get_text(strip=True)
                number = i.find('td', class_='number').find_next('a').get_text(strip=True)
        except TypeError:
            continue
    lst_dict.append({
        'name': name,
        'link': link,
        'price': price,
        'number': number,
    })
    return lst_dict

def main(url):
    html = get_html(url).text
    get_content(html)

if __name__ == '__main__':
    main('https://www.amayama.com/ru/catalogs/nissan/elgrand/1-van-3-right-e50-2000-r-1546/body-parts-6/hood-panel-hinge-fitting-body-571')