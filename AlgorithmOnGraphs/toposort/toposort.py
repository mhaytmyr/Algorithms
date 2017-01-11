#Uses python3

import sys
from collections import deque

#def dfs(adj, used, order, x):
def dfs(graph):
	#write your code here
	visited,index = set(),0
	for vertex in graph:
		if not vertex in visited:
			explore(vertex,graph,visited,index)
	#pass

def dfs_visit(graph, u, color, L, found_cycle):
	if found_cycle[0]:
		return
	color[u] = "gray"
	for v in graph[u]:
		if color[v] == "gray":
			found_cycle[0] = True
			return
		if color[v] == "white":
			dfs_visit(graph, v, color, L, found_cycle)
	color[u] = "black"      # when we're done with u,
	L.append(u)             # add u to list (reverse it later!)

def dfs_topsort(graph):         # recursive dfs with 
	L = []                      # additional list for order of nodes
	color = { u : "white" for u in graph }
	found_cycle = [False]
	for u in graph:
		if color[u] == "white":
			dfs_visit(graph, u, color, L, found_cycle)
		if found_cycle[0]:
			break
	if found_cycle[0]:           # if there is a cycle, 
		L = []                   # then return an empty list  
	L.reverse()                  # reverse the list
	return L                     # L contains the topological sort


if __name__ == '__main__':
	#graph = {'A':['B','E','D'],'B':['C'],'C':['D'],'E':['D'],'D':[]}
	#graph = {'A':['B'],'B':['C'],'C':['A']}
	#graph = {'A':[],'B':['A','E'],'C':['E','F'],'D':['B','G'],'E':['D','F','G'],'F':[],'G':[],'H':['F'],'I':['H']}
	#print(graph)
	#print(dfs_topsort(graph))

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
	#order = dfs(graph)
	order = dfs_topsort(graph)
	for x in order:
		print(x, end=' ')
