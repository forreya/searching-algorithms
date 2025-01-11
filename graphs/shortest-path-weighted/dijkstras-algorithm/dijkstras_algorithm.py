import heapq

def dijkstra(adj_list: dict, start, target) -> list | bool:
	shortest_distance = {vertex: float('inf') for vertex in adj_list}
	shortest_distance[start] = 0
	priority_queue = []
	heapq.heappush(priority_queue, (0, start))
	predecessors = {vertex: None for vertex in adj_list}

	while priority_queue:
		curr_distance, vertex = heapq.heappop(priority_queue)
		if vertex == target:
			break

		if curr_distance > shortest_distance[vertex]:
			continue
		
		for neighbour, edge_distance in adj_list[vertex].items():
			new_distance = curr_distance + edge_distance
			if new_distance < shortest_distance[neighbour]:
				shortest_distance[neighbour] = new_distance
				predecessors[neighbour] = vertex
				heapq.heappush(priority_queue, (new_distance, neighbour))

	if shortest_distance[target] == float('inf'):
		return False

	curr = target
	ret = []
	while curr is not None:
		ret.append(curr)
		curr = predecessors[curr]
	return ret[::-1]

adj_list = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3, 'E': 8},
    'E': {}
}

print(dijkstra(adj_list, 'A', 'E'))