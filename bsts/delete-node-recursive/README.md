<h1 align="center">BST Node Deletion (Recursive)</h1>

## Performance
- **Time Complexity**: O(h), where h is the height of the tree. For balanced trees, this is O(logn), but in the worst case (skewed tree), it can be O(n).
- **Space Complexity**: O(h). The recursive call stack depth is proportional to the height of the tree. For balanced trees, this is O(logn), while for skewed trees, it can be O(n).

## How It Works
Node deletion requires handling three different scenarios:

1. **Deleting a Node with No Children (Leaf Node)**:
	- Simply remove the node by returning `None` to replace the deleted node's place with emptiness.
2. **Deleting a Node with One Child**:
	- Return the non-null child to take the deleted node's place.
3. **Deleting a Node with Two Children**:
	- Replace the node’s value with that of its inorder successor (the smallest node in the right subtree).
	- Remove the inorder successor from its original position by calling the `delete_node_recursive` function on `root.right`.
	```python
	if root.left and root.right:
		successor = find_min(root.right)  # Find the smallest node in the right subtree of the node to be deleted
		root.value = successor.value  # Copy the successor's value to the current node
		root.right = delete_node_recursive(root.right, successor.value) # Remove the successor node from its original position
	```

## Advantages
1. Provides a clear and elegant approach by using recursion.
2. Has logarithmic performance for balanced trees.

## Disadvantages
1. Recursion depth can become O(n), risking stack overflow for very deep trees. Self-balancing trees like AVL or Red-Black trees help mitigate this.
2. Handling the inorder successor logic requires careful implementation as it can be tricky.

## Terminology
- **Skewed Tree**: A tree that behaves like a linked list, where each node has only one child.