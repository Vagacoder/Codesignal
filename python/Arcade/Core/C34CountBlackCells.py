#
# * Core 34, Count Black Cells
# * Medium

# * magine a white rectangular grid of n rows and m columns divided into two parts 
# * by a diagonal line running from the upper left to the lower right corner. Now 
# * let's paint the grid in two colors according to the following rules:

#     A cell is painted black if it has at least one point in common with the diagonal;
#     Otherwise, a cell is painted white.

# Count the number of cells painted black.

# * Example

# For n = 3 and m = 4, the output should be
# countBlackCells(n, m) = 6.

#     There are 6 cells that have at least one common point with the diagonal and 
#       therefore are painted black.

# For n = 3 and m = 3, the output should be
# countBlackCells(n, m) = 7.

#     7 cells have at least one common point with the diagonal and are painted black.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     The number of rows.

#     Guaranteed constraints:
#     1 ≤ n ≤ 105.

#     [input] integer m

#     The number of columns.

#     Guaranteed constraints:
#     1 ≤ m ≤ 105.

#     [output] integer

#     The number of black cells.

#%%
import math

# * Solution 1
# * Check every grid, O(n^2)
# ! TLE error
def countBlackCells1(n, m):
    n, m = (min(n,m), max(n, m))
    k = n/m
    count = 0
    for i in range(m):
        ki = k * i
        ki1 = k * (i+1)
        for j in range(n):
            if j <= ki <= (j+1):
                count += 1
            elif j <= ki1 <= (j+1):
                count += 1

    return count


# * Solution 2
# * Check every column, O(n)
def countBlackCells2(n, m):
    k = n/m
    count = 0
    for i in range(m):
        ki = k * i
        ki1 = k * (i+1)
        count += (math.floor(ki1+1) - math.ceil(ki-1))

    return count-2

# * Solution 3
# ! Mathematics, O(1)
from fractions import gcd

def countBlackCells3(n, m):
    return m + n + gcd(m,n) - 2



n1 = 3
m1 = 4
r1 = countBlackCells2(n1, m1)
print('e: 6, a:{}'.format(r1))

n1 = 3
m1 = 3
r1 = countBlackCells2(n1, m1)
print('e: 7, a:{}'.format(r1))

n1 = 4
m1 = 3
r1 = countBlackCells2(n1, m1)
print('e: 6, a:{}'.format(r1))

n1 = 2
m1 = 5
r1 = countBlackCells2(n1, m1)
print('e: 6, a:{}'.format(r1))

n1 = 5
m1 = 2
r1 = countBlackCells2(n1, m1)
print('e: 6, a:{}'.format(r1))