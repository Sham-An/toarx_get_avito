#https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9&params%5B1283%5D=14756&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1&lastStamp=1611316560&display=list&limit=30

import json
import sqlite3
import time
from datetime import datetime
import requests
from realty import check_database

import ssl
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)

#url_api = 'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9&params%5B1283%5D=14756&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1&lastStamp=1611316560&display=list&limit=30'
url_api = 'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9'#&params[1283]D=14756'#&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1' #&lastStamp=1611316560&display=list&limit=30'


try:
    #r = session.request('GET', 'https://www.avito.ru')
    r = session.request('GET', url_api)
    print(r.text)[1000]
except Exception as exception:
    print(exception)

# def main():
# https://m.avito.ru/api/9
# https://m.avito.ru/api/10
# https://m.avito.ru/api/11
#   OK!!! JSON!!!!  #burp0_url = "https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&priceMin=1&priceMax=9999999&owner[]=private&sort=date&query=iphone&page=1&display=list&limit=30"
#     burp0_url = "https://www.avito.ru/rostov-na-donu/mototsikly_i_mototehnika/turenduro_fuego_scrambler_250_v_nalichii_2562662581"
#     burp0_headers = {
#         "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36",
#         "Accept": "application/json, text/plain, */*", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json;charset=utf-8", "Dnt": "1",
#         "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
#     r = requests.get(burp0_url, headers=burp0_headers)#.json()
#     print(r)
#

# if __name__ == '__main__':
#     main()

############################################################
############################################# BAD key
# import requests
#
# burp0_url = "https://m.avito.ru/api/11/items?key=1&priceMin=1&priceMax=9999999&owner[]=private&sort=date&query=iphone&page=1&display=list&limit=30"
# burp0_headers = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36",
#     "Accept": "application/json, text/plain, */*", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json;charset=utf-8", "Dnt": "1",
#     "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
# r = requests.get(burp0_url, headers=burp0_headers).json()
# print(r)
##################################################
###################################### Bad id

# url = "https://m.avito.ru/api/11/items?key=1&priceMin=1&priceMax=9999999&owner[]=private&sort=date&query=iphone&page=1&display=list&limit=30"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36",
#         "Accept": "application/json, text/plain, */*", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json;charset=utf-8", "Dnt": "1",
#         "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
#     async with aiohttp.ClientSession() as cs:
#         async with cs.get(url, headers=headers) as req:
#             items = await req.json()
#             print(items)
#
