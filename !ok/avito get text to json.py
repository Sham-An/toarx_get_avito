import json
import pprint
import ssl
import requests

from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.poolmanager import PoolManager
from urllib3.poolmanager import PoolManager
from urllib3.util import ssl_
from fake_useragent import UserAgent
from http.cookies import SimpleCookie

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)



# try:
#     r = session.request('GET', 'https://www.avito.ru')
#     print(r.text)
# except Exception as exception:
#     print(exception)
#
# if (r.status_code == requests.codes.ok):
#         print('##################################################')
#         print(r.headers['content-type'])

def get_coocies(cook):
    cookie1 = cook
    # rawdata='u=2xrawwd7.1cwalh0.czes2z3b81o0; _gcl_au=1.1.702261351.1676272634; _ym_d=1676272635; _ym_uid=1676272635946525122; tmr_lvidTS=1676272635851; tmr_lvid=e59de466ad487dec9977deb7ed3ec36b; _ga=GA1.1.221393451.1676272636; adrcid=AIBf2Z3Umq85GKUTxLyQK6A; uxs_uid=2adeba40-ab70-11ed-aa3f-9f3cd45ff357; __zzatw-avito=MDA0dBA=Fz2+aQ==; cfidsw-avito=kvIa7GUvRAWmm1+TzZ1CU86teZmjMuHtt9zPo0CkseP/vSSXS0DeBsDWynIpvtoF3D0OWLUt50aNYMlvwe+ft/kEQSnX7D5xBJ2G2aYi/NJ9eUnuFXYFNchYNuQgVQtcOOE9SxGkauzl+UAVKT61ObUJ2IzcW43CwLuOcA==; gsscw-avito=C2obqhpH73dCTfjRg4WK/7A16kAQvlJKUSuxafkiGxi243BQP+GHugLzwCdH710MY7sQrumaJgjqD+89xEEUFx+RyUn4xGgAkIdKDn385ytOn6SO4RpAfuWSRJ/4vKIOzNwy3pLNm9PvKz49AvXR78o2aQC405YXSErXQ+Y4hPn6UW08epR+xez1guAvMWgQ5iQ+3Z887l4OR6hIh0VKA+0xEqlXJfAR0e0nkoFjcQOt7oCtrNim7R/m59fPtdkr+ic=; fgsscw-avito=seBcd181c886a63aed506cf5c32f80eaf77638d3; _ym_isad=2; v=1676357167; buyer_laas_location=652000; luri=rostov-na-donu; buyer_location_id=652000; _ym_visorc=b; redirectMav=1; sx=H4sIAAAAAAAC/1zWW5LrrA4F4LnkeT8AAgn2bAQCX+LY8SV27FM991Puv5Ld6Ql8phZLwv+7qKSUSyYGSC5xtJQDUCwGWHtQgS9//3dZL38vTTON9dYts6CBZ2iK7t3gVTeMfTfWcPlzyZe/GgmtAk349eei0XgNUZhSJo8qZhvRR4xgAltFLzlKpx8w8n3iNigVD7mHW6uo6FsDdfopW8RTNp6ZDbPoglCSVhgYwWVlimRj80te64ej7naVpSZ8PKCe1kbXS9ttKbb2/kO2Vin99ecC4DklXZSkCEEcBvRYhA0FAxnxJZdHLGjVrWpx4qLkMY7HQmZ6LCIg488zu//SACfZFI5ZoIAoDpCjKyZZ57OYIC+572tvaVptt2jcgVf91Lne4tinyuv9p6ydD6cc0XvU6LywBiS2nsliTIaZdfiX8ygJnmaoN8Lojjw0A3kL/b1qkEL8dYPwLReyxZCwjkolgGCdcBHnrEIbwkvehkfdVlvSSQM/E9asC7fHdg3XJvr+p2wcmlOWaDRyKS5QVi4UH8UlghjBFUvqJfuzYXvVCzxZlul6M81j2m59kmoFdJ9pmO8bzFDO7oAYEE8KvLXIYlGXoAL7l/x8PP3aNV2FuAaEYy7dcfSCWsPc3pvP1jn6lr11toSs0TorRkV2NiXM3hrU0b7kRNHtuYVe1mZKnYrxuT8K+SXeCRP9OvPZDcuISEiKRUW0MaogmU0ElRCceZ/ZeFpopq2/d6zVPAej5U4L7PPa+Bw/ZfiWkylsg8pashInUpSWgEg+o+X4L+ct35Z8RIbGi03G65imyhm3cjcs9CsN+/Xn4kowTqWSQIQyIFhlPKExLpF1/O5G4xTirPYEu0oa/e4aH+9puXaPKgy/+gxn6xARkxCWgMGhxZApZghCTqVE8pajtXNzc26upv0Y2vvM87q1LTyv19u2HT+n25mgv+WExaqsVVQ+WgW5YIpcfE7JcnxPCs06TsukKsVroLhVtwNuUJ5BTYOKw4dsgzplNk4pIWOdhRIQkLxo0pnVOfTlJR8P5VvFvgb9dNDnfeia9t4v10yQ/PqZs/+WpWT2wui99skVjip4TZ5KMD6adxp9MIn3Zq9tZ6dxzn293u7bPj6WqKWdfrXu3BtEBlKiopU5e1lK5JwwBiROPqn35t+f7dTdm23tXXY783OpR6zaUqVl8FZ/bFELZze8zkklbwQjBIeJKCnmEpwCIzGaf90QLTwGd9fPdSzhiPMd6qkPmfbB2p8yeOu+/lxCiWwdClAKpnDKMZTgHWlbSiis37Ks6tnm0EVigPoxH3nOcuislaJh+/WmnDIHBEbFkNglccZkn70i7Yt4gxxfspRumNuKUGTy2Q8He7juVWlayP1t+EwjnGnE4hISe4xODESfgwHjtPNa2eDtO4081q1Nlur8xHLbe8JWx1Zvt7ocVfVr18HZ50RFiKNG7YXAOiOJchIG9iUSvW8Qat3osU4P3Fu/U7Udy4g3cxy4LrHlT1mf3UjBsgqUnSgPOumSHUexEHJxWaf3rrt7g9s8zjOV0HfjbrtHX1+3Xtmnd8/mIw343vwpUI4OfUlWdLAlZ6/Pp1WctjbF9JLH+22AptVb6aDepLXLQgut2/50ce7bz5wdfstBaQSdvKCLRTNZMB5AJcbztf73VzDc1mZJt6ONC2DbDWoo07T7uiuyxI/phu83RQCsV1JEYwnBeaacbWYKFFTw5T2DZFurhR7bcvfutl6xjNTvx3UZadLH9HHm/za/SCo+kAuhOC7BSxZTsk3u/FDS780vrY66otq4caTcjF2juts4ZrU+tq7/+b9hlQlnzpm1C5md9wCpZKOs8cpkSkZBon/7OefB9NuEJj1ksHEbueorO6y526ex+ZCtxjONYgpZq5CLKEju3IEpOxL0yqmo3zM4VddpnIf5GTGodrjyXsb6WROt7fN6bT9ahw6+vv4fAAD//xKnJzuNCgAA; cto_bundle=1ZvLj19kMllyVDRwJTJCYzJSZEhabW0lMkJLUGR4ME1IT2tscTBpSWVBVUVCU0RYYkc1b1VzNGMxVE9KNTZ3UnAybnU3RkpGMSUyRjZtTk84Z2tueDdtcEZtUmZIUEtHZUp4T3NHcU5UeGZ0NkdOekZBTDBXVUtTTXdlOE1FTDZ0NXVuRzNMYk51eCUyQlJPYzRhSDBIRkFXaGZWWkRtUGhvZyUzRCUzRA; f=5.367a37203faa7618a7d90a8d0f8c6e0b47e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d40473de19da9ed218fe287829363e2d856a2e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe2d50b96489ab264ed3de19da9ed218fe23de19da9ed218fe246b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c76ff288cd99dba46e71c24777afa70281d49c1c93fcdfd74ae2a4761d49e98333722a7efdc61f8e20e28148569569b7939c1b38b6a26673a653a8db0a93fc2632ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748367e2c2adde1b2543de19da9ed218fe23de19da9ed218fe2b4af293ec419f67f6cd48844eb16d6d58edd6a0f40cbfd87da3d420d6cca468c; ft="pYqc37xwcBTB+VgjtQnjQpzc9HL3iISsby8RUdc5qIMXbUQl/bQ8arufkmPj48F5aKwPDuweulaGxPDMGOPhycyVnkH/rlLt/H9S/qgfWBsmeFAtVDI6rEDYBM51/iUKF9NI/JwJ64vTjYvk0dJQdujKOW3p63CqTO4UsCFcxCe0mCTI8+EvHneO3enyLYYA"; _mlocation=621540; _mlocation_mode=default; _ga_M29JC28873=GS1.1.1676357171.8.1.1676359169.58.0.0; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi5tLmF2aXRvLnJ1JTIyJTJDJTIyZXhwaXJlcyUyMiUzQSUyMldlZCUyQyUyMDE0JTIwRmViJTIwMjAyNCUyMDA3JTNBMTklM0EzMCUyMEdNVCUyMiUyQyUyMlNhbWVTaXRlJTIyJTNBJTIyTGF4JTIyJTJDJTIydmFsdWUlMjIlM0ElMjIlN0IlNUMlMjJ2YWx1ZSU1QyUyMiUzQSU1QyUyMjc4YzE5ZWM2NzBiYjZiNWIwYzg1ZjliOTk2YTA1NmVmJTVDJTIyJTJDJTVDJTIyZnBqc0Zvcm1hdCU1QyUyMiUzQXRydWUlN0QlMjIlN0Q=; isCriteoSetNew=true; tmr_detect=0|1676359172217'
    # cookie1 = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=4e50185a2b0bf36f9f2d6d12485159e9.1675680145; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1660912321; buyer_laas_location=651110; buyer_location_id=651110; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1660912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg;'  # f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
    cookie = SimpleCookie()
    #cookie.load(rawdata)
    cookie.load(cookie1)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
        #print(cookies)
    #print(js)
    dump_js = json.dumps(cookies, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
               cls=None, indent=2, separators=None, default=None,
               sort_keys=False)
    #print(dump_js)

    return dump_js #cookies

