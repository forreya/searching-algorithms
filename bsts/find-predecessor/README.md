<h1 align="center">Finding Predecessor in a Binary Search Tree (BST)</h1>

## Overview
The predecessor of a node in a Binary Search Tree (BST) is defined as the largest node that is smaller than the node at hand.

## Performance
- **Time Complexity**: O(h), where h is the height of the tree.
- **Space Complexity**: O(1), as no additional space (beyond a few pointers) is used.

### Key Cases
- **If Target Node Has A Left Child**:
	- The predecessor is the largest node in the left subtree.
	- This can be found by traversing to the rightmost node of the left child.
- **If Target Node Has No Left Child**:
	- The predecessor is the nearest ancestor where the target node is in the ancestor’s right subtree.
	- This ancestor is tracked during traversal, and its value is returned