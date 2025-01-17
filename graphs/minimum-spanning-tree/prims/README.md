<h1 align="center">Prim's Algorithm for Minimum Spanning Tree (MST)</h1>

Prim's algorithm is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a connected, weighted graph.

## Scenarios
1. Cyclic Graphs - If the graph contains cycles, Prim's algorithm automatically avoids them by tracking visited vertices and only pushing edges to the priority queue that connect to unvisited vertices. This ensures that the resulting MST is acyclic.
2. Disconnected Graphs - Prim's algorithm will only compute the MST for the connected component containing the starting vertex if a graph isn't connected and so you would need to compute an MST for each connected component (Minimum Spanning Forest).
3. Unweighted Graphs - Prim's algorithm is specifically designed for weighted graphs. Without weights, the notion of a "minimum" spanning tree becomes meaningless. If the graph is unweighted, other algorithms like Breadth-First Search (BFS) can be used to create a spanning tree (not an MST).
4. Directed Graphs- In a directed graph, the concept of "spanning" all vertices is ambiguous because directionality creates asymmetry in reachability.
5. Negative Weight Graphs - Prim's algorithm works with graphs that have negative edge weights. Since it greedily selects the smallest edge connecting a visited vertex to an unvisited vertex, it ensures the minimum cost- regardless of whether the weight is negative or positive.

## Ways To Deal With Directed Graphs
If the graph is directed, you could convert it to an undirected graph by treating every directed edge as an undirected edge with the same weight.

## Performance
- **Time Complexity**: O(E log V): In the worst case, you might need to push and pop every edge in the graph from the priority queue (min-heap). This is in the case where there the global visited check is never met, for example for a linear graph.
- **Space Complexity**: O(V + E): V, for storing the global visited vertices and E, for the maximum size of the priority queue (all the edges pushed from visited neighbours).

## Logic Flow
1. Start with an arbitrary vertex, mark it as visited, and add all its edges to a priority queue.
2. Repeatedly perform greedy extraction for the smallest edge from the priority queue. If the "to" vertex has already been visisted for the extracted edge, skip. Otherwise, add that edge to the edge list and then iterate over the "to" vertex's neighbours.
3. Repeat until all vertices are fully visited.

## Advantages
1. Efficient for dense graphs (many edges) as the priority queue dynamically grows and shrinks as the algorithm progresses, containing only the edges adjacent to the currently visited vertices. Kruskal's, however, globally processes all edges at once, including redundant ones, which is inefficient for dense graphs.

## Disadvantages
1. In sparse graphs, where E<<V^2, the overhead associated with the priority queue operations will start to contribute more and more to the time complexity (aka the log term in E log V). Kruskal's algorithm is more suitable because of its simple edge-centric sorting approach (E log E) as globally sorting E edges is faster than managing a dynamic priority queue for E edges when there are few edges.
2. Requires the graph to be connected; otherwise, it only computes an MST for the connected component.

## Use Cases
1. Network Design: Designing telecommunication, electrical, or computer networks with minimal cost.
2. Graph-Based Logistical Planning: Computing efficient paths for logistics or transportation planning.

## Terminology
- **Connected Graph:** A graph is connected if there exists at least one path between any two vertices. This means all vertices are reachable from any starting vertex.
- **Minimum Spanning Tree (MST):** A subgraph that:
	- Includes all the vertices of the original graph.
	- Has no cycles.
	- Has the minimum possible total edge weight.
