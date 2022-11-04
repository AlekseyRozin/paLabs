import random

def generatePuzzle():
    puzzle = [1,2,3,4,5,6,7,8,0];
    random.shuffle(puzzle)
    while not isSolvable(puzzle):
        random.shuffle(puzzle)
    return puzzle


def isSolvable(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i+1,len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def heuristic(puzzle):
        goal = [1,2,3,4,5,6,7,8,0]
        score = 0
        for i in range(9):
            if puzzle[i] != goal[i]:
                score += 1
        return score