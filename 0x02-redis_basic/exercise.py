#!/usr/bin/env python3
""" python3 with redis db """


from redis import Redis
from uuid import uuid4


class Cache():
    """ cache class """
    _redis = Redis()

    def __init__(self):
        """ init the cache instance """
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """ store data to redis """
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn=None):
        """ get data """
        data = self._redis.get(key)
        if (fn is not None):
            if(isinstance(fn, (str, int))):
                return f'get_{fn}'(data)
            return fn(data)
        return data

    def get_str(self, data):
        """ convert to str """
        return data.decode('utf-8')

    def get_int(self, data):
        """ convert to int """
        return int(data)
