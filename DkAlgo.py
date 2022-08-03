from node import Node
from utils import checkNeighbour
from constants import INFITY, ROW_COMB, COL_COMB, ROW, COL

'''
InShort == is node in shortest path?
value = distance from source
'''

class DKNode(Node) :
	def __init__(self,posx: int,posy: int, value: int):
		self.dist = value
		Node.__init__(self, posx, posy)

	# Reset the node attributes
	def reset(self):
		self.dist = INFITY
		self.visited = False
		self.previousNode = None
		self.type = None
		self.inShort = None
	
	# Reset for rerun
	def resetReRun(self):
		self.dist = INFITY
		self.visited = False
		self.previousNode = None
		self.inShort = None
	
	# Setters
	def setDist(self, val: int):
		self.dist = val	
	
	# Getters
	def getDist(self)-> int:
		return self.dist
	
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
				if (checkNeighbour(possible_neigh)):
					neighbours.append(possible_neigh)
		return neighbours
