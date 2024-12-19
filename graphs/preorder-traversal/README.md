<h1 align="center">Preorder Traversal for Graphs</h1>

## Performance
- **Time Complexity**: O(V+E), where V is the number of vertices and E is the number of edges. Each vertex is visited once, and marking a vertex as visited or adding it to a result list is a constant-time operation. Every edge is iterated over once when traversing the internal list of a vertex.
- **Space Complexity**: O(V), for storing the visited set. In the worst case, additional space can grow to O(V) also for the explicit stack in the iterative approach or recursion stack in the recursive approach if the graph resembles a linked list.

## When To Add To Visited Set In The Iterative Approach?
Mark neighbors as visited as soon as you push them onto the stack, not when processing them. This avoids duplicate visits due to multiple paths leading to the same vertex in the window of time before that neighbor gets processed.

## Use Cases
Preorder traversal is useful in scenarios where you need to process a node before its neighbors.
1. Solving problems like maze exploration where nodes need to be processed as they are reached.
2. Tracking already-visited nodes to identify cycles.

## Note On Edge Cases
If the graph is disconnected, you must iterate over all vertices to ensure full traversal.

## Advantages
1. Easy to implement with both recursive and iterative approaches. Particularly on the reccursive approach, preorder aligns well due to its "visit, then recurse" logic flow.

## Disadvantages
1. Inefficiency with dense graphs as high connectivity means traversing all edges can be computationally expensive.
2. Recursive approaches may cause stack overflow for large graphs, and the iterative approach requires explicit stack management.