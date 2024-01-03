#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move the key to the end (most recently used)
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = list(self.cache_data.keys())[-1]
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            if key in self.cache_data:
                # Move the key to the end (most recently used)
                del self.cache_data[key]
                self.cache_data[key] = key
                return self.cache_data[key]
        return None
