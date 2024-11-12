from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode
from shared.misc import print_separator

def find_maximum_node(root: TreeNode) -> TreeNode | None:
	if not root:
		return None
	while root.right:
		root = root.right
	return root

root = prompt_and_create_bst()
print_separator()
result = find_maximum_node(root)
print(f"Maximum Node: {result.value}") if result else print("Empty root node.")
