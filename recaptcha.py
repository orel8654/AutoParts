import time
import requests
from config import RUCAPTCHA_API_TOKEN, HEADERS
from selenium import webdriver
from datetime import datetime

def get_response(iframe):
    r = requests.get(f'http://rucaptcha.com/in.php?key={RUCAPTCHA_API_TOKEN}&method=userrecaptcha&googlekey={iframe}&pageurl=https://prices.autoins.ru/priceAutoParts')
    id_res = r.text.split('|')[-1]
    cnt = 0
    delay = 30
    while True:
        time.sleep(delay)
        res = requests.get(f'http://rucaptcha.com/res.php?key={RUCAPTCHA_API_TOKEN}&action=get&id={id_res}')
        if cnt !=9:
            if res.text == 'CAPCHA_NOT_READY':
                time.sleep(5)
                res = requests.get(f'http://rucaptcha.com/res.php?key={RUCAPTCHA_API_TOKEN}&action=get&id={id_res}')
                res = res.text.split('|')[-1]
                # print(res)
                cnt += 1
                delay = 10
                continue
            else:
                res = res.text.split('|')[-1]
                # print(res)
                return res
        else:
            return 'CAPCHA_NOT_READY'

def find_past(part_number, car_mark):
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
        time.sleep(2)

        #---------------------------------------------------------------------------------------------------------------INPUT DATE
        # date = datetime.now().date().strftime('%d.%m.%Y')
        class_date = driver.find_element_by_xpath('//*[@id="versionDate"]').click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[5]").click()

        #---------------------------------------------------------------------------------------------------------------INPUT REGION
        class_region = driver.find_element_by_xpath('//*[@id="newRequest"]/div[3]/div/div[2]/b').click()
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[3]/div/div[3]/div/ul/li[10]').click()
        time.sleep(1)
        #---------------------------------------------------------------------------------------------------------------INPUT CAR MARK
        driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[2]/b').click()
        if car_mark.lower() == 'subaru':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[53]').click()
            time.sleep(1)
        elif car_mark.lower() == 'nissan':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[42]').click()
            time.sleep(1)
        elif car_mark.lower() == 'toyota':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[55]').click()
            time.sleep(1)
        elif car_mark.lower() == 'honda':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[23]').click()
            time.sleep(1)
        elif car_mark.lower() == 'mazda':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[36]').click()
            time.sleep(1)
        elif car_mark.lower() == 'mitsubishi':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[41]').click()
            time.sleep(1)
        elif car_mark.lower() == 'suzuki':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[54]').click()
            time.sleep(1)
        elif car_mark.lower() == 'acura':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[2]').click()
            time.sleep(1)
        elif car_mark.lower() == 'audi':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[3]').click()
            time.sleep(1)
        elif car_mark.lower() == 'bmw':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[4]').click()
            time.sleep(1)
        elif car_mark.lower() == 'cadillac':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[6]').click()
            time.sleep(1)
        elif car_mark.lower() == 'chery':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[7]').click()
            time.sleep(1)
        elif car_mark.lower() == 'chevrolet':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[8]').click()
            time.sleep(1)
        elif car_mark.lower() == 'ford':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[18]').click()
            time.sleep(1)
        elif car_mark.lower() == 'hyundai':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[24]').click()
            time.sleep(1)
        elif car_mark.lower() == 'infiniti':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[25]').click()
            time.sleep(1)
        elif car_mark.lower() == 'kia':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[30]').click()
            time.sleep(1)
        elif car_mark.lower() == 'lexus':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[33]').click()
            time.sleep(1)
        elif car_mark.lower() == 'porsche':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[45]').click()
            time.sleep(1)
        elif car_mark.lower() == 'volkswagen':
            class_mark = driver.find_element_by_xpath('//*[@id="newRequest"]/div[4]/div/div[3]/div/ul/li[57]').click()
            time.sleep(1)

        #---------------------------------------------------------------------------------------------------------------INPUT PART NUMBER
        class_part = driver.find_element_by_xpath('//*[@id="article1"]')
        class_part.send_keys(part_number)

        #---------------------------------------------------------------------------------------------------------------TEXT AREA AND INPUT RECAPTCHA
        iframes = driver.find_element_by_class_name('g-recaptcha').get_attribute('data-sitekey')
        element = driver.find_element_by_css_selector('#g-recaptcha-response[style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"]')
        driver.execute_script('arguments[0].setAttribute("style","width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 100px 25px; padding: 0px; resize: none;")', element)
        element2 = driver.find_element_by_xpath('//*[@id="g-recaptcha-response"]')
        res = get_response(iframes)
        element2.send_keys(res)
        time.sleep(1)

        #---------------------------------------------------------------------------------------------------------------INPUT REQUEST PAT NUMBER
        driver.find_element_by_css_selector('body > div.page-wrapper > section > div > div:nth-child(8) > input:nth-child(3)').click()
        time.sleep(1)

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
if __name__ == '__main__':
    find_past('21460-VG100', 'nissan')







# import os
# import random
# import socket
# import subprocess
# import sys
# import time
# import urllib
# import netifaces
# import pydub
# import speech_recognition as sr
# # selenium libraries
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.proxy import Proxy, ProxyType
#
# def change_ip(interface_name, ip_address, mask, gateway):
#     ip_address = '.'.join(ip_address.split('.')[:-1]) + '.' + str(
#         random.randrange(8, 255 - int(mask.split('.')[-1]) - 1))
#     result_1 = subprocess.call(
#         f'netsh interface ipv4 set address name="{interface_name}" static {ip_address} {mask} {gateway}', shell=True)
#     result_2 = subprocess.call(f'netsh interface ipv4 set dns name="{interface_name}" static 8.8.8.8', shell=True)
#     if result_1 == 1 or result_2 == 1:
#         print("[WARN] Unable to change IP. Run the program with admin rights.")
#         sys.exit()
#     print(f"[INFO] New IP Address is: {ip_address}")
#     return True
#
#
# def get_default_network_details():
#     def get_ip_address():
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         ip_address = s.getsockname()[0]
#         s.close()
#         return ip_address
#
#     ip_address = get_ip_address()
#     for i in netifaces.interfaces():
#         try:
#             if str(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) == str(ip_address):
#                 print("[INFO] *Default Network Details*")
#                 print("[INFO] IP Address: ", ip_address)
#                 print("[INFO] Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
#                 print("[INFO] Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0])
#                 return ip_address, \
#                        netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'], \
#                        netifaces.gateways()['default'][netifaces.AF_INET][0]
#         except Exception:
#             pass
#
# def main():
#     delay = 2
#     delay_audio = 10
#     filename = '1.mp3'
#     URL = 'https://prices.autoins.ru/priceAutoParts'
#     BY_pass = 'https://speech-to-text-demo.ng.bluemix.net'
#
#     options = webdriver.ChromeOptions()
#     options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15')
#     options.add_argument('--disable-notifications')
#     options.add_argument("--mute-audio")
#     # options.add_argument('--headless')
#     driver = webdriver.Chrome(
#         executable_path='/Users/egororlov/Desktop/autoparts/webdriver/chromedriver',
#         options=options,
#     )
#
#     try:
#         driver.get(URL)
#         time.sleep(3)
#         frames = driver.find_element_by_tag_name('iframe')
#         print(frames)
#         driver.quit()
#     except Exception as ex:
#         print('Something broken...')
#         print(ex)
#         driver.quit()
#
# if __name__ == '__main__':
#     main()