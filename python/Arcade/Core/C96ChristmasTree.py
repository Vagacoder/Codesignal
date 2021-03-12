#
# * Core 96, Christmas Tree
# * Medium

# * It's Christmas time! To share his Christmas spirit with all his friends, the 
# young Christmas Elf decided to send each of them a Christmas e-mail with a nice 
# Christmas tree. Unfortunately, Internet traffic is very expensive in the North 
# Pole, so instead of sending an actual image he got creative and drew the tree 
# using nothing but asterisks ('*' symbols). He has given you the specs (see below) 
# and your task is to write a program that will generate trees following the spec 
# and some initial parameters.

# Here is a formal definition of how the tree should be built, but before you 
# read it the Elf HIGHLY recommends first looking at the examples that follow:

#     Each tree has a crown as follows:

#      *
#      *
#     ***

#     Define a line as a horizontal group of asterisks and a level as a collection 
#       of levelHeight lines stacked one on top of the other.

#     Below the crown there are levelNum levels.

#     The tree is perfectly symmetrical so all the middle asterisks of the lines 
#       lie on the center of the tree.

#     Each line of the same level (excluding the first one) has two more asterisks 
#       than the previous one (one added to each end);

#     The number of asterisks in the first line of each level is chosen as follows:
#         the first line of the first level has 5 asterisks;
#         the first line of each consecutive level contains two more asterisks 
#         than the first line of the previous level.

#     And finally there is the tree foot which has a height of levelNum and a width of:
#         levelHeight asterisks if levelHeight is odd;
#         levelHeight + 1 asterisks if levelHeight is even.

# Given levelNum and levelHeight, return the Christmas tree of the young elf.

# Example

#     For levelNum = 1 and levelHeight = 3, the output should be

#     christmasTree(levelNum, levelHeight) =
#         ["    *",
#          "    *",
#          "   ***",
#          "  *****",
#          " *******",
#          "*********",
#          "   ***"]

#     , which represents the following tree:

#                 ___
#           *        |
#           *        |-- the crown      
#          ***    ___|       
#         *****      |
#        *******     |-- level 1
#       ********* ___|
#          ***    ___|-- the foot

#     For levelNum = 2 and levelHeight = 4, the output should be

#     christmasTree(levelNum, levelHeight) = 
#         ["      *", 
#          "      *", 
#          "     ***", 
#          "    *****", 
#          "   *******", 
#          "  *********", 
#          " ***********", 
#          "   *******", 
#          "  *********", 
#          " ***********", 
#          "*************", 
#          "    *****", 
#          "    *****"]

#     , which represents the following tree:

#                     ___ 
#             *          |
#             *          | -- the crown
#            ***      ___|
#           *****        |
#          *******       | -- level 1
#         *********      |
#        ***********  ___|
#          *******       |
#         *********      | -- level 2
#        ***********     |
#       ************* ___|
#           *****        | -- the foot
#           *****     ___|

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer levelNum

#     A positive integer, the number of levels.

#     Guaranteed constraints:
#     1 ≤ levelNum ≤ 25.

#     [input] integer levelHeight

#     The number of lines in each level.

#     Guaranteed constraints:
#     1 ≤ levelHeight ≤ 25.

#     [output] array.string

#     The Christmas tree according to the specs and inputs. Output elements should not contain trailing whitespaces, and at least one of them should start with the '*' symbol.

#%%

# * Solution 1
def christmasTree(levelNum: int, levelHeight: int) -> list:
    # indent = 1 + 1 * levelHeight * levelNum - 2 * (levelNum - 1)
    indent = 1 * levelNum + levelHeight
    print(indent)

    def crown()-> list:
        return [
            ' ' * indent + '*',
            ' ' * indent + '*',
            ' ' * (indent - 1) + '***',
        ]

    def foot()-> list:
        if levelHeight%2 ==0:
            width = levelHeight + 1
        else:
            width = levelHeight
        return [
            ' ' * (indent - width // 2) + '*' * width
        ]*levelNum
    
    def trunk() -> list:
        trunk = []
        initWidth = 5
        for i in range(levelNum):
            width = initWidth
            for j in range(levelHeight):
                trunk.append(' ' * (indent - width // 2) + '*' * width)
                width += 2
            initWidth += 2
        return trunk


    result = []
    result.extend(crown())
    result.extend(trunk())
    result.extend(foot())
    return result


a1 = 1
a2 = 3
r1 = christmasTree(a1, a2)
print(r1)

a1 = 2
a2 = 4
r1 = christmasTree(a1, a2)
print(r1)
