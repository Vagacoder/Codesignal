#
# * Intro 55, Different Squares
# * Medium

# * Given a rectangular matrix containing only digits, calculate the number of 
# * different 2 × 2 squares in it.

# * Example

# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]

# the output should be:

#   differentSquares(matrix) = 6.

# Here are all 6 different 2 × 2 squares:

#     1 2
#     2 2

#     2 1
#     2 2

#     2 2
#     2 2

#     2 2
#     1 2

#     2 2
#     2 3

#     2 3
#     2 1

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer matrix

#     Guaranteed constraints:
#     1 ≤ matrix.length ≤ 100,
#     1 ≤ matrix[i].length ≤ 100,
#     0 ≤ matrix[i][j] ≤ 9.

#     [output] integer

#     The number of different 2 × 2 squares in matrix.

#%%

# * Solution 1
def differentSquares1(matrix: list)->int:
    squares = set()
    rowN = len(matrix)
    colN = len(matrix[0])

    for i in range(rowN-1):
        for j in range(colN-1):
            # ! list is NOT hashable, using tuple
            squares.add(getSubSqaure(matrix, i, j))


    return len(squares)


# * helper
def getSubSqaure(m: list, i:int, j:int)->tuple:
    return ((m[i][j], m[i][j+1]),(m[i+1][j], m[i+1][j+1]))




a1 = [[1, 2, 1], [2, 2, 2], [2, 2, 2], [1, 2, 3], [2, 2, 1]]
# print(getSubSqaure(a1, 3,1))
e1 = 6
r1 = differentSquares1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))


# %%
