from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, get_val, print_bst, TreeNode
from shared.misc import print_separator

def insert_node_iterative(root: TreeNode, new_val: int, debug_mode: bool = False) -> TreeNode:
	debug_print = lambda msg: print(msg) if debug_mode else None
	if not root:
		debug_print("Created root node.")
		return TreeNode(new_val)
	curr = root
	while curr:
		if new_val == curr.value:
			debug_print("Node to insert already exists.")
			return root
		elif new_val < curr.value:
			if not curr.left:
				curr.left = TreeNode(new_val)
				debug_print(f"Inserted to the left of {curr.value}.")
				return root
			curr = curr.left
		else:
			if not curr.right:
				curr.right = TreeNode(new_val)
				debug_print(f"Inserted to the right of {curr.value}.")
				return root
			curr = curr.right
	debug_print("Something went wrong, shouldn't ever reach here.")
	return root

root = prompt_and_create_bst()
new_val = get_val()
print_separator()
result = insert_node_iterative(root, new_val, True)
print_bst(root) if result else print("Insertion failed.")
