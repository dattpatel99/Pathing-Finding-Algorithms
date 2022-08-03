import pygame
from constants import ROW_COMB, COL_COMB, ROW, COL
from node import Node

def aStarInsertionSort(ls: list, node):
    ls.append(node)
    # Traverse through 1 to len(arr)
    i = len(ls)-1
    key = ls[i]
    j = i-1
    while j >= 0 and key.getF() < ls[j].getF():
        ls[j + 1] = ls[j]
        j -= 1
    ls[j + 1] = key
    return ls

def drawRect(screen, color, startPosHor, startPosVer, horizontalWidth, verticalHeight):
    pygame.draw.rect(
        screen, color, [startPosHor, startPosVer, horizontalWidth, verticalHeight]
    )

# FIXME: For Future, Trial general neighbour function
def findNeighbours(graph: list, curNode: Node, rowComb: list,colComb: list):
    neighbours = []
    for i in range(len(rowComb)):
        x_val = curNode.x + rowComb[i]
        y_val = curNode.y + colComb[i]
        if (x_val < 0 or x_val >= ROW) or (y_val < 0 or y_val >= COL):
            pass
        else:
            possible_neigh = graph[x_val][y_val]
            if(checkNeighbour(possible_neigh)):
                neighbours.append(possible_neigh)
    return neighbours

# Check if node can be a successor
def checkNeighbour(neigh: Node):
    if (neigh.getType() != "Wall" and neigh.getVisited() != True):
        return True
    return False