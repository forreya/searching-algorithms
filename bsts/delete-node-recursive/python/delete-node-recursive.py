from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, get_val, print_bst, TreeNode
from shared.misc import print_separator

def find_min(node):
	while node.left:
		node = node.left
	return node


def delete_node_recursive(root: TreeNode, new_val: int) -> TreeNode:
	if not root:
		return None
	if new_val < root.value:
		root.left = delete_node_recursive(root.left, new_val)
	elif new_val > root.value:
		root.right = delete_node_recursive(root.right, new_val)
	else:
		if root.right and root.left:
			successor = find_min(root.right)
			root.value = successor.value
			root.right = delete_node_recursive(root.right, successor.value)
		elif root.right:
			return root.right
		else:
			return root.left
	return root

root = prompt_and_create_bst()
val_to_del = get_val()
print_separator()
root = delete_node_recursive(root, val_to_del)
print_bst(root)