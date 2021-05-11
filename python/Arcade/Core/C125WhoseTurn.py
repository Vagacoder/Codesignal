#
# * Core 125. Whose Turn?
#

# * Imagine a standard chess board with only two white and two black knights 
# * placed in their standard starting positions: the white knights on b1 and g1; 
# * the black knights on b8 and g8.

# There are two players: one plays for white, the other for black. During each 
# move, the player picks one of his knights and moves it to an unoccupied square 
# according to standard chess rules. Thus, a knight on d5 can move to any of the 
# following squares: b6, c7, e7, f6, f4, e3, c3, and b4, as long as it is not 
# occupied by either a friendly or an enemy knight.

# The players take turns in making moves, starting with the white player. Given the configuration p of the knights after an unspecified number of moves, determine whose turn it is.

# * Example

# For p = "b1;g1;b8;g8", the output should be
# whoseTurn(p) = true.

# The configuration corresponds to the initial state of the game. Thus, it's white's turn.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string p

#     The positions of the four knights, starting with white knights, separated by a semicolon, in the chess notation.

#     Guaranteed constraints:
#     p.length = 11.

#     [output] boolean

#     true if white is to move, false otherwise.

#%%

# * Solution 1
def whoseTurn(p: str)->bool:

    def chessKnightMoves(position:str)-> list:
        line = ' abcdefgh'
        x = line.index(position[0])
        y = int(position[1])

        ds = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        result = []
        for d in ds:
            if x+d[0]>0 and x+d[0]<9 and y+d[1]>0 and y+d[1]<9:
                result.append(line[x+d[0]] + str(y+d[1]))

        return result

    # ? tests for chessKnightMoves()
    # print(chessKnightMoves('b1'))
    # print(chessKnightMoves('g1'))
    # print(chessKnightMoves('b8'))
    # print(chessKnightMoves('g8'))

    def findSteps(curP:str, iniP:str)->int:
        if curP == iniP:
            return 0
        queue = []
        for p in chessKnightMoves(curP):
            queue.append((p,1))
        
        # print(queue)

        while len(queue) != 0:
            nextP = queue.pop(0)

            # print(nextP[0])
            # print(nextP[1])

            step = nextP[1]
            nextNextPs = chessKnightMoves(nextP[0])
            for p in nextNextPs:
                if p == iniP:
                    return step+1
                else:
                    queue.append((p, step+1))


        return 0
    
    # ? test for findSteps()
    # findSteps('b1', 'b1')
    # print(findSteps('b1', 'b1'))

    ps = p.split(';')

    # print(ps)

    whiteSteps = 0
    whiteSteps += findSteps(ps[0], 'b1')
    print('whiteSteps 1:', whiteSteps)
    whiteSteps += findSteps(ps[1], 'g1')
    print('whiteSteps 2:', whiteSteps)
    
    blackSteps = 0
    blackSteps += findSteps(ps[2], 'b8')
    print('blackSteps 1:', blackSteps)
    blackSteps += findSteps(ps[3], 'g8')
    print('blackSteps 2:', blackSteps)

    return whiteSteps < blackSteps



# * Solution 2
# ! WTF!
def whoseTurn2(p):
    return sum(map(ord, p)) % 2 == 1



# a1 = 'b1;g1;b8;g8'
# r1 = whoseTurn(a1)
# print(r1)

# a1 = 'c3;g1;b8;g8'
# r1 = whoseTurn(a1)
# print(r1)

# a1 = 'g2;d7;h5;h1'
# r1 = whoseTurn(a1)
# print(r1)

a1 = 'a5;d3;c4;h3'
r1 = whoseTurn(a1)
print(r1)
