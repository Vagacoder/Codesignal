#
# * Core 115 Sort by Length
# * Medium

# * Given an array of strings, sort them in the order of increasing lengths. If 
# * two strings have the same length, their relative order must be the same as 
# * in the initial array.

# * Example

# For

# inputArray = ["abc",
#               "",
#               "aaa",
#               "a",
#               "zz"]

# the output should be

# sortByLength(inputArray) = ["",
#                             "a",
#                             "zz",
#                             "abc",
#                             "aaa"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string inputArray

#     A non-empty array of strings.

#     Guaranteed constraints:
#     3 ≤ inputArray.length ≤ 100,
#     0 ≤ inputArray[i].length ≤ 100.

#     [output] array.string

#%%

# * Solution 1
# ! Insertion sort (stable)
def sortByLength(inputArray: list) -> list:
    n = len(inputArray)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if len(inputArray[j]) >= len(inputArray[j-1]):
                continue
            else:
                inputArray[j], inputArray[j-1] = inputArray[j-1], inputArray[j]
    
    return inputArray


# * Solution 2
def sortByLength2(inputArray: list) -> list:
    return sorted(inputArray, key=len)



a1 = ["abc", "", "aaa", "a", "zz"]
r1 = sortByLength2(a1)
print(a1)
