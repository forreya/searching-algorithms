<h1 align="center">Postorder Traversal for BSTs</h1>

## Performance
- **Time Complexity**: O(n), where n is the number of nodes in the tree, as each node is visited once.
- **Space Complexity**: O(h), where h is the height of the tree, due to either the recursive call stack or the explicit stack that is used within the code.

## Logic Flow
Nodes are visited in the following order:
1. Left Subtree - Traverse the left subtree recursively or iteratively.
2. Right Subtree - Traverse the right subtree recursively or iteratively.
3. Root Node - Process the current node after both its subtrees have been traversed.

## Use Cases
- **Tree Deletion**: Postorder traversal is useful when deleting a tree, as it ensures that children are processed before their parent node.

## Iterative Postorder Traversal
#### How It Works:
- Uses an explicit stack to simulate the recursive behavior.
- Nodes are pushed onto the stack in reverse order: root first, then right, then left. 
- A helpful way to think about this is to mimic the reverse of a modified preorder traversal (root, right, left), then reverse the result.
- After all nodes are added to the result list, it is reversed to achieve the postorder sequence.

## Advantages of Recursive Approach
- Shorter and more intuitive, as it directly reflects the natural order of postorder traversal in the code.
- Does not require explicit stack management, unlike the iterative approach.

## Disadvantages of Recursive Approach
- Uses the system call stack, which can cause stack overflow in very deep or highly unbalanced trees.
- Adding modifications for early stopping, skipping nodes, or adjusting traversal logic dynamically is harder than in the iterative approach.

## Notes on the Iterative Approach
- An explicit stack (a list) is used to simulate the recursive call stack, which helps prevents stack overflow.
- The right child is pushed onto the stack before the left child so that the left subtree is processed first, which preserves the correct preorder sequence (root, left, right).

## Advantages of Iterative Approach
- By avoiding the usage of the system call stack, the iterative approach can handle deeper trees without risking stack overflow, as the function manages depth through an explicit list (stack).
- The iterative approach provides finer control over the traversal process, making it easier to add conditions for early stopping, skipping specific nodes, or modifying traversal logic as needed.

## Disadvantages of Iterative Approach
- More complex to implement due to explicit stack management and the need to simulate the recursive behavior.
- Requires pushing the right child before the left child to maintain the correct order, which isn't as intuitive compared to the recursive approach.
- Reversing the list introduces an additional operation, which introduces additional overhead:
	- Since the traversal itself also takes O(n), the additional reversal step doesn’t change the overall asymptotic complexity of the algorithm (it remains O(n)), but it does add a constant factor to the runtime.
	- There is no additional space complexity if we use `.reverse()` as this in-built operation performs the reversal in-place.

## Terminology:
- **Asymptotic Complexity:** In asymptotic complexity, we focus on the growth rate of an algorithm as the input size n -> ∞. This means that constants are ignored because they have a negligible effect as the input size becomes very large. Also, the largest term dominates because they represent the primary driver of growth as input size increases.
