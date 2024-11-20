from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode
from shared.misc import print_separator

def inorder_traversal_recursive(root: TreeNode, ret_arr: list = None) -> list | None:
	if not root:
		return None
	if ret_arr is None:
		ret_arr = []
	inorder_traversal_recursive(root.left, ret_arr)
	ret_arr.append(root.value)
	inorder_traversal_recursive(root.right, ret_arr)
	return ret_arr

def inorder_traversal_iterative(root: TreeNode, ret_arr: list = []) -> list | None:
	stack = []
	curr = root
	while stack or curr:
		while curr:
			stack.append(curr)
			curr = curr.left
		
		curr = stack.pop()
		ret_arr.append(curr.value)

		curr = curr.right
	return ret_arr

root = prompt_and_create_bst()
print_separator()
result = inorder_traversal_iterative(root)
print(f"Result: {result}") if result else print("Empty root node.")
