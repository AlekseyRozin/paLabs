from myNode import *

class MyTree:
    """Клас дерева пошуку"""
    def __init__(self,root):
        self.root = root

    def BreadthFirstSearch(self):
        pathToSolution = []
        openList = []
        iterations = 0
        stateCount = 0

        openList.append(self.root)
        goalFound = False

        while len(openList) > 0 and not goalFound:
            iterations += 1
            currNode = openList.pop(0)
            currNode.extendNode()
            stateCount += 4
            for child in currNode.children:
                if child.isGoal():
                    pathToSolution = self.pathTrace(child)
                    goalFound = True
                
                #if not self.contains(openList,child):
                openList.append(child)

        return pathToSolution[::-1], iterations, len(openList), stateCount
    

    def A(self):
        pathToSolution = []
        openList = []
        closedList = []
        iterations = 0
        stateCount = 0

        openList.append(self.root)
        goalFound = False

        while len(openList) > 0 and not goalFound:
            iterations += 1
            currNode = openList.pop(0)
            closedList.append(currNode)
            currNode.extendNode()
            stateCount += 4
            for child in currNode.children:
                if child.isGoal():
                    pathToSolution = self.pathTrace(child)
                    goalFound = True
                if not self.contains(closedList,child):
                    child.hVal = self.heuristic(child)
                    openList.append(child)
            openList.sort(key = lambda x:x.hVal,reverse=False)


        return pathToSolution[::-1], iterations, (len(openList) + len(closedList)), stateCount


    def contains(self, nodes, myNode):
        contains = False
        for node in nodes:
            if node.puzzle == myNode.puzzle:
                contains = True
                break
        return contains


    def heuristic(self,node):
        goal = [1,2,3,4,5,6,7,8,0]
        score = 0
        for i in range(9):
            if node.puzzle[i] != goal[i]:
                score += 1
        return score


    def pathTrace(self,currentNode):
        path = []
        path.append(currentNode.puzzle)

        while currentNode.parent != None:
            currentNode = currentNode.parent
            path.append(currentNode.puzzle)
        
        return path

