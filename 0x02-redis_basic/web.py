#!/usr/bin/env python3
'''an expiring web cache and tracker'''
from functools import wraps
import redis
import requests
from typing import Callable


def count_access(func: Callable) -> Callable:
    '''a wrapper function for couting access to a function'''
    def func2(*args):
        '''wrapped function'''
        key = "count:" + str(*args)
        _redis = redis.Redis()
        _redis.incr(key)
        result = _redis.get(f"cached{str(*args)}")
        if result:
            return result
        text = func(*args)
        _redis.setex(f"cached{str(*args)}", 10, text)
        return text

    return func2


@count_access
def get_page(url: str) -> str:
    '''takes a url and return the page from that url'''
    return (requests.get(url)).text

if __name__ == "__main__":
    print(get_page("https://www.youtube.com"))