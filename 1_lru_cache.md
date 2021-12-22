# LRU Cache

## Key Decisions

This implementation uses a dictionary (dict) as the cache and and ordered dictionary (OrderedDict) as the LRU tracker.

Dictionaries were chosen for this implementation because they are able to insert, retireve and delete items in O(1) time complexity.

## Complexity

### get

All operations (inserts, lookups and deletes) have a time complexity of O(1). Thus the function as a whole has a time complexity of O(1).

### set

All operations (inserts, lookups and deletes) have a time complexity of O(1). Consequently, the function as a whole has a time comlpexity of O(1).
