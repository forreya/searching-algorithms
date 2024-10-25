from bsts.generate_bst.tree_node import TreeNode

def print_bst(node, level=0):
	# this is basically a DFS reverse in-order traversal
	if node is not None: 
		print_bst(node.right, level + 1)
		print(" " * 8 * level + "->", node.value) 
		print_bst(node.left, level + 1)