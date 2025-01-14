<h1 align="center">Topological Sort For DAGs</h1>

_Note: This README is incomplete. More topological sort info can be found here `graphs/directed-cycle-detection/topological-sort/README.md`_

## Logic Flow
1. Initialize a global visited set to track nodes that have been fully processed.
2. Use a curr_visited set to detect cycles in the current recursion stack.
3. Traverse each vertex using DFS:
	- If a cycle is detected, return an error or False.
	- Otherwise, add nodes to the result list in post-order (as we want to ensure we follow the precedence constraint in the final list).
	- At the end, reverse the result list to obtain the correct topological order.

## Use Cases
1. Course Prerequisites - Determining the order in which courses should be taken based on prerequisite dependencies.
2. Task Dependencies - Organizing tasks in a sequence where certain tasks must be completed before others.
3. Build Systems - Compiling code files in a specific order based on dependency relationships among modules.