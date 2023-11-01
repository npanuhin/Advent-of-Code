from concurrent.futures import ThreadPoolExecutor
import asyncio
import os

from requests.adapters import HTTPAdapter
from requests import Session


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
    return os.path.normpath(os.path.join(*map(str, paths)))


def clamp(value, bottom, top):
    return bottom if value < bottom else top if value > top else value


def md_link(text: str, link: str) -> str:
    return f"[{text}]({link})"


def html_link(text: str, link: str) -> str:
    return f'<a href="{link}">{text}</a>'


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
