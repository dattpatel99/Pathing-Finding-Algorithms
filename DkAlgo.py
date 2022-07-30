from utils import Node
from constants import INFITY

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