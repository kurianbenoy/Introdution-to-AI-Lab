# Task 1 - 15 Puzzle problem using BFS Search Algorithm
# Very interesting problem - https://dev.to/lukegarrigan/what-is-bfs-breadth-first-search-nad
import collections

class graph:
    def __init__(self,adjacency=None):
        if adjacency is None:
            adjacency = {}
        self.adjacency = adjacency


