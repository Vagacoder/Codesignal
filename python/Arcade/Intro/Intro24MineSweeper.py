#
# * Intro 24. Mine Sweeper
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
# https://codesignal.s3.amazonaws.com/tasks/minesweeper/img/example.png?_tm=1582043430722

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.boolean matrix

#     A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

#     Guaranteed constraints:
#     2 ≤ matrix.length ≤ 100,
#     2 ≤ matrix[0].length ≤ 100.

#     [output] array.array.integer

#     Rectangular matrix of the same size as matrix each cell of which contains 
#     an integer equal to the number of mines in the neighboring cells. Two cells 
#     are called neighboring if they share at least one corner.


#%%

# * Solution 1
def minesweeper1(matrix: list) -> list:
    rowN = len(matrix)
    colN = len(matrix[0])

    result = [[0]*colN for _ in range(rowN)]
    # print(result)
    for r in range(rowN):
        for c in range(colN):
            result[r][c] = checkMine(matrix, r, c)

    return result


def checkMine(matrix:list, r, c):
    rowN = len(matrix)
    colN = len(matrix[0])

    rowRange=[r-1, r, r+1]
    colRange=[c-1, c, c+1]

    rowRange = list(filter(lambda x : x >=0 and x < rowN, rowRange))
    colRange = list(filter(lambda x: x>=0 and x < colN, colRange))

    count = 0;
    for rI in rowRange:
        for cI in colRange:
            if rI == r and cI == c:
                continue
            if matrix[rI][cI]:
                count+=1

    return count


# * Solution 2
def minesweeper2(matrix):
    r = []
    
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            # ! SMART, if there is mine, count is set to -1, if no mine, still 0
            count = -matrix[i][j]
            # print('count', count)
            # ! count all 9 grids, if[i][j] has mine, count+= 1, balanced with last step
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        count += matrix[i+x][j+y]

            r[i].append(count)
    
    return r


a1 = [[True, False, False],
      [False, True, False],
      [False, False, False]]
e1 = [[1, 2, 1],
      [2, 1, 1],
      [1, 1, 1]]
r1 = minesweeper2(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))




# ? Tester for helper
# checkMine(a1, 0, 0)
# checkMine(a1, 0, 1)
# checkMine(a1, 0, 2)
# print()
# checkMine(a1, 1, 0)
# checkMine(a1, 1, 1)
# checkMine(a1, 1, 2)
# print()
# checkMine(a1, 2, 0)
# checkMine(a1, 2, 1)
# checkMine(a1, 2, 2)

# %%
