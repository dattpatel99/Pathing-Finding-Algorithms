from cmath import sqrt
from AStar import Astar

def initiateAStarSource(node: Astar):
    node.setF(0.0)
    node.setG(0.0)
    node.setH(0.0)

def caluclateG(prevG: float):
    return 1.0 + prevG
def caluclateH(curNode, dest):
    something = (curNode.x - dest.x)**2 + (curNode.y - dest.y)**2
    return sqrt(something)
def caluclateF(g: float, h: float):
    return (g + h)