#Work path /opt/PycharmProjects/tele_bot/avito_parser_django/avito
# cd avito_parser_django/avito
# python manage.py runserver
# /admin vladimir:111
# cd /opt/PycharmProjects/tele_bot/avito_parser_django/avito/aparser/management/commands/parse_avito.py
# cd /opt/PycharmProjects/tele_bot/avito_parser_django/avito/

#### !!!!!!!!! START !!!!!!!!!
# python manage.py parse_avito_api
# python manage.py parse_avito_api -s
#python manage.py parse_avito_api --help


#import datetime
import json

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

import urllib.parse
import requests
from logging import getLogger
#
# from avito_parser_django.avito.aparser.constants import STATUS_NEW
# from avito_parser_django.avito.aparser.constants import STATUS_READY

from aparser.constants import STATUS_NEW
from aparser.constants import STATUS_READY


#from avito_parser_django.avito.aparser.models import Product
import ssl
from urllib3.util import ssl_
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

from aparser.models import Task
from aparser.models import Product


logger = getLogger(__name__)

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir' # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
#cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
cookie = 'u=2thd5s2p.pzwwe1.1etr7b0jx5r00; _ym_uid=1662353765728917265; _ym_d=1662353765; _gcl_au=1.1.1119694243.1662353765; adrcid=ApqrCZ0fGgHkPN1lmnApjVQ; uxs_uid=419f7cd0-2cd9-11ed-a825-bfa45587e009; buyer_location_id=651110; _ga=GA1.1.1011885097.1662353766; buyer_laas_location=651110; _ym_isad=2; f=5.367a37203faa7618a7d90a8d0f8c6e0b47e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b91772440e04006def90d83bac5e6e82bd59c9621b2c0fa58f915ac1de0d034112251851063192bbc234d62295fceb188df88859c11ff008953de19da9ed218fe23de19da9ed218fe2e992ad2cc54b8aa87fde300814b1e8553de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe2b5b87f59517a23f2a9a996d174584814352c31daf983fa077a7b6c33f74d335c84df0fd22b85d35f79d9917d15a693b61ba6d8b24fb5a1f7844df89026cf8a26ab4f4837d4a574d617c7721dca45217b6c65352774715db435a3e6780a79bb9b2ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748e894de4bdfb6ea9b3de19da9ed218fe23de19da9ed218fe29e05a03e27b662cf3740ddbb7a20c377567037a1138bc3a59ddcb939a425458a; ft="B0jtNY3r7H/uEYH1QdVonjvwI6UJ8cKTVaUS64wh0blXwnjaYjtfR00knmzmA38zfTkUD1n4ZMFZnyN2aFx4v8x2wzttosMSctIS0x/PSUUKPskrWGUKVGv4i/S9rb3C6THoaNpdLq9G2EGqx2E2lH+wkEyK9PCZVTXrdzZClqhooqD4buOLksjS+XTz/1Ni"; v=1669231788; luri=rostovskaya_oblast; sx=H4sIAAAAAAAC/wTAQQ6CMBQE0LvM2gUNdn6nx/G3ikYUo1gj6d15G0jSi/EsKvJIVTvVUcXi4G5FyBu+yLi3KV7+0/qwz9zSb1jbbfbr05ZFL/GNAypyIDWGFFLqfQ8AAP//D10PqVsAAAA=; abp=0; _ga_M29JC28873=GS1.1.1669231791.6.0.1669231791.60.0.0; _ga_9E363E7BES=GS1.1.1669231792.6.0.1669231792.60.0.0; cto_bundle=-ZVwkV9pMmJvTG41bHQxS2g4cUNVQ3ZQZ3pqdW8wY0pFayUyQnFYOGhveEdIYkhadDklMkJFZEk4NU0lMkJZVDZ4Q0o1ZlJjQzMyN1ZXbGM0YkpNQ05SamREJTJCQTJRZHJQWTZTTVV2RGFaazhJcnE4ZExmZiUyRmx2OTZ0QmRoaEQ3MG4lMkZHdmlLNEh5eVhqSEdPZDVCQnpOZmtFNzhwWCUyQnNBZyUzRCUzRA; _ym_visorc=b; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyVGh1JTJDJTIwMjMlMjBOb3YlMjAyMDIzJTIwMTklM0EyOSUzQTUzJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyYTFlYzk2NTAyZGRjYTU2OWI0NmZmYTYwOWZkNzdjNjglNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; isCriteoSetNew=true; tmr_detect=0|1669231794811; buyer_from_page=main'

