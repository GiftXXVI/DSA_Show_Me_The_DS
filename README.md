# Data Structures and Algorithms Project 2: Show me the Data Structures

The test files can be downloaded and unzipped using the following commands:

```bash
curl https://s3.amazonaws.com/udacity-dsand/testdir.zip --output testdir.zip
```
```bash
sudo apt install unzip
```
```bash
unzip testdir.zip
```
## 1. LRU Cache

The implementation uses the following variables:
- an `OrderedDict` to track the least recently used item named `lru`
- a `dict` to track the cache named `cache`
- a timing variable named `counter`, to be used as an index/has key to the `lru`
- a value representing the capacity named `capacity`

### `set`
`set` involves the following operations:
1. Check if the size of the cache matches the `capacity`. If this is the case:
    - pop the least recently used item from the `lru` hash table. This is simply the first item inserted into the table that is still in the table at this moment. An `OderedDict` improves on the `dict` by keeping track of the order of insertion into the hash table, thereby enabling Deletion of the first item inserted in O(1) time.
    - pop the least recently used item from the `cache` using the key returned by the operation in the preceding step
2. Check if the key being inserted/modified already exists in the `lru`. If it already exists, pop it from the `lru` hash table (to maitain the property that the order of insertion reflects the order of recent usage)
3. Update the `cache` and the `lru` table as follows (all O(1) operations)
    - Increment the `counter`
    - Write the new value to the `cache` using the provided key as hash key
    - Create a new `lru` using the `counter` as the hash key

### `get`
`get` involves the following operations:
1. Check if the key is not in the cache, this involves looking for a key in a hash table, thus it is an O(1) operation. If the key is not present, return `-1`
2. Retrieve the value associated with the key from the cache, this also involves looking for a key in a hash table, and is an O(1) operation.
3. Update the `lru` table as follows (all O(1) operations)
    - Increment the `counter`
    - Delete the previous `lru` entry by using the key, 
    - Create a new `lru` using the `counter` as the key
4. Return the value retrieved in step (2) above. This is also an O(1) operation that returns the first index of a `tuple`


## 2. File Recursion

The implementation uses recursion to visit all nodes at all levels of the directory tree.

If 
- n represents the current level(depth) of the directory tree and
- $d_n$ represents the number of directories at level n and
- $f_n$ represents the number of files at level n

then

