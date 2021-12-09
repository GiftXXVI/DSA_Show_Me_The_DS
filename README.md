# DSA_Show_Me_The_DS

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

If 
- n represents the current level(depth) of iteration and
- $d_n$ represents the number of directories at level n and
- $f_n$ represents the number of files at level n

then

[//]: # "$x = \sum_{n=1}^{l}(d_n + f_n)$"

![](https://latex.codecogs.com/svg.latex?x%20%3D%20%5Csum_%7Bn%3D1%7D%5E%7Bl%7D%28d_n%20%2B%20f_n%29)

- represents the number of iterations taken to visit all files and directories at all levels and
- $O(x)$ represents the complexity of the recursive algorithm that returns when it visits every leaf node on the directory tree.
