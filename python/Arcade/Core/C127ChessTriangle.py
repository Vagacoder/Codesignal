#
# * Core 127. Chess Triangle
# * 

# Consider a bishop, a knight and a rook on an n × m chessboard. They are said to 
# form a triangle if each piece attacks exactly one other piece and is attacked 
# by exactly one piece. Calculate the number of ways to choose positions of the 
# pieces to form a triangle.

# Note that the bishop attacks pieces sharing the common diagonal with it; the 
# rook attacks in horizontal and vertical directions; and, finally, the knight 
# attacks squares which are two squares horizontally and one square vertically, 
# or two squares vertically and one square horizontally away from its position.

# * Example

# For n = 2 and m = 3, the output should be
# chessTriangle(n, m) = 8.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     1 ≤ n ≤ 40.

#     [input] integer m

#     Guaranteed constraints:
#     1 ≤ m ≤ 40,
#     3 ≤ n · m.

#     [output] integer

#%%

# * Solution 1
# ! Wrong
def chessTriangle(n: int, m: int)-> int:
    yH = n-2+1
    xH = m-3+1
    H = yH*xH
    yV = n-3+1
    xV = m-2+1
    V = yV*xV
    return max((H+V)*8, 0)


# * Solution 2
# ? in every 2x3 space, there are 2 configurations possible, with reflections and rotations multiplying that by 4
# ? in every 2x4 space, there are an additional 2 configurations possible, with reflections and rotations multiplying that by 4
# ? in every 3x3 space, there are an additional 2 configurations possible up to rotations and reflection
# ? in every 3x4 space, there are an additional 2 configurations possible up to rotation and reflection
def chessTriangle2(n, m):
    m0 = lambda x:max(0,x)

    return 8*(m0(m-1)*m0(n-2)+m0(m-2)*m0(n-1)+m0(m-1)*m0(n-3)+m0(m-3)*m0(n-1)+2*m0(m-2)*m0(n-2)+m0(m-2)*m0(n-3)+m0(m-3)*m0(n-2))


# * Solution 3
def chessTriangle3(n, m):

    # Triangles fit in boxes of dimensions (2,3), (2,4), (3, 3), (3, 4).
    # Each triangle has 4 reflections within the bounding box, and two orientations.
    triangleSizes = [ (2, 3), (3, 2), (2, 4), (4, 2), (3, 3), (3, 3), (3, 4), (4, 3) ]
    count = 0
    
    for x, y in triangleSizes:
        if x <= n and y <= m:
            count += (1 + n - x) * (1 + m - y)
    
    return 8 * count


n1 = 2
m1 = 3
r1 = chessTriangle2(n1, m1)
print(r1)

n1 = 1
m1 = 30
r1 = chessTriangle2(n1, m1)
print(r1)

n1 = 2
m1 = 2
r1 = chessTriangle2(n1, m1)
print(r1)

n1 = 3
m1 = 3
r1 = chessTriangle2(n1, m1)
print(r1)
