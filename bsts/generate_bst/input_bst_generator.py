import random
from bsts.generate_bst.print_bst import print_bst
from bsts.generate_bst.tree_node import TreeNode
from shared.misc import print_separator, assertIsInteger

def generate_bst(size= 100, min_val= 0, max_val= 100):
	if size == 0 or min_val > max_val:
		return None

	root_val = random.randint(min_val, max_val)
	left_tree_size = random.randint(0, size - 1)
	right_tree_size = size - 1 - left_tree_size

	left_subtree = generate_bst(left_tree_size, min_val, root_val - 1)
	right_subtree = generate_bst(right_tree_size, root_val + 1, max_val)

	root = TreeNode(root_val)

	root.left = left_subtree
	root.right = right_subtree
	return root

def prompt_and_create_bst():
	size = int(input("Size of your BST: "))
	print_separator()
	min_val = int(input("Minimum value of BST: "))
	print_separator()
	max_val = int(input("Maximum value of BST: "))
	bst = generate_bst(size, min_val, max_val)
	print_separator()
	print("Your BST: ")
	print_bst(bst)
	return bst

def get_val():
	target = input("Target value: ")
	assertIsInteger(target)
	return int(target)