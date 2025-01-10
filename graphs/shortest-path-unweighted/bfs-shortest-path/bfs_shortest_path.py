from graphs.generate_graph.adjacency_list import AdjacencyList
from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list, print_separator
from collections import deque

def find_shortest_path_bfs(adj_list: AdjacencyList, start: int, target: int) -> list | bool:
	queue = deque([start])
	visited = set([start])
	parents: dict[int, int | None] = {start: None}
	
	while queue:
		curr = queue.popleft()
		if curr == target:
			path = []
			while curr is not None:
				path.append(curr)
				curr = parents[curr]
			return path[::-1]
		for neighbour in adj_list.internal_dict.get(curr, []):
			if neighbour not in visited:
				parents[neighbour] =  curr
				visited.add(neighbour)
				queue.append(neighbour)
	return False

adj_list = prompt_and_create_adj_list()
start, end = adj_list.get_random_vertex(), adj_list.get_random_vertex()
print_separator()
print(f"Your starting and target vertices: {start}, {end}.")
print(f"Shortest Path: {find_shortest_path_bfs(adj_list, start, end)}")