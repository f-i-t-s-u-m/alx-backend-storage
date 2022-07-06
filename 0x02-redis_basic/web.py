#!/usr/bin/env python3
""" python web tracking file """


import requests
from redis import Redis
from typing import Callable
from functools import wraps


def counter(fn: Callable) -> Callable:
    """ counter function """
    red = Redis()
    @wraps(fn)
    def inner(url):
        """ inner decorator function """
        red.incr(f'count:{url}')
        html = red.get(f'cached:{url}')
        if (html):
            return html.decode('utf-8')
        html = fn(url)
        red.setex(f'cached:{url}', 10, html)
        return html
    return inner


@counter
def get_page(url: str) -> str:
    """ get page and track """
    return requests.get(url).text
