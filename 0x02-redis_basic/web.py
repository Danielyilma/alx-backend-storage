#!/usr/bin/env python3
'''an expiring web cache and tracker'''
from functools import wraps
import redis
import requests
from typing import Callable


_redis = redis.Redis()


def count_access(func: Callable) -> Callable:
    '''
        a wrapper function for couting access to a function
    '''
    def func2(*args):
        '''
            wrapped function
        '''
        key = "count:" + str(*args)
        _redis.incr(key)
        result = _redis.get(f"cached:{str(*args)}")
        if result:
            return result.decode("utf-8")
        text = func(*args)
        _redis.setex(f"cached:{str(*args)}", 10, text)
        return text

    return func2


@count_access
def get_page(url: str) -> str:
    '''takes a url and return the page from that url'''
    return (requests.get(url)).text
