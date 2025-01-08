from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list
from graphs.generate_graph.adjacency_list import AdjacencyList
from shared.misc import print_separator

def postorder_traversal_recursive(adj_list: AdjacencyList, curr: int, visited = None, ret_list = None) -> list:
	if visited is None:
		visited = set()
	if ret_list is None:
		ret_list = []
	visited.add(curr)
	for neighbour in adj_list.internal_dict.get(curr, []):
		if neighbour not in visited:
			postorder_traversal_recursive(adj_list, neighbour, visited, ret_list)
	ret_list.append(curr)
	return ret_list

def postorder_traversal_iterative(adj_list: AdjacencyList, start: int) -> list:
	stack = [start]
	ret_list = []
	visited = set([start])
	while stack:
		curr = stack.pop()
		ret_list.append(curr)
		for neighbour in adj_list.internal_dict.get(curr, []):
			if neighbour not in visited:
				stack.append(neighbour)
				visited.add(neighbour)
	ret_list.reverse()
	return ret_list

adj_list = prompt_and_create_adj_list()
start = adj_list.get_random_vertex()
print_separator()
print(f"Starting Vertex: {start}")
result = postorder_traversal_iterative(adj_list, start)
print(result)