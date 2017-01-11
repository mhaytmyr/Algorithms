#Uses python3

import sys

def reachable(adj,vertex,visited,labels,cnt):
	visited.append(vertex)
	labels[vertex] = cnt
	for neighbor in adj[vertex]:
		if not neighbor in visited:
			reachable(adj,neighbor,visited,labels,cnt)	

def number_of_components(adj):
	cnt = 1
	labels, visited = {}, []
	for vertex in adj:
		if not vertex in visited:
			reachable(adj,vertex,visited,labels,cnt)
			cnt+=1
	#write your code here
	return sorted(labels.items(), key=lambda x:-x[1])[0][1]

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	graph = {vertex:[] for vertex in range(1,n+1)}	
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		graph[a].append(b)
		graph[b].append(a)
		adj[a - 1].append(b - 1)
		adj[b - 1].append(a - 1)
	print(number_of_components(graph))
