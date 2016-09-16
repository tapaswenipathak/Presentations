class UnionFind:
	def __init__(self, size):
		self._id = list(range(size))
		self._weight = [1] * size
	
	def _root(self, i):
		j = i
		while j != self._id[j]:
			self._id[j] = self._id[self._id[j]]
			j = self._id[j]
		return j

	def find(self, a, b):
		return self._root(a) == self._root(b)

	def union(self, a, b):
		i = self._root(a)
		j = self._root(b)
		if(self._weight[i] < self._weight[j]):
			self._id[i] = j
			self._weight[j] += self.weight[i]
		else:
			self._id[j] = i
			self._weight[i] += self._weight[j]

uf = UnionFind(10)

uf.union(1, 2)
uf.union(2, 3)

print uf._id

print uf.find(1, 2)
print uf.find(3, 4)
