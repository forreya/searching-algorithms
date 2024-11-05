<h1 align="center">BST Binary Search (Iterative)</h1>

## Performance
- **Time Complexity**: O(logn) in a balanced BST, but can degrade to O(n) if the tree is unbalanced and resembles a linked list.
- **Space Complexity**: O(1) since the iterative approach does not require extra stack space, unlike the recursive method.

## How It Works
1. Start from the root of the tree.
2. Compare the target value with the current node's value.
3. If the target matches the node’s value, the search is successful.
4. If the target is less than the node’s value, move to the left subtree.
5. If the target is greater than the node’s value, move to the right subtree.
6. Repeat until you find the target value or a `None` value.

## Optimization Techniques
1. **Balancing the Tree:** Using a self-balancing tree structure (like AVL trees or Red-Black trees) prevent the BST from becoming skewed or unbalanced, ensuring the height remains approximately O(logn).

## Advantages
1. Binary search is very fast for large trees due to its logarithmic time complexity (assuming a balanced BST).
2. Iterative binary search on a BST keeps space usage at a constant O(1).

## Disadvantages
1. A BST can degrade to a linked-list structure in the worst case, making time complexity O(n).

## Important Notes
1. Binary search is most efficient in a balanced BST, where nodes are evenly distributed.