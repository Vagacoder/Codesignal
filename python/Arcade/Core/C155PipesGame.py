#
# * Core 155. Pipes Game

# Carlos always loved playing video games, especially the well-known computer game 
# "Pipes". Today he finally decided to write his own version of the legendary game 
# from scratch.

# In this game the player has to place the pipes on a rectangular field to make 
# water pour from each source to a respective sink. He has already come up with 
# the entire program, but one question still bugs him: how can he best check that 
# the arrangement of pipes is correct?

# It's your job to help him figure out exactly that.

# Carlos has 7 types of pipes in his game, with numbers corresponding to each type:

#     1 - vertical pipe
#     2 - horizontal pipe
#     3-6 - corner pipes
#     7 - two pipes crossed in the same cell (note that these pipes are not connected)

# Here they are, pipes 1 to 7, respectively:

# Water pours from each source in each direction that has a pipe connected to it 
# (thus it can even pour in all four directions). The puzzle is solved correctly 
# only if all water poured from each source eventually reaches a corresponding 
# sink.

# Help Carlos check whether the arrangement of pipes is correct. If it is correct, 
# return the number of cells with pipes that will be full of water at the end of 
# the game. If not, return -X, where X is the number of cells with water before 
# the first leakage point is reached, or if the first drop of water reaches an 
# incorrect destination (whichever comes first). Assume that water moves from one 
# cell to another at the same speed.

# Example

# For

# state = ["a224C22300000",
#          "0001643722B00",
#          "0b27275100000",
#          "00c7256500000",
#          "0006A45000000"]

# the output should be pipesGame(state) = 19.

# Here is how the game will end:

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string state

#     Array of strings of an equal length representing some state of the game. 
#       The pipes are represented by the numbers '1' to '7', the sources are given 
#       as lowercase English letters, and the corresponding sinks are marked by 
#       uppercase letters. Empty cells are marked with '0'.

#     It is guaranteed that each letter from the English alphabet either is not 
#       present in state, or appears there twice (in uppercase and lowercase).

#     Guaranteed constraints:
#     1 ≤ state.length ≤ 100,
#     1 ≤ state[i].length ≤ 100,
#     state[i][j] ∈ {0-7, a-z, A-Z}.

#     [output] integer

#     If the pipe arrangement is correct, return the number of cells with pipes 
#       that will be filled with water at the end of the game. If not, return -X, 
#       where X is the number of cells with water before the first leakage point 
#       is reached, or if the first drop of water reaches an incorrect destination.

#%%

# * Solution 1
def pipesGame(state: list) -> int:
    n = len(state)
    m = len(state[0])
    # print('n, m: ', n, m)

    starts = {}
    ends = {}

    # * find starting and ending points
    for i in range(n):
        for j in range(m):
            c = state[i][j]
            if 96 < ord(c) < 123:
                starts[c] = (i, j)
            elif 64 < ord(c) < 91:
                ends[c] = (i, j)

    # print(starts)
    # print(ends)

    # * Directions:
    # * 1: up
    # * 2: right
    # * 3: down
    # * 4: left

    go = {
        1: (-1, 0),
        2: (0, 1),
        3: (1, 0),
        4: (0, -1)
    }

    # * Pipe
    # * {pipe # : 
    # *   {in1 : out1, 
    # *    in2 : out2}
    # * }
    pipes = {
        '1': {3: 3, 1: 1},
        '2': {2: 2, 4: 4},
        '3': {1: 2, 4: 3},
        '4': {2: 3, 1: 4},
        '5': {2: 1, 3: 4},
        '6': {3: 2, 4: 1},
        '7': {1: 1, 2: 2, 3: 3, 4: 4}
    }



    # * define a function to check 
    def check(row: int, col: int, direction: int, source: str, steps: int) -> (bool, int):
        newRow = row + go[direction][0]
        newCol = col + go[direction][1]
        # print(newRow, newCol, direction, source, steps)

        # * base case 1: next pipe is out of range
        if newRow > n-1 or newRow < 0 or newCol > m-1 or newCol < 0:
            return (False, steps)
        # * base case 2: find correct sink
        if state[newRow][newCol] == source.upper():
            return (True, steps)
        # * base case 3: find wrong sink or other source
        if state[newRow][newCol].isalpha():
            return (False, steps)
        
        # * get next pipe
        newPipe = state[newRow][newCol]
        # print('newPipe', newPipe)
        # * base case 4: no pipe
        if newPipe == '0':
            return (False, steps)
        # * base case 5: wrong pipe (no connect to this one)
        if direction not in pipes[newPipe]:
            return (False, steps)


        newDirection = pipes[newPipe][direction]
        # print('newDirection', newDirection)
        return check(newRow, newCol, newDirection, source, steps+1)

    # print(check(2, 1, 2, 'b', 0))

    # * A collection of all directions of all sources
    results = {}

    # * is whole puzzle correct?
    isCorrect = True
    
    for key in starts.keys():
        result = {}
        # print('start location:', starts[key])
        for d in range(1,5):
            # print(check(starts[key][0], starts[key][1], d, key, 0))
            result[d] = check(starts[key][0], starts[key][1], d, key, 0)
            if result[d][0] == False and result[d][1] > 0:
                isCorrect = False
        
        results[key] = result

    print(results)
    print(isCorrect)


    # * For counting watered cell number, if whole puzzle is correct
    waterCovery = [[0]*m for _ in range(n)]

    # TODO: define a function extend alone pipe from source to end
    def extend(row: int, col: int, direction: int, steps: int):
        pass

    # * if whole puzzle is correct, count the number of cells full of water
    if isCorrect:
        pass    
    # * if whole puzzle is wrong, count the number of cells full of water
    else:
        pass
        
        


s1 = ["a224C22300000",
      "0001643722B00",
      "0b27275100000",
      "00c7256500000",
      "0006A45000000"]
r1 = pipesGame(s1)
print(r1)

# %%
