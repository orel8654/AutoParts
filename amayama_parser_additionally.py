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
        except Exception:
            continue
    lst_dict.append({
        'name': name,
        'link': link,
        'price': price,
        'number': number,
    })
    return lst_dict

def check_out(url):
    html = get_html(url).text
    return get_content(html)

def get_content_spec(html):
    lst_dict = []
    soup = BeautifulSoup(html, 'lxml')
    try:
        items = soup.find('div', class_='list')
        all_links = items.find_all('a')
        for i in all_links:
            link = i.get('href')
            lst_dict.append('https://www.amayama.com' + link)
        return lst_dict
    except:
        return None

def pre_content_checkout(html):
    lst_dict = []
    soup = BeautifulSoup(html, 'lxml')
    try:
        items = soup.find('div', class_='list')
        all_links = items.find_all('a')
        for i in all_links:
            link = i.get('href')
            lst_dict.append('https://www.amayama.com' + link)
        return lst_dict
    except:
        return None

def get_all_items_category(html):
    lst_links = []
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='schemas-list-item')
    try:
        for i in items:
            link = i.find('a').get('href')
            lst_links.append(link)
    except:
        link = None
        lst_links.append(link)
    return lst_links

def main(car_mark, car_model):
    list_links = []
    all_categories = []
    all_acces = []
    all_items_category = []
    all_pre_items_category = []
    all_return_items = []
    all_return_items_complete = []
    html = get_html(f'https://www.amayama.com/ru/catalogs/{car_mark}/{car_model}').text
    check = get_content_spec(html)
    if check != None:
        list_links.extend(check)
        for i in list_links:
            html = get_html(i).text
            all_acces.append(pre_content_checkout(html))
        for i in all_acces:
            for j in i:
                html = get_html(j).text
                all_items_category.extend(get_all_items_category(html))
            all_pre_items_category.append(all_items_category)
        for i in all_pre_items_category:
            for j in i:
                try:
                    html = get_html('https://www.amayama.com' + j).text
                    all_return_items.extend(get_content(html))
                except:
                    continue
            all_return_items_complete.extend(all_return_items)
            print(all_return_items_complete)
    else:
        print('Информации о машине не найдено!')

if __name__ == '__main__':
    main(car_mark='nissan', car_model='elgrand')