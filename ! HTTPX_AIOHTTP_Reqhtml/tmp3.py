# -*- coding:utf-8 -*-

# Weibo Hot Search
import asyncio
import aiohttp


async def fetch(url):
    conn = aiohttp.TCPConnector(verify_ssl=False)  # Prevent ssl from reporting errors
    async with aiohttp.request('GET', url, connector=conn) as resp:
        if resp.status != 200:
            return ''
        return await resp.text()


async def run():
    url = 'https://s.weibo.com/top/summary'
    url = "https://www.avito.ru/"
    html = await fetch(url)
    return html


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(run())
    print(res)
