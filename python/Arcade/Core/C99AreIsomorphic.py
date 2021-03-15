#
# * Core 99, Are Isomorphic
# * Medium

# * Two two-dimensional arrays are isomorphic if they have the same number of 
# * rows and each pair of respective rows contains the same number of elements.

# Given two two-dimensional arrays, check if they are isomorphic.

# Example

#     For

#     array1 = [[1, 1, 1],
#               [0, 0]]

#     and

#     array2 = [[2, 1, 1],
#               [2, 1]]

#     the output should be
#     areIsomorphic(array1, array2) = true;

#     For

#     array1 = [[2],
#               []]

#     and

#     array2 = [[2]]

#     the output should be
#     areIsomorphic(array1, array2) = false.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.integer array1

#     Guaranteed constraints:
#     1 ≤ array1.length ≤ 5,
#     0 ≤ array1[i].length ≤ 5,
#     0 ≤ array1[i][j] ≤ 50.

#     [input] array.array.integer array2

#     Guaranteed constraints:
#     1 ≤ array2.length ≤ 5,
#     0 ≤ array2[i].length ≤ 5,
#     0 ≤ array2[i][j] ≤ 50.

#     [output] boolean

#%%

# * Solution 1
def areIsomorphic(array1:list, array2:list)-> bool:
    n1 = len(array1)
    n2 = len(array2)
    if n1 != n2:
        return False
    for i in range(n1):
        if len(array1[i]) != len(array2[i]):
            return False

    return True


# * Solution 2
def areIsomorphic2(array1:list, array2:list)-> bool:
    return (len(array1) == len(array2)) and all([len(array1[i]) == len(array2[i]) for i in range(len(array1))])


# * Solution 3
def areIsomorphic3(array1:list, array2:list)-> bool:
    return list(map(len, array1)) == list(map(len, array2))


a1 = [[1,1,1],[0,0]]
a2 = [[2,1,1],[2,1]]
r1 = areIsomorphic3(a1, a2)
print(r1)

a1 = [[2],[0,0]]
a2 = [[2],[1]]
r1 = areIsomorphic3(a1, a2)
print(r1)

a1 = [[2],[0,0]]
a2 = [[2]]
r1 = areIsomorphic3(a1, a2)
print(r1)