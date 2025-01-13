from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list
from graphs.generate_graph.adjacency_list import AdjacencyList

def dfs_detect_cycle_undirected(adj_list: AdjacencyList, curr: int, visited = None, parent = None) -> bool:
	if visited is None:
		visited = set()
	visited.add(curr)
	for neighbour in adj_list.internal_dict.get(curr, []):
		if neighbour in visited and neighbour is not parent:
			return True
		if neighbour not in visited:
			if dfs_detect_cycle_undirected(adj_list, neighbour, visited, curr):
				return True
	return False

adj_list = prompt_and_create_adj_list()
start = adj_list.get_random_vertex()
print(f"Starting Vertex: {start}")
res = dfs_detect_cycle_undirected(adj_list, start)
print(f"Result: {res}")