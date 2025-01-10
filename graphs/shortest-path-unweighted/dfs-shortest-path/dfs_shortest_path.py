from graphs.generate_graph.adjacency_list import AdjacencyList
from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list, print_separator

def find_shortest_path_dfs(adj_list: AdjacencyList, curr: int, target: int, visited = None, curr_path = None, shortest_path = None) -> list | bool:
	if visited is None:
		visited = set()
	if shortest_path is None:
		shortest_path = []
	if curr_path is None:
		curr_path = []
	
	visited.add(curr)
	curr_path.append(curr)

	if curr == target:
		if not shortest_path or len(curr_path) < len(shortest_path):
			shortest_path[:] = curr_path[:]
	else:
		for neighbour in adj_list.internal_dict.get(curr, []):
			if neighbour not in visited:
				find_shortest_path_dfs(adj_list, neighbour, target, visited, curr_path, shortest_path)

	# Backtracking
	visited.remove(curr)
	curr_path.pop()
	return shortest_path if shortest_path else False

adj_list = prompt_and_create_adj_list()
start, end = adj_list.get_random_vertex(), adj_list.get_random_vertex()
print_separator()
print(f"Your starting and target vertices: {start}, {end}.")
print(f"Shortest Path: {find_shortest_path_dfs(adj_list, start, end)}")