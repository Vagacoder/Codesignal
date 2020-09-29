#
# * Intro 29. Chess Board Cell Color
# * Easy

# * Given two cells on the standard chess board, determine whether they have the 
# *same color or not.

# * Example

#     For cell1 = "A1" and cell2 = "C3", the output should be
#     chessBoardCellColor(cell1, cell2) = true

# https://codesignal.s3.amazonaws.com/tasks/chessBoardCellColor/img/example1.png?_tm=1582002259154

# For cell1 = "A1" and cell2 = "H3", the output should be
# chessBoardCellColor(cell1, cell2) = false.

# https://codesignal.s3.amazonaws.com/tasks/chessBoardCellColor/img/example2.png?_tm=1582002260007

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string cell1

#     Guaranteed constraints:
#     cell1.length = 2,
#     'A' ≤ cell1[0] ≤ 'H',
#     1 ≤ cell1[1] ≤ 8.

#     [input] string cell2

#     Guaranteed constraints:
#     cell2.length = 2,
#     'A' ≤ cell2[0] ≤ 'H',
#     1 ≤ cell2[1] ≤ 8.

#     [output] boolean

#     true if both cells have the same color, false otherwise.


#%%

# * Solution 1
def chessBoardCellColor(cell1:str, cell2:str)->bool:
    # print(ord(cell1[0]))
    # print(ord(cell2[0]))
    # print(int(cell1[1]))
    # print(int(cell2[1]))
    return (ord(cell1[0]) + ord(cell2[0]) + int(cell1[1]) + int(cell2[1])) % 2 == 0


a1 = 'A1'
a2 = 'C3'
e1 = True
r1 = chessBoardCellColor(a1, a2)
print('For {} and {}, expected: {}, result: {}'.format(a1, a2, e1, r1))

a1 = 'A1'
a2 = 'H3'
e1 = False
r1 = chessBoardCellColor(a1, a2)
print('For {} and {}, expected: {}, result: {}'.format(a1, a2, e1, r1))

# %%
