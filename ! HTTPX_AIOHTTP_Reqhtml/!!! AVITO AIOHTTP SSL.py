import asyncio
import ssl
from contextlib import contextmanager
#from http import HTTPStatus
import aiohttp
import certifi
import logging

#: Default limit of the simultaneous connections for ssl connector.
DEFAULT_LIMIT = 20
#: Default timeout in seconds used for client session.
DEFAULT_TIMEOUT = 60



def create_tcp_connector(*args, **kwargs) -> aiohttp.TCPConnector:
    """
    Creates TCP connector with resonable defaults.
    For details about available parameters refer to
    `aiohttp.TCPConnector `_
    """
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(certifi.where())
    kwargs.setdefault("ssl", ssl_context)
    kwargs.setdefault("limit", DEFAULT_LIMIT)
    # due to https://github.com/python/mypy/issues/4001
    return aiohttp.TCPConnector(*args, **kwargs)  # type: ignore


async def test():
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


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())

# python3.x
# hint https://github.com/requests/requests/issues/4046

# import ssl
# import aiohttp
# import asyncio
#
#
# async def test():
#     FORCED_CIPHERS = (
#         'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
#         'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES'
#     )
#     sslcontext = ssl.create_default_context()
#     # sslcontext.options |= ssl.OP_NO_SSLv3
#     # sslcontext.options |= ssl.OP_NO_SSLv2
#     # sslcontext.options |= ssl.OP_NO_TLSv1_1
#     sslcontext.options |= ssl.OP_NO_TLSv1_2
#     # sslcontext.options |= ssl.OP_NO_TLSv1_3
#     sslcontext.set_ciphers(FORCED_CIPHERS)
#
#     print(repr(sslcontext.options))
#     session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=50, loop=loop, verify_ssl=False))
#     r = await session.get('https://www.mdnkids.com/news/?Serial_NO=108552', ssl=sslcontext)
#     print(await r.text())
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(test())