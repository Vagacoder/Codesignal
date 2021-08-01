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
    # ! Note: < + > = 5 and ^ + v = 5

    # * map character to number
    mapCharToNum= {
        '<': 1,
        '^': 2,
        'v': 3,
        '>': 4
    }

    SumOfDir = 5

    # * map number to coordination change (x, y)
    mapNumToDir = {
        1: (0, -1),
        2: (-1, 0),
        3: (1, 0),
        4: (0, 1)
    }

    # * Node for snake
    class Node:
        def __init__(self, coord, direction):
            self.coord = coord
            self.direction = direction
            self.next = None

    # * the Class of Snake, which is a linked list
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
        
        # * turn snake right
        def turnR(self):
            pass

        # * turn snake left
        def turnL(self):
            pass


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
    # * find 2nd node
    reversedDirectionUpdate = mapNumToDir[SumOfDir - currentDirection]
    nextCoord = ((currentCoord[0] + reversedDirectionUpdate[0]),
                    (currentCoord[1] + reversedDirectionUpdate[1]))
    print(nextCoord)
    nextNode = Node((nextCoord[0],nextCoord[1]), None)
    print(nextNode)
    snake.addNode(nextNode)
    print(snake.tail.coord)



    # * find other nodes
    while True:
        break


    


        

    






g1 = [['.', '.', '*', '>', '.'],
      ['.', '*', '*', '.', '.'],
      ['.', '.', '.', '.', '.']]
c1 = 'FRFFRFFRFLFF'
r1 = snakeGame(g1, c1)
print(r1)

# %%
