import random
from graphs.generate_graph.adjacency_list import AdjacencyList
from graphs.generate_graph.print_adj_list import print_adj_list
from shared.misc import print_separator

def generate_adjacency_list(vertices=5, edges=5, weighted=False, directed=False, max_weight=10) -> AdjacencyList:
	if (edges > vertices * (vertices - 1) // (2 if not directed else 1)):
		raise ValueError(f"Too many edges for {vertices} vertices...")
	
	adj_list = AdjacencyList(weighted, directed)

	for vertex in range(1,vertices+1):
		adj_list.add_vertex(vertex)

	edges_set = set()
	while len(edges_set) < edges:
		first_vertex, second_vertex = random.sample(range(1,vertices+1), 2)
		if (first_vertex, second_vertex) in edges_set:
			continue
		if (second_vertex, first_vertex) in edges_set and not adj_list.directed:
			continue
		weight = random.randint(1,max_weight) if weighted else None
		adj_list.add_edge(first_vertex, second_vertex, weight)
		edges_set.add((first_vertex,second_vertex))

	return adj_list

def prompt_and_create_adj_list():
	vertices = int(input("Number of vertices? "))
	print_separator()
	edges = int(input("Number of edges? "))
	print_separator()
	weighted = input("Weighted (y/n)? ").lower()
	print_separator()
	directed = input("Directed (y/n)? ").lower()
	print_separator()
	directed = True if directed == "y" else False
	if weighted == "y":
		max_weight = int(input("Max weight (1-10)? "))
		adj_list = generate_adjacency_list(vertices, edges, True, directed, max_weight)
		print_separator()
	else:
		adj_list = generate_adjacency_list(vertices, edges, False, directed)
	print("Your Adjacency List: ")
	print_adj_list(adj_list)
	return adj_list