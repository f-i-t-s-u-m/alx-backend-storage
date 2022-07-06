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

    def store(self, data) -> str :
        """ store data to redis """
        id = str(uuid4())
        self._redis.set(id, data)
        return id

