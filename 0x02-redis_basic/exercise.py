#!/usr/bin/env python3
""" python3 with redis db """


from redis import Redis
from uuid import uuid4
from functools import wraps
from typing import Callable, List, Union, Optional


def count_calls(method: Callable) -> Callable:
    """ decorator for method """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper for the decorator """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ history decorator """
    @wraps(method)
    def inner(self, *args: Union[str, bytes, int, List]) -> Callable:
        """ inner function to hold external function """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        data = method(self, *args)
        self._redis.lpush(f'{method.__qualname__}:outputs', str(data))
        return data
    return inner


class Cache():
    """ cache class """

    def __init__(self):
        """ init the cache instance """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, List]) -> str:
        """ store data to redis """
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """ get data """
        data = self._redis.get(key)
        if (fn is not None):
            if(isinstance(fn, (str, int))):
                return eval(f'get_{fn.__name__}({data})')
            return fn(data)
        return data

    @count_calls
    def get_str(self, data: bytes) -> str:
        """ convert to str """
        return data.decode('utf-8')

    @count_calls
    def get_int(self, data: bytes) -> int:
        """ convert to int """
        return int(data)