def get_html(url, params=None):
    """ получение кода страницы """
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
    # API  652000 Rostov
    #coocies  buyer_laas_location=652000; v=1676357167; buyer_location_id=652000; luri=rostov-na-donu;

    params = (
        ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
        ('categoryId', '14'),
        ('params[201]', '1060'),
        ('locationId', '621552'),
        ('query', search),
        ('priceMin', priceMin),
        ('priceMax', priceMax),
        ('params[504]', '5256'),
        ('owner[]', 'private'),
        ('user', '1'),
        ('s', '1'),
        ('page', '1'),
        ('display', 'list'),
        ('limit', '30'),
    )

    params_web = (
        ('key', 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'),
        ('display', 'list'),
        ('categoryId', '14'),
        ('params[201]', '1060'),
        ('locationId', '621552'),
        ('query', search),
        ('priceMin', priceMin),
        ('priceMax', priceMax),
        ('params[504]', '5256'),
        ('owner[]', 'private'),
        ('user', '1'),
        ('s', '1'),
        ('page', '1'),
        ('display', 'list'),
        ('limit', '30'),
    )

    ua = UserAgent(browsers=['edge', 'chrome'])
    ua_str = ua.random
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    # headers: {
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/json'
    # }

    headers = {
        "Accept": "application/json, */*",
        'Content-Type': 'application/json',
        "User-Agent": ua_str,
    }
    session = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)

    urlm_main = 'https://m.avito.ru'  # 'https://www.m.avito.ru'
    url_main ='https://www.avito.ru' #/tarasovskiy/zapchasti_i_aksessuary?cd=1&d=1&q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80'
    url_loction = ""#'/rostov-na-donu'
    url_category = ""#'/mototsikly_i_mototehnika'
    url = url_main+url_loction+url_category

    html = session.get(url, headers=headers, params=params)#_web)
    cookie_str = get_coocies(html.cookies)
    cookie_dict = json.loads(cookie_str)
