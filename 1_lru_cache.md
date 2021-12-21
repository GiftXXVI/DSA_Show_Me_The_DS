# LRU Cache

This implementation uses a dictionary (dict) as the cache and and ordered dictionary (OrderedDict) as the LRU tracker. 

Dictionaries were chosen for this implementation because they are able to insert, retireve and delete items in O(1) time complexity.

## get

All operations have a time complexity of O(1), thus the function as a whole has a time complexity of O(1).

Details are in the README.md

## set

All operations either access dictionary items using a key or increment an integer and have a time complexity of O(1).

Details are in the README.md