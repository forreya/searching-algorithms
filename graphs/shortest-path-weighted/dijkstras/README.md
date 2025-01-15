<h1 align="center">Dijkstra Algorithm (Non-Negative Weighted Graphs)</h1>

Dijkstra’s algorithm is designed to find the shortest paths from a single source vertex to all other vertices in a weighted graph, provided all edge weights are non-negative. It uses a greedy approach and a priority queue, which is crucial for maintaining the greedy property, where the vertex with the smallest known distance is dequeued first.

## Performance
- **Time Complexity**: O(E log V). This complexity arises because each edge potentially could be processed during edge relaxation with a priority queue operation of log(E) -> log(V^2) -> log(V) as the maximum size of the priority queue could be E in the worst case due to multiple entries for the same vertex being stored due to multiple edges leading to the same vertex.
- **Space Complexity**: O(V + E). V for storing distances and predecessors. The priority queue may simultaneously store multiple entries for the same vertex due to multiple edges leading to the same vertex, leading to a worst-case space usage of E for the priority queue.

## Why can we simplify O(E log E) to O(E log V)?
The maximum number of edges in a graph is approximately V^2. log(V^2) can be simplified to 2log(V), and we ignore constant factors in asymptotic time complexity for Big-0 notation, leaving O(E log V).

## Logic Flow
1. Initialization - Set the distance to all vertices as infinity (∞), except the source vertex, which is set to 0.
2. Use a priority queue (min-heap) to process vertices by their current shortest distance.
3. Edge Relaxation - For each neighbour processed, update the shortest distances to each neighbour if a shorter path is found via the current vertex.
4. Push updated distances into the priority queue.
5. Stopping Condition - Continue processing until the priority queue is empty.
6. Use a predecessors dictionary to reconstruct the shortest path to any target vertex by tracing back from the target to the source.

## Why Non-Negative Weights?
Dijkstra’s algorithm assumes that once a vertex’s shortest distance is finalized, it will not change. This assumption breaks if negative weights exist, as further edge relaxation could yield shorter paths, invalidating the algorithm’s greedy property.

## Use Cases
1. Pathfinding in Games - Calculating the shortest or optimal route for characters or entities.
2. Transportation Planning - Optimizing routes for logistics and public transport.
3. Robot Navigation - Determining the shortest path for movement in a grid or graph-based environment.

## Advantages
1. Can compute paths to all vertices from the source in a single execution.
2. Efficient for graphs with non-negative weights: O(E log V) vs. O(VE) with the Bellman-Ford algorithm.

## Disadvantages
1. Does not work with graphs containing negative edge weights, a different algorithm like Bellman-Ford is needed.
2. Slower than specialized algorithms like A* in certain scenarios with a defined target and where a heuristic is available.

## Terminology
- **Edge Relaxation:** Updating the shortest known distance to a vertex if a shorter path is found via another vertex.
- **Greedy Algorithm:** A problem-solving approach that builds up a solution step-by-step, always choosing the next step that offers the most immediate benefit.