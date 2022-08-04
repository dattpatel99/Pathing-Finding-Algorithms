import pygame
from constants import ROW_COMB, COL_COMB, ROW, COL

def aStarInsertionSort(ls: list, node, fNew):
    c = 0
    for each in ls:
        if each.getDistance() < fNew:
            c+=1
        else:
            break
    ls.insert(c, node)
    return ls

def drawRect(screen, color, startPosHor, startPosVer, horizontalWidth, verticalHeight):
    pygame.draw.rect(
        screen, color, [startPosHor, startPosVer, horizontalWidth, verticalHeight]
    )

# # FIXME: For Future, Trial general neighbour function
# def findNeighbours(graph: list, curNode: Node, rowComb: list,colComb: list):
#     neighbours = []
#     for i in range(len(rowComb)):
#         x_val = curNode.x + rowComb[i]
#         y_val = curNode.y + colComb[i]
#         if (x_val < 0 or x_val >= ROW) or (y_val < 0 or y_val >= COL):
#             pass
#         else:
#             possible_neigh = graph[x_val][y_val]
#             if(checkNeighbour(possible_neigh)):
#                 neighbours.append(possible_neigh)
#     return neighbours

# Check if node can be a successor
def checkNeighbour(neigh):
    if (neigh.getType() != "Wall" and neigh.getVisited() != True):
        return True
    return False