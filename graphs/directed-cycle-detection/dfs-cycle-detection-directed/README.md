<h1 align="center">Depth-First Search (DFS) for Cycle Detection in Directed Graphs</h1>

## Main Idea
DFS for cyclic detection in directed graphs involves two key levels for tracking:
	- Global visited set: Tracks vertices that have been fully processed (all outgoing edges from it has been fully traversed until the very end of each path).
	- Current path visited set: Tracks vertices that are currently in the DFS recursion stack (aka they are currently in the path being analysed).

## Performance
- **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges. Each vertex and edge is processed at most once as the global visited set prevents duplicate edge processing.
- **Space Complexity**: O(V) for storing the recursion stack, current path visited set, and global visited set.

## Logic Flow w/ Recursion
1. Start DFS from any unvisited vertex.
2. Use a global visited set to insert vertices that have had all their outgoing edges fully processed to avoid revisiting them.
3. Use a current path visited set set to track vertices currently in the recursion stack (aka they are currently in the path being analysed) to detect cycles.
4. For each neighbor:
	- If the neighbor is in the current path visited set, a cycle exists.
	- If the neighbor is not in the global visited set, recursively call DFS on the neighbor. If they are, skip that vertex altogether.
5. After exploring all neighbors fully, remove the current vertex from current path visited set (backtracking) and add it to global visited set to mark it as fully processed.

## Why Do We Need The Global Visited Set If We Already Have The Current Path Visited Set?
The global visited set tracks vertices that have been fully processed, meaning all its outgoing edges have been explored. This prevents redundant edge checks in future DFS calls (as the analysis of other different paths that might include the same edge), improving efficiency.

## Cycle Extraction
Once a cycle is detected, the cycle portion of a graph can be extracted by using curr_path.index(neighbor) and slicing the current parent path with the return value to retrieve a sub path that only includes the cycle. This allows the returned cyclic path to begin and end with the same vertex, rather than including irrelevant sections that might have been part of the largest parent path.

## Why Also Use A Current Path Visited Set Instead of Just A Current Path Array?
As the current path visited set is a set, it is optimized for cycle detection as checking membership in a set is O(1). The current path array would need a O(n) operation for membership checking each time (which is slow), and therefore is instead used to maintain the order of vertices in the current path traversal and extract the sub cyclic-paths when a cycle is detected.