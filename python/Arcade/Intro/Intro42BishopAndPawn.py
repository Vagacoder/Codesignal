#
# * Intro 42, Bishop and Pawn
# * Easy

# * Given the positions of a white bishop and a black pawn on the standard chess 
# * board, determine whether the bishop can capture the pawn in one move.

# * The bishop has no restrictions in distance for each move, but is limited to 
# * diagonal movement. Check out the example below to see how it can move:

# https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/bishop.jpg?_tm=1581997207350

# * Example

#   For bishop = "a1" and pawn = "c3", the output should be
#   bishopAndPawn(bishop, pawn) = true.

# https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/ex1.jpg?_tm=1581997207686

# For bishop = "h1" and pawn = "h3", the output should be
# bishopAndPawn(bishop, pawn) = false.

# https://codesignal.s3.amazonaws.com/tasks/bishopAndPawn/img/ex2.jpg?_tm=1581997207976

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string bishop

#     Coordinates of the white bishop in the chess notation.

#     Guaranteed constraints:
#     bishop.length = 2,
#     'a' ≤ bishop[0] ≤ 'h',
#     1 ≤ bishop[1] ≤ 8.

#     [input] string pawn

#     Coordinates of the black pawn in the same notation.

#     Guaranteed constraints:
#     pawn.length = 2,
#     'a' ≤ pawn[0] ≤ 'h',
#     1 ≤ pawn[1] ≤ 8.

#     [output] boolean

#     true if the bishop can capture the pawn, false otherwise.

#%%

# * Solution 1
def bishopAndPawn1(bishop: str, pawn: str)-> bool:
    dict1 = {
        'a':1, 'b':2, 'c':3, 'd':4,
        'e':5, 'f':6, 'g':7, 'h':8
    }

    bCol = dict1[bishop[0]]
    bRow = int(bishop[1])

    pCol = dict1[pawn[0]]
    pRow = int(pawn[1])

    if abs(bRow-pRow) == abs(bCol-pCol):
        return True
    else:
        return False


# * Solution 2
def bishopAndPawn2(bishop: str, pawn: str)-> bool:
    bCol = ord(bishop[0])
    bRow = int(bishop[1])

    pCol = ord(pawn[0])
    pRow = int(pawn[1])

    if abs(bRow-pRow) == abs(bCol-pCol):
        return True
    else:
        return False



a1 = 'a1'
a2 = 'c3'
e1 = True
r1 = bishopAndPawn2(a1, a2)
print('For {},{}, expected: {}, result: {}'.format(a1, a2, e1, r1))

a1 = 'h1'
a2 = 'h3'
e1 = False
r1 = bishopAndPawn2(a1, a2)
print('For {},{}, expected: {}, result: {}'.format(a1, a2, e1, r1))
# %%
