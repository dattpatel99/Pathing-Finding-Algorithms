from utils import aStarInsertionSort
from AStar import Astar
def testInsertion():
    a = Astar()
    a.setF(1.0)
    b = Astar()
    b.setF(3.0)
    c = Astar()
    c.setF(5.0)
    d = Astar()
    d.setF(2.0)
    ls = [a,b,c]

    assert [a,d,b,c] == aStarInsertionSort(ls, d)

testInsertion()