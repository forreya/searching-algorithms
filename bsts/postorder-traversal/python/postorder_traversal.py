from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode
from shared.misc import print_separator

def postorder_traversal_recursive(root: TreeNode, ret_list: list = None) -> list | None:
	if root is None:
		return None
	if ret_list is None:
		ret_list = []
	postorder_traversal_recursive(root.left, ret_list)
	postorder_traversal_recursive(root.right, ret_list)
	ret_list.append(root.value)
	return ret_list

def postorder_traversal_iterative(root: TreeNode) -> list | None:
	stack = []
	if not root:
		return None
	ret_list = []
	stack.append(root)

	while stack:
		curr = stack.pop()
		ret_list.append(curr.value)
		if curr.left:
			stack.append(curr.left)
		if curr.right:
			stack.append(curr.right)
	ret_list.reverse()
	return ret_list

root = prompt_and_create_bst()
print_separator()
result = postorder_traversal_iterative(root)
print(f"Result: {result}") if result else print("Empty root node.")