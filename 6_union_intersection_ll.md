# Union and Intersection

## Key Decisions

This implementation uses dictionaries instead of lists when adding and tracking items in the linked list because dictionaries enable fast lookups and thus make it easy to check if an item is already in the list while constructing the union or intersection.

## Complexity

### Space Complexity

The union function utilizes 1 additional data structure, a dictionary of size n (where n is the input size, with a possible maximum size as that of the sum of the 2 input arrays).

The intersection function utilizes 3 additional data structures. All 3 are dictionaries and 2 have a maximum possible size corresponding to the sizes of the input arrays. The third has a maximum possible size matching that of the smaller of the 2 input arrays (since an intersection has to contain only elements present in both input arrays). 

This means the algorithm has a space complexity of O(n) where n is the larger of the 2 input arrays (since the space requirement will be less than a multiple of the larger array size). 

### Time Complexity

## Union

The loop has a time complexity of O(n) where n is the size of the larger linked list. The extraction of the list of keys from the dictionary has a time complexity of O(n). This means the complexity of the function is O(n).

## Intersection

Both loops are O(n) where n is the size of the large linked list. eating the keys list from the dictionary is also an O(n) operation. Terefore, the complexity of the function is O(n).
