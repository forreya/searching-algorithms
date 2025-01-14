def dfs(adj_list: dict[str, list], vertex, global_visited: set, curr_visited: set, topological_order: list):
	global_visited.add(vertex)
	curr_visited.add(vertex)
	for neighbour in adj_list[vertex]:
		if neighbour in curr_visited:
			return False
		if neighbour in global_visited:
			continue

		if not dfs(adj_list, neighbour, global_visited, curr_visited, topological_order):
			return False
	curr_visited.remove(vertex)
	topological_order.append(vertex)
	return True
		

def topological_sort_detect_cycle(adj_list: dict[str, list]) -> list | bool:
	global_visited = set()
	topological_order = []
	for vertex in adj_list:
		if vertex in global_visited:
			continue
		if not dfs(adj_list, vertex, global_visited, set(), topological_order):
			return False
	return topological_order[::-1]

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

print(topological_sort_detect_cycle(adj_list_acyclic))