# BlockChain

## Key Decisions

Creates a blockchain using a linked list.
A linked list is an intuitive olution for a dynamic data structure where each node is supposed to point to the next node.

## Complexity

Traversing the list requires looping through all Blocks by starting at the head and following the next pointers until the last element is reached. The time taken varies depending on the number of elements in the list. Thus traversal of the BlockChain has a time complexity of O(n).
