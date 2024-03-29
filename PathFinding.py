from node import Node
'''Graph class for all grid related things'''
class Game():
	def __init__(self, row, cols):
		self._grid = self._initialize(row, cols)
		self.source = None
		self.destination = None

	# Initialize as nodes
	def _initialize(self, row, col):
		grid = []
		for i in range(row):
			temp = []
			for j in range(col):
				temp.append(Node(i, j))
			grid.append(temp)
		return grid
	
	# Setters
	def setSource(self, row: int, col: int):
		self.source = (self.getGraph()[row][col])	
	def setDestination(self, row: int, col: int):
		self.destination = (self.getGraph()[row][col])
	def setDist(self, row, col, val):
		(self.getGraph()[row][col]).setDistance(val)
	def setType(self, row, col, type):
		(self.getGraph()[row][col]).setType(type)

	# Getters
	def getSource(self) -> Node:
		return self.source
	def getDestination(self) -> Node:
		return self.destination
	def getGraph(self):
		return self._grid
	def getVisited(self, row, col):
		return (self.getGraph()[row][col]).getVisited()
	def getDist(self, row, col) -> int:
		return (self.getGraph()[row][col]).getDistance()
	def getType(self, row, col) -> int:
		return (self.getGraph()[row][col]).getType()
	def getInShort(self, row, col):
		return (self.getGraph()[row][col]).getInShort()

	# ReSetters
	def resetSource(self):
		self.source = None
	def resetDestination(self):
		self.destination = None

	# Set nodes which are in shortest as True	
	def setPath(self):
		prev = self.getDestination().getPrev()
		while prev != None:
			if prev.getType() != "Source":
				prev.setInShort()
			prev = prev.getPrev()
	
	# Reset whole game map
	def resetAll(self):
		self.resetSource()
		self.resetDestination()
		for row in self.getGraph():
			for eachNode in row:
				eachNode.reset()
	
	def clearWalls(self):
		for row in self.getGraph():
			for eachNode in row:
				if eachNode.getType() == "Wall":
					eachNode.reset()
	
	# Reset game to rerun with different walls or positions
	def resetForReRun(self):
		for row in self.getGraph():
			for eachNode in row:
				eachNode.resetReRun()

# Personal Queue class for easier queue management
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