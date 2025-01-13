def dfs_recursive(adj_list: dict, vertex: int, component: list, visited: set) -> list:
	component.append(vertex)

	for neighbour in adj_list[vertex]:
		if neighbour not in visited:
			dfs_recursive(adj_list, neighbour, component, visited)
	return component

def dfs_iterative(adj_list: dict, vertex: int, component: list, visited: set) -> list:
	stack = [vertex]

	while stack:
		curr = stack.pop()
		component.append(curr)
		for neighbour in adj_list[curr]:
			if neighbour not in visited:
				visited.add(neighbour)
				stack.append(neighbour)
	return component

def connected_components(adj_list: dict) -> list:
	visited = set()
	connected_components = []

	for vertex in adj_list:
		if vertex not in visited:
			component = []
			visited.add(vertex)
			dfs_iterative(adj_list, vertex, component, visited)
			connected_components.append(component)
	return connected_components

adj_list_undirected = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2],
    4: [5],
    5: [4]
}
print(f"Result: {connected_components(adj_list_undirected)}")