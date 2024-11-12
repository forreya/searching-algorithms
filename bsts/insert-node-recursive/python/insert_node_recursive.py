from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, get_val, print_bst, TreeNode
from shared.misc import print_separator

def insert_node_recursive(root: TreeNode, new_val: int, debug_mode: bool = False) -> TreeNode:
	if not root:
		return TreeNode(new_val)
	if new_val == root.value:
		if debug_mode:
			print("The node to insert already exists...")
	elif new_val < root.value:
		root.left = insert_node_recursive(root.left, new_val, debug_mode)
	else:
		root.right = insert_node_recursive(root.right, new_val, debug_mode)
	return root

root = prompt_and_create_bst()
new_val = get_val()
print_separator()
root = insert_node_recursive(root, new_val, True)
print_bst(root)
