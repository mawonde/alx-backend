#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Increment the frequency of the key
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used item(s)
                lfu_keys = [
                    k
                    for k, v in self.frequency.items()
                    if v == min(self.frequency.values())
                ]

                if len(lfu_keys) > 1:
                    # If more than one item, use LRU to discard the least recently used
                    lru_key = min(self.cache_data, key=self.cache_data.get)
                    lfu_keys.remove(lru_key)
                else:
                    lru_key = lfu_keys[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            if key in self.cache_data:
                # Increment the frequency of the key
                self.frequency[key] += 1
                return self.cache_data[key]
        return None

