#
# * Intro 50, Chess Knight
# * Medium

# * Given a position of a knight on the standard chessboard, find the number of 
# * different moves the knight can perform.

# * The knight can move to a square that is two squares horizontally and one square 
# * vertically, or two squares vertically and one square horizontally away from it. 
# * The complete move therefore looks like the letter L. Check out the image below 
# * to see all valid moves for a knight piece that is placed on one of the central 
# * squares.


# * Example

#     For cell = "a1", the output should be
#     chessKnight(cell) = 2.

#     For cell = "c2", the output should be
#     chessKnight(cell) = 6.

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
def chessKnight1(cell: str)-> int:
    row = int(cell[1])
    col = ord(cell[0]) - ord('a')+1

    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

    count = 0
    for m in moves:
        if 0<(row + m[0]) <9 and 0<(col + m[1]) < 9:
            count +=1

    return count

# * Solution 2
def chessKnight2(cell: str)->int:
    col = ord(cell[0]) - ord('a')+1
    row = int(cell[1])

    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    return sum([(0<(row + m[0]) <9 and 0<(col + m[1]) < 9) for m in moves])


a1 = 'a1'
e1 = 2
r1 = chessKnight2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1,r1))

# %%
