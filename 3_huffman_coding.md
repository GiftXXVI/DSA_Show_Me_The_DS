# Huffman Coding

## Key Decisions

This implementation uses the following key data structures:

1. Heap for Huffman Code: the heap made it easy to implement a priority queue data structure that popped out the item with the lowest frequency.

2. Linked List for Huffman Tree: Node class made it easy to encapsulate all of the required information such as the character, its frequency, the nodes bit (0 or 1) and its left and right children.

Another key decision was to do a single traversal to convert the Huffman code into a dictionary of codes during the encoding process instead of traversing the Huffman tree once for each character.

## Complexity

### Space Complexity

This implementation create a list of frequencies (of size n, where n is the input string size), a Heap (of size n+2, where n is input string size), a Huffman Tree (of size 2n+1, wih n input nodes and n+1 intermediate nodes) and a list of size 2n+1 (made up of elements of the Huffman Tree) for decoding. In conclusion, the space complexity of the algorithm is O(n) because the space used is a multiple of the input size.

### Time Complexity

#### Encode function

The process of building a Huffman Tree from the input string and generating its binary code in this implementation contains O(n), O(1) and O(n*d). Of these algebraic terms; n*d < n^2 and is the fastest growing term as input size increases. For a full binary tree, d can be n/2. Therefore, estimating n*d or n*n/2 to n^2, the function has a complexity of O(n^2).

#### Decode function

The time complexity of this function is O(n) where n is the length of the input binary string. (The operation of advancing the node pointer in the Huffman Tree is an O(1) operation.)
