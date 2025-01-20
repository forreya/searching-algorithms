<h1 align="center">Heap-Based Variant of Kruskal's Algorithm</h1>

In this variant, a heap (min-priority queue) is used instead of globally sorting the edge list upfront. This eliminates the explicit sorting step.

## Performance
- **Time Complexity**: O(E log E + E α(V)):
	- E log E: Each edge is pushed into the heap (heapify costs O(E)), and extracting the smallest edge with heappop is O(log E) for each of E edges.
	- E α(V): Union-Find operations (with path compression and union by rank). α(V) is the inverse Ackermann function, which grows very slowly. For practical purposes, α(V) can be considered nearly constant. This is exactly the same as the classic approach.
- **Space Complexity**: O(V + E), O(E) for storing all edges in the heap and O(V) for storing the parent and rank arrays in the Union-Find structure.

## Logic Flow
1. Build a min-heap by pushing all edges into a heap as tuples (weight, u, v), where weight is the sorting key.
2. Repeatedly extract the edge with the smallest weight from the heap.
3. For each edge (u, v, weight): Check if u and v belong to different connected components by comparing their parents using the Union-Find find operation.
4. If they are in different components, add the edge to the MST and merge the components using the union operation.
5. If they are already in the same component, skip the edge to avoid cycles.
6. Stop once V - 1 edges have been added to the MST or when the heap is empty.

## Advantages
Dynamically processes edges without requiring full sorting upfront, unlike the classic variant.

## Disadvantages
Slightly more complex due to heap management compared to the classic variant.