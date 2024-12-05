from bsts.generate_bst.input_bst_generator import prompt_and_create_bst, TreeNode
from shared.misc import print_separator
from collections import deque

def breadth_first_search(root: TreeNode) -> list | None:
	if not root:
		return None
	queue = deque([root])
	ret_list = []
	while queue:
		curr = queue.popleft()
		ret_list.append(curr.value)

		if curr.left:
			queue.append(curr.left)
		if curr.right:
			queue.append(curr.right)
	return ret_list

root = prompt_and_create_bst()
print_separator()
result = breadth_first_search(root)
print(f"Result: {result}") if result else print("Empty root node.")