def dfs(adj_list: dict[str, list], vertex, global_visited: set, curr_visited: set):
	if vertex in curr_visited:
		return False
	if vertex in global_visited:
		return True
	
	global_visited.add(vertex)
	curr_visited.add(vertex)
	for neighbour in adj_list[vertex]:
		if not dfs(adj_list, neighbour, global_visited, curr_visited):
			return False
	curr_visited.remove(vertex)

def topological_sort_detect_cycle(adj_list: dict[str, list]) -> bool:
	global_visited = set()
	curr_visited = set()
	for vertex in adj_list:
		if not dfs(adj_list, vertex, global_visited, curr_visited):
			return True
	return False

adj_list_acyclic = {
	"A": ["B", "C"],
	"B": ["D"],
	"C": ["E"],
	"D": ["F"],
	"E": ["F"],
	"F": [],
	"G": ["H"],
	"H": []
}

adj_list_cyclic = {
	"A": ["B", "C"],
	"B": ["D"],
	"C": ["E"],
	"D": ["F", "A"],
	"E": ["F"],
	"F": [],
	"G": ["H"],
	"H": []
}

print(topological_sort_detect_cycle(adj_list_cyclic))