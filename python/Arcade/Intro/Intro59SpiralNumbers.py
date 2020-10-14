#
# * Intro 59, Spiral Numbers
# * Medium

# * Construct a square matrix with a size N × N containing integers from 1 to N 
# * * N in a spiral order, starting from top-left and in clockwise direction.

# * Example

# For n = 3, the output should be

# spiralNumbers(n) = [[1, 2, 3],
#                     [8, 9, 4],
#                     [7, 6, 5]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Matrix size, a positive integer.

#     Guaranteed constraints:
#     3 ≤ n ≤ 100.

#     [output] array.array.integer


#%%

# * Solution 1
def spiralNumbers1(n:int)->list:
    result = [[0]*n for i in range(n)]
    spiralNumbersBorder(result, 0, 1)
    print(result)
    return result


# * Helper
def spiralNumbersBorder(matrix:list, startLocation:int, startNumber: int):
    n = len(matrix)
    if startLocation >= n/2:
        return 

    endLocation = n-1-startLocation
    # * top line
    for i in range(startLocation, endLocation+1):
        matrix[startLocation][i] = startNumber
        startNumber +=1

    # * right line
    for i in range(startLocation+1, endLocation+1):
        matrix[i][endLocation] = startNumber
        startNumber +=1

    # * bottom line
    for i in range(endLocation-1, startLocation-1, -1):
        matrix[endLocation][i] = startNumber
        startNumber += 1

    # * left line
    for i in range(endLocation-1, startLocation, -1):
        matrix[i][startLocation] = startNumber
        startNumber += 1

    spiralNumbersBorder(matrix, startLocation+1, startNumber)


# * Solution 2
# ! Smart!
def spiralNumbers2(n:int):
    matrix = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, count = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            matrix[x][y] = count
            count += 1
    return matrix

a1 = 3
e1 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
r1 = spiralNumbers2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))



# %%
