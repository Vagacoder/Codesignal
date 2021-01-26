#
# * Core 72, Add Border
# * Easy

# * Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# * Example

# For

# picture = ["abc",
#            "ded"]

# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string picture

#     A non-empty array of non-empty equal-length strings.

#     Guaranteed constraints:
#     1 ≤ picture.length ≤ 100,
#     1 ≤ picture[i].length ≤ 100.

#     [output] array.string

#     The same matrix of characters, framed with a border of asterisks of width 1.

#%%

# * Solution 1
def addBorder(picture:list)-> list:
    n = len(picture[0])
    m = len(picture)
    for i in range(m):
        picture[i] = '*' + picture[i] + '*'
    picture = ['*' * (n+2)] + picture
    picture.append('*' * (n+2))

    return picture


a1 = ['abc','ded']
r1 = addBorder(a1)
print(r1)

