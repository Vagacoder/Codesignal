#
# * Core 129. Pawn Race

# * Pawn race is a game for two people, played on an ordinary 8 × 8 chessboard. 
# * The first player has a white pawn, the second one - a black pawn. Initially 
# * the pawns are placed somewhere on the board so that the 1st and the 8th rows 
# * are not occupied. Players take turns to make a move.

# White pawn moves upwards, black one moves downwards. The following moves are 
# allowed:

#     one-cell move on the same vertical in the allowed direction;
#     two-cell move on the same vertical in the allowed direction, if the pawn is 
#       standing on the 2nd (for the white pawn) or the 7th (for the black pawn) 
#       row. Note that even with the two-cell move a pawn can't jump over the 
#       opponent's pawn;
#     capture move one cell forward in the allowed direction and one cell to the 
#       left or to the right.

# The purpose of the game is to reach the the 1st row (for the black pawn) or the 
# 8th row (for the white one), or to capture the opponent's pawn.

# Given the initial positions and whose turn it is, determine who will win or 
# declare it a draw (i.e. it is impossible for any player to win). Assume that 
# the players play optimally.

# * Example

#     For white = "e2", black = "e7", and toMove = 'w', the output should be
#     pawnRace(white, black, toMove) = "draw";
#     For white = "e3", black = "d7", and toMove = 'b', the output should be
#     pawnRace(white, black, toMove) = "black";
#     For white = "a7", black = "h2", and toMove = 'w', the output should be
#     pawnRace(white, black, toMove) = "white".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string white
#     Coordinates of the white pawn in the chess notation.

#     [input] string black
#     Position of the black pawn in the same notation. It is guaranteed that white ≠ black.

#     [input] char toMove
#     'w' if it is the first player's turn, 'b' otherwise.

#     [output] string
#     "white", "black" or "draw" depending on the result of the game.


#%%

# * Solution 1
def pawnRace(white: str, black: str, toMove: str) -> str:
    line = ' abcdefgh'

    def move(location: str, side: str)->str:
        if side == 'w':
            if location[1] == 2:
                return location[0] + str(int(location[1]))
    
    # * same col
    if white[0] == black[0]:
        if int(black[1]) <= int(white[1]):
            pass
        else:
            return 'draw'

    # * next cols
    if abs(line.index(white[0]) - line.index(black[0])) == 1:
        # * no capture
        if int(black[1]) <= int(white[1]):
            pass

        # * 1 row, Ok
        elif int(black[1]) - int(white[1]) == 1:
            if toMove == 'w':
                return 'white'
            else:
                return 'black'
        
        # * 2 rows, Ok
        elif int(black[1]) - int(white[1]) == 2:
            if toMove == 'w':
                return 'black'
            else:
                return 'white'
        
        # * 5 rows 
        elif abs(int(white[1]) - int(black[1])) == 5:
            if toMove == 'w':
                return 'black'
            else:
                return 'white'
        
        # * other odd rows, exculde 1, 5 rows
        elif abs(int(white[1]) - int(black[1]))%2 == 1:
            if toMove == 'w':
                return 'white'
            else:
                return 'black'
        # * even rows, exclude 0, 2 rows
        elif abs(int(white[1]) - int(black[1]))%2 == 0:
            if toMove == 'w':
                if white[1] != '2':
                    return 'black'
                else:
                    return 'white'
            else:
                if black[1] != '7':
                    return 'white'
                else:
                    return 'black'

    # * racing, not same col, or not next cols, or next cols without capture
    whiteSteps = 8 - int(white[1])
    if white[1] == '2':
        whiteSteps -= 1
    
    blackSteps = int(black[1]) - 1
    if black[1] == '7':
        blackSteps -= 1
    
    if toMove == 'w':
        if whiteSteps <= blackSteps:
            return 'white'
        else:
            return 'black'
    else:
        if blackSteps <= whiteSteps:
            return 'black'
        else:
            return 'white'



# w1 = 'e2'
# b1 = 'e7'
# t1 = 'w'
# r1 = pawnRace(w1, b1, t1)
# print(r1)

# w1 = 'a7'
# b1 = 'h2'
# t1 = 'w'
# r1 = pawnRace(w1, b1, t1)
# print(r1)

# w1 = 'e3'
# b1 = 'd7'
# t1 = 'b'
# r1 = pawnRace(w1, b1, t1)
# print(r1)

# w1 = 'g2'
# b1 = 'f2'
# t1 = 'b'
# r1 = pawnRace(w1, b1, t1)
# print(r1)

w1 = 'c2'
b1 = 'd7'
t1 = 'b'
r1 = pawnRace(w1, b1, t1)
print(r1)