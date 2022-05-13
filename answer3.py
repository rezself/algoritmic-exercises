from collections import deque


# A class to represent a graph object
class Graph:
	# Constructor
	def __init__(self, edges, n):

		# A list of lists to represent an adjacency list
		self.adjList = [[] for _ in range(n)]

		# add edges to the directed graph
		for (src, dest) in edges:
			self.adjList[src].append(dest)


# Function to perform BFS traversal from a given source vertex in a graph to
# determine if a destination vertex is reachable from the source or not
def isReachable(graph, src, dest):

	# get the total number of nodes in the graph
	n = len(graph.adjList)

	# to keep track of whether a vertex is discovered or not
	discovered = [False] * n

	# create a queue for doing BFS
	q = deque()

	# mark the source vertex as discovered
	discovered[src] = True

	# enqueue source vertex
	q.append(src)

	# loop till queue is empty
	while q:

		# dequeue front node and print it
		v = q.popleft()

		# if destination vertex is found
		if v == dest:
			return True

		# do for every edge (v, u)
		for u in graph.adjList[v]:
			if not discovered[u]:
				# mark it as discovered and enqueue it
				discovered[u] = True
				q.append(u)

	return False


if __name__ == '__main__':

	# List of graph edges as per the above diagram
	edges = [
		(0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
		(3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
	]

	# total number of nodes in the graph (labeled from 0 to 7)
	n = 8

	# build a graph from the given edges
	graph = Graph(edges, n)

	# source and destination vertex
	(src, dest) = (0, 7)

	# perform BFS traversal from the source vertex to check the connectivity
	if isReachable(graph, src, dest):
		#print(f'Path exists from vertex {src} to vertex {dest}')
		print(1)
	else:
		#print(f'No path exists between vertices {src} and {dest}')
		print(0)