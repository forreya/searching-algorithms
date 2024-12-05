<h1 align="center">Finding Successor in a Binary Search Tree (BST)</h1>

## Overview
The successor of a node in a Binary Search Tree (BST) is defined as the smallest node that is larger than the node at hand.

## Performance
- **Time Complexity**: O(h), where h is the height of the tree.
- **Space Complexity**: O(1), as no additional space (beyond a few pointers) is used.

### Key Cases
- **If Target Node Has A Right Child**:
	- The successor is the smallest node in the right subtree.
	- This is found by traversing to the leftmost node of the right child.
- **If Target Node Has No Right Child**:
	- The successor is the nearest ancestor where the target node is in the ancestor's left subtree.
	- This ancestor is tracked during the traversal, and its value is returned.