<h1 align="center">Kruskal's Algorithm for Minimum Spanning Tree</h1>

Kruskal's algorithm is a greedy algorithm designed to find the Minimum Spanning Tree (MST) of a connected, undirected graph. It builds the MST by processing edges in increasing order of their weights and adding them to the tree if they do not form a cycle.

## Performance
- **Time Complexity**: O(E log E + E α(V)):
	- E log E: Sorting the edge list by weight. This complexity is due to the sorting algorithm typically used, such as merge sort, heap sort, or quick sort, all of which have a worst-case time complexity of O(nlogn) for sorting n elements.
	- E α(V): Union-Find operations (with path compression and union by rank). α(V) is the inverse Ackermann function, which grows very slowly. For practical purposes, α(V) can be considered nearly constant.
- **Space Complexity**: O(V), for storing the attributes of Union-Find structure (parents and ranks).

## Why Is Kruskal's Algorithm Greedy?
1. Edge Selection by Minimum Weight: It processes edges in increasing order of weight (globally sorted beforehand).
2. No Reassessment of Previous Choices: Once an edge is added, it is never removed or reconsidered. This is a hallmark of greedy algorithms.

## Logic Flow
1. Start by globally sorting all edges in ascending order of their weights. This ensures the algorithm processes the shortest edges first.
2. Initialize a Union-Find object.
3. For each edge (u, v, weight): Check if u and v belong to different connected components by comparing their parents using the Union-Find find operation.
4. If they are in different components, add the edge to the MST and merge the components using the union operation.
5. If they are already in the same component, skip the edge to avoid cycles.
6. Stop once V - 1 edges have been added to the MST return list or when the sorted edge list has been fully traversed.

## What Happens If We Don't Perform Global Sorting?
Without globally sorting the edges by weight, the algorithm may select heavier edges before lighter ones, leading to a spanning tree but not necessarily a minimum spanning tree (MST).

## Use Cases
1. Network Design: Building efficient communication networks with minimal cost.
2. Transportation Planning: Constructing roads, railways, or pipelines with the most efficiency.

## Advantages
1. Simple and Intuitive: Relatively easy to implement (especially if the Union-Find data structure is predefined).
2. Efficient for Sparse Graphs: For sparse graphs, E is small, so log(E) grows slowly, making global sorting relatively fast compared to the heap-based Prim's algorithm.
3. Great for scenarios where the input is represented as an edge list, as no additional preprocessing is needed to convert an adjacency list into an edge list.

## Disadvantages
1. Globally sorting all edges by weight upfront adds computational overhead, especially for dense graphs (with E ~ V²). Prim's is better scales better with denser graphs as it processes vertices and their edges incrementally rather than all at once.

## Notes
1. Iterative Nature: BFS is inherently iterative due to its reliance on a queue. Recursive implementations are rare and inefficient.
2. Weighted Graphs: BFS does not account for edge weights. For shortest paths in weighted graphs, algorithms like Dijkstra's or Bellman-Ford are needed.
3. Graph Representation: BFS is most efficient with adjacency lists, where neighbors of a vertex can be accessed in O(1) on average.