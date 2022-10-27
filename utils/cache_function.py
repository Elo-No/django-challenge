from django.core.cache import cache
from django_redis import get_redis_connection


def get_all_key():
    conn = get_redis_connection()
    data = conn.keys
    return list(map(lambda x: int(x.decode()), data))


# This function increase value by one
def incrKey(key, value, timeout=None):
    return cache.incr(key, delta=value)


# This function set value
def setKey(key, value, timeout=None):
    return cache.set(key, value, timeout=timeout)


# This function set value if key exist then give error
def addKey(key, value, timeout=None):
    return cache.add(key, value, timeout=timeout)


# this function get value by key
def getKey(key):
    return cache.get(key)

# This function ...


def ttlKey(key):
    return cache.ttl(key)


# this function delete value by key
def deleteKey(key):
    return cache.delete(key)


# this function delete value by pattern
def getAllKey(pattern):
    return cache.keys(pattern)
