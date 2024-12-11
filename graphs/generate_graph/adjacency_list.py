class AdjacencyList:
	def __init__(self, weighted=False, directed=False):
		self.internal_dict = {}
		self.directed = directed
		self.weighted = weighted

	def add_vertex(self, value):
		if value not in self.internal_dict:
			self.internal_dict[value] = []

	def add_edge(self, from_value, to_value, weight = None):
		self.add_vertex(from_value)
		self.add_vertex(to_value)
		if self.weighted and weight:
			self.internal_dict[from_value].append((to_value, weight))
			if not self.directed:
				self.internal_dict[to_value].append((from_value, weight))
		if not self.weighted:
			self.internal_dict[from_value].append(to_value)
			if not self.directed:
				self.internal_dict[to_value].append(from_value)