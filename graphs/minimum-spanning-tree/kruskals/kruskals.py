import heapq

class UnionFindStrRanked:
	def __init__ (self):
		self.parents = {}
		self.ranks = {}
	
	def maybe_add_new_node(self, node):
		if node not in self.parents:
			self.parents[node] = node
			self.ranks[node] = 0

	def find(self, x: str) -> str:
		self.maybe_add_new_node(x)
		if self.parents[x] != x: # Path compression
			self.parents[x] = self.find(self.parents[x])
		return self.parents[x]
	
	def union(self, x: str, y: str) -> bool:
		root_of_x = self.find(x)
		root_of_y = self.find(y)
		if root_of_x != root_of_y:
			if self.ranks[root_of_x] > self.ranks[root_of_y]:
				self.parents[root_of_y] = root_of_x
			elif self.ranks[root_of_x] < self.ranks[root_of_y]:
				self.parents[root_of_x] = root_of_y
			else:
				self.parents[root_of_y] = root_of_x
				self.ranks[root_of_x] += 1
			return True
		return False

def kruskal_classic(edge_list: list[tuple]) -> list[tuple]:
	edge_list.sort(key=lambda edge : edge[2])
	union_find = UnionFindStrRanked()
	ret_list = []

	for u, v, weight in edge_list:
		if union_find.union(u,v):
			ret_list.append((u,v,weight))

	return ret_list

def kruskal_heap_variant(edge_list: list[tuple]) -> list[tuple]:
	union_find = UnionFindStrRanked()
	priority_list = []
	heapq.heapify(priority_list)
	ret_list = []

	for u, v, weight in edge_list:
		heapq.heappush(priority_list, (weight, u, v))

	while priority_list:
		weight, u, v = heapq.heappop(priority_list)

		if union_find.union(u,v):
			ret_list.append((u,v,weight))

	return ret_list

edge_list = [
	("I", "J", 0),
	("A", "E", 1),
	("C", "I", 1),
	("E", "F", 1),
	("G", "H", 1),
	("B", "D", 2),
	("C", "J", 2),
	("D", "E", 2),
	("D", "H", 2),
	("A", "D", 4),
	("B", "C", 4),
	("C", "H", 4),
	("G", "I", 4),
	("A", "B", 5),
	("D", "F", 5),
	("H", "I", 6),
	("F", "G", 7),
	("D", "G", 11)
]

print(f"Result: {kruskal_heap_variant(edge_list)}")