import json
import sqlite3
import time
from datetime import datetime
import requests

from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.poolmanager import PoolManager
from urllib3.poolmanager import PoolManager
# from requests.packages.urllib3.util import ssl_
from urllib3.util import ssl_
from datetime import datetime
from realty import check_database
from realty import realty_ok

import ssl
import requests
from fake_useragent import UserAgent
from random import randint

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)


# session = requests.session()
# adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
# session.mount("https://", adapter)
#
# try:
#     r = session.request('GET', 'https://www.avito.ru')
#     print(r.text)[1000]
# except Exception as exception:
#     print(exception)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        # col[0] is the column name
        d[col[0]] = row[idx]
    return d
    #         variant 2
    # fields = [column[0] for column in cursor.description]
    # return {key: value for key, value in zip(fields, row)}


def get_data_to_json():
    database = 'realty.db'
    conn = sqlite3.connect(database)  # conn.row_factory = sqlite3.Row
    conn.row_factory = dict_factory
    c = conn.cursor()
    temp = c.execute("SELECT * FROM cityes WHERE cityes.url_path = 'None' AND cityes.id > 662800")
    # result = [{k: item[k] for k in item.keys()} for item in temp] #print(f'!!!!!!!!!!!!!! result = {result}')
    rst = c.fetchall()  # rst is a list of dict
    # pprint(rst)#, depth=0) #print(json.dumps(rst, sort_keys=False, indent=4))
    #list_id(rst)
    #conn.close()
    return rst #jsonify(rst)


def get_offer(item):
    offer = {}

    offer["url"] = "https://www.avito.ru" + item["uri_mweb"]
    offer["offer_id"] = item["id"]

    price = ''.join(item['price'].replace(' ₽ в месяц', '').split())
    title = item['title'].split(', ')
    area = ('m2')  # float(title[1].replace(' м²', '').replace(',', '.'))
    rooms = title[0]

    floor_info = ""  # title[2].replace(' эт.', '').split('/')
    floor = floor_info[0]
    total_floor = floor_info[-1]

    timestamp = datetime.fromtimestamp(item['time'])
    timestamp = datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')
    offer["date"] = timestamp

    offer["price"] = price
    offer["address"] = f"{item['location']}, {item['address']}"
    offer["area"] = area
    offer["rooms"] = rooms
    offer["floor"] = floor
    offer["total_floor"] = total_floor

    return offer


def get_offers(data):
    items = data["result"]["items"]
    for item in items:
        if "item" in item["type"]:
            offer = get_offer(item["value"])
            check_database(offer)


def get_json_cat_for_city(id_sity):
    id_sity = id_sity
    # categories json
    ua = UserAgent(browsers=['edge', 'chrome'])
    ua_str = ua.random
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    headers = {
        'user-agent': ua_str,
    }
    # Web parameters: смотри внизу файла
    priceMin = 100
    priceMax = 4500

    # ('categoryId', '14'),
    # ('locationId', '623110'),
    # ('query', search),
    # ('priceMin', priceMin),
    # ('priceMax', priceMax),
    # ('display', 'list'),
    # ('params[201]', '1060'),

    # search = 'скутер !имз !Мопед !альфа -альфа -Дельта'  # OK!!!  'suzuki+gsx-r'
    search = 'а'  # OK!!!  'suzuki+gsx-r'

    # API
    params = (
        ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
        ('locationId', {id_sity}),
    )

    params_web = (
        ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
        ('categoryId', '14'),
        ('params[201]', '1060'),
        ('locationId', '652000'),
        ('query', search),
        ('priceMin', priceMin),
        ('priceMax', priceMax),
        ('params[504]', '5256'),
        ('owner[]', 'private'),
        ('user', '1'),
        ('s', '1'),
        ('page', '1'),
        ('display', 'list'),
        ('limit', '50'),
    )

    url = "https://m.avito.ru/api/2/search/main"
    # https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=621552
    # 'https://m.avito.ru/api/11/items'
    # url_web = 'https://avito.ru'
    # url = 'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9'  # &params[1283]D=14756'#&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1' #&lastStamp=1611316560&display=list&limit=30'
    # OK https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=24&params[1283]D=14756%27#&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1'%20#&lastStamp=1611316560

    session = requests.session()
    session_web = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    adapter_web = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)
    session_web.mount("https://", adapter)
    response = session.request('GET', "https://m.avito.ru/", headers=headers, params=params)
    time.sleep(3)

    try:
        response = session.request('GET', url, headers=headers, params=params)
        # r = session.request('GET', 'https://www.avito.ru')
        # resp = open('items_api_21.json').read()
        ress = response.json()
        with open(f'F:\Data\json\cat_{id_sity}.json', 'w', encoding='utf-8') as file:
            json.dump(ress, file, indent=2, ensure_ascii=False)
            # file.write(json)

        print(f'response {response.status_code}, {response.url}')  # .text)[1000]
    except Exception as exception:
        print(exception)

    # response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    # data = response
    return data


