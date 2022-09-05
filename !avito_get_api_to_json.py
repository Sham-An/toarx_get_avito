#авито парсер на питончике ._py
#https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9&params%5B1283%5D=14756&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1&lastStamp=1611316560&display=list&limit=30

import requests
from urllib.parse import quote
from urllib.parse import unquote
from datetime import datetime
from math import floor
from time import sleep
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
from time import time
import warnings

warnings.filterwarnings("ignore")
CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)


class HttpParser:
    REGION_INFO = 'region_info'
    CATEGORIES_INFO = 'categories_info'
    AVITO_MAIN = 'avito_main'

    avito_urls = {
        'region_info': 'https://m.avito.ru/api/1/slocations?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=621540&limit=10&q=',
        'categories_info': 'https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=',
        'avito_main': 'https://avito.ru'
    }

    def __init__(self):
        pass

    @staticmethod
    def get_json_by_request(url):
        session = requests.session()
        adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
        session.mount("https://", adapter)

        #r = session.request('GET', 'https://www.avito.ru')

        try:
            # resp = requests.get(
            #     url, verify=False
            # )
            resp = session.request('GET', url, verify=False)
                #requests.get(
                #url, verify=False
           # )

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
        print(region_name)
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
        )
        filters = json_content['result']['filters']

        for sub_category_item in filters:

            if sub_category_item['id'] not in ['shortcut']:  # JUST RUINED MY CODE
                continue

            sub_category_name = sub_category_item['title']
            # print(f'sub_category: {sub_category_item}')
            sub_category_link = f'{HttpParser.avito_urls[HttpParser.AVITO_MAIN]}{sub_category_item["value"]["url"]}'

            yield sub_category_name, sub_category_link

    @staticmethod
    def get_all_categories_by_region_id(region_id):
        json_content = HttpParser.get_json_by_request(f'{HttpParser.avito_urls[HttpParser.CATEGORIES_INFO]}{region_id}')
        main_categories = json_content['categories']

        output_categories = {}

        for parent_category in main_categories[1:]:
            parent_id = parent_category['id']
            parent_name = parent_category['name']

            category_link = HttpParser.get_category_link_by_id(region_id, parent_id)

            if category_link is not None:
                output_categories[parent_name] = {
                    'id': parent_id,
                    'link': category_link
                }

            for child_category in parent_category['children']:
                child_id = child_category['id']
                child_name = child_category['name']

                child_category_link = HttpParser.get_category_link_by_id(region_id, child_id)

                if child_category_link is not None:
                    output_categories[child_name] = {
                        'id': child_id,
                        'link': child_category_link
                    }

                for sub_category_name, sub_category_link in HttpParser.get_sub_categories_by_id(region_id, child_id):
                    output_categories[sub_category_name] = {
                        'id': None,
                        'link': sub_category_link
                    }

        return output_categories

    @staticmethod
    def get_add_json_info_by_id(add_id):
        json_content = HttpParser.get_json_by_request(
            f'https://m.avito.ru/api/14/items/{add_id}?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        )

        return json_content

    @staticmethod
    def get_phone_number_by_add_id(add_id):
        json_content = HttpParser.get_json_by_request(
            f'https://m.avito.ru/api/1/items/{add_id}/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        )

        return unquote(json_content['result']['action']['uri'].split('=')[-1])

    @staticmethod
    def get_add_info_by_id(add_id):
        add_json_info = HttpParser.get_add_json_info_by_id(add_id)

        del add_json_info['contacts']

        add_json_info['seller']['connection']['sources'][0]['type'] = HttpParser.get_phone_number_by_add_id(add_id)

        return add_json_info

    @staticmethod
    def get_adds_list(category_name_for_search, region_id, categories_dict, limit_shows=1):
        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))

        adds_list = []

        for category_name in categories_dict.keys():
            if category_name_for_search not in category_name:
                continue

            category = categories_dict[category_name]
            category_id = category['id']
            category_link = category['link']
            orig_uri = category_link.replace(HttpParser.avito_urls[HttpParser.AVITO_MAIN], '')

            if category_id is None:
                json_content = HttpParser.get_json_by_request(
                    'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
                    f'page=1&lastStamp={time}&display=list&limit={limit_shows}&url={orig_uri}'
                )
            else:
                json_content = HttpParser.get_json_by_request(
                    'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
                    f'locationId={region_id}&categoryId={category_id}&page=1&display=list&limit={limit_shows}'
                )

            items = json_content['result']['items']

            for item in items:
                if 'type' in item.keys() and item['type'] == 'vip':
                    add_id = item['value']['list'][0]['value']['id']
                else:
                    add_id = item['value']['id']

                add_json_info = HttpParser.get_add_json_info_by_id(add_id)

                del add_json_info['contacts']

                add_json_info['seller']['connection']['sources'][0]['type'] = HttpParser.get_phone_number_by_add_id(add_id)

                adds_list.append(add_json_info)

        return adds_list

session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)

region_id = HttpParser.get_region_id_by_name('Казань')
all_categories = HttpParser.get_all_categories_by_region_id(region_id)
all_adds = HttpParser.get_adds_list('Квартиры', region_id, all_categories, limit_shows=50)
example_add = HttpParser.get_add_info_by_id(1861843197)


print(all_categories)
print(all_adds)
print(example_add)

# Telegram: @xmm_0