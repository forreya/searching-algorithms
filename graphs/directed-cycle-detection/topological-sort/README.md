<h1 align="center">Topological Sort For DAGs</h1>

## What Is Topological Sort?
Topological sorting is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u→v, vertex u comes before v in the ordering. If the graph contains a cycle, topological sorting is not possible. This means topological sort can be exploited to detect cycles in a directed graph.

## Why Topological Sort Fails for Undirected Graphs
In an undirected graph, edges have no direction, so the lack of direction makes the concept of “ordering” meaningless. Without direction:
1. No Precedence Constraint: There’s no way to determine which node should come first in a topological order.
2. Cycles Are Ambiguous: In directed graphs, a back edge indicates a cycle. In undirected graphs, every edge can technically form a "cycle" unless additional rules are applied.

## Performance
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges. Each vertex and edge is processed at most once as the global visited set prevents duplicate edge processing.
- **Space Complexity**: O(V) for storing the recursion stack, current path visited set, and global visited set.

## Summary
Essentially we are doing the following:
1. Looping through all the vertices in the graph.
	- For each vertex, we run recursive DFS on it until all paths starting from it has been fully traversed and checked for cycles (using a current path set)
2. We then continue that process for the next vertex in line, and then the next.
	- If any of these subsequent vertices have already been fully traversed from the recursive traversal of a previous vertex, it will be skipped, ensuring efficiency.