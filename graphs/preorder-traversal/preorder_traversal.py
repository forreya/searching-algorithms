from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list
from graphs.generate_graph.adjacency_list import AdjacencyList
from shared.misc import print_separator
from typing import List

def preorder_traversal_recursive(adj_list: AdjacencyList, vertex: int, visited = None, ret_list = None) -> List[int]:
	if ret_list is None:
		ret_list = []
	if visited is None:
		visited = set()
	ret_list.append(vertex)
	visited.add(vertex)
	for neighbour in adj_list.internal_dict.get(vertex, []):
		if neighbour not in visited:
			preorder_traversal_recursive(adj_list, neighbour, visited, ret_list)
	return ret_list

def preorder_traversal_iterative(adj_list: AdjacencyList, vertex: int) -> List[int]:
	stack, ret_list, visited = [], [], set()
	stack.append(vertex)
	visited.add(vertex)
	while stack:
		curr = stack.pop()
		ret_list.append(curr)
		for neighbour in adj_list.internal_dict.get(curr, []):
			if neighbour not in visited:
				stack.append(neighbour)
				visited.add(neighbour)
	return ret_list

adj_list = prompt_and_create_adj_list()
starting_vertex = adj_list.get_random_vertex()
print_separator()
print(f"Your starting vertex is {starting_vertex}.")
print_separator()
print(f"Result: {preorder_traversal_iterative(adj_list, starting_vertex)}")