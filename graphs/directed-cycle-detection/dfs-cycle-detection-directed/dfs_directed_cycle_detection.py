from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list, print_separator
from graphs.generate_graph.adjacency_list import AdjacencyList

def dfs_cycle_detection_directed(adj_list: AdjacencyList, curr: int, curr_path_visited=None, curr_path=None, visited=None) -> list[int] | bool:
	if curr_path_visited is None:
		curr_path_visited = set()
	if curr_path is None:
		curr_path = []
	if visited is None:
		visited = set()

	curr_path_visited.add(curr)
	curr_path.append(curr)

	for neighbour in adj_list.internal_dict.get(curr, []):
		if neighbour in curr_path_visited:
			cycle_start_index = curr_path.index(neighbour)
			return curr_path[cycle_start_index:] + [neighbour]
		if neighbour not in visited:
			result = dfs_cycle_detection_directed(adj_list, neighbour, curr_path_visited, curr_path, visited)
			if result:
				return result

	curr_path_visited.remove(curr)
	visited.add(curr) 
	curr_path.pop()
	return False

adj_list = prompt_and_create_adj_list()
start = adj_list.get_random_vertex()
print_separator()
print(f"Starting Vertex: {start}")
print(f"Result: {dfs_cycle_detection_directed(adj_list, start)}")