from os.path import join as os_join, normpath as os_normpath
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from requests import Session
import asyncio


SESSION = Session()
SESSION.mount(
    'http://',
    HTTPAdapter(
        pool_connections=100,
        pool_maxsize=100
    )
)
req_get = SESSION.get


def mkpath(*paths):
    return os_normpath(os_join(*map(str, paths)))


def clamp(x, bottom, top):
    return bottom if x < bottom else top if x > top else x


def md_link(text, link):
    return "[{}]({})".format(text, link)


def req_get_parallel(urls):
    async def get_pages(urls):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [
                loop.run_in_executor(executor, req_get, url)
                for url in urls
            ]
        return await asyncio.gather(*futures)

    return asyncio.get_event_loop().run_until_complete(get_pages(urls))
