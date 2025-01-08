from graphs.union_find.union_find_ranked import UnionFindRanked

def detect_cycle(edge_list, num_of_vertices) -> bool:
	uf = UnionFindRanked(num_of_vertices)
	for x, y in edge_list:
		if uf.find(x) == uf.find(y):
			return True
		uf.union(x,y)
	return False

edge_list_undirected = [(0, 1), (1, 2), (2, 0)]
print(detect_cycle(edge_list_undirected, 3))