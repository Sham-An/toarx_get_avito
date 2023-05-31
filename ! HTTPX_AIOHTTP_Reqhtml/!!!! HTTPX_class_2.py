#https://www.python-httpx.org/advanced/
#https://github.com/encode/httpx/tree/master/httpx
#avito_parser_django\avito>
# python manage.py HTTPX_class_2

import asyncio
import threading
import httpx
import ssl

from lxml import html

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from aparser.models import Product
from aparser.models import Task

STATUS_NEW = 1
STATUS_READY = 2
##########################################
CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir' # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
#############################
#cookie = 'u=2tfvnhcb.ctv4iw.tymf98eh5pg0; _ym_d=1660584169; _ym_uid=166058416969271515; _gcl_au=1.1.56989214.1660584169; tmr_lvid=6bb642e099f3f60718329989304e0ddf; tmr_lvidTS=1660584170025; adrcid=Abu-CyKSxNnrOfCzX3o7WJw; buyer_laas_location=652000; uxs_uid=9f96c750-2309-11ed-a6ad-f34fafad57a6; buyer_location_id=652000; luri=rostov-na-donu; _gid=GA1.2.1638777385.1661600246; f=5.cc913c231fb04ced4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e92157fc552fc06411bc8794f0f6ce82fe915ac1de0d034112dc0d86d9e44006d8143114829cf33ca7143114829cf33ca7c772035eab81f5e1fb0fb526bb39450a87829363e2d856a2b5b87f59517a23f2c772035eab81f5e13de19da9ed218fe23de19da9ed218fe2c772035eab81f5e1143114829cf33ca7172c80659da4d447f1cc8f457244b1a81ac794a8d120d7dc3fa8c565c3a4ea025cc116b628bd61b75d3d12014bda85a4087cf35ba7d977642e1c124e209506cf29aa4cecca288d6b767bc15421a53740cde1c78086b997c046b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac4c51f6e3637213638418bac8c3b019882da10fb74cac1eab2da10fb74cac1eabbe1b8fec550f290a09360354b9a5173a3778cee096b7b985bf37df0d1894b088; ft="24CG5tzXFLJmY1UjO4748/U5Wcmjkkpj5FkT7xo1OJOtPxazmZH4rWeEs53H+1m4zGnvXGHl1CG3Bmd7e5oe3VPMAgdQODpzZIXYsqzn4VVeI0PjJZgrr3/niuxjq49Lnjdw6Pf4xPbI6I6F8mC1JpbNVUms1vF9Vz5kj7DeX7tOHeBWSFgRv+VfOvBROhO6"; redirectMav=1; v=1661674970; dfp_group=38; _ym_visorc=b; _ym_isad=2; isCriteoSetNew=true; SEARCH_HISTORY_IDS=0%2C2%2C%2C4; sx=H4sIAAAAAAAC%2F1zRS67iMBBA0b1kzMC%2FqrLfbuwqO%2BSDQ4AkJE%2FsvcWAbtEbOLrS%2FW10KFSUiuAhglUlJbBFWBgVUCyu%2Bflt1uanKQuPotuzB9pwKQyZrnwM%2B%2BHmOvS1OTW5%2BdGImlCjpdepAa2MCTqD0jpp43ymVEwJkQXRGvORRRZn4elcTtOK47G5PDwEbunAeqD%2BJ2PQFv1bdhCVOM%2BmRIksmpOPtmRHpCjn%2BJGXspmB7q6fpjZ1bdwdVczd3HcHX0v71ewpvOWogkrRE2QOolViUYaigozFJs8fud7y0epxEM%2FPYzPVuKTjrtbpnla%2FTV%2Byo3czIiILYQkYAB2GTCnbIASKmSR8ZOpjGR5OXS4tLW7EutZl3ve6DcPTlfk%2F2b5OTUSvFTkqEoUyBLQ5hmTYKrLo2X7kKw28zABFXyzjuR7QcVs1VVplafdvOcDr1IgvBbNkZXSEzNYYCQgcnPJiWMrf5mmO3f0x2a2%2FPQFoefK5P9%2BXwfhuHMPXQRPo9foTAAD%2F%2FwJADIJ3AgAA; abp=0; _ga_9E363E7BES=GS1.1.1661674982.17.1.1661675492.60.0.0; buyer_from_page=catalog; _ga_M29JC28873=GS1.1.1661674982.17.1.1661675492.60.0.0; _ga=GA1.2.1813055663.1660584170; _dc_gtm_UA-2546784-1=1; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyTW9uJTJDJTIwMjglMjBBdWclMjAyMDIzJTIwMDglM0EzMSUzQTMyJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyY2YzMDY3ZDU1MTc0NDRlZWRmNzMzNDgwZWQ2ZWNmYjglNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; cto_bundle=2JKQZV93UlJZZW1obWZ3Tm1oQkolMkJNVVppZnRYaG95bzlzQ3FJVmIwOUZDdmxLaG4yVUNkam9WZXJmVWdNU05lYmZvRXZIc3N4ZnJhVnhlTDRzV2VXclg0TnFVNTklMkJvJTJCVzlzTkdhMjJyd0pkakQlMkYzbVFrciUyRnAlMkZCbWZSNGxtNVpBb2pDZG5JM1NyV3FNSCUyRnJuNyUyQmh5S3JzYTlRJTNEJTNE; tmr_reqNum=280; tmr_detect=0%7C1661675496313'
'''
Мы также включаем вспомогательную функцию для создания правильно настроенных SSLContextэкземпляров.
>>> context = httpx.create_ssl_context()
Функция create_ssl_contextпринимает тот же набор аргументов конфигурации SSL ( trust_env, verify, certи http2аргументы), что httpx.Clientи илиhttpx.AsyncClient
>>> import httpx
>>> context = httpx.create_ssl_context(verify="/tmp/client.pem")
>>> httpx.get('https://example.org', verify=context)
<Response [200 OK]>
'''
ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)#+PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
ssl_context = httpx.create_ssl_context()
ssl_context.set_alpn_protocols(["h2"])
ssl_context.set_ciphers(CIPHERS)
# r = httpx.get(url_av, verify=ssl_context)

