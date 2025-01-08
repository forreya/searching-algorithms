class UnionFindRanked:
	def __init__ (self, size):
		self.parents = list(range(size))
		self.ranks = [0] * size

	def find(self, x: int) -> int:
		if self.parents[x] != x: # Path compression
			self.parents[x] = self.find(self.parents[x])
		return self.parents[x]
	
	def union(self, x: int, y: int) -> None:
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