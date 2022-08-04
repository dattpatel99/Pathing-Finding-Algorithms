# Node class
from constants import MX_DIST, ROW_A_COMB, COL_A_COMB,COL_COMB,ROW_COMB, ROW, COL
from utils import checkNeighbour
'''
Note to self: Distance is distacne for DJK and f for A*
'''

class Node (object):
    def __init__(self, posx: int, posy: int):
        self.x = posx
        self.y = posy
        self.visited = False
        self.previousNode = None
        self.type = "Open"
        self.inShort = False
        self.distance = MX_DIST
        self.g = MX_DIST
        self.h = MX_DIST

    # Mutators
    def setDistance(self, dis):
        self.distance = dis
    def setType(self, newType):
        self.type = newType
    def setVisited(self):
        self.visited = True
    def setPrev(self, prev):
        self.previousNode = prev
    def setInShort(self):
        self.inShort = True
    def setG(self,g):
        self.g = g
    def setH(self,h):
        self.h = h

    # Accessors
    def getDistance(self) -> float:
        return self.distance
    def getType(self):
        return self.type
    def getVisited(self) -> bool:
        return self.visited
    def getPrev(self):
        return self.previousNode
    def getInShort(self):
        return self.inShort
    def getPosition(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def getG(self) -> float:
        return self.g
    def getH(self)-> float:
        return self.h
    
# Reset Node attributes
    def reset(self):
        self.visited = False
        self.previousNode = None
        self.type = "Open"
        self.inShort = None
        self.distance = MX_DIST
        self.h = MX_DIST
        self.g = MX_DIST
    
# Reset to rerun game with same positions or different walls
# FIXME: Implement reset of distance, g, and h based on type
    def resetReRun(self):
        self.visited = False
        self.previousNode = None
        self.inShort = None
# Find valid neighbours for A* algo
    def findNeighboursAStar(self, graph: list) -> list:
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
# Find valid neighbours for DJK algo
    def findNeighboursDJK(self, graph: list) -> list:
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
# Initiate the A Star source object
    def initiateAStarSource(self):
        self.setDistance(0.0)
        self.setG(0.0)
        self.setH(0.0)