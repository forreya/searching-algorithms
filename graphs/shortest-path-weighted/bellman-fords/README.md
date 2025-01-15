<h1 align="center">Bellman-Ford's Algorithm (Negative Weighted Graphs)</h1>

## Performance
- **Time Complexity**: O(VE). Each edge is relaxed V-1 times as the main outer for loop runs V-1 times to guarantee the shortest paths for each vertex as paths can only have a maximum length of V-1. Checking for negative weight cycles adds one additional iteration after the main loop, but it does not affect the overall asymptotic complexity.
- **Space Complexity**: O(V) or O(V^2).
	- The shortest distances is O(V) and the predecessors is also O(V).
	- If paths are stored explicitly (instead of predecessors), the space complexity increases to O(V^2) as each vertex will have an associated shortest path that could be length V in the worst case.

## Why Negative Cycles Render This Algorithm Useless
A negative weight cycle technically allows the total path length to decrease indefinitely by repeatedly traversing the cycle. Without a cycle, it is mathematically impossible for a valid shortest path to require more than ∣V∣−1 edges. In the presence of a negative cycle, the algorithm’s edge relaxation step will continue to find “better” paths in subsequent iterations beyond |V| - 1 by continually traversing the negative cycle.

## How To Optimize Space Usage If You Only Need The Shortest Path For One Target Vertex
Use predecessors instead of storing full paths for each vertex. This reduces space complexity to O(V) while still enabling path reconstruction for the specific target vertex.

## Use Cases
1. **Financial Arbitrage:** Arbitrage is when an asset (stocks, currencies, etc.) is bought in one market and sold in another for a higher price. Bellman-Ford can detect arbitrage opportunities by identifying negative weight cycles in currency exchange graphs. 
2. **Game Development:** Solve problems involving graphs with penalties or rewards associated with specific paths.

## Algorithm Logic
1. Create a shortest_distances dictionary to store the minimum distance from the source to each vertex. Each vertex should be set to infinity (float('inf')) except for the source, which is set to 0.
2. Create a predecessors dictionary to store the predecessor of each vertex along the shortest path.
3. Relax each edge |V| - 1 times. This involves iterating over each vertex's neighbors and updating the shortest distances (this is done |V| -1 times). This ensures that the shortest paths stabilize for all vertices.
4. After the main |V| - 1 loop, we perform one more iteration over all edges to detect any negative weight cycles. If any distance can still be relaxed, it indicates the presence of a negative weight cycle, as the shortest possible non-vertex-repeating path would be |V| - 1 and so no changes should be expected after the main |V| - 1 loop.
5. If no negative cycle exists, reconstruct the shortest path to a target vertex using the predecessors dictionary by backtracking from the target to the source.

## Why Is Negative Weight Cycle Detection Needed Even After The Shortest Path Is Already Found
It might seem that the algorithm would only compute valid shortest paths with lengths less than |V| - 1, so detecting negative weight cycles afterward could be unnecessary. However, a shortest path with fewer than |V| - 1 edges could already have traversed a negative weight cycle multiple times before the main loop completes. This can artificially cause side-effects and lower the shortest distances to other interrelated vertices, including the target vertex, making the computed shortest path incorrect.