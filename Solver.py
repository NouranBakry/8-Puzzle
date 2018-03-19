from collections import deque
import math
from heapq import heappush, heappop

#   This defines the goal state that the puzzle desires to reach.
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]


#   This function traces the moves made along the path to reach the goal state.
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


#   This function traces the path from the final state back to the parent state and
#   prints the path taken and the depth of the graph.

def print_goal_from_parent(state):
    goal_path = [state.value]
    depth = state.depth
    while state.parent:
        state = state.parent
        goal_path.append(state.value)
    goal_path.reverse()
    print(goal_path)
    print('depth:', depth)
    print('moves:', len(goal_path) - 1)


""" This class performs all the search operations. BFS, DFS and A* with both manhattan's and
    euclidean's heuristic. """


class Solver:

    def __init__(self, state):
        self.state = state
        self.puzzle = self.state.value

    def bfs(self):
        queue = deque()
        frontier = set()
        queue.append(self.state)
        frontier.add(self.state.hash_value)
        explored = set()
        nodes_expanded = depth = 0
        while queue:
            position = queue.popleft()
            frontier.remove(position.hash_value)
            if position.value == goal:
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                trace_path(position)
                print('max depth:', depth)
                return 'success'

            explored.add(position.hash_value)
            neighbours = position.generate_neighbours()
            nodes_expanded += 1

            for neighbour in neighbours:
                if not (neighbour.hash_value in frontier or neighbour.hash_value in explored):
                    depth = max(depth, neighbour.depth)
                    queue.append(neighbour)
                    frontier.add(neighbour.hash_value)

    def dfs(self):
        stack = deque()
        frontier = set()
        stack.append(self.state)
        frontier.add(self.state.hash_value)
        explored = set()
        nodes_expanded = depth = 0
        while stack:
            position = stack.pop()
            frontier.remove(position.hash_value)
            if position.value == goal:
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                print('max depth:', depth)
                trace_path(position)
                return 'success'

            explored.add(position.hash_value)
            neighbours = position.generate_neighbours()
            neighbours.reverse()
            nodes_expanded += 1
            for neighbour in neighbours:
                if not (neighbour.hash_value in frontier or neighbour.hash_value in explored):
                    depth = max(depth, neighbour.depth)
                    stack.append(neighbour)
                    frontier.add(neighbour.hash_value)

    def astar_manh(self):
        heap = []
        heappush(heap, (manhattan_distance(self.state), self.state))
        keys = dict()
        keys[self.state.hash_value] = self.state
        nodes_expanded = depth = 0
        explored = set()

        while heap:
            score, position = heappop(heap)
            del keys[position.hash_value]
            explored.add(position.hash_value)

            if position.value == goal:
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                print('max depth:', depth)
                trace_path(position)
                return 'success'
            neighbours = position.generate_neighbours()
            nodes_expanded += 1
            for neighbour in neighbours:
                if not (neighbour.hash_value in keys or neighbour.hash_value in explored):
                    heappush(heap, (manhattan_distance(neighbour) + neighbour.depth, neighbour))
                    depth = max(neighbour.depth, depth)
                    keys[neighbour.hash_value] = neighbour
                elif neighbour.hash_value in keys:
                    node = keys[neighbour.hash_value]
                    if manhattan_distance(neighbour) < manhattan_distance(node):
                        node.parent = position
                        node.depth = neighbour.depth

    def astar_euc(self):
        heap = []
        heappush(heap, (euclidean_distance(self.state), self.state))
        keys = dict()
        keys[self.state.hash_value] = self.state
        nodes_expanded = depth = 0
        explored = set()

        while heap:
            score, position = heappop(heap)
            del keys[position.hash_value]
            explored.add(position.hash_value)

            if position.value == goal:
                print_goal_from_parent(position)
                print('nodes expanded:', nodes_expanded)
                print('max depth:', depth)
                trace_path(position)
                return 'success'
            neighbours = position.generate_neighbours()
            nodes_expanded += 1
            for neighbour in neighbours:
                if not (neighbour.hash_value in keys or neighbour.hash_value in explored):
                    heappush(heap, (euclidean_distance(neighbour) + neighbour.depth, neighbour))
                    depth = max(neighbour.depth, depth)
                    keys[neighbour.hash_value] = neighbour
                elif neighbour.hash_value in keys:
                    node = keys[neighbour.hash_value]
                    if euclidean_distance(neighbour) < euclidean_distance(node):
                        node.parent = position
                        node.depth = neighbour.depth


#   calculates manhattan's distance h(n)
def manhattan_distance(state):
        puzzle = state.value
        dist = 0
        for i, val in enumerate(puzzle):
            if val == 0:
                continue

            goal_y, goal_x = val // 3, val % 3
            y, x = i // 3, i % 3
            dist += abs(goal_y-y) + abs(goal_x-x)
        return dist


#   calculates euclidean's distance h(n)
def euclidean_distance(state):
        puzzle = state.value
        dist = 0
        for i, val in enumerate(puzzle):
            if val == 0:
                continue

            goal_y, goal_x = val // 3, val % 3
            y, x = i // 3, i % 3
            dist += math.sqrt(abs(goal_y-y)**2 + abs(goal_x-x)**2)
        return dist
