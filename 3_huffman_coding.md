
# Huffman Coding

Heap for Huffman Code: the heap made it easy to implement a priority queue data structure that popped out the item with the lowest frequency.

Linked List for Huffman Tree: Node class made it easy to encapsulate all of the required information such as the character, its frequency, the nodes bit (0 or 1) and its left and right children.

Encoding does one traversal to convert the code into a dictionary of codes instead of traversing the Huffman tree once for each character.

## Encode function

The process of building a Huffman Tree from the input string and generating its binary code in this implementation has been shown to have 2 O(n) steps, 1 O(1) step and 1 O(n*d) step. Of these algebraic terms; n*d < n^2 and is the fastest growing term as input size increases. For a full binary tree, d can be n/2. Therefore, estimating n*d or n*n/2 to n^2, the function has a complexity of O(n^2).

## Decode function

The decode function for this implementation of a Huffman Tree has been shown to have a complexity of O(d*n(logn)^2).

more details are in the README.md