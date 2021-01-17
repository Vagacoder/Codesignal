#
# * Core 64. Different Square
# * Medium

# * Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# * Example

# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]

# the output should be
# differentSquares(matrix) = 6.

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
def differentSquares(matrix:list)->int:
    collections = set()
    n = len(matrix)
    m = len(matrix[0])

    for i in range(0, n-1):
        for j in range(0, m-1):
            curMatrix = (
                (matrix[i][j],   matrix[i][j+1]),
                (matrix[i+1][j], matrix[i+1][j+1])
               )
            collections.add(curMatrix)
    
    return len(collections)



a1 =  [[1, 2, 1],
    [2, 2, 2],
    [2, 2, 2],
    [1, 2, 3],
    [2, 2, 1]]
r1 = differentSquares(a1)
print(r1)
