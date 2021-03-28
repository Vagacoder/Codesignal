#
# * Core 106. Sudoku
# * Medium

# * Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

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

# The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
# These examples are represented on the image below.

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
def sudoku(grid: list)-> bool:
    nums = [1,2,3,4,5,6,7,8,9]

    # * checkout whether a row contains 1-9
    def checkRow(row: list)-> bool:
        for num in nums:
            if num not in row:
                return False
        return True

    # * convert cols to rows
    newGrid = list(zip(*grid))  

    # * 
    def getSmallGrid(x: int, y: int)-> list:
        smallGrid = []
        for i in range(3):
            smallGrid.append(grid[y+i][x+0])
            smallGrid.append(grid[y+i][x+1])
            smallGrid.append(grid[y+i][x+2])
        return smallGrid

    for i in range(9):
        # * Check row
        if not checkRow(grid[i]):
            return False
        # * check col
        if not checkRow(newGrid[i]):
            return False

        # * check small grids
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                smallGrid = getSmallGrid(y, x)
                for num in nums:
                    if num not in smallGrid:
                        return False

    return True


# * Solution 2
def sudoku2(grid):
    nine = set(range(1,10))
    
    def row(i):
        return set(grid[i])
    
    def col(j):
        return set(grid[i][j] for i in range(9))
    
    def cell(o):
        return set(grid[o - o % 3 + i // 3][(o % 3)*3 + i % 3] for i in range(9))
    
    return all(nine == row(i) == col(i) == cell(i) for i in range(9))



grid1 = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
r1 = sudoku(grid1)
print(r1)


grid2 = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
r2 = sudoku(grid2)
print(r2)