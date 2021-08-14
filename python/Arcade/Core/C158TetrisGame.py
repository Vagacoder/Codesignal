#
# * Core 158. Tetris Game
#

# * Let's play Tetris! But first we need to define the rules, especially since 
# * they probably differ from the way you've played Tetris before.

# There is an empty field with 20 rows and 10 columns, which is initially empty. 
# Random pieces appear on the field, each composed of four square blocks. You 
# can't change the piece's shape, but you can rotate it 90 degree clockwise 
# (possibly several times) and choose which columns it will appear within. Once 
# you've rotated the piece and have set its starting position, it appears at the 
# topmost row where you placed it and falls down until it can't fall any further. 
# The objective of the game is to create horizontal lines composed of 10 blocks. 
# When such a line is created, it disappears, and all lines above the deleted one 
# move down. The player receives 1 point for each deleted row.

# Your task is to implement an algorithm that places each new piece optimally. 
# The piece is considered to be placed optimally if:

#     The total number of blocks in the rows this piece will occupy after falling 
#       down is maximized;
#     Among all positions with that value maximized, this position requires the 
#       least number of rotations;
#     Among all positions that require the minimum number of rotations, this one 
#       is the leftmost one (i.e. the leftmost block's position is as far to the 
#       left as possible).

# The piece can't leave the field. It is guaranteed that it is always possible 
# to place the Tetris piece in the field.

# Implement this algorithm and calculate the number of points that you will get 
# for the given set of pieces.

# Example

# For

# pieces = [[[".", "#", "."], 
#            ["#", "#", "#"]],
#           [["#", ".", "."], 
#            ["#", "#", "#"]],
#           [["#", "#", "."], 
#            [".", "#", "#"]],
#           [["#", "#", "#", "#"]],
#           [["#", "#", "#", "#"]],
#           [["#", "#"], 
#            ["#", "#"]]]

# the output should be
# tetrisGame(pieces) = 1.

# For this explanation, we are representing each block by the index of the piece 
# it belongs to. After the first 5 blocks fall, the field looks like this:

# ...
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . 3 4
# . . . . . . . . 3 4
# . 0 . 1 . 2 2 . 3 4
# 0 0 0 1 1 1 2 2 3 4

# Note that the 0th, 1st, and 2nd pieces all fell down without rotating, while 
# the 3rd and the 4th pieces were rotated one time each.

# Since there is now a row composed of 10 blocks, it is deleted, and you get 1 
# point.

# When the last piece falls, the final field looks like this:

# ...
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# 5 5 . . . . . . 3 4
# 5 5 . . . . . . 3 4
# . 0 . 1 . 2 2 . 3 4

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.array.char pieces

#     A non-empty array of pieces in the order in which they fall. Each piece is 
#       represented as a rectangular matrix, where '#' represents a block and '.' 
#       represents an empty cell.

#     Each piece consists of 4 blocks, and each block shares a common side with 
#       at least one another block. It's guaranteed that each piece contains 
#       neither empty rows nor empty columns.

#     Guaranteed constraints:
#     3 ≤ pieces.length ≤ 30,
#     1 ≤ pieces[i].length ≤ 2,
#     2 ≤ pieces[i][j].length ≤ 4.

#     [output] integer

#     The number of points you will have by the end of the game.

#%%
import numpy

# * Solution 1, start ==========================================================
def tetrisGame(pieces: list) -> int:
    # ! original rotation function
    rot=lambda m:list(zip(*m[::-1]))

    # * my rotation function
    def rotate(matrix: list)-> list:
        return list(zip(*(matrix[::-1])))


    f = numpy.zeros((20,10))
    s = [0]*20
    res = 0

    for k,piece in enumerate(pieces):
        w=-1
        rd=-1
        rs=-1

        # * rotation 4 times
        for r in range(4):
            # * i: starting col #
            i = 0 
            while i <= 10 - len(piece[0]):
                c = 0
                j = 0
                while (not c) and j < 20 - len(piece):
                    j+=1
                    for n,line in enumerate(piece):
                        for m,x in enumerate(line):
                            if x=='#' and f[j+n][i+m]:
                                c = 1
                    j-=c
                o=sum(s[j:j+len(piece)])
                if o>w:
                    w,rd,rs = o,(i,j),r
                i+=1

            piece=rotate(piece)


        for _ in range(rs):
            piece=rotate(piece)

        bi,bj=rd
        for n,line in enumerate(piece):
            for m,x in enumerate(line):
                if x=='#':
                    f[bj+n][bi+m]=k+1
        s,nf=[*map(sum,f)],[]
        for n,s in enumerate(f):
            if all(s):
                res+=1
            else:
                nf.append(f[n])
        
        f=[[0]*10 for _ in range(20-len(nf))]+nf
        s=[*map(sum,f)]
    return res