#logger = getLogger(__name__)
##########################################
url_0 = str('https://www.avito.ru/rostovskaya_oblast/mototsikly_i_mototehnika?cd=1&f=ASgCAgECAUXGmgwXeyJmcm9tIjoyMDAwLCJ0byI6NzAwMH0&q'+'=скутер&s=1')

# r = httpx.get(url_av, verify=ssl_context)
# # print(r.text)
# parse_xml(r.text)
'''
Настройка аутентификации
При выдаче запросов или создании экземпляра клиента authаргумент может использоваться для передачи используемой схемы аутентификации. Аргумент authможет быть одним из следующих...
Два кортежа username/ passwordдля использования с базовой проверкой подлинности.
Экземпляр 
httpx.BasicAuth() 
или 
httpx.DigestAuth().
Вызываемый объект, принимающий запрос и возвращающий аутентифицированный экземпляр запроса.
Экземпляр подклассов 

httpx.Auth
Наиболее сложным из них является последний, который позволяет создавать потоки аутентификации, включающие один или несколько запросов. Подкласс httpx.Authдолжен реализовывать def auth_flow(request)и выдавать любые запросы, которые необходимо сделать...
'''
#class MyCustomAuth(httpx.Auth): #
class MyCustomAuth:  #
    '''
Пользовательские классы проверки подлинности предназначены для того, чтобы не выполнять никаких операций ввода-вывода,
поэтому их можно использовать как с синхронизирующими, так и с асинхронными экземплярами клиента.
Если вы реализуете схему аутентификации, для которой требуется тело запроса, вам необходимо указать это в классе
с помощью свойства requires_request_body.
После этого вы сможете получить доступ request.contentк .auth_flow()методу.
    '''
    requires_response_body = True
    PAGE_LIMIT = 10

    def __init__(self): #(self, access_token, refresh_token, refresh_url)

        self.session = httpx.Client() #requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }
        self.task = None
        #
        # self.access_token = access_token
        # self.refresh_token = refresh_token
        # self.refresh_url = refresh_url

    def auth_flow(self, request):
        request.headers["X-Authentication"] = self.access_token
        response = yield request

        if response.status_code == 401:
            # If the server issues a 401 response, then issue a request to
            # refresh tokens, and resend the request.
            refresh_response = yield self.build_refresh_request()
            self.update_tokens(refresh_response)

            request.headers["X-Authentication"] = self.access_token
            yield request

    def build_refresh_request(self):
    # Return an `httpx.Request` for refreshing tokens.
    #request = httpx.Request("GET", "https://example.com")
        pass

    def find_task(self):
        obj = Task.objects.filter(status=STATUS_NEW).first()
        if not obj:
            raise CommandError('no tasks found')
        self.task = obj
