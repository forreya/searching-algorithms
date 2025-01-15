from shared.misc import print_separator
from pprint import pprint

def update_shortest_distance(adj_list: dict[str, list], vertex: str, shortest_distances: dict[str, float]) -> None:
	for neighbour, weight in adj_list[vertex]:
		if shortest_distances[vertex] + weight < shortest_distances[neighbour]:
			shortest_distances[neighbour] = shortest_distances[vertex] + weight

def bellman_ford_shortest_distances(adj_list: dict[str, list], starting_vertex: str) -> dict[str, float]:
	shortest_distances = {vertex: float("inf") for vertex in adj_list}
	shortest_distances[starting_vertex] = 0

	for i in range(len(adj_list)-1):
		for vertex in adj_list:
			update_shortest_distance(adj_list, vertex, shortest_distances)

	return shortest_distances

def update_shortest_path(
	adj_list: dict[str, list[tuple]],
	vertex: str,
	shortest_paths: dict[str, dict],
) -> bool:
	relaxed = False
	for neighbour, weight in adj_list[vertex]:
		current_distance = shortest_paths[vertex]["distance"] + weight
		if current_distance < shortest_paths[neighbour]["distance"]:
			shortest_paths[neighbour]["distance"] = current_distance
			shortest_paths[neighbour]["path"] = shortest_paths[vertex]["path"] + [neighbour]
			relaxed = True
	return relaxed

def bellman_ford_shortest_paths_V2_space_complexity(
	adj_list: dict[str, list[tuple]],
	starting_vertex: str,
	target_vertex: str
) -> dict | bool:
	shortest_paths = { vertex: {"path": [], "distance": float("inf")} for vertex in adj_list}
	shortest_paths[starting_vertex] = {"path": [starting_vertex], "distance": 0}

	# Relax edges |V| - 1 times
	for _ in range(len(adj_list) - 1):
		for vertex in adj_list:
			update_shortest_path(adj_list, vertex, shortest_paths)

	for vertex in adj_list:
		if update_shortest_path(adj_list, vertex, shortest_paths):
			return False

	return shortest_paths[target_vertex]

adj_list = {
	'S': [('E',8), ('A',10)],
	'A': [('C',2)],
	'B': [('A',1)],
	'C': [('B',0)],
	'D': [('A',-4),('C',-1)],
	'E': [('D',1)],
}

print(bellman_ford_shortest_paths_V2_space_complexity(adj_list, 'S', 'A'))