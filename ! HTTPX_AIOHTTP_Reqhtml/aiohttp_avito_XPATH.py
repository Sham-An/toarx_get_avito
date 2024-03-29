import asyncio
import requests
import aiohttp

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "https://m.avito.ru/api/11/items?key=1") as resp:
            print(resp.status)
            print(await resp.text())
    r = requests.get(
        "https://m.avito.ru/api/11/items?key=1").text
    print(r)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# import asyncio
# import json
# from aiohttp import ClientSession, web
# from aiologger.loggers.json import JsonLogger
#
# key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
# CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
#
#
# logger = JsonLogger.with_default_handlers(
#             level='DEBUG',
#             serializer_kwargs={'ensure_ascii': False},
#         )
#
#
#
# async def main():
#     app = web.Application()
#     app.add_routes([web.get('/weather', handle)])
#     runner = web.AppRunner(app)
#     await runner.setup()
#     site = web.TCPSite(runner, 'localhost', 8080)
#     await site.start()
#
#     while True:
#         await asyncio.sleep(3600)
#

if __name__ == '__main__':
    asyncio.run(main())


# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
#
#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             try:
#                 return weather_json["weather"][0]["main"]
#             except KeyError:
#                 return 'Нет данных'
#
#
# async def get_translation(text, source, target):
#     await logger.info(f'Поступил запрос на на перевод слова: {text}')
#
#     async with ClientSession() as session:
#         url = 'https://libretranslate.de/translate'
#
#         data = {'q': text, 'source': source, 'target': target, 'format': 'text'}
#
#         async with session.post(url, json=data) as response:
#             translate_json = await response.json()
#
#             try:
#                 return translate_json['translatedText']
#             except KeyError:
#                 logger.error(f'Невозможно получить перевод для слова: {text}')
#                 return text
#
#
# async def handle(request):
#     city_ru = request.rel_url.query['city']
#
#     await logger.info(f'Поступил запрос на город: {city_ru}')
#
#     city_en = await get_translation(city_ru, 'ru', 'en')
#     weather_en = await get_weather(city_en)
#     weather_ru = await get_translation(weather_en, 'en', 'ru')
#
#     result = {'city': city_ru, 'weather': weather_ru}
#
#     return web.Response(text=json.dumps(result, ensure_ascii=False))
#
#
# async def main():
#     app = web.Application()
#     app.add_routes([web.get('/weather', handle)])
#     runner = web.AppRunner(app)
#     await runner.setup()
#     site = web.TCPSite(runner, 'localhost', 8080)
#     await site.start()
#
#     while True:
#         await asyncio.sleep(3600)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())