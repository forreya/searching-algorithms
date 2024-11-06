<h1 align="center">BST Node Insertion (Iterative)</h1>

## Performance
- **Time Complexity**: O(logn) in a balanced BST, but can degrade to O(n) if the tree is unbalanced and resembles a linked list.
- **Space Complexity**: O(1) since the iterative approach does not require extra stack space, unlike the recursive method.

## Common Approaches
There are two primary methods for performing the final insertion:
1. Using a Parent and Direction Tracker:
	- **How it works:** As you traverse the tree, you keep track of the parent node and the direction (left or right) where the new node should be inserted at every iteration, just in case the loop exits after the current iteration. When the loop is exited, you then perform the insertion using the most recent parent and direction variables.
	- **Clear Seperation:** Seperating traversal and insertion makes the main loop cleaner as it's solely responsible for finding the insertion point.
	- **Readability** Improves readability by keeping the insertion logic outside the loop.
2. Checking for None on the Spot within the Loop:
	- **How it works:** You check if the next child node (left or right) is None at each step within the loop. If the next child is None, perform the insertion immediately.
	- **Concise Implementation:** Fewer variables are needed for this approach, resulting in a more concise implementation.
	- **Harder to Debug:** This approach blends traversal and insertion within the loop, which can make the logic slightly harder to understand.

## Advantages
By avoiding recursion, this iterative approach maintains constant space usage, O(1).

## Disadvantages
Insertion time can degrade to O(n) if the BST is completely unbalanced, as we would have to traverse through every node.

## Notes
- This function assumes that duplicates are not allowed, as duplicate insertion returns without modifying the tree.
- For optimal performance, it’s best to use this approach with self-balancing trees to prevent degradation in time complexity.