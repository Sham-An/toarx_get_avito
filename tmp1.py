#Requests в Python по умолчанию использует устаревший протокол TLS V1.
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

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir' # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
#############################
#cookie = 'u=2tfvnhcb.ctv4iw.tymf98eh5pg0; _ym_d=1660584169; _ym_uid=166058416969271515; _gcl_au=1.1.56989214.1660584169; tmr_lvid=6bb642e099f3f60718329989304e0ddf; tmr_lvidTS=1660584170025; adrcid=Abu-CyKSxNnrOfCzX3o7WJw; buyer_laas_location=652000; uxs_uid=9f96c750-2309-11ed-a6ad-f34fafad57a6; buyer_location_id=652000; luri=rostov-na-donu; _gid=GA1.2.1638777385.1661600246; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e92157fc552fc06411bc8794f0f6ce82fe915ac1de0d034112dc0d86d9e44006d8143114829cf33ca7143114829cf33ca7c772035eab81f5e1fb0fb526bb39450a87829363e2d856a2b5b87f59517a23f2c772035eab81f5e13de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca7172c80659da4d447f1cc8f457244b1a81ac794a8d120d7dc3fa8c565c3a4ea025cc116b628bd61b75d3d12014bda85a4087cf35ba7d977642e1c124e209506cf29aa4cecca288d6b767bc15421a53740cde1c78086b997c046b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac4c51f6e3637213638418bac8c3b019882da10fb74cac1eab2da10fb74cac1eabbe1b8fec550f290a09360354b9a5173a3778cee096b7b985bf37df0d1894b088; ft="24CG5tzXFLJmY1UjO4748/U5Wcmjkkpj5FkT7xo1OJOtPxazmZH4rWeEs53H+1m4zGnvXGHl1CG3Bmd7e5oe3VPMAgdQODpzZIXYsqzn4VVeI0PjJZgrr3/niuxjq49Lnjdw6Pf4xPbI6I6F8mC1JpbNVUms1vF9Vz5kj7DeX7tOHeBWSFgRv+VfOvBROhO6"; redirectMav=1; v=1661674970; dfp_group=38; _ym_visorc=b; _ym_isad=2; isCriteoSetNew=true; SEARCH_HISTORY_IDS=0%2C2%2C%2C4; sx=H4sIAAAAAAAC%2F1zRS67iMBBA0b1kzMC%2FqrLfbuwqO%2BSDQ4AkJE%2FsvcWAbtEbOLrS%2FW10KFSUiuAhglUlJbBFWBgVUCyu%2Bflt1uanKQuPotuzB9pwKQyZrnwM%2B%2BHmOvS1OTW5%2BdGImlCjpdepAa2MCTqD0jpp43ymVEwJkQXRGvORRRZn4elcTtOK47G5PDwEbunAeqD%2BJ2PQFv1bdhCVOM%2BmRIksmpOPtmRHpCjn%2BJGXspmB7q6fpjZ1bdwdVczd3HcHX0v71ewpvOWogkrRE2QOolViUYaigozFJs8fud7y0epxEM%2FPYzPVuKTjrtbpnla%2FTV%2Byo3czIiILYQkYAB2GTCnbIASKmSR8ZOpjGR5OXS4tLW7EutZl3ve6DcPTlfk%2F2b5OTUSvFTkqEoUyBLQ5hmTYKrLo2X7kKw28zABFXyzjuR7QcVs1VVplafdvOcDr1IgvBbNkZXSEzNYYCQgcnPJiWMrf5mmO3f0x2a2%2FPQFoefK5P9%2BXwfhuHMPXQRPo9foTAAD%2F%2FwJADIJ3AgAA; abp=0; _ga_9E363E7BES=GS1.1.1661674982.17.1.1661675492.60.0.0; buyer_from_page=catalog; _ga_M29JC28873=GS1.1.1661674982.17.1.1661675492.60.0.0; _ga=GA1.2.1813055663.1660584170; _dc_gtm_UA-2546784-1=1; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyTW9uJTJDJTIwMjglMjBBdWclMjAyMDIzJTIwMDglM0EzMSUzQTMyJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyY2YzMDY3ZDU1MTc0NDRlZWRmNzMzNDgwZWQ2ZWNmYjglNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; cto_bundle=2JKQZV93UlJZZW1obWZ3Tm1oQkolMkJNVVppZnRYaG95bzlzQ3FJVmIwOUZDdmxLaG4yVUNkam9WZXJmVWdNU05lYmZvRXZIc3N4ZnJhVnhlTDRzV2VXclg0TnFVNTklMkJvJTJCVzlzTkdhMjJyd0pkakQlMkYzbVFrciUyRnAlMkZCbWZSNGxtNVpBb2pDZG5JM1NyV3FNSCUyRnJuNyUyQmh5S3JzYTlRJTNEJTNE; tmr_reqNum=280; tmr_detect=0%7C1661675496313'


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)


def main():
    #CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
    session = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)

    try:
        url_api_9 = 'https://m.avito.ru/api/9/items'  # Урл первого API, позволяет получить id и url объявлений по заданным фильтрам
        url_av_1 = 'https://www.avito.ru/novosibirsk/muzykalnye_instrumenty/midi-klaviatura_cme_u-key_2521013620'
        url_av = url_av_1


        #https://m.avito.ru/api/11/items
        #https://www.avito.ru
        r = session.request('GET', url_av)
        print(r.text)#[1000])#[1000]
    except Exception as exception:
        print(exception)


if __name__ == '__main__':
    main()
