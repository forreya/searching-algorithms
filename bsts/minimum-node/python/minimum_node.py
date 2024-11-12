from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode
from shared.misc import print_separator

def find_minimum_node(root: TreeNode) -> TreeNode | None:
	if not root:
		return root
	while root.left:
		root = root.left
	return root

root = prompt_and_create_bst()
print_separator()
result = find_minimum_node(root)
print(f"Minimum Node: {result.value}") if result else print("Empty root node.")
