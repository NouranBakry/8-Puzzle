from State import State
from Solver import Solver
import time

puzzle =  [1, 2, 0, 3, 4, 5, 6, 7, 8]
puzzle0 = [6, 1, 8, 4, 0, 2, 7, 3, 5]
puzzle1 = [1, 2, 3, 4, 5, 0, 6, 7, 8]
puzzle2 = [1, 2, 5, 3, 4, 0, 6, 7, 8]
puzzle3 = [0, 1, 3, 4, 2, 5, 7, 8, 6]
puzzle4 = [8, 3, 5, 4, 1, 6, 2, 7, 0]
puzzle5 = [2, 8, 3, 1, 0, 5, 4, 7, 6]
puzzle6 = [8, 0, 6, 5, 4, 7, 2, 3, 1]
puzzle7 = [1, 2, 3, 4, 8, 0, 7, 6, 5]
game = State(puzzle)
search = Solver(game)
start_time = time.time()
queue = search.bfs()
# print('time taken:', time.time()-start_time)
stack = search.dfs()
heap1 = search.astar_manh()
heap2 = search.astar_euc()
print('time taken:', time.time()-start_time)