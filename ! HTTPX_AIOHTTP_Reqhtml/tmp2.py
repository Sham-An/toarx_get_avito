from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from openpyxl import Workbook
import asyncio
import aiohttp

data2 = []
wb = Workbook()
ws = wb.active
ws.title = 'Товары'
ws.append(['Артикул', 'Количество', 'Цена', 'Тип', 'Вес', 'Вставка', 'Коллекция', 'Ссылка на изображение'])


async def get_page_data(page, session):
    cookies = {
        'ASP.NET_SessionId': 'i1gip0fre5uzl4iqlkubv1cp',
        'SLG_G_WPT_TO': 'ru',
        'SLG_GWPT_Show_Hide_tmp': '1',
        'SLG_wptGlobTipTmp': '1',
        'ICusrcartgd': 'be6d8ad2-c52e-49b8-83b2-f384a9feaa60',
        'IWusrsesckgd': 'jojhbQMjYWEdV9ohRKijJKalgxKEvPEPzVqoH/F2376n50ziaNRcMA==',
    }

    headers = {
        'authority': 'catalog.aquamarine.kz',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Opera GX";v="85"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://catalog.aquamarine.kz',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://catalog.aquamarine.kz/catalog/index.aspx',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ASP.NET_SessionId=i1gip0fre5uzl4iqlkubv1cp; SLG_G_WPT_TO=ru; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; ICusrcartgd=be6d8ad2-c52e-49b8-83b2-f384a9feaa60; IWusrsesckgd=jojhbQMjYWEdV9ohRKijJKalgxKEvPEPzVqoH/F2376n50ziaNRcMA==',
    }

    data = {
        'msearch': '',
    }
    async with session.post(
            f'https://catalog.aquamarine.kz/catalog/products.ashx?rnd=958090487&q=&spec=&mip=317&map=7777%20777&mippg=161&mappg=5466%20222&miw=0.14&maw=137.74&miq=1&maq=241&miprcs=999999.999&maprcs=0&page={page}&sort=art-down&view=2&spc=1,&brid=7',
            cookies=cookies, headers=headers, data=data).text.replace('\\', '') as response:
        soup = BeautifulSoup(await response, 'lxml')
        contain = soup.find('div', class_='products')
        products = contain.find_all('div', class_='item wide')

        for product in products:
            articul = product.find('div', class_='head row').find('div', class_='val').text.strip()
            count = product.find_all('div', class_='row')[-2].find('div', class_='val').text.strip()
            link = 'https://catalog.aquamarine.kz' + (product.find('a').get('href'))
            link_img = 'https://catalog.aquamarine.kz' + (product.find('a').find('img').get('src'))

            price = product.find_all('div', class_='row')[2].find('div', class_='val').text.strip().split('K')[0]
            type = product.find('div', class_='head row').find('div', class_='name').text.strip()
            weight = product.find_all('div', class_='row')[1].find('div', class_='val').text.strip().split('г')[0]

            async with aiohttp.ClientSession() as session:
                request = await session.get(link, headers=headers, cookies=cookies)
                soup2 = BeautifulSoup(request.text, 'lxml')
                try:
                    collection = soup2.find('td', text="Коллекция").find_next_sibling('td').text.strip()
                except:
                    collection = 'None'
                try:
                    insert = soup2.find('td', text="Вставки").find_next_sibling('td').text.strip().replace(';', ',')
                except:
                    insert = 'None'

            ws.append([articul, count, price, type, weight, insert, collection, link_img])
        print(f'Страница {page}')


async def gather_data(page=1):
    cookies = {
        'ASP.NET_SessionId': 'i1gip0fre5uzl4iqlkubv1cp',
        'SLG_G_WPT_TO': 'ru',
        'SLG_GWPT_Show_Hide_tmp': '1',
        'SLG_wptGlobTipTmp': '1',
        'ICusrcartgd': 'be6d8ad2-c52e-49b8-83b2-f384a9feaa60',
        'IWusrsesckgd': 'jojhbQMjYWEdV9ohRKijJKalgxKEvPEPzVqoH/F2376n50ziaNRcMA==',
    }

    headers = {
        'authority': 'catalog.aquamarine.kz',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Opera GX";v="85"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://catalog.aquamarine.kz',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://catalog.aquamarine.kz/catalog/index.aspx',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ASP.NET_SessionId=i1gip0fre5uzl4iqlkubv1cp; SLG_G_WPT_TO=ru; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; ICusrcartgd=be6d8ad2-c52e-49b8-83b2-f384a9feaa60; IWusrsesckgd=jojhbQMjYWEdV9ohRKijJKalgxKEvPEPzVqoH/F2376n50ziaNRcMA==',
    }

    data = {
        'msearch': '',
    }
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            f'https://catalog.aquamarine.kz/catalog/products.ashx?rnd=958090487&q=&spec=&mip=317&map=7777%20777&mippg=161&mappg=5466%20222&miw=0.14&maw=137.74&miq=1&maq=241&miprcs=999999.999&maprcs=0&page={page}&sort=art-down&view=2&spc=1,&brid=7',
            cookies=cookies, headers=headers, data=data)
        tasks = []
        while True:
            soup = BeautifulSoup((await response.read()), 'lxml')
            contain = soup.find('div', class_='products')
            products = contain.find_all('div', class_='item wide')
            tasks.append(asyncio.create_task(get_page_data(page, session)))
            await asyncio.gather(*tasks)
            if products < 24:
                break
            page += 1


def main():
    asyncio.run(gather_data())


if __name__ == '__main__':
    main()