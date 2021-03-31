#
# * Core 107, Minesweeper
# * Medium

# * In the popular Minesweeper game you have a board with some mines and those 
# * cells that don't contain a mine have a number in it that indicates the total 
# * number of mines in the neighboring cells. Starting off with some arrangement 
# * of mines we want to create a Minesweeper game setup.

# * Example

# For

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]

# the output should be

# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]

# Check out the image below for better understanding:

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.boolean matrix

#     A non-empty rectangular matrix consisting of boolean values - true if the 
#       corresponding cell contains a mine, false otherwise.

#     Guaranteed constraints:
#     2 ≤ matrix.length ≤ 100,
#     2 ≤ matrix[0].length ≤ 100.

#     [output] array.array.integer

#     Rectangular matrix of the same size as matrix each cell of which contains 
#       an integer equal to the number of mines in the neighboring cells. Two 
#       cells are called neighboring if they share at least one corner.

#%%

# * Solution 1
def minesweeper(matrix: list)-> list:
    n = len(matrix)
    m = len(matrix[0])

    def countMine(y:int, x:int)->int:
        count = 0
        #* top row
        if y!=0:
            # * top left
            if x!=0 and matrix[y-1][x-1]:
                count += 1
            # * top center
            if matrix[y-1][x]:
                count += 1
            # * top right
            if x!=m-1 and matrix[y-1][x+1]:
                count += 1
        # * bottom row
        if y!=n-1:
            # * bottom left
            if x!=0 and matrix[y+1][x-1]:
                count += 1
            # * bottom center
            if matrix[y+1][x]:
                count += 1
            # * bottom right
            if x!=m-1 and matrix[y+1][x+1]:
                count += 1
        # * center row
        # * center left
        if x!=0 and matrix[y][x-1]:
            count += 1
        # * center right
        if x!=m-1 and matrix[y][x+1]:
            count += 1

        return count

    result = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[i][j] = countMine(i, j)

    return result


m1 = [[True, False, False],
      [False, True, False],
      [False, False, False]]
r1 = minesweeper(m1)
print(r1)
