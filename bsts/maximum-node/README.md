<h1 align="center">Finding the Maximum Node in a BST</h1>

## Performance
- **Time Complexity**: O(logn) in a balanced BST, but can degrade to O(n) if the tree is unbalanced and resembles a linked list.
- **Space Complexity**: O(1), as it uses a simple iterative approach without extra memory usage.

## Use Cases
- **Predecessor Calculations:** Algorithms that find the in-order predecessor (the next-lowest node) such as BST node deletion, often use the maximum node in the left subtree. Specifically, when deleting a node with two children, the maximum node in the left subtree can replace the deleted node to maintain the BST’s ordered structure.