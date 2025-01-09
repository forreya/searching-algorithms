<h1 align="center">Connected Components Using Depth-First Search (DFS) for Undirected Adjacency Lists</h1>

## Performance
- **Time Complexity**: O(V + E), where V is the total number of vertices and E is the total number of edges. Each vertex is visited once, and each edge is traversed at most twice (once in each direction).
- **Space Complexity**: O(V). One for the visited set to track processed vertices. Two, O(V) for the recursion stack in the worst case of a deep and tall graph structure. In the iterative approach, the stack size can also reach O(V) in cases where the graph is flat (i.e., a graph with a high branching factor, where each node has many neighbors), as all neighbors of a node may be added to the stack simultaneously.

## Why "Connected Components" Usually Refers to Undirected Graphs?
The symmetry of undirected edges makes it straightforward to group sets of vertices into connected components, as visiting u automatically connects v and vice versa. In directed graphs, the symmetry of edges is absent, so the definition of connectivity splits into strong and weak connectedness.

## Use Cases
1. **Cluster Detection:** Finding groups of interconnected nodes, such as communities in social networks.
2. **Network Connectivity Analysis:** Identifying isolated sub-networks to determine areas of poor connectivity. Also, identifying critical edges in network connectivity. For example, if the network splits into multiple connected components after removing an edge, it indicates that the particular edge was critical for connectivity. These analysis can help improve robustness in networks.
3. **Preprocessing for Graph Algorithms:** Decomposing a graph into connected components can simplify problems like Minimum Spanning Tree or shortest path calculations by working on each component separately.

## Common Interview Questions
1. How would you modify connected components to work with a directed graph instead of an undirected one?
	- Modify the undirected approach to handle strongly connected components using Kosaraju’s or Tarjan’s algorithm.
2. What if the graph has weighted edges when it comes to connected components?
	- Weight is irrelevant for finding connected components since it only concerns connectivity.

## Terminology
- **Connected Component:** A set of vertices where any two vertices in the set are connected by a path and no vertex in the set is connected to any vertex outside the set (aka from another set).