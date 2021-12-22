# Union and Intersection

This implementation uses dictionaries instead of lists when adding and tracking items in the linked list because dictionaries enable fast lookups and thus make it easy to check if an item is already in the list while constructing the union or intersection.

## Union

The loop has a time complexity of O(n) where n is the size of the larger linked list.  The extraction of the list of keys from the dictionary has a time complexity of O(n). This means the complexity of the function is O(n). 

## Intersection

Both loops are O(n) where n is the size of the large linked list. eating the keys list from the dictionary is also an O(n) operation. Terefore, the complexity of the function is O(n).