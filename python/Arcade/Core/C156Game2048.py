#
# * Core 156, Game 2048

# You are most likely familiar with the game 2048.

# 2048 is played on a gray 4 × 4 grid with numbered tiles that slide smoothly when a player moves them using one of the four arrow keys - Up, Down, Left or Right. On every turn, a new tile with a value of either 2 or 4 randomly appears on an empty spot of the board. After one of the keys is pressed, the tiles slide as far as possible in the chosen direction until they are stopped either by another tile or by the edge of the grid. If two tiles with the same number collide while moving, they merge into a tile with this number doubled. You can't merge an already merged tile in the same turn. If there are more than 2 tiles in the same row (column) that can merge, the farthest (closest to an edge) pair will be merged first (see the second example).

# In this problem you are not going to solve the 2048 puzzle, but you are going to find the final state of the board from the given one after a defined set of n arrow key presses, assuming that no new random tiles will appear on the empty spots.

# The following example shows the next state of the board after pressing Right.

# This example shows the next state of the board after pressing Down.

# For more details you can visit http://gabrielecirulli.github.io/2048/ and play 
# online 😃

# You are given a matrix 4 × 4 which corresponds to the 2048 game grid. grid[0][0] 
# corresponds to the upper left tile of the grid. Each element of the grid is 
# equal to some power of 2 if there is a tile with that value in the corresponding 
# position, and 0 if it corresponds to the empty spot.

# You are also given a sequence of key presses as a string path. Each character 
# of the string equals L, R, U, or D corresponding to Left, Right, Up or Down 
# respectively.

# Please note that in some cases after pressing an arrow key nothing will be changed.

# Example

# For

# grid = [[0, 0, 0, 0],
#         [0, 0, 2, 2],
#         [0, 0, 2, 4],
#         [2, 2, 4, 8]]

# and path = "RR", the output should be

# game2048(grid, path) = [[0, 0, 0, 0],
#                         [0, 0, 0, 4],
#                         [0, 0, 2, 4],
#                         [0, 0, 8, 8]]

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer grid

#     A square matrix of size 4 × 4, the starting state of the board. Each value 
#       of the matrix is 0 a power of 2.

#     Guaranteed constraints:
#     grid[i][j] ∈ {0} ∪ {2i | i = 0, 1, ..., 16}.

#     [input] string path

#     String representing key presses. Each character of the string equals L, R, 
#       U, or D.

#     Guaranteed constraints:
#     1 ≤ path.length ≤ 30.

#     [output] array.array.integer

#     The final state of the board after the given key presses are applied.

#%%

def game2048(grid: list, path: str) -> list:

    N = 4

    # * 1, moving left
    def moveL():
        def stackL(row: list):
            row = [x for x in row if x != 0]
            for j in range(N-len(row)):
                row.append(0)
            return row

        for i in range(N):
            # * 1, stack tiles
            grid[i] = stackL(grid[i])

            # * 2, merge tiles
            for j in range(N-1):
                if grid[i][j] == grid[i][j+1]:
                    grid[i][j] *= 2
                    grid[i][j+1] = 0
                    # break

            # * 3, stack tiles again
            grid[i] = stackL(grid[i])  


    # * 2, moving up
    def moveU():
        def stackU(col: list):
            col = [x for x in col if x != 0]
            for j in range(N-len(col)):
                col.append(0)
            return col

        for j in range(N):
            col = [grid[0][j], grid[1][j], grid[2][j], grid[3][j]]
            # print(col)
            
            # * 1 stack tiles
            col = stackU(col)
            # print(col)

            # * 2 merge tiles
            for i in range(N-1):
                if col[i] == col[i+1]:
                    col[i] *= 2
                    col[i+1] = 0
                    # break
            
            # * 3 stack tiles again
            col = stackU(col)
            [grid[0][j], grid[1][j], grid[2][j], grid[3][j]] = col
            
            # print(grid)
            

        

    # * 3, moving right
    def moveR():
        def stackR(row: list):
            row = [x for x in row if x != 0]
            for j in range(N-len(row)):
                row.insert(0, 0)
            return row

        for i in range(N):
            # * 1, stack tiles
            grid[i] = stackR(grid[i])
            # print(grid)
            # print()

            # * 2, merge tiles
            for j in range(N-1, 0, -1):
                if grid[i][j] == grid[i][j-1]:
                    grid[i][j] *= 2
                    grid[i][j-1] = 0
                    # break
            # print(grid)

            # * 3, stack tiles again
            grid[i] = stackR(grid[i])  
            # print(grid)


    # * 4, moving down
    def moveD():
        def stackD(col: list):
            col = [x for x in col if x != 0]
            for j in range(N-len(col)):
                col.insert(0, 0)
            return col

        for j in range(N):
            col = [grid[0][j], grid[1][j], grid[2][j], grid[3][j]]
            # print(col)
            
            # * 1 stack tiles
            col = stackD(col)
            # print(col)

            # * 2 merge tiles
            for i in range(N-1, 0, -1):
                if col[i] == col[i-1]:
                    col[i] *= 2
                    col[i-1] = 0
                    # break
            
            # * 3 stack tiles again
            col = stackD(col)
            [grid[0][j], grid[1][j], grid[2][j], grid[3][j]] = col


    # * Directions:
    # * L: move left
    # * U: move up
    # * R: move right
    # * D: move down
    go = {
        'L': moveL,
        'U': moveU,
        'R': moveR,
        'D': moveD
    }
    
    # print(grid)

    # moveR()
    # moveL()
    # moveU()
    # moveD()

    for p in path:
        go[p]()


    # print(grid)
    return grid



# g1 = [[0, 0, 0, 0],
#       [0, 0, 2, 2],
#       [0, 0, 2, 4],
#       [2, 2, 4, 8]]
# p1 = 'RR'
# r1 = game2048(g1, p1)
# print(r1)

g1 = [[0,0,0,2], 
      [0,0,4,2], 
      [0,0,4,2], 
      [0,0,4,2]]
p1 = 'D'
r1 = game2048(g1, p1)
print(r1)

# %%
