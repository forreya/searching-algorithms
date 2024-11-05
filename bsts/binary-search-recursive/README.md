<h1 align="center">BST Binary Search (Recursive)</h1>

## Performance
- **Time Complexity**: O(logn) in a balanced BST, but can degrade to O(n) if the tree is unbalanced and resembles a linked list.
- **Space Complexity**: O(h), where h is the height of the tree. This space is required for the call stack during recursion, resulting in O(logn) for a balanced BST and up to O(n) for an unbalanced BST.

## Advantages
1. Binary search is very fast for large trees due to its logarithmic time complexity (assuming a balanced BST).
2. The recursive approach to binary search in BSTs can be more intuitive for some people.

## Disadvantages
1. Each recursive call adds to the call stack, so for large, unbalanced trees, recursion can lead to significant space usage and even stack overflow in extreme cases.
2. A BST can degrade to a linked-list structure in the worst case, making time complexity O(n).

## Terminology
- **Call Stack** - Part of system memory that keeps track of function calls during execution. In recursive binary search, each recursive call adds a frame to the call stack, which stores the function’s local variables and state. If the recursion depth is too great (e.g., in an unbalanced tree), it can lead to stack overflow.