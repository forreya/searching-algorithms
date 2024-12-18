from graphs.generate_graph.input_graph_generator import prompt_and_create_adj_list
from collections import deque

def breadth_first_search(adj_list) -> list:
	root = adj_list.get_random_vertex()
	visited = set()
	queue = deque([root])
	ret = []
	while queue:
		curr = queue.popleft()
		ret.append(curr)
		visited.add(curr)
		for neighbour in adj_list.internal_dict[curr]:
			neighbour = neighbour if not adj_list.weighted else neighbour[0]
			if neighbour in visited or neighbour in queue:
				continue
			queue.append(neighbour)
	return ret

adj_list = prompt_and_create_adj_list()
print(breadth_first_search(adj_list))