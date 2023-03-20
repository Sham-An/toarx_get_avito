import asyncio
import csv
import json
import time
import aiohttp
from bs4 import BeautifulSoup


async def save_product(book_name, product_info):
    json_file_name = book_name.replace(' ', '_')
    with open(f'data/{json_file_name}.json', 'w') as book_file:
        json.dump(product_info, book_file)


async def scrape(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')
            book_name = soup.select_one('.product_main').h1.text
            rows = soup.select('.table.table-striped tr')
            product_info = {row.th.text: row.td.text for row in rows}
            await save_product(book_name, product_info)


async def main():
    start_time = time.time()

    tasks = []
    with open('urls.csv') as file:
        csv_reader = csv.DictReader(file)
        for csv_row in csv_reader:
            task = asyncio.create_task(scrape(csv_row['url']))
            tasks.append(task)

    print('Saving the output of extracted information')
    await asyncio.gather(*tasks)

    time_difference = time.time() - start_time
    print(f'Scraping time: %.2f seconds.' % time_difference)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
#
# #async with aiohttp.ClientSession() as cs:
# async with aiohttp.ClientSession(headers={"Referer": "https://streamable.com"}) as cs:
#     async with cs.get('https://cdn-e1.streamable.com/video/mp4/kphjz.mp4') as r:
#         print(r.status)
#         # if r.status == 200:
#         #     img = await r.read()
#         #     with open('C:/xxxx/xxxx/xxxx/xxxx/Streamables/' + url.split('/')[-1], 'wb') as f:
#         #         f.write(img)
#         #         f.close()
#         #         print('Downloaded {0}'.format(url.split('/')[-1]))