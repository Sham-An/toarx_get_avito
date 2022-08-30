# Инструкции:
# первый метод: get_region_id_by_name - принимает аргрумент названия города, возвращает id города
# второй метод: get_all_categories_by_region_id - выдает ВСЕ существующие категории в этом городе. вход - id города
# третий метод get_adds_list - принимает на вход ВСЕ категории, которые мы получили из метода get_all_categories_by_region_id, id региона и название нужной нам рубрики, например Квартиры(можно тоже через id сделать). На выходе у нас список из 50 обьявлен в заданной категории. И ВСЯ информация о них
# и последний get_add_info_by_id - принимает на вход id обьявления, на выход ВСЮ информацию о нем
#
# req:
# python 3.8 >

import requests
from urllib.request import quote
from urllib.request import unquote
from datetime import datetime
from math import floor
from time import sleep
from time import time

import warnings

warnings.filterwarnings("ignore")


class HttpParser:
    REGION_INFO = 'region_info'
    CATEGORIES_INFO = 'categories_info'
    AVITO_MAIN = 'avito_main'

    avito_urls = {
        'region_info': 'https://m.avito.ru/api/1/slocations?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
                       '&locationId=621540&limit=10&q=',
        'categories_info': 'https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=',
        'avito_main': 'https://avito.ru'
    }

    def __init__(self):
        pass

    @staticmethod
    def get_json_by_request(url):
        try:
            resp = requests.get(
                url, verify=False
            )
            json_content = resp.json()
            if 'status' in json_content.keys():
                if json_content['status'] == 'internal-error':
                    print('internal-error')
                    HttpParser.get_json_by_request(url)
            return json_content
        except requests.exceptions.ProxyError:
            sleep(0.001)
            HttpParser.get_json_by_request(url)

    @staticmethod
    def get_region_id_by_name(region_name):
        json_content = HttpParser.get_json_by_request(
            f'{HttpParser.avito_urls[HttpParser.REGION_INFO]}{quote(region_name)}')
        locations = json_content['result']['locations']

        return locations[0]['id']

    @staticmethod
    def get_category_link_by_id(region_id, category_id):
        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))
        json_content = HttpParser.get_json_by_request(
            'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
            f'lastStamp={time}&locationId={region_id}&categoryId={category_id}&page=1&display=list&limit=1'
        )

        if json_content is None:
            return None

        #print(json_content)

        item = json_content['result']['seo']
        link = item['canonicalUrl']

        return link

    @staticmethod
    def get_sub_categories_by_id(region_id, category_id):
        if category_id == 9:  # Skip automobiles category
            return

        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))

        json_content = HttpParser.get_json_by_request(
            'https://m.avito.ru/api/1/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
            f'lastStamp={time}&parameters[locationId]={region_id}&parameters[categoryId]={category_id}'