#!/usr/bin/env python3
"""
web cache file
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ decorator counting accessing to url """
    @wraps(method)
    def wrapper(url):
        ket_of_cache = "cached:" + url
        data_from_cache = store.get(ket_of_cache)
        if data_from_cache:
            return data_from_cache.decode("utf-8")

        key_counter = "count:" + url
        html = method(url)

        store.incr(key_counter)
        store.set(ket_of_cache, html)
        store.expire(ket_of_cache, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ HTML of the url """
    result = requests.get(url)
    return result.text