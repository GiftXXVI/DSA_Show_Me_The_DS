from datetime import datetime, now

class Queue(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self,node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.prev
            self.head.next = None
            return node

class Node(object):
    def __init__(self, value, key) -> None:
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hash_map = dict()
        self.lru = Queue()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.hash_map[key] is not None:
            stamp = now.strftime("%m%d%Y%H%M%S%f")
            self.set_lru(key,stamp)
            self.hash_map[key][1] = stamp
            return self.hash_map[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.hash_map)==self.capacity:
            node = self.get_lru()
            if node.key in self.hash_map.keys:
                self.hash_map.pop(self.get_lru())
        stamp = now.strftime("%m%d%Y%H%M%S%f")
        self.set_lru(key,stamp)
        self.hash_map[key] = [value,stamp]    
    
    def get_lru(self):
        node = self.lru.dequeue()
        return node

    def set_lru(self, key, stamp):        
        event = Node(stamp, key)
        self.lru.enqueue(event)

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
