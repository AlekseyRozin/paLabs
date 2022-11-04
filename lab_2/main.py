from myTree import *
from funcs import *
import time
import datetime

# генерация и вывод случайного решаемого пазла
puzzle = generatePuzzle()
#puzzle = [1,2,8,4,5,3,7,6,0]
puzzle = [1,2,3,4,5,6,0,7,8]
print("\nStart puzzle: ",puzzle)
print("-----------------------------------------------------------------------------------------")

start_node = Node(puzzle)
my_tree = MyTree(start_node)

start_time = time.time()
A_solution, A_iterations, AinMemory, AgeneratedStates = my_tree.A()

print("\n\nA solution: ",A_solution,"\n")
print("\n\nNumber of moves to solution with A algorithm: ",len(A_solution),"\n")
print("\n--- %s seconds to find the solution with A algorithm ---" % (time.time() - start_time),"\nNumber of iterations with A algorithm: ",A_iterations,"\n")
print("\nNumber of states in memory: ", AinMemory,"\n")
print("\nNumber of all generated states: ",AgeneratedStates,"\n\n")
print("-----------------------------------------------------------------------------------------")

time.sleep(2)
start_node_2 = Node(puzzle)
my_tree_2 = MyTree(start_node_2)
start_time_2 = time.time()
BFS_solution, BFS_iterations, BFSinMemory, BFSgeneratedStates = my_tree_2.BreadthFirstSearch()

print("\n\nBFS solution: ",BFS_solution,"\n")
print("\nNumber of moves to solution with BFS algorithm: ",len(BFS_solution),"\n")
print("\n--- %s seconds to find the solution with BFS algorithm ---" % (time.time() - start_time_2),"\nNumber of iterations with BFS algorithm: ",BFS_iterations,"\n")
print("\nNumber of states in memory: ", BFSinMemory,"\n")
print("\nNumber of all generated states: ",BFSgeneratedStates,"\n\n")
print("-----------------------------------------------------------------------------------------\n")