#
# * Core 39. Remove Array Part
# * Easy

# * Remove a part of a given array between given 0-based indexes l and r (inclusive).

# * Example

# For inputArray = [2, 3, 2, 3, 4, 5], l = 2, and r = 4, the output should be
# removeArrayPart(inputArray, l, r) = [2, 3, 5].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     2 ≤ inputArray.length ≤ 104,
#     -105 ≤ inputArray[i] ≤ 105.

#     [input] integer l

#     Left index of the part to be removed (0-based).

#     Guaranteed constraints:
#     0 ≤ l ≤ r.

#     [input] integer r

#     Right index of the part to be removed (0-based).

#     Guaranteed constraints:
#     l ≤ r < inputArray.length.

#     [output] array.integer

#%%
# * Solution 1
def removeArrayPart1(inputArray:list, l:int, r:int)-> list:
    return inputArray[:l] + inputArray[r+1:]


# * Solution 2
# ! del element(s)
def removeArrayPart2(inputArray:list, l:int, r:int)-> list:
    del inputArray[l:r+1]
    return inputArray


a1 = [2, 3, 2, 3, 4, 5]
l1 = 2
r1 = 4
re1 = removeArrayPart2(a1, l1, r1)
print(re1)

# %%
