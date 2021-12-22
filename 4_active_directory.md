# Active Directory

## Key Decisions

Uses recursion to search for user inside a group and all its subgroups and recursively inside subgroups to the lowest level. Just like the File Recursion problem before, the dynamic hieararchical nature of the group membership structure makes recursion an intuitive solution for this problem.

## Complexity

If the depth of nesting is represented by d, and the n represents the number of items in each group, then the time complexity of the search function is:

O(d _ nlogn _ logn)

or

O(d\*n(logn)^2)
