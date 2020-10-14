#
# * Intro 60, Sudoku
# * Medium

# * Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid 
# * with digits so that each column, each row, and each of the nine 3 × 3 sub-
# * grids that compose the grid contains all of the digits from 1 to 9.

# * This algorithm should check if the given grid of numbers represents a correct 
# * solution to Sudoku.

# * Example

#     For

# grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
#         [4, 6, 5, 8, 7, 9, 3, 2, 1],
#         [7, 9, 8, 2, 1, 3, 6, 5, 4],
#         [9, 2, 1, 4, 3, 5, 8, 7, 6],
#         [3, 5, 4, 7, 6, 8, 2, 1, 9],
#         [6, 8, 7, 1, 9, 2, 5, 4, 3],
#         [5, 7, 6, 9, 8, 1, 4, 3, 2],
#         [2, 4, 3, 6, 5, 7, 1, 9, 8],
#         [8, 1, 9, 3, 2, 4, 7, 6, 5]]

# the output should be
# sudoku(grid) = true;

#     For

# grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
#         [4, 6, 5, 8, 7, 9, 3, 8, 1],
#         [7, 9, 8, 2, 1, 3, 6, 5, 4],
#         [9, 2, 1, 4, 3, 5, 8, 7, 6],
#         [3, 5, 4, 7, 6, 8, 2, 1, 9],
#         [6, 8, 7, 1, 9, 2, 5, 4, 3],
#         [5, 7, 6, 9, 8, 1, 4, 3, 2],
#         [2, 4, 3, 6, 5, 7, 1, 9, 8],
#         [8, 1, 9, 3, 2, 4, 7, 6, 5]]

# the output should be
# sudoku(grid) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer grid

#     A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

#     Guaranteed constraints:
#     grid.length = 9,
#     grid[i].length = 9,
#     1 ≤ grid[i][j] ≤ 9.

#     [output] boolean

#     true if the given grid represents a correct solution to Sudoku, false otherwise.

#%%

# * Solution 1
def sudoku1(grid:list)->bool:
    for i in range(9):
        if not checkRow(grid, i):
            return False
        if not checkCol(grid, i):
            return False

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not checkSubSquare(grid, i, j):
                return False
    
    return True


# * Helpers
def checkRow(grid:list, rowN :int)->bool:
    rowList= grid[rowN][:]
    for i in range(1, 10):
        if i not in rowList:
            return False
    
    return True


def checkCol(grid:list, colN:int)->bool:
    colList = [grid[x][colN] for x in range(9)]
    for i in range(1, 10):
        if i not in colList:
            return False
    
    return True


def checkSubSquare(grid:list, startR:int, startCol:int)->bool:
    subList = [grid[r][c] for r in range(startR, startR+3) for c in range(startCol, startCol+3)]
    for i in range(1, 10):
        if i not in subList:
            return False
    
    return True




a1 = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
      [4, 6, 5, 8, 7, 9, 3, 2, 1],
      [7, 9, 8, 2, 1, 3, 6, 5, 4],
      [9, 2, 1, 4, 3, 5, 8, 7, 6],
      [3, 5, 4, 7, 6, 8, 2, 1, 9],
      [6, 8, 7, 1, 9, 2, 5, 4, 3],
      [5, 7, 6, 9, 8, 1, 4, 3, 2],
      [2, 4, 3, 6, 5, 7, 1, 9, 8],
      [8, 1, 9, 3, 2, 4, 7, 6, 5]]

e1 = True
r1 = sudoku1(a1)
print('For {}, expected: {}, reuslt: {}'.format(a1, e1, r1))

a1 = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
      [4, 6, 5, 8, 7, 9, 3, 8, 1],
      [7, 9, 8, 2, 1, 3, 6, 5, 4],
      [9, 2, 1, 4, 3, 5, 8, 7, 6],
      [3, 5, 4, 7, 6, 8, 2, 1, 9],
      [6, 8, 7, 1, 9, 2, 5, 4, 3],
      [5, 7, 6, 9, 8, 1, 4, 3, 2],
      [2, 4, 3, 6, 5, 7, 1, 9, 8],
      [8, 1, 9, 3, 2, 4, 7, 6, 5]]

e1 = False
r1 = sudoku1(a1)
print('For {}, expected: {}, reuslt: {}'.format(a1, e1, r1))
# %%
