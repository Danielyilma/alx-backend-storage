#!/usr/bin/env python3
'''creating a cache with redis database'''
import redis
from typing import Union, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
        decorator that counts the number of time a function is called
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
            wraped function that counts and call the main function
        '''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
        stores a history calles of a function
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
            wrapped function
        '''
        key = method.__qualname__
        self._redis.rpush(key + ":inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(key + ":outputs", str(result))
        return result

    return wrapper


class Cache:
    '''
        cache class
    '''
    def __init__(self) -> None:
        '''initialize class attribute'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[int, float, str, bytes]) -> str:
        '''stores in redis database'''
        random_num = str(uuid.uuid4())
        self._redis.set(random_num, data)
        return random_num

    def get(self, key: str, fn: Union[Callable, None] = None) \
            -> Union[int, float, str, bytes]:
        '''get data from redis database'''
        result = self._redis.get(key)

        if fn is None:
            return result
        return fn(result)

    def get_int(self, key: str) -> int:
        return int(self._redis.get(key))

    def get_str(self, key: str) -> str:
        return str(self._redis.get(key))


def replay(func: Callable) -> None:
    '''
        replay the history of a function includes
        function name , inputs and outputs from this function
    '''
    key = func.__qualname__

    _redis = redis.Redis()
    count = _redis.get(key).decode("utf-8")
    outputs = _redis.lrange(key + ":outputs", 0, -1)
    inputs = _redis.lrange(key + ":inputs", 0, -1)

    print(f"{key} was called {count} times:")

    for inp, out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            key, inp.decode("utf-8"), out.decode("utf-8")
        ))
