#
# * Core 157. Snake Game

# Your task is to imitate a turn-based variation of the popular "Snake" game.

# You are given the initial configuration of the board and a list of commands 
# which the snake follows one-by-one. The game ends if one of the following happens:

#     the snake tries to eat its tail;
#     the snake tries to move out of the board;
#     it executes all the given commands.

# Output the board configuration after the game ends.

# Example

#     For

# gameBoard = [['.', '.', '.', '.'],
#              ['.', '.', '<', '*'],
#              ['.', '.', '.', '*']]

# and commands = "FFFFFRFFRRLLF", the output should be

# snakeGame(gameBoard, commands) = [['.', '.', '.', '.'],
#                                   ['X', 'X', 'X', '.'],
#                                   ['.', '.', '.', '.']]

#     For

# gameBoard = [['.', '.', '^', '.', '.'],
#              ['.', '.', '*', '*', '.'],
#              ['.', '.', '.', '*', '*']]

# and commands = "RFRF", the output should be

# snakeGame(gameBoard, commands) = [['.', '.', 'X', 'X', '.'],
#                                   ['.', '.', 'X', 'X', '.'],
#                                   ['.', '.', '.', 'X', '.']]

#     For

# gameBoard = [['.', '.', '*', '>', '.'],
#              ['.', '*', '*', '.', '.'],
#              ['.', '.', '.', '.', '.']]

# and commands = "FRFFRFFRFLFF", the output should be

# snakeGame(gameBoard, commands) = [['.', '.', '.', '.', '.'],
#                                   ['<', '*', '*', '.', '.'],
#                                   ['.', '.', '*', '.', '.']]

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.char gameBoard

#     A rectangular matrix of characters. It is guaranteed that it represents a 
#       correct game board configuration, i.e. there is exactly one snake. 
#       Direction of snake's head is depicted by one of the following characters 
#       ('^', '>', 'v', '<'). All of the other snake's body parts are depicted by 
#       '*'s (note, that if the snake has length 1 then there is no asterisks in 
#       its representation). All cells which are not occupied by the snake are 
#       depicted by '.'s.

#     It is guaranteed that all snake cells are connected and no snake cell has 
#       more than two neighbors.

#     Guaranteed constraints:
#     1 ≤ gameBoard.length ≤ 10,
#     1 ≤ gameBoard[0].length ≤ 10.

#     [input] string commands

#     A list of commands, where 'F' means go one cell forward in the current 
#       direction, 'L' and 'R' mean change current direction 90 degrees left 
#       (counter-clockwise) or right (clockwise) correspondingly.

#     Guaranteed constraints:
#     0 ≤ commands.length ≤ 40.

#     [output] array.array.char

#     Configuration of the board after the end of the game.

#     If the snake dies, output its state before the losing move and replace each 
#       of the cells it occupied with Xs.

#%%

