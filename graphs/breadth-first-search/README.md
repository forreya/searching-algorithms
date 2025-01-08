<h1 align="center">Breadth-First Search (BFS) for Graphs</h1>

## Disclaimer
The explanations below assumes a graph representation of Adjancency Lists.

## Performance
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges. This is because eventhough you might ignore edges that connect to vertices that have already been processed, this process of ignoring is also part of the iteration process of each vertex's neighbours list.
- **Space Complexity**: O(V) for storing the visited set and the queue.

## Logic Flow
1. Initialize a queue with the source node, a set to track visited nodes, and a list to store the traversal order.
2. Popleft (deque) from the queue and mark that vertex as visited.
3. Add it to the result list.
4. Enqueue all unvisited neighbors (or neighbours that already are in the queue).

## Why Use Sets Instead of Lists for Tracking Visited Nodes?
Sets are significantly faster when it comes to determining if an element is present in the set, but its elements are not ordered so you cannot access items by index as you would in a list. One thing to note, is that it can only contain unique items.

## Use Cases
1. Shortest Path in Unweighted Graphs: BFS guarantees the shortest path (minimum edges) from the source to any reachable vertex.
2. Cycles in Undirected Graphs: BFS can detect cycles by checking if a node is visited twice during the traversal process. It works by using the following logic: if you encounter a vertex that has already been visited and is not the immediate parent of the current vertex, a cycle exists.
3. Level Order Traversal: BFS provides a level-by-level traversal in graph or tree-like structures such as company hierachies or file system traversal.

## Advantages
1. Simple to Implement: BFS is straightforward and uses intuitive data structures like queues.
2. Shortest Path Guarantee: For unweighted graphs, BFS guarantees the shortest path in terms of edge count.

## Disadvantages
1. Memory Usage: BFS requires a queue to store vertices, which can grow to the size of the graph's maximum degree- although this doesn't affect the asymptotic complexity.
2. Inefficiency with Large Graphs: BFS explores all neighbors, which can be computationally expensive for dense graphs with many edges.

## Notes
1. Iterative Nature: BFS is inherently iterative due to its reliance on a queue. Recursive implementations are rare and inefficient.
2. Weighted Graphs: BFS does not account for edge weights. For shortest paths in weighted graphs, algorithms like Dijkstra's or Bellman-Ford are needed.
3. Graph Representation: BFS is most efficient with adjacency lists, where neighbors of a vertex can be accessed in O(1) on average.