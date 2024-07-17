#!/usr/bin/env python3
'''creating a cache with redis database'''
import redis
from typing import Union
import uuid
from functools import wraps

class Cache:
    '''cache class'''

    def __init__(self):
        '''initialize class attribute'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(func: callable):
        '''decorator that counts the number of time a function is called'''
        @wraps(func)
        def func2(self, *args, **kwargs):
            '''wraped function that counts and call the main function'''
            self._redis.incr(func.__qualname__)
            return func(self, *args, **kwargs)
        
        return func2

    @count_calls
    def store(self, data: Union[int, float, str, bytes]) -> str:
        '''stores in redis database'''
        random_num = str(uuid.uuid4())
        self._redis.set(random_num, data)
        return random_num

    def get(self, key: str, fn: Union[callable, None]=None) -> Union[int, float, str, bytes]:
        result = self._redis.get(key)

        if fn is None:
            return result
        return fn(result)
    
    def get_int(self, key: str) -> int:
        return int(self._redis.get(key))
    
    def get_str(self, key: str) -> str:
        return str(self._redis.get(key))

    