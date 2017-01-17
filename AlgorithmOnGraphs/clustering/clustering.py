#Uses python3
import sys,numpy as np
import math
from queue import PriorityQueue

class DisJointSet:
	def __init__(self,n):
		self.parents = {item:item for item in range(n)} # item:root; pointer to root node
		self.clusters = {item for item in range(n)}

	def find_item(self,item):
		if self.parents[item]==item:
			return item
		else:
			return self.find_item(self.parents[item])

	def join_sets(self,set1,set2):
		nodes = [self.find_item(set1),self.find_item(set2)]
		mother = np.random.choice([0,1])
		child = 2+(~mother)
		self.parents[nodes[child]] = nodes[mother]
		
		#now delete child from keys	
		if nodes[child] in self.clusters:
			self.clusters.remove(nodes[child])

	def cluster_size(self):
		return self.clusters.__len__()	


def clustering(x, y, k):
	#write your code here
	n = len(x)
	p = PriorityQueue()
	p_all = PriorityQueue()
	clusters = DisJointSet(n)
	for i in range(n):
		for j in range(i+1,n):
			distance = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
			p.put((distance,(i,j))) #it is symmetric
			p_all.put((distance,(i,j)))

	while not p.empty(): #iterate over all edges

		dist,curr = p.get() #get distance and edges
		if clusters.cluster_size()==k: #if reached number of clusters halt
			break
		if clusters.find_item(curr[0])==clusters.find_item(curr[1]): #if both vertices are in same cluser, 
			continue				# it will produce cycle  
		clusters.join_sets(curr[0],curr[1]) #else join them into cluster
		x0,y0 = x[curr[0]],y[curr[0]]
		x1,y1 = x[curr[1]],y[curr[1]]
		#print("Joining ({},{}) to ({},{}) at {}".format(x0,y0,x1,y1,dist))
		#print("Cluster size {}".format(clusters.cluster_size()))
	#print(p.queue)
	#print(dist)	
	
	'''
	partitions = {}	
	for i in range(n):
		x0,y0 = x[i],y[i]
		cluster = clusters.find_item(i)
		if not cluster in partitions:
			partitions[cluster] = [(x0,y0)]
		else:
			partitions[cluster].append((x0,y0))
	'''

	#print(partitions)
	min_dist = sys.maxsize
	for dist,edges in p_all.queue:
		if clusters.find_item(edges[0])==clusters.find_item(edges[1]): #points are within same cluster 
			continue 
		if dist	<= min_dist:
			min_dist = dist

	return min_dist
	#return p.queue[0][0]


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	data = data[1:]
	x = data[0:2 * n:2]
	y = data[1:2 * n:2]
	data = data[2 * n:]
	k = data[0]
	print("{0:.12f}".format(clustering(x, y, k)))
