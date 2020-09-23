#
# * Intro 17. Array Change
# * Easy

# * You are given an array of integers. On each move you are allowed to increase 
# * exactly one of its element by one. Find the minimal number of moves required 
# * to obtain a strictly increasing sequence from the input.

# * Example

# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     3 ≤ inputArray.length ≤ 1e5,
#     -105 ≤ inputArray[i] ≤ 1e5.

#     [output] integer

#     The minimal number of moves needed to obtain a strictly increasing sequence 
#     from inputArray.
#     It's guaranteed that for the given test cases the answer always fits signed 
#     32-bit integer type.

#%%

def arrayChange(inputArray: list)->int:
    # n = len(inputArray)
    # count = 0
    # i = 1;
    # while i < n:
    #     n0 = inputArray[i-1]
    #     n1 = inputArray[i]
    #     if n1 <= n0:
    #         inputArray[i] = n0 + 1
    #         count+= (n0 - n1 +1)
    #     i+=1
    
    # return count

    count = 0
    for i, x in enumerate(inputArray):
        if i > 0 and inputArray[i] <= inputArray[i-1]:
            count+= (inputArray[i-1] - inputArray[i] + 1)
            inputArray[i] = inputArray[i-1] + 1

    return count


a1 = [1,1,1]
r1 = arrayChange(a1)
e1 = 3
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
