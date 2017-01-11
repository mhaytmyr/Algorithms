#Uses python3

import sys

def acyclic(graph):
	path,visited = set(),set()

	def visit(vertex):
		if vertex in visited:
			return False
		visited.add(vertex)
		path.add(vertex)
		for neighbor in graph[vertex]:
			if neighbor in path or visit(neighbor):
				return True
		path.remove(vertex)
		return False

	if any(visit(v) for v in graph):
		return 1
	else:
		return 0

if __name__ == '__main__':
	#graph = {'A':['B','E','D'],'B':['C'],'C':['D'],'E':['D'],'D':[]}
	#graph = {'A':['B'],'B':['C'],'C':['A']}
	#graph = {'A':[],'B':['A','E'],'C':['E','F'],'D':['B','G'],'E':['D','F','G'],'F':[],'G':[],'H':['F'],'I':['H']}
	#print(acyclic(graph))

	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	graph = {vertex:[] for vertex in range(1,n+1)}	
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
		graph[a].append(b)
	#print(acyclic(adj))
	print(acyclic(graph))
