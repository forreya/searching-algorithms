<h1 align="center">Preorder Traversal for BSTs</h1>

## Performance
- **Time Complexity**: O(n), where n is the number of nodes in the tree, as each node is visited once.
- **Space Complexity**: O(h) due to the recursive call stack, which is O(logn) in a balanced BST and degrades to O(n) in a linear-shaped BST.

Note: Any space taken by a list that stores the order of traversal values is typically not included in the space complexity analysis as it would be considered part of the function's output rather than auxiliary space required by the traversal process itself.

## Logic Flow
Nodes are visited in the following order:
1. Root Node - Start at the root and process it (e.g., store the value in a list or perform a specific operation on it).
2. Left Subtree - Recursively perform the same operations on the left sub-tree.
3. Right Subtree - Recursively perform the same operations on the right sub-tree.

## Use Cases
- **Tree Cloning:** Preorder traversal is often used to copy a tree because it allows creating the parent node before its children.
- **File Structure Navigation:** Preorder traversal can represent the order in which directories & files are encountered in a file system, where each directory is processed before its contents.

## Advantages of Recursive Approach
- Shorter and more intuitive, as it directly reflects the natural order of preorder traversal in the code.
- Does not require explicit stack management, unlike the iterative approach.

## Disadvantages of Recursive Approach
- Uses the system call stack, which can cause stack overflow in very deep or highly unbalanced trees.
- Once recursion begins, adding complex logic for early stopping, skipping nodes, or adjusting traversal logic dynamically is harder than in the iterative approach.

## Notes on the Iterative Approach
- An explicit stack (a list) is used to simulate the recursive call stack, which helps prevents stack overflow.
- The right child is pushed onto the stack before the left child so that the left subtree is processed first, which preserves the correct preorder sequence (root, left, right).

## Advantages of Iterative Approach
- By avoiding the usage of the system call stack, the iterative approach can handle deeper trees without risking stack overflow, as the function manages depth through an explicit list (stack).
- The iterative approach provides finer control over the traversal process, making it easier to add conditions for early stopping, skipping specific nodes, or modifying traversal logic as needed.

## Disadvantages of Iterative Approach
- The explicit stack and order management make the code more complex than the recursive approach.
- Requires pushing the right child before the left child to maintain the correct order, which isn't as intuitive compared to the recursive approach.