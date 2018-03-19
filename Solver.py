from collections import deque
from Frontier import Frontier
from functools import cmp_to_key
import math
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def goal_test(state):
    if state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return 1


def trace_path(state):
    path = []
    while state.parent:
        child = state
        state = state.parent
        child_index = child.value.index(0)
        parent_index = state.value.index(0)
        if child_index is not parent_index:
            difference = child_index - parent_index
            if difference == -3:
                path.append('up')
            elif difference == 3:
                path.append('down')
            elif difference == -1:
                path.append('left')
            else:
                path.append('right')
    path.reverse()
    print('path:', path)


def print_goal_from_parent(state):
    goal_path = [state.value]
    depth = state.depth
    while state.parent:
        state = state.parent
        goal_path.append(state.value)
    goal_path.reverse()
    print(goal_path)
    print('depth:', depth)
    print('cost :', goal_path.__len__())


class Solver:

    def __init__(self, state):
        self.state = state
        self.puzzle = self.state.value

    def bfs(self):
        initial_state = self.state
        frontier = deque()
        frontier.append(self.state)
        print('BFS:')
        explored = set()
        nodes_expanded = 0
        # print('frontier', frontier)
        # print('explored', explored)
        while frontier:
            # print('frontier', frontier)
            position = frontier.popleft()
            print('State POPPED FROM FRONTIER')
            print(position)
            if goal_test(position.value):
                print("===================================================")
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                trace_path(position)
                return 'success'

            explored.add(position)
            # print('explored:', explored)
            neighbours = position.generate_neighbours()
            nodes_expanded = nodes_expanded + len(neighbours)
            # print('new neighbours', neighbours)

            for neighbour in neighbours:
                neighbour_puzzle = neighbour.value
                if not (any(neighbour_puzzle == state.value for state in frontier) or any(neighbour_puzzle == state.value for state in explored)):
                    frontier.append(neighbour)

    def dfs(self):
        print('\nDFS:')
        stack = [self.state]
        explored = set()
        nodes_expanded = 0
        # print('explored', explored)
        while stack:
            # print('stack', stack)
            position = stack.pop()
            print('Popped from Stack')
            print(position)
            if goal_test(position.value):
                print("======================================================")
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                trace_path(position)
                return 'success'

            explored.add(position)
            # print('explored:', explored)
            neighbours = position.generate_neighbours()
            nodes_expanded = nodes_expanded + len(neighbours)
            # print('new neighbours', neighbours)

            for neighbour in neighbours:
                neighbour_puzzle = neighbour.value
                if not (any(neighbour_puzzle == state.value for state in stack) or any(neighbour_puzzle == state.value for state in explored)):
                    stack.append(neighbour)

    def astar_euc(self):

        print('\nA* by Euclidean heuristic:')
        heap = [self.state]
        # heap.append(self.state)
        nodes_expanded = 0
        explored = set()

        while heap:
            heap.sort(key=cmp_to_key(cmpfn))
            position = heap.pop(0)
            print('Popped from Heap')
            print(position)
            if goal_test(position.value):
                print("=======================================")
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                trace_path(position)
                return 'success'

            explored.add(position)

            neighbours = position.generate_neighbours()
            nodes_expanded = nodes_expanded + len(neighbours)
            for neighbour in neighbours:
                neighbour_puzzle = neighbour.value
                if not (any(neighbour_puzzle == state.value for state in heap) or any(neighbour_puzzle == state.value for state in explored)):
                    heap.append(neighbour)

    def astar_manh(self):

        print('\nA* by Manhattan heuristic  : ')
        heap = [self.state]
        nodes_expanded = 0
        explored = set()
        while heap:
            heap.sort(key=cmp_to_key(cmparfn))
            position = heap.pop(0)
            print('Popped from Heap')
            print(position)
            if goal_test(position.value):
                print("=============================================")
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                trace_path(position)
                return 'success'

            explored.add(position)

            neighbours = position.generate_neighbours()
            nodes_expanded = nodes_expanded + len(neighbours)
            for neighbour in neighbours:
                neighbour_puzzle = neighbour.value
                if not (any(neighbour_puzzle == state.value for state in heap) or any(neighbour_puzzle == state.value for state in explored)):
                    heap.append(neighbour)


def cmparfn(x, y):        # f(n)=g(n)+h(n)
    return (x.depth + manhattan( x.value)) - (y.depth + manhattan(y.value))


def manhattan(state):    # h(n)
    h = sum(abs(x % 3 - g % 3) + abs(x//3 - g//3) for x, g in ((state.index(i), goal.index(i)) for i in range(1, 9)))
    return h


def cmpfn(x, y):     # f(n)=g(n)+h(n)
    return (x.depth + euclidean(x.value)) - (y.depth + euclidean(y.value))


def euclidean(state): #h(n)
    h=math.sqrt(sum(abs(x%3 - g%3)**2+ abs(x//3 - g//3)**2  for x,g in ((state.index(i) , goal.index(i)) for i in range(1, 9))))
    return h
