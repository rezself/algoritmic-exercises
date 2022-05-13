# A class to represent a graph object
class Graph:
	def __init__(self, edges, n):
		# resize the list to hold `n` elements
		self.adj = [[] for _ in range(n)]

		# add an edge from source to destination
		for edge in edges:
			self.adj[edge[0]].append(edge[1])


# Function to perform DFS traversal on the graph
def DFS(graph, v, discovered):

	# mark the current node as discovered
	discovered[v] = True		

	# do for every edge (v, u)
	for u in graph.adj[v]:
		if not discovered[u]:   # `u` is not discovered
			DFS(graph, u, discovered)


# Function to find the root vertex of a graph
def findRootVertex(graph, n):

	# to keep track of all previously discovered vertices in DFS
	discovered = [False] * n

	# find the last starting vertex `v` in DFS
	v = 0
	for i in range(n):
		if not discovered[i]:
			DFS(graph, i, discovered)
			v = i

	# reset the discovered vertices
	discovered[:] = [False] * n

	# perform DFS on the graph from the last starting vertex `v`
	DFS(graph, v, discovered)

	# return -1 if all vertices are not reachable from vertex `v`
	for i in range(n):
		if not discovered[i]:
			return -1

	# we reach here only if `v` is a root vertex
	return v


if __name__ == '__main__':

	# List of graph edges as per the above diagram
	edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]

	# total number of nodes in the graph (0 to 5)
	n = 6

	# build a directed graph from the given edges
	graph = Graph(edges, n)

	# find the root vertex in the graph
	root = findRootVertex(graph, n)

	if root != -1:
		#print('The root vertex is', root)
		print(root)
	else:
		#print('The root vertex does not exist')
		print(-1)
