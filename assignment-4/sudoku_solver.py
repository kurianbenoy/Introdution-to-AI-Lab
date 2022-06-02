# Sudoku Solver - Assignment 4
# Runs in Python 3.10+
import numpy as np

def possible(y: int, x: int, n:int)-> bool:
    """The grid elements which when passing at position x & y the value n
    ie possible(4, 4, 3) = False
    ie possible(4, 4, 5) = True
    """
    global grid

    # accross all elements in y-axis, check if n exists
    for i in range(9):
        if grid[y][i] == n:
            return False
    
    # across all elements in x axis (vertically) to see if any elements has n
    for i in range(9):
        if grid[i][x] == n:
            return False

    x0 = (x//3) * 3
    y0 = (y//3) * 3

    # used to check in all elements of box of element grid if any element has n
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False

    # If no other conditions experience, then make it as True
    return True

def sudoku_solver()->None:
    """A 9* 9 sudokku puzzle solver, expecting grid as 9x9 value"""
    global grid

    for y in range(9):
        for x in range(9):
            # Find elements in all the row which are unfilled by 0
            if grid[y][x] == 0:
                # Now run a routine to fill this element to fill element between 1 - 9
                for n in range(1, 10):
                    # If possible returns True only Fill the function
                    if possible(y, x, n):
                        grid[y][x] = n
                        ## Recursssion, to run and find again
                        sudoku_solver()
                        # if our choice is always a bad solution we take it out and try againn
                        grid[y][x] = 0
                # if all choices are filled, we end up in return where there is 
                # no more elements to be filled
                return
    print(np.matrix(grid))
    input("More solution needed ??")

def solve_sudoku_min_heuristics()->None:
    """"A 9* 9 sudokku puzzle solver, expecting grid as 9x9 value
    to be solved with minimum values remaining heuristics approach
    """
    global grid

    # initialize a list to calcluate indexes of minimum values of grid-element to fill next
    min_heuristics = []
    min_val = 0
    

    for idx, sublist in enumerate(grid):
        # TODO: optimize method
        if(sublist.count(0)<=min_val):
            min_val = sublist.count(0)
            # insert at first of list
            min_heuristics.insert(0, idx)
        else:
            # insert at end of list
            min_heuristics.append(idx)

    for y in range(9):
        for x in min_heuristics:
            # Find elements in all the row which are unfilled by 0
            if grid[y][x] == 0:
                # Now run a routine to fill this element to fill element between 1 - 9
                for n in range(1, 10):
                    # If possible returns True only Fill the function
                    if possible(y, x, n):
                        grid[y][x] = n
                        ## Recursssion, to run and find again
                        sudoku_solver()
                        # if our choice is always a bad solution we take it out and try againn
                        grid[y][x] = 0
                # if all choices are filled, we end up in return where there is 
                # no more elements to be filled
                return
    print(np.matrix(grid))
    input("More solution needed ??")

if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print(solveSudoku(grid, row=0, col=0))
    sudoku_solver()
    solve_sudoku_min_heuristics()


## References

# 1. Python Sudoku Solver - Computerphile- https://youtu.be/G_UYXzGuqvM
