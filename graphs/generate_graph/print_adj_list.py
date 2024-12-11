from graphs.generate_graph.adjacency_list import AdjacencyList

def print_adj_list(adj_list: AdjacencyList):
	for vertex, edges in adj_list.internal_dict.items():
		print(f"{vertex}: {edges}")