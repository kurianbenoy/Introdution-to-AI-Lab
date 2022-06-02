"""Function for map colouring"""
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isSafe(graph, color, v, c):
    # check the color of every adjacent vertex of `v`
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
    return True

def kColorable(g, color, k, v, n):
 
    # if all colors are assigned, print the solution
    if v == n:
        print([COLORS[color[v]] for v in range(n)])
        return 0
 
    # try all possible combinations of available colors
    for c in range(1, k + 1):
        # if it is safe to assign color `c` to vertex `v`
        if isSafe(g, color, v, c):
            # assign color `c` to vertex `v`
            color[v] = c
 
            # recur for the next vertex
            kColorable(g, color, k, v + 1, n)
 
            # backtrack
            color[v] = 0
    return None

if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    # edges = [(1, 2), (1, 3), (2, 3), (2, 5), (2, 4), (3, 5), (4, 5), (4, 6), (5,6)]
    edges = [(0, 1), (0, 2), (1, 2), (1, 4), (1, 3), (2, 4), (3, 4), (3, 5), (4,5)]
 
    # A list to store colors (can handle 10–colorable graph)
    COLORS = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE']
 
    # Set number of vertices in the graph
    n = 6
 
    # build a graph from the given edges
    g = Graph(edges, n)
 
    k = 3
 
    color = [None] * n
 
    # print all k–colorable configurations of the graph
    print(kColorable(g, color, k, 0, n) )

    # on experiment k = 3 is minimum value of colour configuration
    # for i in range(n):
    #     if(kColorable(g, color, i, 0, n) != None):
    #         print(i)
    #         break