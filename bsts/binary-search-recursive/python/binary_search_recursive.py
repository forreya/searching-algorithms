from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, get_val, TreeNode

def binary_search_recursive(root: TreeNode, target: int) -> bool:
	if not root:
		return False
	if target == root.value:
		return True
	return binary_search_recursive(root.left, target) if target < root.value else binary_search_recursive(root.right, target)

root = prompt_and_create_bst()
target = get_val()
print(f"Result: {binary_search_recursive(root, target)}")