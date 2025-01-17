import heapq

def prims_calculate_minimum_cost(adj_list: dict) -> int:
	if not adj_list:
		return -1
	
	global_visited = set()
	minimum_cost = 0
	priority_queue = [(0,None,next(iter(adj_list)))]
	heapq.heapify(priority_queue)
	while priority_queue:
		curr = heapq.heappop(priority_queue)
		current_vertex = curr[2]

		if current_vertex in global_visited:
			continue
		
		global_visited.add(current_vertex)
		minimum_cost += curr[0]
		for neighbour, weight in adj_list[current_vertex]:
			if neighbour in global_visited:
				continue
			heapq.heappush(priority_queue, (weight, current_vertex, neighbour))
	return minimum_cost

def prims_get_edge_list(adj_list: dict) -> list:
	if not adj_list:
		return []
	
	global_visited = set()
	edge_list = []
	priority_queue = [(0,None,next(iter(adj_list)))]
	heapq.heapify(priority_queue)
	while priority_queue:
		curr = heapq.heappop(priority_queue)
		current_vertex = curr[2]

		if current_vertex in global_visited:
			continue
		
		global_visited.add(current_vertex)
		edge_list.append(curr)
		for neighbour, weight in adj_list[current_vertex]:
			if neighbour in global_visited:
				continue
			heapq.heappush(priority_queue, (weight, current_vertex, neighbour))
	return edge_list[1:]

adj_list = {
	'A': [('B',10),('C',3)],
	'B': [('A',10),('C',4),('D',1)],
	'C': [('A',3),('B',4),('D',4),('E',4)],
	'D': [('B',1),('C',4),('E',2)],
	'E': [('C',4),('D',2)]
}

print(f"Result: {prims_calculate_minimum_cost(adj_list)}")