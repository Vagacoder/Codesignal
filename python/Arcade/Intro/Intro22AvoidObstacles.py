#
# * Intro 22. Avoid Obstacles

# * You are given an array of integers representing coordinates of obstacles 
# * situated on a straight line.

# * Assume that you are jumping from the point with coordinate 0 to the right. 
# * You are allowed only to make jumps of the same length represented by some 
# * integer.

# * Find the minimal length of the jump enough to avoid all the obstacles.

# * Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.

# Check out the image below for better understanding:
# https://codesignal.s3.amazonaws.com/tasks/avoidObstacles/img/example.png?_tm=1581994811750

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Non-empty array of positive integers.

#     Guaranteed constraints:
#     2 ≤ inputArray.length ≤ 1000,
#     1 ≤ inputArray[i] ≤ 1000.

#     [output] integer

#     The desired length.

#%%

# * Solution 1
def avoidObstacles1(inputArray: list) -> int:
    inputArray.sort()
    maxJumpDistance = inputArray[-1]
    for jDis in range(1, maxJumpDistance):
        p = 0 
        goodJump = True
        while p <= maxJumpDistance:
            if p in inputArray:
                goodJump = False
                break;
            p += jDis

        if goodJump:
            return jDis

    return maxJumpDistance+1


# * Solution 2
def avoidObstacles2(inputArray: list)-> int:
    inputArray.sort()
    maxJumpDistance = inputArray[-1]
    for jDis in range(1, maxJumpDistance):
        landings = [x  for x in range(0, maxJumpDistance+1, jDis)]
        if len(set(inputArray).intersection(set(landings)))== 0:
            return jDis

    return maxJumpDistance + 1


# * Solution 3
# ! Idea: none of elements in obstacle list can be full divided by jump distance
def avoidObstacles3(inputArray: list)-> int:
    jump = 1
    while True:
        # !! for ... else 
        for x in inputArray:
            if x%jump == 0:
                break;
        else:
            break;
        jump+=1

    return jump


# * Solution 4
def avoidObstacles4(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1


a1 = [5, 3, 6, 7, 9]
e1 = 4
r1 = avoidObstacles3(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a2 = [2,3]
e2 = 4
r2 = avoidObstacles3(a2)
print('For {}, expected: {}, result: {}'.format(a2, e2, r2))

a3 = [1, 4, 10, 6, 2]
e3 = 7
r3 = avoidObstacles3(a3)
print('For {}, expected: {}, result: {}'.format(a3, e3, r3))

# %%
