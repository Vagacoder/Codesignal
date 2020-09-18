#
#  * Intro 09. All Longest String
#  * Given an array of strings, return another array containing all of its longest 
#  * strings.

#  * Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

#  * Input/Output

#     [execution time limit] 3 seconds (java)

#     [input] array.string inputArray

#     A non-empty array.

#     Guaranteed constraints:
#     1 ≤ inputArray.length ≤ 10,
#     1 ≤ inputArray[i].length ≤ 10.

#     [output] array.string

#     Array of the longest strings, stored in the same order as in the inputArray.

#%%

def allLongestStrings(inputArray: list) -> list:
    maxLength = max(len(s) for s in inputArray)
    result = [s for s in inputArray if len(s) == maxLength]
    return result


str1 = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(str1))

