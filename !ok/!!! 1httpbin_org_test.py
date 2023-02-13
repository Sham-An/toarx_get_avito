import json
import requests
from fake_useragent import UserAgent

ua = UserAgent(browsers=['edge', 'chrome'])
ua_str = ua.random
#print(ua_str)

headers = { 'Host': 'm.avito.ru',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': ua_str,
            'accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'ru-RU,ru;q=0.9',}


response = requests.get("http://httpbin.org/get?name=max&height=178")
#print(response.json())

search = 'suzuki+gsx-r'     # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = 4
locationId = 621590 #641780         # Новосибирск
searchRadius = 10
priceMin = 1000
priceMax = 20000
sort = 'priceDesc'
withImagesOnly = 'true'     # Только с фото
limit_page = 50     # Количество объявлений на странице 50 максимум


params1 = {
    'key': 'f1cfe913d6f44732a4b1601444eccb74',
    'categoryId': 14,
    'locationId': locationId,
    'searchRadius': searchRadius,
    'priceMin': priceMin,
    'priceMax': priceMax,
    'sort': sort,
    'withImagesOnly': withImagesOnly,
    'lastStamp': 1670975970,
    'display': 'list',
    'limit': limit_page,
    'query': search
}


params2 = (
    ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
    ('categoryId', '9'),
    ('params[201]', '1060'),
    ('locationId', '107620'),
    ('params[504]', '5256'),
    ('owner[]', 'private'),
    ('sort', 'date'),
    ('page', '1'),
    ('display', 'list'),
    ('limit', '30'),
)

# params = {
# 	'name': "Nick",
# 	'age': "17",
# }

#response = requests.get("http://httpbin.org/get", params=params)
response = requests.get("http://httpbin.org/get", headers=headers, params=params2)

#print(response.json()) #смотрим агента и параметры в заголовках ("Accept": "text/html" *)
print(f'json.loads(response.content) {json.loads(response.content)}')
print(f'status code {response.status_code}')
print(f' URL {response.url}')
#print(response.headers)
#print(response.text)


