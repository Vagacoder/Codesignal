#
# * Core 109, Coutours Shifting
# * Medium

# * Mark got a rectangular array matrix for his birthday, and now he's thinking about all the fun things he can do with it. He likes shifting a lot, so he decides to shift all of its i-contours in a clockwise direction if i is even, and counterclockwise if i is odd.

# Here is how Mark defines i-contours:

#     the 0-contour of a rectangular array as the union of left and right columns as well as top and bottom rows;
#     consider the initial matrix without the 0-contour: its 0-contour is the 1-contour of the initial matrix;
#     define 2-contour, 3-contour, etc. in the same manner by removing 0-contours from the obtained arrays.

# Implement a function that does exactly what Mark wants to do to his matrix.

# * Example

#     For

#     matrix = [[ 1,  2,  3,  4],
#                [ 5,  6,  7,  8],
#                [ 9, 10, 11, 12],
#                [13, 14, 15, 16],
#                [17, 18, 19, 20]]

#     the output should be

#     contoursShifting(matrix) = [[ 5,  1,  2,  3],
#                                  [ 9,  7, 11,  4],
#                                  [13,  6, 15,  8],
#                                  [17, 10, 14, 12],
#                                  [18, 19, 20, 16]]

#     For matrix = [[238, 239, 240, 241, 242, 243, 244, 245]],
#     the output should be
#     contoursShifting(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]].

#     Note, that if a contour is represented by a 1 × n array, its center is considered to be below it.

#     For

#     matrix = [[238],
#                [239],
#                [240],
#                [241],
#                [242],
#                [243],
#                [244],
#                [245]]

#     the output should be

#     contoursShifting(matrix) = [[245],
#                                  [238],
#                                  [239],
#                                  [240],
#                                  [241],
#                                  [242],
#                                  [243],
#                                  [244]]

#     If a contour is represented by an n × 1 array, its center is considered to be to the left of it.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer matrix

#     Guaranteed constraints:
#     1 ≤ matrix.length ≤ 100,
#     1 ≤ matrix[i].length ≤ 100,
#     1 ≤ matrix[i][j] ≤ 1000.

#     [output] array.array.integer

#     The given matrix with its contours shifted.

#%%

# * Solution 1
def contoursShifting(matrix: list)-> list:
    n = len(matrix)
    m = len(matrix[0])
    result = [[0]*m for _ in range(n)]
    
    if n == 1:
        result = [[matrix[0][-1]] + matrix[0][0:-1]]
    elif m == 1:
        result = [matrix[-1]] + matrix[0:-1]
    else:
        maxC = min(n,m)//2
        extraC = min(n,m) - maxC*2
        # print(maxC)
        # print(extraC)
        for c in range(maxC):
            # * contour even number
            if c%2 == 0:
                # * left col
                for i in range(c+1, n-c):
                    result[i-1][c] = matrix[i][c]
                # * bottom row
                for i in range(c+1, m-c):
                    result[n-1-c][i-1] = matrix[n-1-c][i]
                # * right col
                for i in range(n-1-c, c, -1):
                    result[i][m-1-c] = matrix[i-1][m-1-c]
                # * top row
                for i in range(m-1-c, c, -1):
                    result[c][i] = matrix[c][i-1]
            # * contour odd number
            else:
                # * top row
                for i in range(c, m-1-c):
                    result[c][i] = matrix[c][i+1]
                # * right col
                for i in range(c, n-1-c):
                    result[i][m-1-c] = matrix[i+1][m-1-c]
                # * bottom row
                for i in range(m-1-c, c, -1):
                    result[n-1-c][i] = matrix[n-1-c][i-1]
                # * left col
                for i in range(n-1-c, c, -1):
                    result[i][c] = matrix[i-1][c]

        if extraC > 0:
            # * extra row
            if n < m:
                i = maxC
                j = maxC
                endJ = m - maxC -1
                temp = matrix[i][j]
                while j < endJ:
                    result[i][j] = matrix[i][j+1]
                    j+=1
                result[i][j] = temp
            # * extra col
            else:
                j = maxC
                i = maxC
                endI = n - maxC -1
                temp = matrix[i][j]
                while i < endI:
                    result[i][j] = matrix[i+1][j]
                    i+=1
                result[i][j] = temp
    return result


# m1 = [[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12],
#         [13, 14, 15, 16],
#         [17, 18, 19, 20]]
# r1 = contoursShifting(m1)
# print(r1)

m1 = [[238, 239, 240, 241, 242, 243, 244, 245]]
r1 = contoursShifting(m1)
print(r1)

# m1 = [[238],
#     [239],
#     [240],
#     [241],
#     [242],
#     [243],
#     [244],
#     [245]]
# r1 = contoursShifting(m1)
# print(r1)

m1 = [[1,2,3], 
      [6,7,8], 
      [11,12,13], 
      [16,17,18], 
      [21,22,23], 
      [24,25,26]]
r1 = contoursShifting(m1)
print(r1)

# m1 = [[1,2,3,4,5], 
#       [6,7,8,9,10], 
#       [11,12,13,14,15]]
# r1 = contoursShifting(m1)
# print(r1)
