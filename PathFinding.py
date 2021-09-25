import copy

# update distances
'''
Update the Distance between neighbours using the sources preious array and sources location
If destination value found then return True else False
'''
def updateDis(graph,neigh,dist,startR,startC):
	for each in neigh:
		r, c = int(each[0]), int(each[1])
		nodeInfo = dist[str(r)+str(c)]
		if nodeInfo["weight"] == None and nodeInfo["prev"] == None:
			nodeInfo["prev"] = copy.deepcopy(dist[str(startR)+str(startC)]["prev"])
			nodeInfo["prev"].append([startR, startC])
			nodeInfo["weight"] = len(nodeInfo["prev"])
		if graph[r][c] == 9:
			return True
	return False

# Get neighbours
'''
'''
def getNeighbours(graph, dist, numR, numC):
	maxRow = len(graph)
	maxCol = len(graph[0])
	neighs = []
	try:
		# Below
		if numR-1>=0 and dist[str(numR-1)+str(numC)]["weight"] == None:
			neighs.append(str(numR-1)+ str(numC))
	except KeyError as err:
		pass
	try:
		# Above
		if numR+1<maxRow and dist[str(numR+1)+str(numC)]["weight"] == None:
			neighs.append(str(numR+1)+str(numC))
	except KeyError as err:
		pass
	try:
		# Left
		if numC-1>=0 and dist[str(numR)+str(numC-1)]["weight"] == None:
			neighs.append(str(numR)+str(numC-1))
	except KeyError as err:
		pass
	try:
		# Right
		if numC+1<maxCol and dist[str(numR)+str(numC+1)]["weight"] == None:
			neighs.append(str(numR)+str(numC+1))
	except KeyError as err:
		pass
	return neighs

# Find the source coords
'''
'''
def findSource(graph):
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			val = graph[i][j]
			if val == 0:
				return i,j
			elif val != 1 and val != -1 and val != 9:
				return -1,-1 
	return -1,-1

#set up Distance
'''
'''
def setupDistance(graph):
	dist = {}
	final = False
	dest = [-1,-1]
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			val = graph[i][j]
			if val == 0:
				dist[str(i) + str(j)] = {'weight': 0, 'prev': []}
			elif val == 1 or val == 9:
				dist[str(i) + str(j)] = {'weight': None, 'prev': None} 
			if val == 9:
				final = True
				dest[0] = i
				dest[1] = j
	if final:
		return dist, dest
	return None, None

# setup the graph
'''
'''
def setup():
	b = [[1,0,1,-1,1], [1,1,-1,1,9], [-1,1,1,1,-1]]
	return b

# recursive
'''
'''
def djakartas(reached, validNeighbours, graph, dist, startR, startC):
	if reached or len(validNeighbours) == 0:
		return reached
	for each in validNeighbours:
		newNeigh = getNeighbours(graph, dist, int(each[0]), int(each[1]))
		reached = updateDis(graph, newNeigh, dist, int(each[0]), int(each[1]))
		reached = djakartas(reached, newNeigh, graph, dist, int(each[0]), int(each[1]))
		if reached:
			return reached

# start
def main():
	reached = False
	graph = setup()
	
	# Get index for sources
	startR, startC = findSource(graph)
	
	# if no source end
	if startR == -1 and startC == -1:
		print("Invalid Graph recheck")
	else:
		# Setup all distance to infitiny and return final blocks indices else end
		dist, destFinal = setupDistance(graph)
		if dist == None:
			print("Error, no final destination.")
		else:
			# update dist for source block
			dist[str(startR)+str(startC)]["prev"] = [] 
			dist[str(startR)+str(startC)]["weight"] = len(dist[str(startR)+str(startC)]["prev"])
			
			# Run first with source block as start
			validNeighbours = getNeighbours(graph, dist, startR, startC)
			reached = updateDis(graph, validNeighbours, dist, startR, startC)
			
			# Run recursive loop with rest
			reached = djakartas(reached, validNeighbours, graph, dist, startR, startC)
			
			# Print path
			if reached:
				list = dist[str(destFinal[0])+str(destFinal[1])]["prev"]
				for i in range(0, len(list)):
					if i != len(list)-1:
						print(str(list[i][0]) + "," + str(list[i][1]) + " ->", end =" ")
					else:
						print(str(list[i][0]) + "," + str(list[i][1]))
			else:
				print("No path")

main()