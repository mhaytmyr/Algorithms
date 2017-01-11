#Uses python3
import sys
import math
from queue import PriorityQueue


import numpy as np
class DisJointSet:
	def __init__(self,n):
		self.parent = {item:item for item in range(n)}

	def find_item(self,item):
		if self.parent[item]==item: #set is singleton
			return item
		else:
			return self.find_item(self.parent[item])

	def union_sets(self,set1,set2):
		nodes = [self.find_item(set1),self.find_item(set2)]
		#root = np.random.choice([0,1])
		#child = 2+(~root) 
		#self.parent[nodes[root]] = nodes[child]
		self.parent[nodes[0]] = nodes[1]


def kruscal_distance(x,y,n):
	p = PriorityQueue()
	mySet = DisJointSet(n) #has find_item and union_sets

	for i in range(n):
		for j in range(i+1,n):
			distance = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
			p.put((distance,(i,j))) #it is symmetric

	minimalGraph = {}
	minDistance = 0
	while not p.empty(): # while there exist edges

		dist,curr = p.get() #get vertex of edge
		print("Trying to merge {} and {}".format(curr[0],curr[1]))
		if mySet.find_item(curr[0])==mySet.find_item(curr[1]): #if both already added, it is cycle
			continue
		mySet.union_sets(curr[0],curr[1]) #union these two nodes
		minDistance+=dist
		if not curr[0] in minimalGraph: 
			minimalGraph[curr[0]] = {curr[1]:dist} 
		else:
			minimalGraph[curr[0]][curr[1]] = dist
		print(mySet.parent)

		#print(minimalGraph)
	return minDistance

def prims_distance(x,y,n):
	graph = create_graph(x,y,n)
	cost, parent, visited = {},{}, {}
	for i in graph:
		cost[i] = sys.maxsize
		parent[i] = None
		visited[i] = False

	p = PriorityQueue()
	cost[0] = 0 #start from the first item
	p.put((cost[0],0)) #insert first item into queue
	
	for item in graph:
		p.put((cost[item],item))

	while not p.empty():
		tmp = [item for item in list(p.queue)]
		print("List of items {}".format(tmp))
		curr = p.get()[1] #get priority key
		items = [item[1] for item in list(p.queue)]
		for node in graph[curr]:
			if node in items and cost[node]>graph[curr][node]:
				cost[node] = graph[curr][node]
				parent[node] = curr
				p.put	
	print(cost)		
	
if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	print("{0:.9f}".format(kruscal_distance(x,y,n)))
	#prims_distance(x,y,n)
