#
# * Intro 37, Array Max Consecutive Sum
# * Easy

# * Given array of integers, find the maximal possible sum of some of its k 
# * consecutive elements.

# * Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

#     2 + 3 = 5;
#     3 + 5 = 8;
#     5 + 1 = 6;
#     1 + 6 = 7.
#     Thus, the answer is 8.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Array of positive integers.

#     Guaranteed constraints:
#     3 ≤ inputArray.length ≤ 105,
#     1 ≤ inputArray[i] ≤ 1000.

#     [input] integer k

#     An integer (not greater than the length of inputArray).

#     Guaranteed constraints:
#     1 ≤ k ≤ inputArray.length.

#     [output] integer

#     The maximal possible sum.

#%%

# ! Timeout
# * Solution 1
def arrayMaxConsecutiveSum1(inputArray:list, k:int)-> int:
    n = len(inputArray)
    max = 0
    for i in range(n-k+1):
        thisSum = sum(inputArray[i: i+k])
        if thisSum > max:
            max = thisSum

    return max


# ! Timeout
# * Solution 2
def arrayMaxConsecutiveSum2(inputArray:list, k:int)-> int:
    n = len(inputArray)
    max = 0
    for i in range(n-k+1):
        if 0< i < (n-k) and inputArray[i+k-1] < inputArray[i-1]:
            continue
        thisSum = sum(inputArray[i: i+k])
        if thisSum > max:
            max = thisSum

    return max



# * Solution 3
# ! Improved sliding window
def arrayMaxConsecutiveSum3(inputArray:list, k:int)-> int:
    n = len(inputArray)
    maxSum = sum(inputArray[:k])
    curSum = maxSum
    for i in range(1,n-k+1):
        curSum = curSum - inputArray[i-1] + inputArray[i+k-1]
        if curSum > maxSum:
            maxSum = curSum

    return maxSum



a1 = [2, 3, 5, 1, 6]
a2 = 2
e1 = 8
r1 = arrayMaxConsecutiveSum3(a1, a2)
print('For {} and {}, expected: {}, result: {}'.format(a1, a2, e1, r1))


# %%
