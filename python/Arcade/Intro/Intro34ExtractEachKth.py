#
# * Intro 34, Extract Each Kth
# * Easy

# * Given array of integers, remove each kth element from it.

# * Example

# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
# extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     5 ≤ inputArray.length ≤ 15,
#     -20 ≤ inputArray[i] ≤ 20.

#     [input] integer k

#     Guaranteed constraints:
#     1 ≤ k ≤ 10.

#     [output] array.integer

#     inputArray without elements k - 1, 2k - 1, 3k - 1 etc.


#%%

# * Solution 1
def extractEachKth1(inputArray:list, k:int) -> int:
    return [x for i, x in enumerate(inputArray) if (i+1)%k != 0]


# * Solution 2
# ! Smart del
def extractEachKth2(inputArray, k):
    del inputArray[k-1::k]
    return inputArray


a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = 3
e1 = [1, 2, 4, 5, 7, 8, 10]
r1 = extractEachKth2(a1, a2)
print('For {} and {}, expected: {}, result: {}'.format(a1, a2, e1, r1))

# %%
