#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Move the key to the end (most recently used)
                self.order.remove(key)
                self.order.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Discard the least recently used item
                    lru_key = self.order.pop(0)
                    del self.cache_data[lru_key]
                    print("DISCARD: {}".format(lru_key))
                self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            if key in self.cache_data:
                # Move the key to the end (most recently used)
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
