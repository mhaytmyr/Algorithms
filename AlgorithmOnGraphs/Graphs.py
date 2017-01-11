def Naive(graph):

	visited = []
	for node in graph:
		if not node in visited:
			visited.append(node)
			for item in graph[node]:
				if not item in visited: visited.append(item)
	print(visited)				
		
def Explore(graph,vertex,visited):
	print("Calling function {},{}".format(vertex,visited))
	visited.append(vertex)
	for neighbor in graph[vertex]:
		if not neighbor in visited:
			Explore(graph,neighbor,visited) 

def DFS(graph,visited):
	for vertex in graph:
		if not vertex in visited:
			Explore(graph,vertex,visited)

def Connectivity(graph,visited):
	label = 1
	connection = {}
	for vertex in graph:
		if not vertex in visited:
			connection[vertex]=label
			Explore2(graph,vertex,visited,connection,label)
			label+=1
	print(connection)

def Explore2(graph,vertex,visited,connection,label):
	connection[vertex] = label
	visited.append(vertex)
	for neighbor in graph[vertex]:
		if not neighbor in visited:
			Explore2(graph,neighbor,visited,connection,label)
	


graph = {'A':{'B','E'},'B':{'A'},'C':{'D'},'D':{'C'},'E':{'A'},'F':{'G'},'G':{'F'}}
visited = []
print(graph)
Connectivity(graph,visited)
#Explore(graph,'A',visited)
#DFS(graph,visited)
#print(visited)
