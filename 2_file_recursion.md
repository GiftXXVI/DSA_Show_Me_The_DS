# File Recursion
This implementation uses recursion to visit all nodes at all levels of the directory tree. Recursion was chosen because it is an intuitive algorithm for any scenario where an algorithm needs to explore a hierarchy of items with an unknown number of levels and uknown number of items per level. 

If 
- n represents the current level(depth) of the directory tree and
- $d_n$ represents the number of directories at level n and
- $f_n$ represents the number of files at level n

then

$x = \sum_{n=1}^{l}(d_n + f_n)$ 

or (the same equation as an image):

![](https://latex.codecogs.com/svg.latex?x%20%3D%20%5Csum_%7Bn%3D1%7D%5E%7Bl%7D%28d_n%20%2B%20f_n%29)

- represents the number of iterations taken to visit all files and directories at all levels and
- $O(x)$ represents the complexity of the recursive algorithm that visits every leaf node on the directory tree.

