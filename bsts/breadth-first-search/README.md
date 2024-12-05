<h1 align="center">Breadth-First Search (BFS) for BSTs</h1>

## Performance
- **Time Complexity**: O(n), where n is the number of nodes in the tree. Each node is visited exactly once.
- **Space Complexity**: O(w), where w is the maximum width of the tree. The maximum number of nodes that can be stored in the queue corresponds to the maximum number of nodes at any level of the tree, which is the width of the tree. In a balanced tree, the space complexity would be O(n/2)- which represents the width of the final level of the tree.

## Algorithm
1. Initialize an empty queue and add the root node.
2. While the queue is not empty:
   - Dequeue a node and process it (e.g., append its value to a result list).
   - Enqueue the node's left and right children (if they exist).
3. This logic flow results in a level-by-level traversal as upper levels are dequeued first- from left to right.

## Use Cases
- **Shortest Path in Unweighted Trees**: BFS can help find the shortest path from the root to any node.
- **Level-By-Level Analysis**: BFS is useful for analyzing or displaying a tree level-by-level, such as in company hierarchies.

## Disadvantages
1. Requires additional memory for the queue, with space complexity proportional to the maximum number of nodes at any level.
2. Not recursive, which means the code is less concise compared to depth-first traversal methods.

## Why is the width n/2 for a balanced tree?
In a completely balanced binary tree with n nodes:

1. The last level contains about n/2 nodes.
2. The second-to-last level contains n/4 nodes.
3. The third-to-last level contains n/8 nodes, and so on.

This pattern arises because in a balanced binary tree each level has twice as many nodes as the previous level.

## Notes
- BFS is inherently iterative because it relies on a queue. While recursion is common for depth-first traversal, BFS cannot be implemented recursively without additional data structures to simulate the queue.
- BFS doesn't rely on this ordering property of BSTs. It only cares about the structure of the tree (nodes and their children).

## Terminology
- **Enqueue**: This is the action of adding an element to the **end of the queue**.
- **Dequeue**: This is the action of removing an element from the **front of the queue**.