# * Solution 1
def snakeGame(gameBoard: list, commands: str)-> list:

    N = len(gameBoard)
    M = len(gameBoard[0])

    # * Direction
    # * 1: left
    # * 2: up
    # * 3: down
    # * 4: right
    # ! Note: < + > = 5 and ^ + v = 5, to easy find reverese direction

    # * map direction in character to number
    mapCharToNum: dict[str: int] = {
        '<': 1,
        '^': 2,
        'v': 3,
        '>': 4
    }

    # * map direction in number to character
    mapNumToChar: dict[int: str] = {
        1: '<',
        2: '^',
        3: 'v',
        4: '>'
    }

    # * turn left
    turnLeft: dict[int: int] = {
        1: 3,
        2: 1,
        3: 4,
        4: 2
    }

    # * turn right
    turnRight: dict[int: int] = {
        1: 2,
        2: 4,
        3: 1,
        4: 3
    }

    # ! Note: < + > = 5 and ^ + v = 5,
    SumOfDir: int = 5

    # * map direction in number to coordination changing (row, col)
    # * this is also next coordination changing for moving forward
    # * 1: going left,  row no change, col -= 1
    # * 2: going up,    row -= 1     , col no change
    # * 3: going down,  row += 1     , col no change
    # * 4: going right, row no change, col += 1
    mapNumToDir: dict[int: tuple[int, int]] = {
        1: (0, -1),
        2: (-1, 0),
        3: (1, 0),
        4: (0, 1)
    }

    # * next coordination changing for turn left
    nextCordForLeft: dict[int: tuple[int, int]] = {
        1: (1, 0),
        2: (0, -1),
        3: (0, 1),
        4: (-1, 0),
    }

    # * next coordination changing for turn right
    nextCordForRight: dict[int: tuple[int, int]] = {
        1: (-1, 0),
        2: (0, 1),
        3: (0, -1),
        4: (1, 0),
    }

    # * Node for snake
    class Node:
        def __init__(self, coord: tuple, direction: int):
            self.coord = coord
            self.direction = direction
            self.next = None

    # * the Class of Snake, which is a linked list, start ======================
    class Snake:
        # * Constructor
        def __init__(self, head: Node):
            self.head = head
            self.tail = head
            self.error = False

        # * add a new node to snake
        def addNode(self, newNode: Node):
            self.tail.next = newNode
            self.tail = newNode

        # * move snake forward
        def moveF(self):
            if not self.error:
                direction = self.head.direction

                # * check if moving out of gameboard
                headCoord = self.head.coord
                nextCoord = (headCoord[0] + mapNumToDir[direction][0],
                             headCoord[1] + mapNumToDir[direction][1])
                if nextCoord[0] < 0 or nextCoord[0] >= N or nextCoord[1] < 0 or nextCoord[1] >= M:
                    self.error = True
                    self.setErrorSnake()
                    return

                # * check if eating self
                if gameBoard[nextCoord[0]][nextCoord[1]] == '*':
                    self.error = True
                    self.setErrorSnake()
                    return

                # * moving forward
                nextNode = Node((nextCoord[0],nextCoord[1]), direction)
                nextNode.next = self.head
                self.head = nextNode

                cur = self.head
                while cur.next != None:
                    if cur.next == self.tail:
                        cur.next = None
                        self.tail = cur
                    else:
                        cur = cur.next
                
                self.redrawGameBoard()


        
        # * turn snake right
        def turnR(self):
            if not self.error:
                direction = self.head.direction
                
                # # * check if moving out of gameboard
                # headCoord = self.head.coord
                # nextCoord = (headCoord[0] + nextCordForRight[direction][0],
                #              headCoord[1] + nextCordForRight[direction][1])
                # if nextCoord[0] < 0 or nextCoord[0] >= N or nextCoord[1] < 0 or nextCoord[1] >= M:
                #     self.error = False
                #     self.setErrorSnake()
                #     return

                # # * check if eating self
                # if gameBoard[nextCoord[0]][nextCoord[1]] == '*':
                #     self.error = False
                #     self.setErrorSnake()
                #     return

                # * turning right
                newDirection = turnRight[direction]
                self.head.direction = newDirection
                # nextNode = Node((nextCoord[0],nextCoord[1]), newDirection)
                # nextNode.next = self.head
                # self.head = nextNode

                # cur = self.head
                # while cur.next != None:
                #     if cur.next == self.tail:
                #         cur.next = None
                #         self.tail = cur
                #     else:
                #         cur = cur.next
                
                self.redrawGameBoard()

        # * turn snake left
        def turnL(self):
            if not self.error:
                direction = self.head.direction

                # # * check if moving out of gameboard
                # headCoord = self.head.coord
                # nextCoord = (headCoord[0] + nextCordForLeft[direction][0],
                #              headCoord[1] + nextCordForLeft[direction][1])
                # if nextCoord[0] < 0 or nextCoord[0] >= N or nextCoord[1] < 0 or nextCoord[1] >= M:
                #     self.error = False
                #     self.setErrorSnake()
                #     return

                # # * check if eating self
                # if gameBoard[nextCoord[0]][nextCoord[1]] == '*':
                #     self.error = False
                #     self.setErrorSnake()
                #     return

                # * turning left
                newDirection = turnLeft[direction]
                self.head.direction = newDirection
                # nextNode = Node((nextCoord[0],nextCoord[1]), newDirection)
                # nextNode.next = self.head
                # self.head = nextNode

                # cur = self.head
                # while cur.next != None:
                #     if cur.next == self.tail:
                #         cur.next = None
                #         self.tail = cur
                #     else:
                #         cur = cur.next
                
                self.redrawGameBoard()

    
        # * set error snake
        def setErrorSnake(self):
            for i in range(N):
                for j in range(M):
                    if gameBoard[i][j] == '*' or gameBoard[i][j] in '<^>v':
                        gameBoard[i][j] = 'X'

        # * redraw game board
        def redrawGameBoard(self):
            for i in range(N):
                for j in range(M):
                    gameBoard[i][j] = '.'
            gameBoard[self.head.coord[0]][self.head.coord[1]] = mapNumToChar[self.head.direction]
            cur = self.head.next
            while cur != None:
                gameBoard[cur.coord[0]][cur.coord[1]] = '*'
                cur = cur.next
                
        
    # * the Class of Snake, which is a linked list, end ========================



    # * Build Snake, start =====================================================
    # ! Maybe should make a copy of game board and go through the copy
    # * find head of snake
    head = Node(None, None)
    for i in range(N):
        for j in range(M):
            if gameBoard[i][j] in '<^>v':
                head.coord = (i, j)
                head.direction = mapCharToNum[gameBoard[i][j]]
                snake = Snake(head)
    
    # print('snake', snake.head, snake.tail, snake.error)
    # * create full snake
    currentDirection = snake.head.direction
    currentCoord = snake.head.coord

    # TODO
    # * find 2nd node, 
    # ! the direction of 2nd node is fixed
    reversedDirectionUpdate = mapNumToDir[SumOfDir - currentDirection]
    nextCoord = ((currentCoord[0] + reversedDirectionUpdate[0]),
                    (currentCoord[1] + reversedDirectionUpdate[1]))
    # print('nextCoord', nextCoord)

    nextNode = Node((nextCoord[0],nextCoord[1]), None)
    # print(nextNode)

    # * if has 2nd node
    if gameBoard[nextCoord[0]][nextCoord[1]] == '*':
        snake.addNode(nextNode)
        # print('snake tail coord', snake.tail.coord)

        currentCoord = nextNode.coord        
        # print('currentCoord', currentCoord)

        # * find other nodes, 
        # ! the direction of other nodes is not fixed
        while True:
            isTail = True

            # * check all direction except currentDirection (not going back)
            for direc in mapNumToDir.keys():
                if direc != currentDirection:
                    direcChange = mapNumToDir[direc]
                    nextCoord = ((currentCoord[0] + direcChange[0]),
                                 (currentCoord[1] + direcChange[1]))
                    
                    # print('nextCoord for other', nextCoord)

                    # * if nextCoord out of gameboard
                    if nextCoord[0] < 0 or nextCoord[0] >= N or nextCoord[1] < 0 or nextCoord[1] >= M:
                        continue
                    # * find next node
                    if gameBoard[nextCoord[0]][nextCoord[1]] == '*':
                        nextNode = Node((nextCoord[0],nextCoord[1]), None)
                        snake.addNode(nextNode)
                        currentDirection = SumOfDir - direc
                        currentCoord = nextNode.coord  
                        isTail = False
                        break
            
            if isTail:
                break

    # * Build Snake, end =======================================================
    


    # snake.moveF()
    # snake.moveF()
    # snake.moveF()
    # snake.turnR()
    # snake.turnR()
    # snake.turnL()

    for com in commands:
        if com == 'F':
            snake.moveF()
        elif com == 'L':
            snake.turnL()
        elif com == 'R':
            snake.turnR()
    

    return gameBoard




# g1 = [['.', '.', '*', '>', '.'],
#       ['.', '*', '*', '.', '.'],
#       ['.', '.', '.', '.', '.']]
# c1 = 'FRFFRFFRFLFF'
# r1 = snakeGame(g1, c1)
# print(r1)


g1 = [[".",".",".","."], 
      [".",".","<","*"], 
      [".",".",".","*"]]
c1 = 'FFFFFRFFRRLLF'
r1 = snakeGame(g1, c1)
print(r1)

# %%
