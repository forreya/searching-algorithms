from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode
from shared.misc import print_separator

def preorder_traversal_recursive(root: TreeNode, ret_list: list = None) -> list | None:
	if ret_list is None:
		ret_list = []
	if root:
		ret_list.append(root.value)
		preorder_traversal_recursive(root.left, ret_list)
		preorder_traversal_recursive(root.right, ret_list)
	return ret_list

def preorder_traversal_iterative(root: TreeNode) -> list | None:
	if not root:
		return None
	ret_list = []
	stack = [root]
	curr = root
	while stack:
		curr = stack.pop()
		ret_list.append(curr.value)
		if curr.right:
			stack.append(curr.right)
		if curr.left:
			stack.append(curr.left)
	return ret_list

root = prompt_and_create_bst()
print_separator()
result = preorder_traversal_iterative(root)
print(f"Result: {result}") if result else print("Empty root node.")
