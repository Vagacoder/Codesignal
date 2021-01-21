#
# * Core 68, All Longest Strings
# * Easy

# * Given an array of strings, return another array containing all of its longest 
# * strings.

# * Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string inputArray

#     A non-empty array.

#     Guaranteed constraints:
#     1 ≤ inputArray.length ≤ 10,
#     1 ≤ inputArray[i].length ≤ 10.

#     [output] array.string

#     Array of the longest strings, stored in the same order as in the inputArray.

#%%

# * Solution 1
def allLongestStrings(inputArray):
    return [x for x in inputArray if len(x) == max([len(y) for y in inputArray])]


# * Solution 2
def allLongestStrings2(inputArray):
    return [x for x in inputArray if len(x) == max(map(len, inputArray))]




a1 = ["aba", "aa", "ad", "vcd", "aba"]
r1 = allLongestStrings2(a1)
print(r1)

# %%
