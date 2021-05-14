#
# * Core 126. Chess Bishop Dream
# * In ChessLand there is a small but proud chess bishop with a recurring dream. 
# * In the dream the bishop finds itself on an n × m chessboard with mirrors along 
# * each edge, and it is not a bishop but a ray of light. This ray of light moves 
# * only along diagonals (the bishop can't imagine any other types of moves even 
# * in its dreams), it never stops, and once it reaches an edge or a corner of 
# * the chessboard it reflects from it and moves on.

# Given the initial position and the direction of the ray, find its position after k steps where a step means either moving from one cell to the neighboring one or reflecting from a corner of the board.

# * Example

# For boardSize = [3, 7], initPosition = [1, 2],
# initDirection = [-1, 1], and k = 13, the output should be
# chessBishopDream(boardSize, initPosition, initDirection, k) = [0, 1].

# Here is the bishop's path:

# [1, 2] -> [0, 3] -(reflection from the top edge)-> [0, 4] -> 
# [1, 5] -> [2, 6] -(reflection from the bottom right corner)-> [2, 6] ->
# [1, 5] -> [0, 4] -(reflection from the top edge)-> [0, 3] ->
# [1, 2] -> [2, 1] -(reflection from the bottom edge)-> [2, 0] -(reflection from the left edge)->
# [1, 0] -> [0, 1]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer boardSize

#     An array of two integers, the number of rows and columns, respectively. Rows are numbered by integers from 0 to boardSize[0] - 1, columns are numbered by integers from 0 to boardSize[1] - 1 (both inclusive).

#     Guaranteed constraints:
#     1 ≤ boardSize[i] ≤ 20.

#     [input] array.integer initPosition

#     An array of two integers, indices of the row and the column where the bishop initially stands, respectively.

#     Guaranteed constraints:
#     0 ≤ initPosition[i] < boardSize[i].

#     [input] array.integer initDirection

#     An array of two integers representing the initial direction of the bishop. If it stands in (a, b), the next cell he'll move to is (a + initDirection[0], b + initDirection[1]) or whichever it'll reflect to in case it runs into a mirror immediately.

#     Guaranteed constraints:
#     initDirection[i] ∈ {-1, 1}.

#     [input] integer k

#     Guaranteed constraints:
#     1 ≤ k ≤ 109.

#     [output] array.integer

#     The position of the bishop after k steps.

#%%

# * Solution 1
# ! TLE
def chessBishopDream(boardSize: list, initPosition: list, initDirection: list, k: int)-> list:
    n = boardSize[0]
    m = boardSize[1]
    curP = initPosition

    # print(curP)

    for i in range(k):
        if ((curP[0] == 0 and initDirection[0] < 0) or (curP[0] == n-1 and initDirection[0] > 0)) \
            and ((curP[1] == 0 and initDirection[1] < 0) or (curP[1] == m-1 and initDirection[1] > 0)):
            initDirection = [-initDirection[0], -initDirection[1]]
        elif (curP[0] == 0 and initDirection[0] < 0) or (curP[0] == n-1 and initDirection[0] > 0):
            initDirection = [-initDirection[0], initDirection[1]]
            if initDirection[1] > 0:
                curP = [curP[0], curP[1]+1]
            else:
                curP = [curP[0], curP[1]-1]
        elif (curP[1] == 0 and initDirection[1] < 0) or (curP[1] == m-1 and initDirection[1] > 0):
            initDirection = [initDirection[0], -initDirection[1]]
            if initDirection[0] > 0:
                curP = [curP[0]+1, curP[1]]
            else:
                curP = [curP[0]-1, curP[1]]
        else:
            curP = [curP[0]+initDirection[0], curP[1]+initDirection[1]]
        # print(i)
        # print(initDirection)
        # print(curP)

    return curP


# * Solution 2
def chessBishopDream2(boardSize: list, initPosition: list, initDirection: list, k: int)-> list:
    n = boardSize[0]
    m = boardSize[1]
    result = [0, 0]
    
    # * Y axis
    fY = initPosition[0] + k * initDirection[0]
    if (fY // n)%2 == 0:
        result[0] = (fY % n + n) % n
    else:
        result[0] = (n-1) - (fY % n + n) % n
    
    # * X axis
    fX = initPosition[1] + k * initDirection[1]
    if (fX //m)%2 == 0:
        result[1] = (fX % m + m) % m
    else:
        result[1] = (m-1) - (fX % m + m) % m

    return result


# b1 = [3, 7]
# p1 = [1, 2]
# d1 = [-1, 1]
# k1 = 13
# r1 = chessBishopDream2(b1, p1, d1, k1)
# print(r1)

# b1 = [1, 1]
# p1 = [0, 0]
# d1 = [1, -1]
# k1 = 1000000000
# r1 = chessBishopDream2(b1, p1, d1, k1)
# print(r1)

b1 = [1, 2]
p1 = [0, 0]
d1 = [1, 1]
k1 = 6
r1 = chessBishopDream2(b1, p1, d1, k1)
print(r1)
