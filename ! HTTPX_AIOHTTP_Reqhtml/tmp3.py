# -*- coding:utf-8 -*-

# Weibo Hot Search
import asyncio
import aiohttp
import ssl

setattr(asyncio.sslproto._SSLProtocolTransport, "_start_tls_compatible", True)


async def fetch(url):

    FORCED_CIPHERS = (
        'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
        'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES'
    )
    sslcontext = ssl.create_default_context()
    sslcontext.options |= ssl.OP_NO_SSLv3
    sslcontext.options |= ssl.OP_NO_SSLv2
    sslcontext.options |= ssl.OP_NO_TLSv1_1
    sslcontext.options |= ssl.OP_NO_TLSv1_2
    sslcontext.options |= ssl.OP_NO_TLSv1_3
    sslcontext.set_ciphers(FORCED_CIPHERS)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=50, loop=loop)) as session:
        r = await session.get('https://www.mdnkids.com/news/?Serial_NO=108552', ssl=sslcontext)
        print(await r.text())


    # conn = aiohttp.TCPConnector(verify_ssl=False)  # Prevent ssl from reporting errors
    # async with aiohttp.request('GET', url, connector=conn) as resp:
    #     if resp.status != 200:
    #         return ''
    #     return await resp.text()

def create_tcp_connector(*args, **kwargs) -> aiohttp.TCPConnector:
    """
    Creates TCP connector with resonable defaults.
    For details about available parameters refer to
    `aiohttp.TCPConnector <https://docs.aiohttp.org/en/stable/client_reference.html#tcpconnector>`_
    """
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(certifi.where())
    kwargs.setdefault("ssl", ssl_context)
    kwargs.setdefault("limit", DEFAULT_LIMIT)
    return aiohttp.TCPConnector(*args, **kwargs)  # type: ignore due to https://github.com/python/mypy/issues/4001
async def run():
    url = 'https://s.weibo.com/top/summary'
    url = "https://www.avito.ru/"
    html = await fetch(url)
    return html


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(run())
    print(res)
