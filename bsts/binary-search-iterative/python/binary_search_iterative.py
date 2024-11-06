from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, get_val, TreeNode

def binary_search_iterative(root: TreeNode, target: int) -> bool:
	while root:
		if target == root.value:
			return True
		root = root.left if target < root.value else root.right
	return False

root = prompt_and_create_bst()
target = get_val()
print(f"Result: {binary_search_iterative(root, target)}")