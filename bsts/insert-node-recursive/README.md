<h1 align="center">BST Node Insertion (Recursive)</h1>

## Performance
- **Time Complexity**: O(logn) in a balanced BST, but can degrade to O(n) if the tree is unbalanced and resembles a linked list.
- **Space Complexity**: O(h). Each recursive call adds a frame to the call stack, so the space complexity is proportional to the height. This is O(logn) for balanced trees, but O(n) in the worst case.

## Recursion Logic
1. **Implicit Handling of Empty Trees**
	- The base case (`if not root`) handles both reaching the end of a branch and inserting a new root if the tree is initially empty. If root is `None`, the function creates and returns a new TreeNode, either as the root or as a child node.
2. **Returning `root` & Backtracking**
	- When a new node is added at a leaf position, each level of recursion returns root back up the call stack, maintaining all parent-child relationships while including the newly inserted node.

## Advantages
- **Concise Implementation:** The recursive approach provides a much cleaner and elegant solution for node insertion compared to the iterative approach.

## Disadvantages
- **Risk of Stack Overflow:** In unbalanced trees, the recursion depth can reach O(n), risking a stack overflow if the tree is very deep.
- **Space Usage:** Recursive methods use stack space proportional to the height of the tree. In scenarios where space is a concern, an iterative approach may be preferable as it maintains O(1) space complexity.

## Notes
- This function assumes that duplicates are not allowed, as duplicate insertion returns without modifying the tree.

## Terminology:
- **Stack Overflow:** When the program exhausts the available memory allocated for the call stack (which is for managing the state of function calls). In many programming languages with strict memory management like C++ and Python, the stack overflow triggers an error or exception.