# * Solution 1, end ============================================================

# * Solution 2, python 2 using class, start ====================================
class Piece():
    def __init__(self, piece):
        self.piece = piece

    @property
    def width(self):
        return len(self.piece[0])

    @property
    def height(self):
        return len(self.piece)

    # * key method: rotate the piece
    def rotate(self, times = 1):
        for i in range(times):
            self.piece = [row[::-1] for row in zip(*self.piece)]

    # * for debug
    def __str__(self):
       return '\n'.join(''.join(line) for line in self.piece)


# * class of board
class Board():
    def __init__(self):
        self.MAX_HEIGHT = 20
        self.MAX_WIDTH = 10
        self.board = [['.' for _ in range(self.MAX_WIDTH)] for __ in range(self.MAX_HEIGHT)]

    # * find lines which is full of '#', return its row index
    def completed_line(self):
        for i, line in enumerate(self.board):
            if line.count('.') == 0:
                yield i

    # * remove a line, and insert empty line at the top
    def clear_line(self, index):
        del self.board[index]
        self.board.insert(0, ['.' for _ in range(10)])

    # * find the row index when a piece dropped at offset
    def drop(self, piece, offset):
        last_level = self.MAX_HEIGHT - piece.height + 1 # ? why need + 1 for last_level?
        for level in range(last_level):
            for i in range(piece.height):
                for j in range(piece.width):                    
                    if self.board[level+i][offset+j] == "#" and piece.piece[i][j] == "#":
                        return level - 1
        return last_level - 1

    # * place a piece at pos(level, offset)
    def place_piece(self, piece, pos):
        level, offset = pos
        for i in range(piece.height):
            for j in range(piece.width):
                if piece.piece[i][j] == "#":
                    self.board[level+i][offset+j] = piece.piece[i][j]

    # * for debug
    def __str__(self):
       return '\n'.join(''.join(line) for line in self.board)


# * find the best position for single piece on the board
def find_best_position(board: Board, piece: Piece) -> list:
    result = []
    for rotation in range(4):
        for offset in range(board.MAX_WIDTH - piece.width + 1):        
            # * find the row index after dropping
            level = board.drop(piece, offset)
            # * count block '#' number in board
            blocks = sum([b.count('#') for b in board.board[level:level + piece.height]])
            result.append([blocks, rotation, offset, level])
        piece.rotate()

    # * The total number of blocks in the rows this piece will occupy after falling down is maximized;
    result = list(filter(lambda x: x[0] == max(result, key = lambda x: x[0])[0], result))
    # * Among all positions with that value maximized, this position requires the least number of rotations;
    result = list(filter(lambda x: x[1] == min(result, key = lambda x: x[1])[1], result))
    # * Among all positions that require the minimum number of rotations, this one is the leftmost one
    result = list(filter(lambda x: x[2] == min(result, key = lambda x: x[2])[2], result))[0]
    return result


def tetrisGame(pieces: list) -> int:
    board = Board()
    score = 0
    for p in pieces:
        piece = Piece(p)
        _, rotate, offset, level = find_best_position(board, piece)

        piece.rotate(rotate)
        board.place_piece(piece ,(level, offset))

        for i in board.completed_line():
            board.clear_line(i)
            score += 1

    return score


# * Solution 2, end ============================================================


p1 = [
      [[".", "#", "."], 
       ["#", "#", "#"]],
      [["#", ".", "."], 
       ["#", "#", "#"]],
      [["#", "#", "."], 
       [".", "#", "#"]],
      [["#", "#", "#", "#"]],
      [["#", "#", "#", "#"]],
      [["#", "#"], 
       ["#", "#"]]
     ]
r1 = tetrisGame(p1)
print(r1)


# %%
