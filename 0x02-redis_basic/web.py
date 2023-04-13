#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ Decorator counting how many times
    a URL is accessed """
    @wraps(method)
    def wrapper(url):
        c_k = "cached:" + url
        c_d = store.get(c_k)
        if c_d:
            return c_d.decode("utf-8")

        countkey = "count:" + url
        hml = method(url)

        store.incr(countkey)
        store.set(c_k, hml)
        store.expire(c_k, 10)
        return hml
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Get HTML of given url """
    result = requests.get(url)
    return result.text
