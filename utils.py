import pygame
from constants import ROW_COMB, COL_COMB, ROW, COL

def drawRect(screen, color, startPosHor, startPosVer, horizontalWidth, verticalHeight):
    pygame.draw.rect(
        screen, color, [startPosHor, startPosVer, horizontalWidth, verticalHeight]
    )


class Node (object):
    def __init__(self, posx: int, posy: int):
        self.x = posx
        self.y = posy
        self.visited = False
        self.previousNode = None
        self.type = None
        self.inShort = False
    # Mutators
    def setType(self, newType):
        self.type = newType

    def setVisited(self):
        self.visited = True

    def setPrev(self, prev):
        self.previousNode = prev

    def setInShort(self):
        self.inShort = True
    # Accessors
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
                if (
                    possible_neigh.getType() != "Wall"
                    and possible_neigh.getVisited() != True
                ):
                    neighbours.append(possible_neigh)
        return neighbours
