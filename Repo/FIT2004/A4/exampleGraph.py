class Graph:

	class WeightedEdge:
		def __init__(self, dest, weight):
			self.dest = dest
			self.weight = weight

	def __init__(self, n):
		self.adj_list = [[] for _ in range(n)]
		self.num_vertices = n

	def add_directed_edge(self, source, dest, weight):
		self.adj_list[source].append(Graph.WeightedEdge(dest, weight))


#usage example
g = Graph(4)
g.add_directed_edge(0,1,5)
g.add_directed_edge(0,2,10)

#print neighbours of 0
for edge in g.adj_list[0]:
	print(edge.dest, edge.weight)

print(g.adj_list)