#
# * Core 110, Polygon Perimeter
# * Medium

# * You have a rectangular white board with some black cells. The black cells 
# * create a connected black figure, i.e. it is possible to get from any black 
# * cell to any other one through connected adjacent (sharing a common side) black 
# * cells.

# Find the perimeter of the black figure assuming that a single cell has unit length.

# It's guaranteed that there is at least one black cell on the table.

# * Example

#     For

#     matrix = [[false, true,  true ],
#               [true,  true,  false],
#               [true,  false, false]]

#     the output should be
#     polygonPerimeter(matrix) = 12.

#     For

#     matrix = [[true, true,  true],
#             [true, false, true],
#             [true, true,  true]]

#     the output should be
#     polygonPerimeter(matrix) = 16.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.boolean matrix

#     A matrix of booleans representing the rectangular board where true means a 
#       black cell and false means a white one.

#     Guaranteed constraints:
#     2 ≤ matrix.length ≤ 5,
#     2 ≤ matrix[0].length ≤ 5.

#     [output] integer

#%%

# * Solution 1
def polygonPerimeter(matrix: list)-> int:
    n = len(matrix)
    m = len(matrix[0])
    counts = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                # * check up
                if i == 0:
                    counts += 1
                elif not matrix[i-1][j]:
                    counts += 1
                # * check down
                if i == n-1:
                    counts += 1
                elif not matrix[i+1][j]:
                    counts += 1
                # * check left
                if j == 0:
                    counts += 1
                elif not matrix[i][j-1]:
                    counts += 1
                if j == m-1:
                    counts += 1
                elif not matrix[i][j+1]:
                    counts += 1

    return counts


m1 = [[False, True,  True ],
      [True,  True,  False],
      [True,  False, False]]
r1 = polygonPerimeter(m1)
print(r1)

m1 = [[True,  True,  True ],
      [True,  False, True],
      [True,  True,  True]]
r1 = polygonPerimeter(m1)
print(r1)
