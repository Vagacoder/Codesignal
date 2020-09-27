#
# * Intro 25. Array Replace
# * Easy

# * Given an array of integers, replace all the occurrences of elemToReplace with 
# * substitutionElem.

# * Example

# For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the 
# output should be arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     0 ≤ inputArray.length ≤ 104,
#     0 ≤ inputArray[i] ≤ 109.

#     [input] integer elemToReplace

#     Guaranteed constraints:
#     0 ≤ elemToReplace ≤ 109.

#     [input] integer substitutionElem

#     Guaranteed constraints:
#     0 ≤ substitutionElem ≤ 109.

#     [output] array.integer

#%%

# * Solution 1

def arrayReplace1(inputArray: list, elemToReplace: int, substitutionElem: int)-> list:
    result = []
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            result.append(substitutionElem)
        else:
            result.append(inputArray[i])

    return result

# * Solution 2
# ! Simple syntax
def arrayReplace2(inputArray: list, elemToReplace: int, substitutionElem: int)-> list:
    return [x if x!=elemToReplace else substitutionElem for x in inputArray]


a1 = [1, 2, 1]
t1 = 1
s1 = 3
e1 = [3, 2, 3]
r1 = arrayReplace2(a1, t1, s1)
print('For {} to replace {} with {}, expected: {}, result: {}'.format(a1, t1, s1, e1, r1))




# %%
