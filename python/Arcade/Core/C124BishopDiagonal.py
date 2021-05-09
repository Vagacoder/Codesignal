#
# * Core 124. Bishop Diagonal
# * In the Land Of Chess, bishops don't really like each other. In fact, when two 
# * bishops happen to stand on the same diagonal, they immediately rush towards 
# * the opposite ends of that same diagonal.

# Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

# * Example

#     For bishop1 = "d7" and bishop2 = "f5", the output should be
#     bishopDiagonal(bishop1, bishop2) = ["c8", "h3"].

#     For bishop1 = "d8" and bishop2 = "b5", the output should be
#     bishopDiagonal(bishop1, bishop2) = ["b5", "d8"].

#  The bishops don't belong to the same diagonal, so they don't move.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string bishop1

#     Coordinates of the first bishop in chess notation.

#     Guaranteed constraints:
#     bishop1.length = 2,
#     'a' ≤ bishop1[0] ≤ 'h',
#     1 ≤ bishop1[1] ≤ 8.

#     [input] string bishop2

#     Coordinates of the second bishop in the same notation.

#     Guaranteed constraints:
#     bishop2.length = 2,
#     'a' ≤ bishop2[0] ≤ 'h',
#     1 ≤ bishop2[1] ≤ 8.

#     [output] array.string

#     Coordinates of the bishops in lexicographical order after they check the diagonals they stand on.

#%%

# * Solution 1
def bishopDiagonal(bishop1, bishop2):
    line = ' abcdefgh'
    x1 = line.index(bishop1[0])
    y1 = int(bishop1[1])
    x2 = line.index(bishop2[0])
    y2 = int(bishop2[1])

    print(x1, y1, x2, y2)

    if abs(x1-x2) != abs(y1-y2):
        return sorted([bishop1, bishop2])
    else:
        sx = min(x1, x2)
        lx = max(x1, x2)
        sy = min(y1, y2)
        ly = max(y1, y2)

        print()

        if x1-x2 == y1-y2:
            lInc = min((8-lx), (8-ly))
            lx += lInc
            ly += lInc
            sDec = min((sx-1), (sy-1))
            sx -= sDec
            sy -= sDec
            print(lx, ly, sx, sy)
            return sorted([(line[lx] + str(ly)), (line[sx] + str(sy))])
        else:   
            lInc = min((8-lx), (sy-1))
            lx += lInc
            sy -= lInc
            sDec = min((sx-1), (8-ly))
            sx -= sDec
            ly += sDec
            print(lx, sy, sx, ly)
            return sorted([(line[lx] + str(sy)), (line[sx] + str(ly))])


a1 = 'd7'
a2 = 'f5'
r1 = bishopDiagonal(a1, a2)
print(r1)

a1 = 'd8'
a2 = 'b5'
r1 = bishopDiagonal(a1, a2)
print(r1)

a1 = 'a1'
a2 = 'h8'
r1 = bishopDiagonal(a1, a2)
print(r1)
