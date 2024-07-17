#!/usr/bin/env python3
'''creating a cache with redis database'''
import redis
from typing import Union
import uuid

class Cache:
    '''cache class'''

    def __init__(self):
        '''initialize class attribute'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, str, bytes]) -> str:
        '''stores in redis database'''
        random_num = str(uuid.uuid4())
        self._redis.set(random_num, data)
        return random_num