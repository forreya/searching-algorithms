from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode, get_val
from shared.misc import print_separator

def find_min(curr: TreeNode) -> int:
	while curr.left:
		curr = curr.left
	return curr.value

def find_successor(root: TreeNode, target_val: int) -> int | None:
	successor = None
	curr = root
	while curr:
		if target_val > curr.value:
			curr = curr.right
		elif target_val < curr.value:
			successor = curr
			curr = curr.left
		else:
			if curr.right:
				return find_min(curr.right)
			else:
				return successor.value if successor else None
	return None

root = prompt_and_create_bst()
target = get_val()
print_separator()
result = find_successor(root, target)
print(f"Result: {result}") if result else print("Empty root node.")