[//]: # "$x = \sum_{n=1}^{l}(d_n + f_n)$"

![](https://latex.codecogs.com/svg.latex?x%20%3D%20%5Csum_%7Bn%3D1%7D%5E%7Bl%7D%28d_n%20%2B%20f_n%29)

- represents the number of iterations taken to visit all files and directories at all levels and
- $O(x)$ represents the complexity of the recursive algorithm that returns when it visits every leaf node on the directory tree.

## 3. Huffman Coding
There are 2 algorithms, the first algorithm builds the Huffman tree and uses it to encode the message. The second algorithm uses the Huffman tree to decode the coded message back into its original form.

### 1. Encode
#### prepare_string()
The encode function starts by calling a prepare_string() function. This function tabulates the frequency of each unique character as it loops through the input string and stores the frequency in a dictionary with the character as the key.

This loop is an O(n) operation because it cycles through all characters in the string and searches for each character in the dictionary to record or increment its frequency.(Checking the dictionary for a key is an O(1) operation.)

The final section of the function consists of a zip function that takes the dictionary's keys list and its values list as inputs. Generating these 2 lists is an O(n) operation. The zip function depends on the size and number of list inputs, thus it is an O(n^2) operation. 

In summary, this function has a complexity of O(n^2 + n). With n^2 coming from the zip operation and n coming from the loop. Since O(n^2) is the largest term (and grows at the highest rate with increasing input size) in the expression, the prepare_string() function is an O(n^2) operation.
 
#### Initialize Heap
The next step is to create a heap. The heap is implemented as an array of size of the array returned by prepare_string() plus 2 additional indices.

The process of initializing the Heap includes loop that get each element of the array returned from prepare_string() function (this is an O(n) operation). 

After retrieval, the element is immediately inserted into the first available index of the Heap(which is also the bottom level of the tree). This is an O(1) operation.

The element is then moved to its proper position in the tree by the heapify function which compares its value with the value of its parent and swaps the 2 if the child has a lower value than the parent. The maximum number of comparisons possible is equal to the depth of the tree. Thus, this is an O(d) operation where d represents the depth of the leaf nodes of the Heap. 

Therefore, looping through the input list to add items to the heap is an O(n*d) operation for n items and d levels of the tree.

#### Create Huffman Tree

##### Create Intermediate Node

This task is split in 2 subtasks.
The first is to create the intermediate nodes of the Huffman tree. This process involves repeating the following steps:
 
1. extract the 2 smallest elements of the Heap. 
2. create a new node whose value is the sum of the values of the 2 removed nodes (set the left and right pointers of this node to the 2 extracted nodes, these pointers are used in the Huffman Tree later) and 
3. insert the new node into its correct place in the Heap. 

This loop runs n-2 times where n is the initial number of items in the heap (this can be approximated to O(n), a function of the initial input size). Each loop removes 2 items from the heap and inserts one. Each removal triggers a heapify function. Then finally, there is an insert operation which also triggers a heapify function call (which has already been shown to be an O(d) operation). 

In summary, the 3 heapify calls are O(3d). Taking the loop into consideration, this part of the function can be approximated to O(n*d) where n is the number of items in the heap and d is the number of levels of the heap.

##### Create the Root of the Huffmann Tree
This step takes advantage of the left and right pointers set in the previous step to complete the tree by creating a root node and setting the 2 remaining subtrees to be its left and right children.

The root element is created by extracting the last 2 elements of the Heap and initialising the tree with a new node (root) with the last 2 nodes on the Heap as its left and right nodes. This is an O(1) operation because it extracts the item at the first index of the Heap.

##### Create a dictionary of codes

The first step is to perform a preorder traversal of the Huffman Tree, usig recursion to take note of every bit on the path to a node and use this to create a dictionary of all characters mapped to their binary codes.

The traversal is an O(n) operation, since it visits all items in the Huffman Tree. On the other hand, inserting into a hash map/dictionary is an O(1) operation. Therefore this process is an O(n) process.

##### Encoding the Data
The final step is to encode the data. This process involves looping through each character in the input string, retrieving its binary code from the dictionary and appending the code to the output binary string. This is an O(n) process where n is the size of the input string.

##### Conclusion
The process of building a Huffman Tree from the input string and generating its binary code has been shown to have 2 O(n) steps, 1 O(1) step and 1 O(n*d) step. Of these algebraic terms; n*d < n^2 and is the fastest growing term as input size increases. For a full binary tree, d can be n/2. Therefore, estimating n*d or n*n/2 to n^2, the function has a complexity of O(n^2).

### 2. Decode
The decode function takes in the encoded binary string and the Huffman tree created during the encoding process as its inputs.

The rest of the function iterates through each bit of the binary string. If the current bit is a 0, the agorithm advances to the left child of the current node while if the current bit is 1, it advances to the right child. 

If it lands at a leaf node, it appends the character in the node and points back to the root to repeat the process and identify the next character.

This function is O(n) where n is the length of the input binary string. (The operation of advancing the node pointer in the Huffman Tree is an O(1) operation, therefore it is ingored in the analysis.)

## 4. Active Directory
Uses recursion to search for user inside a group and all its subgroups and recursively inside subgroups to the lowest level. 

The recursive function accepts a search term and a group in which to search. It extracts the list of users and sorts them in ascending alphabetical order. The sort function has a complexity of O(n log n).

Next, it uses a binary search to try and find the search term in the sorted users list. The binary search algorithm has a complextity of O(log n).

The final part recursively calls each of the subgroups until the search term is found in one of the subgroups. This also happens recursively and the number of calls depends on the depth of the nesting.

## 5. Blockchain
Creates a blockchain using a linked list.
The linked list is implemented as a class called Blockchain. It contains properties such as head and tail which track the head and tail nodes (Blocks) of the Blockchain.
The insert operation is an O(1) operation that sets the inserted node as head if the list is empty or sets the inserted node as tail if there are already items in the linked list.

Traversing the list requires looping through all Blocks by starting at the head and following the next pointers until the last element is reached. The time taken varies depending on the number of elements in the list. Thus this is an O(n) operation.

## 6. Union and Intersection
 
### Union 
The union function uses a single loop, which runs for as many iterations as the number of elements of the linked list with the most elements. It checks if the value of the current element of the either linked list is in the union dictionary and adds it if it is not found. Then it returns the keys array created from the dictionary.

The loop is an O(n) process where n is the size of the larger linked list and the extraction of the list of keys from the dictionary is an O(n) process. This means the complexity of the function is O(n). 

### Intersection
The intersection function uses 3 dictionries and 2 loops. 

The first loop navigates the 2 input linked lists using their next pointers and runs until the end of the longer linked list.

For each item in the first linked list, it adds the value of the item to the first dictionary (dict1). 

Similarly, each item in the second linked list is added to the second dictionary (dict2).

The second loop navigates through the 2 linked lists and adds the value of any node that is in both dict1 and dict2 to the intersection dictionary (interection).

Finally, just like the union function before, the keys list of the intersection dictionary is returned by the function.

Both loops are O(n) where n is the size of the large linked list. eating the keys list from the dictionary is also an O(n) operation. Terefore, the complexity of the function is O(n).