########## coocies
    print(cookie_str)#['buyer_laas_location'])
    pretty_dict_str = pprint.pformat(cookie_dict)
    print(pretty_dict_str)
    print(html.url)
    return '1' #html


if __name__ == '__main__':

    rawdata='u=2xrawwd7.1cwalh0.czes2z3b81o0; _gcl_au=1.1.702261351.1676272634; _ym_d=1676272635; _ym_uid=1676272635946525122; tmr_lvidTS=1676272635851; tmr_lvid=e59de466ad487dec9977deb7ed3ec36b; _ga=GA1.1.221393451.1676272636; adrcid=AIBf2Z3Umq85GKUTxLyQK6A; uxs_uid=2adeba40-ab70-11ed-aa3f-9f3cd45ff357; __zzatw-avito=MDA0dBA=Fz2+aQ==; cfidsw-avito=kvIa7GUvRAWmm1+TzZ1CU86teZmjMuHtt9zPo0CkseP/vSSXS0DeBsDWynIpvtoF3D0OWLUt50aNYMlvwe+ft/kEQSnX7D5xBJ2G2aYi/NJ9eUnuFXYFNchYNuQgVQtcOOE9SxGkauzl+UAVKT61ObUJ2IzcW43CwLuOcA==; gsscw-avito=C2obqhpH73dCTfjRg4WK/7A16kAQvlJKUSuxafkiGxi243BQP+GHugLzwCdH710MY7sQrumaJgjqD+89xEEUFx+RyUn4xGgAkIdKDn385ytOn6SO4RpAfuWSRJ/4vKIOzNwy3pLNm9PvKz49AvXR78o2aQC405YXSErXQ+Y4hPn6UW08epR+xez1guAvMWgQ5iQ+3Z887l4OR6hIh0VKA+0xEqlXJfAR0e0nkoFjcQOt7oCtrNim7R/m59fPtdkr+ic=; fgsscw-avito=seBcd181c886a63aed506cf5c32f80eaf77638d3; _ym_isad=2; v=1676357167; buyer_laas_location=652000; luri=rostov-na-donu; buyer_location_id=652000; _ym_visorc=b; redirectMav=1; sx=H4sIAAAAAAAC/1zWW5LrrA4F4LnkeT8AAgn2bAQCX+LY8SV27FM991Puv5Ld6Ql8phZLwv+7qKSUSyYGSC5xtJQDUCwGWHtQgS9//3dZL38vTTON9dYts6CBZ2iK7t3gVTeMfTfWcPlzyZe/GgmtAk349eei0XgNUZhSJo8qZhvRR4xgAltFLzlKpx8w8n3iNigVD7mHW6uo6FsDdfopW8RTNp6ZDbPoglCSVhgYwWVlimRj80te64ej7naVpSZ8PKCe1kbXS9ttKbb2/kO2Vin99ecC4DklXZSkCEEcBvRYhA0FAxnxJZdHLGjVrWpx4qLkMY7HQmZ6LCIg488zu//SACfZFI5ZoIAoDpCjKyZZ57OYIC+572tvaVptt2jcgVf91Lne4tinyuv9p6ydD6cc0XvU6LywBiS2nsliTIaZdfiX8ygJnmaoN8Lojjw0A3kL/b1qkEL8dYPwLReyxZCwjkolgGCdcBHnrEIbwkvehkfdVlvSSQM/E9asC7fHdg3XJvr+p2wcmlOWaDRyKS5QVi4UH8UlghjBFUvqJfuzYXvVCzxZlul6M81j2m59kmoFdJ9pmO8bzFDO7oAYEE8KvLXIYlGXoAL7l/x8PP3aNV2FuAaEYy7dcfSCWsPc3pvP1jn6lr11toSs0TorRkV2NiXM3hrU0b7kRNHtuYVe1mZKnYrxuT8K+SXeCRP9OvPZDcuISEiKRUW0MaogmU0ElRCceZ/ZeFpopq2/d6zVPAej5U4L7PPa+Bw/ZfiWkylsg8pashInUpSWgEg+o+X4L+ct35Z8RIbGi03G65imyhm3cjcs9CsN+/Xn4kowTqWSQIQyIFhlPKExLpF1/O5G4xTirPYEu0oa/e4aH+9puXaPKgy/+gxn6xARkxCWgMGhxZApZghCTqVE8pajtXNzc26upv0Y2vvM87q1LTyv19u2HT+n25mgv+WExaqsVVQ+WgW5YIpcfE7JcnxPCs06TsukKsVroLhVtwNuUJ5BTYOKw4dsgzplNk4pIWOdhRIQkLxo0pnVOfTlJR8P5VvFvgb9dNDnfeia9t4v10yQ/PqZs/+WpWT2wui99skVjip4TZ5KMD6adxp9MIn3Zq9tZ6dxzn293u7bPj6WqKWdfrXu3BtEBlKiopU5e1lK5JwwBiROPqn35t+f7dTdm23tXXY783OpR6zaUqVl8FZ/bFELZze8zkklbwQjBIeJKCnmEpwCIzGaf90QLTwGd9fPdSzhiPMd6qkPmfbB2p8yeOu+/lxCiWwdClAKpnDKMZTgHWlbSiis37Ks6tnm0EVigPoxH3nOcuislaJh+/WmnDIHBEbFkNglccZkn70i7Yt4gxxfspRumNuKUGTy2Q8He7juVWlayP1t+EwjnGnE4hISe4xODESfgwHjtPNa2eDtO4081q1Nlur8xHLbe8JWx1Zvt7ocVfVr18HZ50RFiKNG7YXAOiOJchIG9iUSvW8Qat3osU4P3Fu/U7Udy4g3cxy4LrHlT1mf3UjBsgqUnSgPOumSHUexEHJxWaf3rrt7g9s8zjOV0HfjbrtHX1+3Xtmnd8/mIw343vwpUI4OfUlWdLAlZ6/Pp1WctjbF9JLH+22AptVb6aDepLXLQgut2/50ce7bz5wdfstBaQSdvKCLRTNZMB5AJcbztf73VzDc1mZJt6ONC2DbDWoo07T7uiuyxI/phu83RQCsV1JEYwnBeaacbWYKFFTw5T2DZFurhR7bcvfutl6xjNTvx3UZadLH9HHm/za/SCo+kAuhOC7BSxZTsk3u/FDS780vrY66otq4caTcjF2juts4ZrU+tq7/+b9hlQlnzpm1C5md9wCpZKOs8cpkSkZBon/7OefB9NuEJj1ksHEbueorO6y526ex+ZCtxjONYgpZq5CLKEju3IEpOxL0yqmo3zM4VddpnIf5GTGodrjyXsb6WROt7fN6bT9ahw6+vv4fAAD//xKnJzuNCgAA; cto_bundle=1ZvLj19kMllyVDRwJTJCYzJSZEhabW0lMkJLUGR4ME1IT2tscTBpSWVBVUVCU0RYYkc1b1VzNGMxVE9KNTZ3UnAybnU3RkpGMSUyRjZtTk84Z2tueDdtcEZtUmZIUEtHZUp4T3NHcU5UeGZ0NkdOekZBTDBXVUtTTXdlOE1FTDZ0NXVuRzNMYk51eCUyQlJPYzRhSDBIRkFXaGZWWkRtUGhvZyUzRCUzRA; f=5.367a37203faa7618a7d90a8d0f8c6e0b47e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d40473de19da9ed218fe287829363e2d856a2e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe2d50b96489ab264ed3de19da9ed218fe23de19da9ed218fe246b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c76ff288cd99dba46e71c24777afa70281d49c1c93fcdfd74ae2a4761d49e98333722a7efdc61f8e20e28148569569b7939c1b38b6a26673a653a8db0a93fc2632ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748367e2c2adde1b2543de19da9ed218fe23de19da9ed218fe2b4af293ec419f67f6cd48844eb16d6d58edd6a0f40cbfd87da3d420d6cca468c; ft="pYqc37xwcBTB+VgjtQnjQpzc9HL3iISsby8RUdc5qIMXbUQl/bQ8arufkmPj48F5aKwPDuweulaGxPDMGOPhycyVnkH/rlLt/H9S/qgfWBsmeFAtVDI6rEDYBM51/iUKF9NI/JwJ64vTjYvk0dJQdujKOW3p63CqTO4UsCFcxCe0mCTI8+EvHneO3enyLYYA"; _mlocation=621540; _mlocation_mode=default; _ga_M29JC28873=GS1.1.1676357171.8.1.1676359169.58.0.0; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi5tLmF2aXRvLnJ1JTIyJTJDJTIyZXhwaXJlcyUyMiUzQSUyMldlZCUyQyUyMDE0JTIwRmViJTIwMjAyNCUyMDA3JTNBMTklM0EzMCUyMEdNVCUyMiUyQyUyMlNhbWVTaXRlJTIyJTNBJTIyTGF4JTIyJTJDJTIydmFsdWUlMjIlM0ElMjIlN0IlNUMlMjJ2YWx1ZSU1QyUyMiUzQSU1QyUyMjc4YzE5ZWM2NzBiYjZiNWIwYzg1ZjliOTk2YTA1NmVmJTVDJTIyJTJDJTVDJTIyZnBqc0Zvcm1hdCU1QyUyMiUzQXRydWUlN0QlMjIlN0Q=; isCriteoSetNew=true; tmr_detect=0|1676359172217'
    cookie1 = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=4e50185a2b0bf36f9f2d6d12485159e9.1675680145; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1660912321; buyer_laas_location=651110; buyer_location_id=651110; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1660912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg;'  # f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
    #js = get_coocies(rawdata)
    #print(js)
    #dump_js = json.dumps(js, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
    #           cls=None, indent=2, separators=None, default=None,
    #           sort_keys=False)
    #print(dump_js)

    url = 'https://www.avito.ru/'
    get_html(url)
