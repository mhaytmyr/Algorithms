#Uses python3

import sys
from queue import Queue

def BelmanFord(graph):
	dist,prev = {},{}
	for item in graph:
		dist[item] = sys.maxsize
		prev[item] = None
	
	for i in range(1,graph.__len__()): #repeat relaxation V-1 times
	#for i in range(1,3): #repeat relaxation V-1 times
		q = Queue()
		q.put(i)
		dist[i] = 0
		visited = {item:False for item in graph}
		while not q.empty():
			curr = q.get()
			visited[curr] = True
			for node in graph[curr]:
				if not visited[node]:
					q.put(node)
				if dist[node]>dist[curr]+graph[curr][node]:
					dist[node] = dist[curr]+graph[curr][node]

		print("Iteration {} distances: {}".format(i,dist))		
	#Do cylce one more time
	q = Queue()
	q.put(i)
	visited = {item:False for item in graph}
	while not q.empty():
		curr = q.get()
		visited[curr] = True
		for node in graph[curr]:
			if not visited[node]:
				q.put(node)
			if dist[node]>dist[curr]+graph[curr][node]:#found cycle in graph
				return 1
	return 0


def negative_cycle(adj, cost):
    #write your code here
    return 0


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	graph = {item:{} for item in range(1,n+1)}
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
		graph[a][b] = w
	#print(negative_cycle(adj, cost))
	print(BelmanFord(graph))
