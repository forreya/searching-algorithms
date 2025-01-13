<h1 align="center">Depth-First Search (DFS) for Cycle Detection in Undirected Graphs</h1>

## Performance
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges. Each vertex is visited once, and all edges are processed at most once when traversing the neighbours of each vertex.
- **Space Complexity**: O(V), for storing the visited set. In the worst case, the recursion stack can grow to O(V) if the graph has a depth resembling a linked list.

## Logic Flow w/ Recursion
1. Start DFS from any unvisited vertex in the graph.
2. Use a visited set to track nodes that have been processed.
3. For each neighbor of the current node: If the neighbor has already been visited and is not the immediate parent of the current node, a cycle is detected. If the neighbor has not been visited, recursively call DFS on the neighbor while passing in the current node as its parent.
6. Return True if a cycle is detected, otherwise continue exploring all nodes until the top-level recursion frame finishes- at which point we return False.

## Why Do We Need A "Parent" Reference?
In undirected graphs, every edge connects two nodes in both directions. Without a "parent" reference, DFS cannot distinguish between a valid backtracking edge, which is when the traversal revisits the node it came from (its parent), and a cycle.

## Which Graph Representation Is DFS Best Suited For?
DFS for cycle detection is most efficient with adjacency lists, as it allows for O(1) average-time neighbor access.

## Terminology
- **Backtracking Edge:** A backtracking edge in an undirected graph is an edge that connects the current node back to its parent during traversal. This type of edge is not considered a cycle.