def Reachable(graph,start,visited):
	visited.append(start)
	#print("Pre-order {}".format(start))
	for neighbor in graph[start]:
		if not neighbor in visited:
			Reachable(graph,neighbor,visited)

	#print("Post-order {}".format(start))
if __name__=="__main__":
	graph = {'A':{'B','E','F'},'B':{'A'},'C':{'D'},'D':{'C'},'E':{'A'},'F':{'G'},'G':{'F'}}	
	visited = []
	Reachable(graph,'E',visited)
	print(visited)
	print('G' in visited)



