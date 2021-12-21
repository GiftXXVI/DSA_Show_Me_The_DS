from collections import OrderedDict
import unittest


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.counter = 0
        self.lru = OrderedDict()
        self.cache = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        item = self.cache[key]  # O(1)-Time
        self.counter += 1
        del self.lru[self.cache[key][1]]  # O(1)-Time
        self.lru[self.counter] = item  # O(1)-Time
        self.cache[key] = (self.cache[key][0], self.counter)
        return item[0]

    def set(self, key, value):
        try:
            if value is not None:
                value = int(value)
                # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
                if key not in self.cache and len(self.cache) == self.capacity:
                    i, v = self.lru.popitem(last=False)  # O(1)-Time
                    self.cache.pop(v)  # O(1)-Time
                if key in self.cache:
                    del self.lru[self.cache[key][1]]  # O(1)-Time
                self.counter += 1
                self.cache[key] = (value, self.counter)  # O(1)-Time
                self.lru[self.counter] = key  # O(1)-Time
            else:
                raise ValueError
        except ValueError:
            print('Invalid input, expeected an integer!')


class Tests(unittest.TestCase):
    def setUp(self):
        self.cache = LRU_Cache(5)

    def test_lru(self):
        self.cache.set(1, 1)
        self.cache.set(2, 2)
        self.cache.set(3, 3)
        self.cache.set(4, 4)
        self.assertEqual(self.cache.get(1), 1)
        self.assertEqual(self.cache.get(2), 2)
        self.assertEqual(self.cache.get(9), -1)
        self.cache.set(5, 5)
        self.cache.set(6, 6)
        self.assertEqual(self.cache.get(3), -1)

    def test_null(self):
        self.cache.set(None, None)
        self.assertEqual(self.cache.get(None), -1)

    def test_large(self):
        self.cache.set(100000000000000, 100000000000000)
        self.assertEqual(self.cache.get(100000000000000), 100000000000000)


if __name__ == "__main__":
    unittest.main()
