from multiprocessing.pool import INIT
from node import Node
from utils import checkNeighbour
from constants import INFITY, ROW_A_COMB, COL_A_COMB, ROW, COL, MX_FLT
'''
Need Node to have an g and h value. IF value of found g' is less than g or h' less than h replace.
f = g + h
Check all nodes and choose node with minimum
Node == cell space
'''

class Astar(Node):
    def __init__(self, posx:int, posy:int):
        self.dist = INFITY
        self.f = MX_FLT
        self.g = MX_FLT
        self.h = MX_FLT
        self.open = False
        Node.__init__(self, posx, posy)

# Mutators
    def setDist(self, val: int):
        self.dist = val
    def setG(self,g):
        self.g = g
    def setF(self,f):
        self.f = f
    def setH(self,h):
        self.h = h
    def setOpen(self, op: bool):
        self.open = op
# Accessors
    def getDist(self)-> int:
        return self.dist
    def getOpen(self):
        return self.open
    def getG(self):
        return self.g
    def getF(self):
        return self.f
    def getH(self):
        return self.h

# Behaviors
# Reset the node attributes
    def reset(self):
        self.dist = INFITY
        self.visited = False
        self.previousNode = None
        self.type = None
        self.inShort = None
        self.f = MX_FLT
        self.h = MX_FLT
        self.g = MX_FLT
        self.open = False

    def findNeighbours(self, graph: list) -> list:
        neighbours = []
        for i in range(len(ROW_A_COMB)):
            x_val = self.x + ROW_A_COMB[i]
            y_val = self.y + COL_A_COMB[i]
            if (x_val < 0 or x_val >= ROW) or (y_val < 0 or y_val >= COL):
                pass
            else:
                possible_neigh = graph.getGraph()[x_val][y_val]
                if(checkNeighbour(possible_neigh)):
                    neighbours.append(possible_neigh)
        return neighbours