#
# * Core 119. Rows Rearranging
# * Given a rectangular matrix of integers, check if it is possible to rearrange 
# * its rows in such a way that all its columns become strictly increasing sequences 
# * (read from top to bottom).

# * Example

#     For

#     matrix = [[2, 7, 1], 
#               [0, 2, 0], 
#               [1, 3, 1]]

#     the output should be
#     rowsRearranging(matrix) = false;

#     For

#     matrix = [[6, 4], 
#               [2, 2], 
#               [4, 3]]

#     the output should be
#     rowsRearranging(matrix) = true.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer matrix

#     A 2-dimensional array of integers.

#     Guaranteed constraints:
#     1 ≤ matrix.length ≤ 10,
#     1 ≤ matrix[0].length ≤ 10,
#     -300 ≤ matrix[i][j] ≤ 300.

#     [output] boolean

#%%

# * Solution 1
def rowsRearranging1(matrix: list)-> bool:
    n = len(matrix)
    m = len(matrix[0])

    def checkMatrix(ma:list)-> bool:
        for j in range(m):
            for i in range(1, n):
                if ma[i][j]<= ma[i-1][j]:
                    return False
        return True


    for k in range(m):
        matrix.sort(key=lambda x : x[k])
        if checkMatrix(matrix):
            return True

    return False


a1 = [[2, 7, 1], 
      [0, 2, 0], 
      [1, 3, 1]]
r1 = rowsRearranging1(a1)
print(r1)

a1 = [[6, 4], 
      [2, 2], 
      [4, 3]]
r1 = rowsRearranging1(a1)
print(r1)
