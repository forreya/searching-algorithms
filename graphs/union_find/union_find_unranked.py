class UnionFindNoRank:
	def __init__ (self, size):
		self.parents = list(range(size))

	def find(self, x: int) -> int:
		if self.parents[x] != x: # Path compression
			self.parents[x] = self.find(self.parents[x])
		return self.parents[x]
	
	def union(self, x: int, y: int) -> None:
		root_of_x = self.find(x)
		root_of_y = self.find(y)
		if root_of_x != root_of_y:
			self.parents[root_of_y] = root_of_x

uf = UnionFindNoRank(5)
uf.union(0,1)
uf.union(2,3)
print(f"Is 0 and 1 in the same set? {uf.find(0) == uf.find(1)}")
print(f"Is 0 and 2 in the same set? {uf.find(0) == uf.find(2)}")
uf.union(2,1)
print(f"Is 3 and 0 in the same set? {uf.find(3) == uf.find(0)}")
print(f"Is 3 and 4 in the same set? {uf.find(3) == uf.find(4)}")