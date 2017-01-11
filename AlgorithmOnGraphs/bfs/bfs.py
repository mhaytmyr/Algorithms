#Uses python3

import sys
from queue import Queue

def distance(adj, s, t):
	#write your code here
	q = Queue()
	q.put(s)
	allNodes = {item:'White' for item in adj}
	distance = {item:sys.maxsize for item in adj}
	distance[s] = 0
	while not q.empty():
		node = q.get()#get latest element
		allNodes[node] = 'Black' #processing node
		for item in adj[node]:
			if allNodes[item]=='White' and distance[item]==sys.maxsize:
				allNodes[item] = 'Grey' #discovered
				distance[item] = distance[node]+1
				q.put(item) #put in queue

	if distance[t]==sys.maxsize:
		return -1
	else:
		return distance[t]

if __name__ == '__main__':
	#graph = {'A':['B','E'],'B':['C'],'C':['D'],'E':['D'],'D':[]}
	#graph = {'A':['B'],'B':['C'],'C':['A']}
	#graph = {'A':[],'B':['A','E'],'C':['E','F'],'D':['B','G'],'E':['D','F','G'],'F':[],'G':[],'H':['F'],'I':['H']}
	#print(graph)
	#print(distance(graph,'I','F'))

	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	graph = {vertex:[] for vertex in range(1,n+1)}
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
		adj[b - 1].append(a - 1)
		graph[a].append(b)
		graph[b].append(a)
		s, t = data[2 * m], data[2 * m + 1]
	print(distance(graph, s, t))
