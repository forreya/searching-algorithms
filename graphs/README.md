<h1 align="center">Graphs</h1>

## Overview
A graph is a non-linear data structure consisting of nodes (also called vertices) and connections between them (edges). Graphs are structures that are used to represent various relationships and connections such as social networks, road maps, or task dependency charts.

## Graph Properties:
1. **Directed Graphs:** Edges have a direction, meaning they point from one vertex to another. For example, one-way streets, task dependencies.
2. **Undirected Graphs:** Edges have no direction, meaning connections are bidirectional. For example, social friendships, roads between cities.
3. **Weighted Graphs:** Edges have weights or costs associated with them. For example, distance between cities, network bandwidth. These weights can represent different things like cost, distance, or capacity.
4. **Unweighted Graphs:** Edges have no weights. For example, pure relationships, such as friendships.
5. **Cyclic and Acyclic Graphs:**
	- Cyclic: Graphs containing at least one cycle (a path where a vertex can be revisited).
	- Acyclic: Graphs with no cycles. Directed Acyclic Graphs (DAGs) are used in applications like task scheduling, which is the process of organizing tasks or jobs in a sequence, often subject to dependencies between them.

## Types of Graph Representations:
The following are some representations which are used to model and store the relationships between nodes and edges in a graph.

#### 1. Adjacency Matrix
A 2D array where matrix[i][j] represents the presence (and weight, if applicable) of an edge between vertices i and j. For example:

```
   0  1  2
0 [0, 1, 0]  # Edge from 0 to 1
1 [0, 0, 1]  # Edge from 1 to 2
```

Pros:
- Simple to implement.
- Efficient for dense graphs (many edges).

Cons:
- Uses O(V²) space no matter what, so inefficient for sparse graphs (fewer edges).

#### 2. Adjacency List
A collection of lists or dictionaries where each vertex points to its neighbors.

```
graph = {
    0: [1], # Edge from 0 to 1
    1: [2], # Edge from 1 to 2
    2: []
}
```

Pros:
- Space-efficient for sparse graphs (fewer edges).
- Adjacency lists inherently support weighted graphs by storing edge weights alongside the neighbor node.

Cons:
- Slightly slower for edge lookups compared to adjacency matrices.

#### 3. Edge List
A list of edges represented as pairs or triplets (u, v, weight).

```
graph = [(0, 1), (1, 2)]
```

Pros: 
- Compact and simple.

Cons:
- Inefficient for operations like edge existence checks.

## Maximum Number of Edges
1. Undirected Graphs: V * (V-1) // 2
2. Directed Graphs: V * (V-1)

## Performance Comparison: Adjacency Matrix vs Adjacency List
1. Space Complexity:
	- Adjacency Matrix: O(V²)
	- Adjacency List: O(V + E)
2. Add Edge:
	- Adjacency Matrix: O(1)
	- Adjacency List: O(1)
3. Remove Edge:
	- Adjacency Matrix: O(1)
	- Adjacency List: O(E)
4. Check Edge Existence:
	- Adjacency Matrix: O(1)
	- Adjacency List: O(E)
5. Iterating Neighbors:
	- Adjacency Matrix: O(V)
	- Adjacency List: O(degree of vertex)

## Advantages
1. Graphs can represent virtually any relationship, so are very versatile.
2. Flexible representations (matrix, list, edge list) allow for optimizing based on the use case (e.g., dense vs. sparse graphs).

## Disadvantages
1. Graphs can require significant memory for dense graphs, especially when using adjacency matrices.
2. Many graph algorithms (e.g., shortest path, minimum spanning tree) have high time complexity for large datasets.

## Optimizations
1. Sparse Graph Representation: Use adjacency lists for memory efficiency.
2. Heuristic Search: Algorithms like A*, which is a graph search algorithm that finds the shortest path between two vertices, use heuristics (a strategy that helps solve a problem faster by focusing on the most promising options) to reduce computation time for shortest-path problems.
3. Graph Compression: Reduce memory usage by storing only relevant subgraphs or using compression techniques such as only storing the parts of a graph (subgraphs) relevant to a specific query or task.

## DFS Traversals
Inorder traversal doesn’t apply to general graphs because it relies on a binary tree’s left-to-right ordering of children. General graphs do not have an inherent "order" property. General graphs has two variants of DFS:
1. Preorder DFS: Process the node before its neighbors.
2. Postorder DFS: Process the node after all its neighbors.

## Terminology
1. **Vertex:** The fundamental units in a graph, aka the nodes in a graph.
2. **Edge:** A connection between two vertices.
3. **Degree:**
	- **In-Degree:** Number of incoming edges to a vertex.
	- **Out-Degree:** Number of outgoing edges from a vertex.
	- **Degree (undirected):** Total edges connected to a vertex.
4. **Path:** A sequence of edges connecting a series of vertices.
5. **Cycle:** A path that starts and ends at the same vertex.
