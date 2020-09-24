#
# * Intro 20. Array Maximal Adjacent Difference
# * Easy

# * Given an array of integers, find the maximal absolute difference between any 
# * two of its adjacent elements.

# * Example

# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     3 ≤ inputArray.length ≤ 10,
#     -15 ≤ inputArray[i] ≤ 15.

#     [output] integer

#     The maximal absolute difference.

#%%
# * Solution 1
def arrayMaximalAdjacentDifference1(inputArray:list)-> int:
    result = 0
    for i, x in enumerate(inputArray):
        if i != 0:
            diff = abs(x - inputArray[i-1])
            if diff > result:
                result = diff

    return result


# * Solution 2
def arrayMaximalAdjacentDifference2(inputArray:list)-> int:
    return max([abs(x-inputArray[i-1]) for i, x in enumerate(inputArray) if i >0])


a1 = [2, 4, 1, 0]
e1 = 3
r1 = arrayMaximalAdjacentDifference2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))
