<h1 align="center">Inorder Traversal for BSTs</h1>

## Performance
- **Time Complexity**: O(n), where n is the number of nodes in the tree, as each node is visited once.
- **Space Complexity**: 
  - **Recursive Approach**: O(h), where h is the height of the tree, due to the recursive call stack.
  - **Iterative Approach**: O(h) as well, since an explicit stack is used to manage traversal.

## Logic Flow
Nodes are visited in the following order:
1. Left Subtree - Traverse the left subtree until the leftmost node is reached.
2. Root Node - Process the current node (e.g., add its value to a result list or perform a specific operation on it).
3. Right Subtree - Traverse the right subtree.

## Use Cases
- **Sorting Tree Elements**: Inorder traversal produces a sorted list of values in a Binary Search Tree (BST).
- **Tree Validation**: Used to verify if a tree satisfies BST properties.

## Some Details On The Implementations
1. **Why Do We Not Use `not ret_arr` in Recursive Approach?**
   - Using `ret_arr is None` ensures that a new instance of `ret_arr` is created only once at the start of the recursion when the default value of `None` is passed in. If `not ret_arr` were used, a new instance could inadvertently be created during recursive calls (as an empty `[]` also satisfies `not ret_arr`), leading to separate `ret_arr` objects in memory.

2. **Why Check `stack or curr` in Iterative Approach?**
   - Both `stack` and `curr` are critical to the traversal process:
     - The `stack` ensures backtracking to parent nodes after left subtree traversal.
     - The `curr` pointer handles the traversal of right subtrees as `curr` is set to the right subtree just before a new iteration begins.
     - If you check only `stack`, you may miss processing the current node’s right subtree when `stack` is empty but there is still a right subtree stored in `curr`.

## Advantages of Recursive Approach
1. Simpler and more intuitive code that mirrors the natural definition of inorder traversal (left, root, right).

## Disadvantages of Recursive Approach
1. Recursion uses the system call stack, which can lead to stack overflow for very deep or unbalanced trees.
2. Dynamically modifying traversal logic during recursion is more difficult, there is less fine-grained control when it comes to debugging.

## Advantages of Iterative Approach
1. Prevents stack overflow by avoiding the use of the system call stack.
2. Provides finer control over the traversal process, making it easier to add conditions for early stopping, skipping nodes, or modifying traversal logic.

## Disadvantages of Iterative Approach
1. More complex to implement compared to recursion due to explicit stack management and having to manually manage the traversal path by pushing nodes onto the stack.
2. Requires careful handling of left and right subtree traversal to maintain the correct inorder sequence.