def get_json_items():
    # categories json
    ua = UserAgent(browsers=['edge', 'chrome'])
    ua_str = ua.random
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    headers = {
        'user-agent': ua_str,
    }

    # Web parameters: смотри внизу файла
    priceMin = 10000
    priceMax = 45000

    # ('categoryId', '14'),
    # ('locationId', '623110'),
    # ('query', search),
    # ('priceMin', priceMin),
    # ('priceMax', priceMax),
    # ('display', 'list'),

    # search = 'скутер !имз !Мопед !альфа -альфа -Дельта'  # OK!!!  'suzuki+gsx-r'
    search = 'а'  # OK!!!  'suzuki+gsx-r'
    # API
    params = (
        ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
        ('categoryId', '2'),
        ('params[201]', '1060'),
        ('locationId', '623110'),
        ('query', search),
        ('params[504]', '5256'),
        ('owner[]', 'private'),
        ('user', '1'),
        ('s', '104'),
        ('page', '1'),
        ('limit', '5'),
        ('bt', '0'),
    )

    params_web = (
        ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
        ('categoryId', '14'),
        ('params[201]', '1060'),
        ('locationId', '652000'),
        ('query', search),
        ('priceMin', priceMin),
        ('priceMax', priceMax),
        ('params[504]', '5256'),
        ('owner[]', 'private'),
        ('user', '1'),
        ('s', '1'),
        ('page', '1'),
        ('display', 'list'),
        ('limit', '50'),
    )

    url = 'https://m.avito.ru/api/11/items'
    url_web = 'https://avito.ru'
    # url = 'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9'  # &params[1283]D=14756'#&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1' #&lastStamp=1611316560&display=list&limit=30'
    # OK https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=24&params[1283]D=14756%27#&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1'%20#&lastStamp=1611316560

    session = requests.session()
    session_web = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    adapter_web = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)
    session_web.mount("https://", adapter)
    response = session.request('GET', "https://m.avito.ru/", headers=headers, params=params)
    time.sleep(3)

    try:
        response = session.request('GET', url, headers=headers, params=params)
        # r = session.request('GET', 'https://www.avito.ru')
        # resp = open('items_api_21.json').read()
        ress = response.json()
        with open('F:\Data\json\!!!res_cookies_9.json', 'w', encoding='utf-8') as file:
            json.dump(ress, file, indent=2, ensure_ascii=False)
            # file.write(json)

        print(f'response {response.status_code}, {response.url}')  # .text)[1000]
    except Exception as exception:
        print(exception)

    # response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    # data = response
    return data


def main():

    cityes_dmp = get_data_to_json()


    with sqlite3.connect('realty.db', timeout=300) as connection:
        cursor = connection.cursor()

        query_str = f"""UPDATE cityes 
        SET index_post = '1' WHERE id = ?
        """

        for cit in cityes_dmp:
            cit_name = cit['name']
            cit_id = int(cit['id'])
            data_get = get_json_cat_for_city(cit_id)
            #print(f'##################################### {data_get.kod}')
            print(f"cit_name = {cit_name}, cit_id = {cit_id}")
#            cursor.execute((query_str), (cit_id,))  # !!!!OK
#            connection.commit()
            print('Update ', connection.total_changes)  # rowcount())#total_changes total_changes() )
            connection.commit()
            tim = randint(5, 15)
            time.sleep(2)


        # data_items = get_json_items()
        # data_cat = get_json_cat_for_city()
#        id_sity = '621568'
#        data_get = get_json_cat_for_city(id_sity)
        print(f'\n\n {data_get}')
        # print(data_items)
        # print(f'data = get_json() {data}')
        # get_offers(data)


if __name__ == '__main__':
    main()

"""
    # 'bt': 1 (или 'bt': 0) — 1- поиск с учетом включения запроса в название (0 — без учета запроса в названии)
    # 'pmax': max_price и 'pmin': min_price — это верхняя и нижняя граница диапазона цен, переменные max_price и min_price принимаются от пользователя.
    # 'q': search — основной параметр запроса, то что мы вводив в поиск
    # 's': 2 ('s': 1', 's': 101, 's': 104) — сортировка выданных результатов поиска:
    # 's': 2 - сортировка по цене (от дорогого к дешевому),
    # 's': 1— сортировка по цене (от дешевого к дорогому),
    # 's': 101- сортировка по умолчанию,
    # 's': 104 — сортировка по дате объявления (от свежих к старым)
    # 'view': 'gallety' (либо не указывать) — показывает как будет распологаться выдача

    #    ('priceMin', priceMin)
    priceMin = 10000
    # 'priceMax': priceMax,
    priceMax = 45000
    # ('drawId', 'b53e6cb32c3737cd3cd0706646bae52c'),
    # ('sort', 'date'), {date,price,price_desc} ('sort', 'price_desc'),
    # ('s', '104'), 104 от свежих к старым  1 от дешевого к дорогому
    # ('query', search) ('q', search),
    # BAD search = 'Урал+%21Мопед+%21альфа+-Мопед+-альфа+-Дельта' #'suzuki+gsx-r'
    search = 'Урал !имз !Мопед !альфа -альфа -Дельта'  # OK!!!  'suzuki+gsx-r'



# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
"""
