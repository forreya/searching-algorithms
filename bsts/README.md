<h1 align="center">Binary Search Trees (BST)</h1>

## Overview
A Binary Search Tree (BST) is a tree data structure with the following properties:

1. Each node has a maximum of two children (left and right).
2. For each node:
	- The left subtree contains only values less than the node’s value.
	- The right subtree contains only values greater than the node’s value.
	- This arrangement enables efficient searching, insertion, and deletion.

BSTs are commonly used in applications that require dynamic data storage with frequent searches, insertions, or deletions, such as databases and file systems.

## Performance
- Time Complexity (Balanced):
	- Search: O(logn)
	- Insert: O(logn)
	- Delete: O(logn)
- Time Complexity (Unbalanced):
	- Search: O(n)
	- Insert: O(n)
	- Delete: O(n)

## Advantages
1. BSTs can expand and shrink naturally as elements are inserted or deleted, unlike arrays, which often have fixed sizes or require costly resizing operations.
2. The addition and deletion of elements in a BST only requires local restructuring, unlike the shifting required in arrays.
3. Elements are by default stored in a sorted order, allowing efficient binary search without needing a pre-sorted array.

## Disadvantages
1. An unbalanced BST can degrade to linear search times for many operations.
2. Each node requires memory for pointers to its left and right children, making BSTs more memory-intensive than arrays.
3. Nodes do not have a defined position or index. Each node is organized by value rather than by a sequential position. Thus, accessing a particular node requires traversal, making random access inefficient compared to arrays.

## Types of BSTs
1. **Unbalanced BST:** A standard BST with no mechanism to maintain balance. Inserting nodes in sorted order can lead to a skewed, linear structure.
2. **Self-Balancing BSTs:** Types of BSTs that automatically maintain their balance as nodes are inserted and deleted in order to prevent degradation:
	- **AVL Tree:** Ensures that the height difference between left and right subtrees of any node is at most 1.
	- **Red-Black Tree:** Uses color properties and specific rules to balance the tree.

## Optimization Techniques
1. **Lazy Deletion:** In scenarios where deletions are frequent, marking nodes as "deleted" without actually removing them can make searches faster, especially in large trees. Full deletion can be done during rebalancing or periodically.

## Terminology
1. **Lazy Deletion:** A deletion technique where nodes are marked as “deleted” without being immediately removed from the tree. This approach can improve performance in scenarios with frequent deletions by deferring the actual tree restructuring until a convenient time, such as during a periodic cleanup operation.
	- **Marking:** The act of marking a node as "deleted" without removing it from the tree. Marked nodes are ignored during searches but can still affect tree height until they are removed in a later cleanup phase.
	- **Periodic Cleanup:** A process in which all nodes marked as "deleted" are fully removed from the tree. This cleanup may include rebalancing to restore the tree’s optimal structure, ensuring efficient future searches and operations.
1. Both of the following nodes are particularly useful during deletion, as they allow replacement of a deleted node while maintaining the tree’s order.
	- **In-Order Predecessor:** The largest node in the left subtree.
	- **In-Order Successor:** The smallest node in the right subtree.
