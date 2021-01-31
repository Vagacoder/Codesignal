#
# * Core 77, Are Similar?
# * Medium

# * Two arrays are called similar if one can be obtained from another by swapping 
# * at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

# * Example

#     For a = [1, 2, 3] and b = [1, 2, 3], the output should be
#     areSimilar(a, b) = true.

#     The arrays are equal, no need to swap any elements.

#     For a = [1, 2, 3] and b = [2, 1, 3], the output should be
#     areSimilar(a, b) = true.

#     We can obtain b from a by swapping 2 and 1 in b.

#     For a = [1, 2, 2] and b = [2, 1, 1], the output should be
#     areSimilar(a, b) = false.

#     Any swap of any two elements either in a or in b won't make a and b equal.

# *Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Array of integers.

#     Guaranteed constraints:
#     3 ≤ a.length ≤ 105,
#     1 ≤ a[i] ≤ 1000.

#     [input] array.integer b

#     Array of integers of the same length as a.

#     Guaranteed constraints:
#     b.length = a.length,
#     1 ≤ b[i] ≤ 1000.

#     [output] boolean

#     true if a and b are similar, false otherwise.

#%%

# * Solution 1
def areSimilar(a:list, b:list)-> bool:
    count = 0
    indexAndValue = []
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            count += 1
            indexAndValue.append((i, a[i], b[i]))
    
    print(count)

    if count == 0:
        return True
    elif count == 2:
        if indexAndValue[0][1] != indexAndValue[1][2] or\
            indexAndValue[0][2] != indexAndValue[1][1] :
            return False
        else:
            return True
    else:
        return False


a1 = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b1 = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
r1 = areSimilar(a1, b1)
print(r1)

# %%

