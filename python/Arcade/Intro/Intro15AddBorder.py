#
# * Intro 15. Add Border
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
def addBorder(picture: list)-> list:
    result = []
    for s in picture:
        result.append('*' + s + '*')

    n = len(result[0])
    border = '*' * n
    result.insert(0, border)
    result.append(border)

    return result


# * Solution 2
def addBorder2(picture: list)-> list:
    result = []
    for s in picture:
        result.append('*' + s + '*')

    border = '*' * len(result[0])

    return [border] + result + [border]


p1 = ["abc", "ded"]
r1 = addBorder2(p1)
e1 = ["*****", "*abc*", "*ded*", "*****"]
print('For {}, expexcted: {}, result: {}'.format(p1, e1, r1))


