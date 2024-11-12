<h1 align="center">Finding the Minimum Node in a BST</h1>

## Performance
- **Time Complexity**: O(logn) in a balanced BST, but can degrade to O(n) if the tree is unbalanced and resembles a linked list.
- **Space Complexity**: O(1), as it uses a simple iterative approach without extra memory usage.

## Use Cases
- **Successor Calculations:** Algorithms that find the in-order successor (the next-highest node) such as BST node deletion, often use the minimum node in the right subtree. Specifically, when deleting a node with two children, the minimum node in the right subtree can replace the deleted node to maintain the BST’s ordered structure.