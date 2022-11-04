class Node:
    """Клас вузла дерева"""
    def __init__(self,puzzle):
        self.children = []
        self.parent = None
        self.puzzle = puzzle
        self.zeroInd = self.puzzle.index(0)
    
    def isGoal(self):
        return self.puzzle == [1,2,3,4,5,6,7,8,0]

    def moveToRight(self):
        if self.zeroInd != 2 and self.zeroInd != 5 and self.zeroInd != 8:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd+1] = newPuzzle[self.zeroInd+1], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    def moveToLeft(self):
        if self.zeroInd != 0 and self.zeroInd != 3 and self.zeroInd != 6:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd-1] = newPuzzle[self.zeroInd-1], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    def moveToUp(self):
        if self.zeroInd > 2:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd-3] = newPuzzle[self.zeroInd-3], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    def moveToDown(self):
        if self.zeroInd < 6:
            newPuzzle = self.puzzle.copy()
            newPuzzle[self.zeroInd], newPuzzle[self.zeroInd+3] = newPuzzle[self.zeroInd+3], newPuzzle[self.zeroInd]
            newNode = Node(newPuzzle)
            newNode.parent = self
            self.children.append(newNode)

    def extendNode(self):
        self.moveToRight()
        self.moveToLeft()
        self.moveToUp()
        self.moveToDown()

