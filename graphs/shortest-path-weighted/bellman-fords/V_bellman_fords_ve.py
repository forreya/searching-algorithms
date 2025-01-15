def update_shortest_path(
	adj_list: dict[str, list[tuple]],
	vertex: str,
	shortest_distances: dict[str, float],
	predecessors: dict,
) -> bool:
	relaxed = False
	for neighbour, weight in adj_list[vertex]:
		current_distance = shortest_distances[vertex] + weight
		if current_distance < shortest_distances[neighbour]:
			shortest_distances[neighbour] = current_distance
			predecessors[neighbour] = vertex
			relaxed = True
	return relaxed

def bellman_ford_shortest_paths_V_space_complexity(
	adj_list: dict[str, list[tuple]],
	starting_vertex: str,
	target_vertex: str
) -> tuple[list, float] | bool:
	shortest_distances = {vertex: float("inf") for vertex in adj_list}
	predecessors = {vertex: None for vertex in adj_list}
	shortest_distances[starting_vertex] = 0

	# Relax edges |V| - 1 times
	for _ in range(len(adj_list) - 1):
		for vertex in adj_list:
			update_shortest_path(adj_list, vertex, shortest_distances, predecessors)

	for vertex in adj_list:
		if update_shortest_path(adj_list, vertex, shortest_distances, predecessors):
			return False

	ret = []
	curr = target_vertex
	while curr:
		ret.append(curr)
		curr = predecessors[curr]
	return ret[::-1], shortest_distances[target_vertex]

adj_list = {
	'S': [('E',8), ('A',10)],
	'A': [('C',2)],
	'B': [('A',1)],
	'C': [('B',0)],
	'D': [('A',-4),('C',-1)],
	'E': [('D',1)],
}

print(bellman_ford_shortest_paths_V_space_complexity(adj_list, 'S', 'A'))