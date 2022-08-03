# Node class
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

