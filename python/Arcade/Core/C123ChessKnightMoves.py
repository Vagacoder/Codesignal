#
# * Core 123. Chess Knight Moves
# * Given a position of a knight on the standard chessboard, find the number of 
# * different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square 
# vertically, or two squares vertically and one square horizontally away from it. 
# The complete move therefore looks like the letter L. Check out the image below 
# to see all valid moves for a knight piece that is placed on one of the central 
# squares.

# * Example

#     For cell = "a1", the output should be
#     chessKnightMoves(cell) = 2.

#     For cell = "c2", the output should be
#     chessKnightMoves(cell) = 6.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string cell

#     String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

#     Guaranteed constraints:
#     cell.length = 2,
#     'a' ≤ cell[0] ≤ 'h',
#     1 ≤ cell[1] ≤ 8.

#     [output] integer

#%%

# * Solution 1
def chessKnightMoves(cell):
    line = ' abcdefgh'
    x = line.index(cell[0])
    y = int(cell[1])

    ds = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    count = 0
    for d in ds:
        if x+d[0]>0 and x+d[0]<9 and y+d[1]>0 and y+d[1]<9:
            count += 1

    return count


a1 = 'a1'
r1 = chessKnightMoves(a1)
print(r1)

a1 = 'c2'
r1 = chessKnightMoves(a1)
print(r1)
