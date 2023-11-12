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
