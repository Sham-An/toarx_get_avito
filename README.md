# realty
Мониторинг недвижимости
https://www.youtube.com/playlist?list=PLveyMGRVUwrB6r-krN8cfR1QPiNcpUouV

view-source:

view-source:https://www.avito.ru/rostov-na-donu/transport?q=%D0%BC%D0%BE%D1%82%D0%BE

Я получал случайные ошибки подключения от очень старого сервера (он получил рейтинг F по https://www.ssllabs.com ), пока я не начал использовать этот код в своем HTTPAdapter:

def init_poolmanager(self, *args, **kwargs):
    ssl_context = ssl.create_default_context()

    # Sets up old and insecure TLSv1.
    ssl_context.options &= ~ssl.OP_NO_TLSv1_3 & ~ssl.OP_NO_TLSv1_2 & ~ssl.OP_NO_TLSv1_1
    ssl_context.minimum_version = ssl.TLSVersion.TLSv1

    # Also you could try to set ciphers manually as it was in my case.
    # On other ciphers their server was reset the connection with:
    # [Errno 104] Connection reset by peer
    # ssl_context.set_ciphers("ECDHE-RSA-AES256-SHA")

    # See urllib3.poolmanager.SSL_KEYWORDS for all available keys.
    kwargs["ssl_context"] = ssl_context

    return super().init_poolmanager(*args, **kwargs)

#####################################################################

# Для корректной работы парсера рекомендую вам использовать TLS не ниже V1.2.

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

try:
    r = session.request('GET', 'https://www.avito.ru')
    print(r.text)[1000]
except Exception as exception:
    print(exception)