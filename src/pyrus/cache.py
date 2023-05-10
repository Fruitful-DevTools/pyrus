from . import *


class Cache:
    def __init__(self, maxsize=100):
        """
        Initialize Cache class with a maximum cache size.

        ARGS:
            maxsize (int): The maximum size of the cache. 
            Default is 100.

        RETURNS:
            None
        """
        self.maxsize = maxsize
        self.cache = OrderedDict()

    def get(self, key):
        """
        Retrieve a value from the cache for a given key.

        ARGS:
            key (hashable): The key to retrieve the value for.

        RETURNS:
            The value for the given key, 
            if it exists in the cache and has not expired. 
            None otherwise.
        """
        if key in self.cache:
            value, expiration_time = self.cache[key]

            if expiration_time is None or expiration_time > time.time():
                return value
            else:
                del self.cache[key]

    def set(self, key, value, ttl=None):
        """
        Set a value in the cache for a given key.

        ARGS:
            key (hashable): The key to set the value for.
            value (object): The value to set for the given key.
            ttl (int or None): The time-to-live (in seconds) 
            for the cached value. 
            If None, the value will not expire.

        RETURNS:
            None
        """
        if len(self.cache) >= self.maxsize:
            self.cache.popitem(last=False)
        if ttl is not None:
            self.cache[key] = (value, time.time() + ttl)
        else:
            self.cache[key] = value

    def delete(self, key):
        """
        Remove a key-value pair from the cache.

        ARGS:
            key (hashable): The key to remove.

        RETURNS:
            None
        """
        if key in self.cache:
            del self.cache[key]
