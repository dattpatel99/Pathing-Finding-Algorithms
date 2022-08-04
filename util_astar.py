from math import hypot
from node import Node

def caluclateG(prevG: float):
    return 1.0 + prevG

def caluclateH(curNode, dest):
    a = curNode.x - dest.x
    b = curNode.y - dest.y
    return hypot(a,b)

def caluclateF(g: float, h: float):
    return (g + h)