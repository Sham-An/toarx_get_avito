import asyncio
import aiohttp
import time


start_time = time.time()
all_data = []

async def get_page_data(session, category: str, page_id: int) -> str:
    if page_id:
        url = f'https://ozon.ru/brand/{category}/?page={page_id}'
    else:
        url = f'https://ozon.ru/brand/{category}/'
    async with session.get(url) as resp:
        assert resp.status == 200
        print(f'get url: {url}')
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text


async def load_site_data():
    categories_list = ['playstation-79966341', 'adidas-144082850', 'bosch-7577796', 'lego-19159896']
    async with aiohttp.ClientSession() as session:
        tasks = []
        for cat in categories_list:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(session, cat, page_id))
                tasks.append(task)
                # process text and do whatever we need...
        await asyncio.gather(*tasks)


asyncio.run(load_site_data())

end_time = time.time() - start_time
print(all_data)
print(f"\nExecution time: {end_time} seconds")