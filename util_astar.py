from math import hypot
from AStar import Astar

def initiateAStarSource(node: Astar):
    node.setF(0.0)
    node.setG(0.0)
    node.setH(0.0)

def caluclateG(prevG: float):
    return 1.0 + prevG
def caluclateH(curNode, dest):
    a = curNode.x - dest.x
    b = curNode.y - dest.y
    return hypot(a,b)
def caluclateF(g: float, h: float):
    return (g + h)