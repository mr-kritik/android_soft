from concurrent.futures.thread import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import random
import string
import re


chromeOptions = Options()
chromeOptions.headless = True #как будет запускаться хром - в фоне или нет
executor = ThreadPoolExecutor(20) #количество одновременных потоков

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

# простейшая функция выгрузки всех ссылок с заданой страницы
def getlinks(url):
    driver = webdriver.Chrome(r"путь к chromedriver", options=chromeOptions) # path к chromedriver
    list = []
    driver.get(url)
    a = driver.find_elements_by_xpath('.//a')
    i = 0
    for b in a:
        i = i+1
        link = b.get_attribute("href")
        list.insert(i, link)
        driver.quit()
    return list

def scrape(url):
    executor.submit(scraper, url)
    executor.submit(scraper, "адрес_тестируемого_ресурса/"+generate_random_string(10))
#генерируем мусорные ссылки, если надо. кстати, если в тестируемом сайте есть функция поиска или любые другие страницы с тяжелыми запросами в БД, этот вариант - твой



def scraper(url):
    driver = webdriver.Chrome(r"путь_к_chromedriver", options=chromeOptions) #path к chromedriver
    driver.get(url)
    time.sleep(15)
    driver.quit()

    urls = getlinks("адрес_тестируемого_ресурса")
    for url in urls * 10: #количество инстансов
        scrape(url)