
from time import sleep
from constants import INFITY, ROW_COMB, COL_COMB, ROW, COL
'''
Node class to hold each cells data
'''
class Node():
	
	def __init__(self,posx: int,posy: int, value: int):
		self.x = posx
		self.y = posy
		self.dist = value
		self.visited = False
		self.previousNode = None
		self.type = None
		self.inShort = False
	
	# Setters
	def setType(self, newType):
		self.type = newType

	def setVisited(self):
		self.visited = True

	def setDist(self, val: int):
		self.dist = val
	
	def setPrev(self, prev):
		self.previousNode = prev
	
	def setInShort(self):
		self.inShort = True

	# Getters

	def getType(self):
		return self.type

	def getVisited(self) -> bool:
		return self.visited
	
	def getDist(self)-> int:
		return self.dist

	def getPrev(self):
		return self.previousNode
	
	def getInShort(self):
		return self.inShort

	def getPosition(self) -> str:
		return "(" + str(self.x) + "," + str(self.y) + ")"

	# Behaviors
	def findNeighbours(self, graph: list) -> list:
		neighbours = []
		for i in range(len(ROW_COMB)):
			x_value = self.x + ROW_COMB[i]
			y_value = self.y + COL_COMB[i]
			if (x_value < 0 or x_value >= ROW) or (y_value < 0 or y_value >= COL):
				pass
			else:
				possible_neigh = graph[x_value][y_value]
				if possible_neigh.getType() != "Wall" and possible_neigh.getVisited() != True:
					neighbours.append(possible_neigh)
		return neighbours

'''
Graph class for all grid related things
'''
class Graph():

	def __init__(self, row, cols):
		self._graph = self._initializeNodes(row, cols)
		self.source = None
		self.destination = None

	# Initialize as nodes
	def _initializeNodes(self, row, col):
		grid = []
		for i in range(row):
			temp = []
			for j in range(col):
				temp.append(Node(i, j, INFITY))
			grid.append(temp)
		return grid
	
	# Setters
	def setSource(self, row: int, col: int):
		self.source = (self.getGraph()[row][col])
	
	def setDestination(self, row: int, col: int):
		self.destination = (self.getGraph()[row][col])
	
	def setDist(self, row, col, val):
		(self.getGraph()[row][col]).setDist(val)

	def setType(self, row, col, type):
		(self.getGraph()[row][col]).setType(type)

	# Getters
	def getSource(self) -> Node:
		return self.source
	
	def getDestination(self) -> Node:
		return self.destination

	def getGraph(self):
		return self._graph

	def getDist(self, row, col) -> int:
		return (self.getGraph()[row][col]).getDist()
	
	def getType(self, row, col) -> int:
		return (self.getGraph()[row][col]).getType()

	def getInShort(self, row, col):
		return (self.getGraph()[row][col]).getInShort()

	# ReSetters
	def resetSource(self):
		self.source = None
	
	def resetDestination(self):
		self.destination = None

	def setPath(self):
		prev = self.getDestination().getPrev()
		while prev != None:
			if prev.getType() != "Source":
				prev.setInShort()
			prev = prev.getPrev()

class Queue():
	def __init__ (self):
		self.queue = []
	
	def insert(self, item: Node):
		self.queue = [item] + self.queue
	
	def pop(self) -> Node:
		item = self.queue[-1]
		self.queue = self.queue[:-1]
		return item
	
	def length(self):
		return len(self.queue)