#        logger.info(f'Работаем над заданием {self.task}')
        print(f'Работаем над заданием {self.task}')

    def finish_task(self):
        self.task.status = STATUS_READY
        self.task.save()
        logger.info(f'Завершили задание')

    def get_pagination_limit(self):
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
        limit = 1
        print(limit)
        #return min(int(params['p'][0]), self.PAGE_LIMIT)
        return limit

    def get_page(self, page: int = None):
        params = {
            'radius': 0,
            'user': 1,
        }
        if page and page > 1:
            params['p'] = page

        url = self.task.url
        print(url)
        #r = self.session.get(url, params=params)
        r = httpx.get(url, verify=ssl_context)
        print(r.status_code)
        print(r.text[:2000])
        # r.raise_for_status()
        # return r.text
        return 'get_page'


    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        # soup = bs4.BeautifulSoup(text, 'lxml')
        #
        # # Запрос CSS-селектора, состоящего из множества классов, производится через select
        # container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        # for item in container:
        #     self.parse_block(item=item)


    def parse_all(self):
        # Выбрать какое-нибудь задание
        self.find_task()

        limit = self.get_pagination_limit()
#        logger.info(f'Всего страниц: {limit}')
        print(f'Всего страниц: {limit}')

        for i in range(1, limit + 1):
#            logger.info(f'Работаем над страницей {i}')
            print(f'Работаем над страницей {i}')
            self.get_blocks(page=i)

        # Завершить задание
        #self.finish_task()

    def update_tokens(self, response):
        # Update the `.access_token` and `.refresh_token` tokens
        # based on a refresh response.
        data = response.json()

    def test(self):
        say = 'start_'
        #print(say)
        return say

# class test():
#     def say(self):
#         print('start_')

class Command(BaseCommand):
    # help = 'The Zen of Python'
    #
    # def handle(self, *args, **options):
    #     import this
    help = 'Парсинг Avito'

    def handle(self, *args, **options):
        p = MyCustomAuth()
        #print(p.test())
        # p = AvitoParser()
        p.parse_all()
        # s=test()
        # s.say()


#Пользовательские классы проверки подлинности предназначены для того,
# чтобы не выполнять никаких операций ввода-вывода, поэтому их можно использовать
# как с синхронизирующими, так и с асинхронными экземплярами клиента.
# Если вы реализуете схему аутентификации, для которой требуется тело запроса,
# вам необходимо указать это в классе с помощью свойства requires_request_body.

#После этого вы сможете получить доступ request.contentк .auth_flow()методу.
'''
class MyCustomAuth(httpx.Auth):
    requires_request_body = True

    def __init__(self, token):
        self.token = token

    def auth_flow(self, request):
      response = yield request
      if response.status_code == 401:
          # If the server issues a 401 response then resend the request,
          # with a custom `X-Authentication` header.
          request.headers['X-Authentication'] = self.sign_request(...)
          yield request

    def sign_request(self, request):
        # Create a request signature, based on `request.method`, `request.url`,
        # `request.headers`, and `request.content`.
        ...
#Точно так же, если вы реализуете схему, требующую доступа к тексту ответа,
# используйте это requires_response_bodyсвойство. После этого вы сможете получить
# доступ к свойствам и методам тела ответа, таким как response.content, response.text, response.json()и т. д.

class MyCustomAuth(httpx.Auth):
    requires_response_body = True

    def __init__(self, access_token, refresh_token, refresh_url):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_url = refresh_url

    def auth_flow(self, request):
        request.headers["X-Authentication"] = self.access_token
        response = yield request

        if response.status_code == 401:
            # If the server issues a 401 response, then issue a request to
            # refresh tokens, and resend the request.
            refresh_response = yield self.build_refresh_request()
            self.update_tokens(refresh_response)

            request.headers["X-Authentication"] = self.access_token
            yield request

    def build_refresh_request(self):
        # Return an `httpx.Request` for refreshing tokens.
        ...

    def update_tokens(self, response):
        # Update the `.access_token` and `.refresh_token` tokens
        # based on a refresh response.
        data = response.json()
'''
