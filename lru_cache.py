from typing import Counter


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.counter = 0
        self.lru = dict()
        self.cache = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        item = self.cache[key]
        self.counter = (self.counter + 1) % self.capacity
        self.lru[self.counter] = item
        return item

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        #if len(self.cache) == self.capacity:
            #self.lru.pop(self.counter)
        if self.cache[key] is None:
            self.lru.pop(self.cache[key][1])
        self.counter += 1
        self.cache[key] = (value, self.counter)
        self.lru[self.counter] = key


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(3)
