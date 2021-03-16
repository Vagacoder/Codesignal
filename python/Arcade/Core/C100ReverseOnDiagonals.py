#
# * Core 100, Reverse on Diagonals
# * Easy

# * The longest diagonals of a square matrix are defined as follows:

#     the first longest diagonal goes from the top left corner to the bottom right one;
#     the second longest diagonal goes from the top right corner to the bottom left one.

# Given a square matrix, your task is to reverse the order of elements on both of 
# its longest diagonals.

# * Example

# For

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# the output should be

# reverseOnDiagonals(matrix) = [[9, 2, 7],
#                               [4, 5, 6],
#                               [3, 8, 1]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer matrix

#     Guaranteed constraints:
#     1 ≤ matrix.length ≤ 100,
#     matrix.length = matrix[i].length,
#     1 ≤ matrix[i][j] ≤ 105.

#     [output] array.array.integer

#     Matrix with the order of elements on its longest diagonals reversed.

#%%

# * Solution 1
def reverseOnDiagonals(matrix: list)-> list:
    n = len(matrix)
    for i in range(n//2):
        j = n - 1 - i
        matrix[i][i], matrix[j][j] = matrix[j][j], matrix[i][i]
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


a1 = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
r1 = reverseOnDiagonals(a1)
print(r1)
