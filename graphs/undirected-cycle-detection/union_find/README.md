<h1 align="center">Union-Find for Edge Lists</h1>

## What Is Union-Find And What Does It Do?
Union-Find (or Disjoint Set Union, DSU) is a data structure used to efficiently manage a collection that is partitioned into disjoint (non-overlapping) sets. It supports two main operations:
1. Find: Determine which set or group a particular element belongs to.
2. Union: Merge two sets. For example, it might take `union(x, y)` and merges the two groups or sets that contains x and y.

## Performance

### With Rank and Path Compression
- **Find Operation:** Amortized O(α(V)), where α(V) is the inverse Ackermann function, which grows extremely slowly (effectively constant for practical inputs).
- **Union Operation:** Amortized O(α(V)). 
- **Undirected Edge Lists Cycle Detection:** Processing E edges takes O(E⋅α(V)).
- **Space Complexity:** O(V), for storing the parent and rank arrays.

### Without Rank
- **Find Operation:** Worst-case O(V), since trees can become tall and unbalanced, resembling linked lists.
- **Union Operation:** Worst-case O(V), due to the lack of balancing when merging sets.
- **Undirected Edge Lists Cycle Detection:** Processing E edges takes O(E⋅V).
- **Space Complexity:** O(V), for storing the parent array.

## What Does Union-Find Solve?
1. Connected Components: Identify clusters or groups in a graph (e.g., friend circles, social networks).
2. Cycle Detection: Detect cycles in undirected graphs.
3. Kruskal's Algorithm: Construct the Minimum Spanning Tree (MST) by processing edges in sorted order.

## Why Use Rank?
Rank tracks the depth (or height) of the trees in the Union-Find structure. When performing a union, the smaller tree is always attached under the larger one. This minimizes the height of the resulting tree. Without rank, trees can grow tall and unbalanced, leading to inefficient operations with O(V) time complexity. For large graphs or dense inputs, rank is neccesary to maintain the near-constant time performance of Union-Find.

## What Is Path Compression in Union-Find?
Path Compression is an optimization technique in the Find operation of Union-Find, designed to flatten the tree structure and minimize its height. During a Find operation, the algorithm traverses up the tree to locate the root of the set. With path compression, every node visited along the way is updated to point directly to the root, effectively shortening the path for future operations. This incremental flattening significantly reduces the height of the tree over time, ensuring that subsequent Find operations are faster. When combined with union by rank, path compression guarantees an amortized time complexity of O(α(V)), as repeated Find operations progressively flatten the tree structure to approach constant time performance.

## How Does Union-Find Work for Undirected Edge Lists?
1. Initialization: Start with every node as its own set (disjoint sets). 
2. Processing Each Edge:
	- For each edge (u,v):
		- Use the find operation to check the roots of u and v.
		- If find(u)==find(v), u and v are already connected, and so adding the edge would create a cycle- return True.
		- If find(u)!=find(v), merge the sets containing u and v using the union operation.
	- If no edges create a cycle, the graph is acyclic.

## Terminology
- **Inverse Ackermann Function:** α(V) is the inverse of the Ackermann function, which means it grows extremely slowly. For practical values of n (less than 2^65536), α(V)≤5. This makes α(V) effectively constant for all realistic applications. 