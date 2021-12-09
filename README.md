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
## LRU Cache

## File Recursion

If 
- n represents the current level(depth) of iteration and
- $d_n$ represents the number of directories at level n and
- $f_n$ represents the number of files at level n

then
```markdown
x = $\sum_{n=1}^{l}(d_n + f_n)$
```

- represents the number of iterations taken to visit all files and directories at all levels and
- O(x) represents the complexity of the recursive algorithm that returns when it visits every leaf node on the directory tree.
