# 8-Puzzle Solver
Created this project for my Artificial Intelligence course.
The puzzle consists of an area divided into a grid, 3 by 3 for the 8-puzzle. On each grid
square is a tile, expect for one square which remains empty. Thus, there are eight tiles in
the 8-puzzle. A tile that is next to the empty grid square can be moved into the empty space,
leaving its previous position empty in turn. Tiles are numbered, 1 through 8 for the 8-puzzle, so
that each tile can be uniquely identified.


The aim of the puzzle is to achieve an ordered configuration of tiles from a given (different)
configuration by sliding the individual tiles around the grid as described above.

Data structures used:
  To implement BFS we use a queue to simulate horizontal expansion of nodes, to
explore the breadth of a vertex depth before moving on. This behavior guarantees
that the first path located is one of the shortest-paths present.
  To implement DFS we use a stack to simulate depth traversal, to explore possible
vertices (from a supplied root) down each branch before backtracking. Below is a
listing of the actions performed upon each visit to a node:
    Mark the current vertex as being visited.
    Explore each adjacent vertex that is not included in the visited set.
Algorithms used:
  Breadth-First Search
Starts at the tree root and explores the neighbor nodes first, before moving to the next level
neighbors.
  Depth-First Search
Starts at the root and explores as far as possible along each branch before backtracking.
Informed Search: A* Search algorithm was used using manhattan's distance heuristic and Euclidean's distance heuristic.
