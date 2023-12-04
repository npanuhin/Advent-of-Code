import os

# from requests.adapters import HTTPAdapter
from requests import Session


SESSION = Session()
# SESSION.mount(
#     'http://',
#     HTTPAdapter(
#         pool_connections=100,
#         pool_maxsize=100
#     )
# )
req_get = SESSION.get


def mkpath(*paths: str) -> str:
    return os.path.normpath(os.path.join(*map(str, paths)))


def clamp(value: int, bottom: int, top: int) -> int:
    return bottom if value < bottom else top if value > top else value


def format_time(milliseconds: int) -> str:
    assert milliseconds is not None

    if milliseconds < 1:
        return '< 1ms'

    if milliseconds < 290:
        return f'{round(milliseconds)}ms'

    if milliseconds < 950:
        return '< 1s'

    return f'{round(milliseconds / 1000)}s'