search = 'suzuki+gsx-r'     # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = 14
locationId = 641780         # Новосибирск
searchRadius = 200
priceMin = 100000
priceMax = 200000
sort = 'priceDesc'
withImagesOnly = 'true'     # Только с фото
limit_page = 50     # Количество объявлений на странице 50 максимум



class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)


class AvitoParser:
    PAGE_LIMIT = 10

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }
        self.task = None

    def find_task(self):
        obj = Task.objects.filter(status=STATUS_NEW).first()
        if not obj:
            raise CommandError('no tasks found')
        self.task = obj
        logger.info(f'Работаем над заданием {self.task}')

    def finish_task(self):
        self.task.status = STATUS_READY
        self.task.save()
        logger.info(f'Завершили задание')

    def get_page(self, page: int = None):
        logger.info(f'get_page start: ')

        headers = {'Host': 'm.avito.ru',
                   'pragma': 'no-cache',
                   'cache-control': 'no-cache',
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'sec-fetch-site': 'none',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-user': '?1',
                   'sec-fetch-dest': 'document',
                   'accept-language': 'ru-RU,ru;q=0.9', }
        if cookie:  # Добавим куки, если есть внешние куки
            headers['cookie'] = cookie
        #print(f'куки = {cookie}')
        #s.headers.update(headers)  # Сохраняем заголовки в сессию
        # #
        # params = {
        #     'radius': 0,
        #     'user': 1,
        # }

        params = {
            'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
            'categoryId': 14,
            'params[30]': 4969,
            'locationId': locationId,
            'searchRadius': searchRadius,
            'priceMin': priceMin,
            'priceMax': priceMax,
            'params[110275]': 426645,
            'sort': sort,
            'withImagesOnly': withImagesOnly,
            'lastStamp': 1660975970,
            'display': 'list',
            'limit': limit_page,
            'query': search,
        }
        proxiess = {'http': '185.170.215.228:80'}  # 79.143.225.152:60517
        proxiess = {'http': '79.143.225.152:60517'}  # 79.143.225.152:60517

        # if page and page > 1:
        #     params['p'] = page
        url = self.task.url
        logger.info(f'URL: {url}')
        adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
        #s.mount("https://", adapter)
        url_api_9 = 'https://m.avito.ru/api/9/items'
        #ad = self.session.mount("https://", adapter)

        self.session.mount("https://", adapter)
        self.session.headers.update(headers)

        #r = self.session.get(url, params=params)
        r = self.session.get(url_api_9, params=params, proxies=proxiess)  # , useragent = UA) #, useragent = str(UA))

        logger.info(f'Adapter: {r.status_code}')
        # with open('results.json', 'w', encoding='utf-8') as file:
        #     json.dump(r.content, file, indent=2, ensure_ascii=False)

        logger.info(f'json : {r.json()}')
        #r = ad.get(url, params=params)
        #r.raise_for_status()
#        print(f'################################################################## Status.url = {r.status_code}')
        return 0 #r.text

    def get_pagination_limit(self):
        return 1
        # text = self.get_page()
        # soup = bs4.BeautifulSoup(text, 'lxml')
        #
        # container = soup.select('a.pagination-page')
        # if not container:
        #     return 1
        # last_button = container[-1]
        # href = last_button.get('href')
        # if not href:
        #     return 1
        #
        # r = urllib.parse.urlparse(href)
        # params = urllib.parse.parse_qs(r.query)
        # return min(int(params['p'][0]), self.PAGE_LIMIT)

    def get_blocks(self, page: int = None):
        page = 1
        #text = self.get_page(page=page)
        json_get = self.get_page(page=page)
        logger.info(f'json_get {json_get}')
        #soup = bs4.BeautifulSoup(text, 'lxml')
        # Запрос CSS-селектора, состоящего из множества классов, производится через select
        # container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        # for item in container:
        #     self.parse_block(item=item)


    def parse_all(self):
        # Выбрать какое-нибудь задание
        self.find_task()

        limit = self.get_pagination_limit()
        logger.info(f'limit: {limit}')
        #
        # for i in range(1, limit + 1):
        #     logger.info(f'Работаем над страницей {i}')
        #     self.get_blocks(page=i)
        self.get_blocks(page=1)
        #
        # # Завершить задание
        # self.finish_task()


class Command(BaseCommand):
    help = 'The Avito_Api of Python'


    def handle(self, *args, **options):
        p = AvitoParser()
        p.parse_all()


    def add_arguments(self, parser):
        parser.add_argument(
        '-s',
        '--short',
        action='store_true',
        default=False,
        help='Вывод короткого сообщения'
        )
