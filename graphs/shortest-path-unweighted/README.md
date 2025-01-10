<h1 align="center">Shortest Path Algorithms for Unweighted Graphs: DFS vs BFS</h1>

## Performance

### DFS
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges. Even though some edges might get "unvisited" during backtracking, each vertex is still processed once per path and each edge is only explored at most twice (for undirected graphs) or once (for directed graphs).
- **Space Complexity**: O(V), for storing the visited set. In the worst case, the recursion stack can also grow to O(V) if the graph has a depth resembling a linked list.

### BFS
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges. If you think about it, every vertex is visited once to mark as visited and then we need to process all its neighbours, which means eventually every edge in the graph is visited once.
- **Space Complexity**: O(V), for storing the visited set. In the worst case, the queue can also grow to O(V) if the graph has a very short and shallow structure where many vertices are at the same level. The parents dictionary also in the worst case will take O(V) space complexity.

## BFS
BFS explores nodes level by level, making it ideal for finding the shortest path in an unweighted graph.

### How Do You Reconstruct The Shortest Path Once The Target Is Found?
Parent Map - Maintain a parents dictionary to keep track of the parent vertex of every vertex. If the target is reached, the shortest path can then be rebuilt into an array by looping up each vertex's parent. This list can then be reversed using [::-1].

### Advantages
1. BFS's use of a queue makes it straightforward to implement.
2. BFS guarantees the shortest path is the first one when the target vertex is found, due to its level-by-level logic flow. This means explicit comparison between all possible paths isn't needed like DFS.

### Disadvantages
1. BFS requires additional memory for the queue and the parents dictionary. In a wide graph, the queue can grow to a size proportional to the number of vertices at the current depth.

## DFS
DFS explores as deep as possible before backtracking, which is less intuitive for shortest path finding but can be adapted for this purpose.

### Backtracking
At the end of each recursive call (which indicates the end of a path), the algorithm pops the last visited node from current path and marks it as unvisited in visited.
This ensures the current path and visited state are reset for other branches of the search as the recursion calls unravels up one or more levels.

### Why is DFS Generally Not Preferred Over BFS For Shortest-Path Algorithms?
In DFS, you need to keep track of the current path, backtrack when necessary, and compare all possible paths explicitly to determine the shortest one- which is a lot of additional overhead. Furthermore, although DFS and BFS have the same asymptotic time complexity, the actual runtime can differ significantly as BFS avoids redundant exploration by halting once the target is found. Contrarily, DFS may explore irrelevant branches deeply before realizing they don’t lead to the target.

### What Situations Is DFS Better Suited For Instead Of Shortest-Path Algorithms?
DFS is better suited in situations where you need to explore every possible path, such as in connectivity checks, detecting cycles, or solving puzzles. 

### Advantages
1. DFS can be implemented both recursively and iteratively (using an explicit stack).

### Disadvantages
1. Less efficient in many cases than BFS for shortest path problems in unweighted graphs, as it may explore many irrelevant branches deeply before backtracking.
2. Does not guarantee the shortest path unless all paths are explicitly compared.

## Are Weighted Graphs Suitable For Shortest Path Algorithms w/ BFS or DFS?
BFS & DFS are not naturally suited for weighted graphs because they don’t account for edge weights and therefore doesn't prioritize shorter edges over longer ones. They assume that each edge has the same cost (or weight of 1). For weighted graphs, their logic would need to be modified into algorithms like Dijkstra's or A*.

## Random Important Trivia

1. What's the difference between list[::-1] and list[:-1]?
	- list[::-1] reverses an entire list.
	- list[:-1] excludes the last element of a list, essentially slicing out the last element.

2. What's the difference between arr = arr2[:] and arr[:] = arr2[:]?
	- arr = arr2[:]: A new list is created in memory, containing a copy of the elements in arr2. The variable 'arr' is updated to point to this new list. If 'arr' was pointing to another list before, that connection is severed, and the old list is no longer accessible through 'arr' (but it may still exist if another variable is pointing to it).
	- arr[:] = arr2[:]: This keeps the existing 'arr' list but replaces all its contents with those of arr2. This is useful when you need to modify the same list in memory (e.g., in recursion) so that changes are reflected wherever the list is being used at any level of recursion.