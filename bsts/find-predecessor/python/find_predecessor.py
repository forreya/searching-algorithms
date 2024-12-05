from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode, get_val
from shared.misc import print_separator

def find_max(curr: TreeNode) -> int:
	while curr.right:
		curr = curr.right
	return curr.value

def find_predecessor(root: TreeNode, target: int) -> int | None:
	curr = root
	predecessor = None
	while curr:
		if target < curr.value:
			curr = curr.left
		elif target > curr.value:
			predecessor = curr
			curr = curr.right
		else:
			if curr.left:
				return find_max(curr.left)
			else:
				return predecessor.value if predecessor else None
	return None

root = prompt_and_create_bst()
target = get_val()
print_separator()
result = find_predecessor(root, target)
print(f"Result: {result}") if result else print("Empty root node.")
