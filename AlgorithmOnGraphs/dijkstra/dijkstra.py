#Uses python3

import sys
from queue import Queue


def Dijkstra(adj, s, t):
	dist, prev = {},{}
	for vertex in adj:
		dist[vertex] = sys.maxsize
		prev[vertex] = None
	dist[s] = 0
	q = Queue()
	
	print(adj)
	return -1

def NaivePaths(adj,s,t):
	dist, prev = {},{}
	for vertex in adj:
		dist[vertex] = sys.maxsize
		prev[vertex] = None
	dist[s] = 0 #distance to itself is zero
	q = Queue()
	q.put(s)
	while not q.empty():
		current = q.get()
		for node in adj[current]:
			if not prev[node]: 
				q.put(node)
			if dist[node]>dist[current]+adj[current][node]:
				dist[node] = dist[current]+adj[current][node]
				prev[node] = current

		#print("Traversing {} updated distance {}".format(current,dist)) 
	if dist[t]==sys.maxsize:
		return -1
	else:
		return dist[t]		

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	graph = {vertex:{} for vertex in range(1,n+1)}
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
		graph[a][b] = w
	#s, t = data[0] - 1, data[1] - 1
	#print(distance(adj, cost, s, t))
	s, t = data[0], data[1]
	#print(distance(graph, s, t))
	print(NaivePaths(graph,s,t))
