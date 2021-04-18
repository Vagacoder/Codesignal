#
# * Core 113, Correct Nonogram
# * Medium

# * A nonogram is also known as Paint by Numbers and Japanese Crossword. The aim 
# * in this puzzle is to color the grid into black and white squares. At the top 
# * of each column, and at the side of each row, there are sets of one or more 
# * numbers which describe the runs of black squares in that row/column in exact 
# * order. For example, if you see 10 1 along some column/row, this indicates that 
# * there will be a run of exactly ten black squares, followed by one or more white 
# * squares, followed by a single black square. The cells along the edges of the 
# * grid can also be white.

# You are given a square nonogram of size size. Its grid is given as a square 
# matrix nonogramField of size (size + 1) / 2 + size, where the first (size + 1) / 2 
# cells of each row and and each column define the numbers for the corresponding 
# row/column, and the rest size × size cells define the the grid itself.

# Determine if the given nonogram has been solved correctly.

# Note: here / means integer division.

# * Example

#     For size = 5 and

#     nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
#                      ["-", "-", "-", "2", "2", "1", "-", "1"],
#                      ["-", "-", "-", "2", "1", "1", "3", "3"],
#                      ["-", "3", "1", "#", "#", "#", ".", "#"],
#                      ["-", "-", "2", "#", "#", ".", ".", "."],
#                      ["-", "-", "2", ".", ".", ".", "#", "#"],
#                      ["-", "1", "2", "#", ".", ".", "#", "#"],
#                      ["-", "-", "5", "#", "#", "#", "#", "#"]]

#     the output should be correctNonogram(size, nonogramField) = true;

#     For size = 5 and

#     nonogramField = [["-", "-", "-", "-", "-", "-", "-", "-"],
#                      ["-", "-", "-", "-", "-", "1", "-", "-"],
#                      ["-", "-", "-", "3", "3", "2", "5", "5"],
#                      ["-", "-", "3", ".", ".", ".", "#", "#"],
#                      ["-", "2", "2", "#", "#", "#", "#", "#"],
#                      ["-", "-", "5", "#", "#", "#", "#", "#"],
#                      ["-", "-", "5", "#", "#", "#", "#", "#"],
#                      ["-", "-", "2", ".", ".", ".", "#", "#"]]

#     the output should be correctNonogram(size, nonogramField) = false.

#     There are three mistakes in the nonogram:
#         In the 5th (1-based) row there are numbers ["-", "2", "2"], so there should be two runs of 2 black squares separated by at least one white square. However, there is only one run of 5 black squares.
#         In the 6th column there are numbers ["-", "1", "2"], so there should be a run of exactly 1 black square, followed by one or more white squares, followed by another 2 black squares. However, there is a single run of 3 black squares not separated by white ones.
#         Finally, in the 4th row there are numbers ["-", "-", "3"], so there should be a single run of exactly 3 black squares. However, there is just a 2-square run in that row.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer size

#     A positive integer, the size of the grid.

#     Guaranteed constraints:
#     5 ≤ size ≤ 10.

#     [input] array.array.string nonogramField

#     A square matrix of strings of size (size + 1) / 2 + size defining the puzzle field.
#     The first (size + 1) / 2 cells of each row and each column define the numbers for this row/column. If there is no number in the cell, its value is "-".
#     The remaining size × size cells define the grid, where string "#" denotes black cells and string "." denotes white ones.

#     Guaranteed constraints:
#     8 ≤ nonogramField.length ≤ 15,
#     nonogramField[i].length = nonogramField.length.

#     [output] boolean

#     true if the given nonogram is solved correctly and false otherwise.

#%%

# * Solution 1
def correctNonogram(size: int, nonogramField: list)-> bool:
    n = len(nonogramField)
    newNonogramField = list(zip(*nonogramField))
    # print(newNono)

    def checkRow(rowIndex: int)-> bool:
        # print(nonogramField[rowIndex])
        
        check = nonogramField[rowIndex][:n-size]
        check = [int(x) for x in check if x.isdigit()]
        # if len(check) == 0:
        #     check.append(0)
        # print(check)
        nono = nonogramField[rowIndex][n-size:]
        nono = ''.join(nono)
        nono = nono.split('.')
        nono = [len(x) for x in nono if x != '']
        # print(nono)
        # print(check == nono)
        return check == nono

    
    # print(checkRow(5))


    def checkCol(colIndex: int)-> bool:
        check = newNonogramField[colIndex][:n-size]
        check = [int(x) for x in check if x.isdigit()]
        nono = newNonogramField[colIndex][n-size:]
        nono = ''.join(nono)
        nono = nono.split('.')
        nono = [len(x) for x in nono if x != '']
        return check == nono
        

    # print(checkCol(3))


    for j in range(n-size, n):
        # print('check row ', j, checkRow(j))
        if not checkRow(j):
            # print('row', j)
            # print(nonogramField[j])
            return False

    for j in range(n-size, n):
        if not checkCol(j):
            # print('col', j)
            return False


    return True

s1 = 5
n1 = [["-", "-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "2", "2", "1", "-", "1"],
      ["-", "-", "-", "2", "1", "1", "3", "3"],
      ["-", "3", "1", "#", "#", "#", ".", "#"],
      ["-", "-", "2", "#", "#", ".", ".", "."],
      ["-", "-", "-", ".", ".", ".", ".", "."],
      ["-", "1", "2", "#", ".", ".", "#", "#"],
      ["-", "-", "5", "#", "#", "#", "#", "#"]]
r1 = correctNonogram(s1, n1)
print(r1)

s1 = 5
n1 = [["-", "-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "2", "2", "1", "-", "1"],
      ["-", "-", "-", "2", "1", "1", "3", "3"],
      ["-", "3", "1", "#", "#", "#", ".", "#"],
      ["-", "-", "2", "#", "#", ".", ".", "."],
      ["-", "-", "2", ".", ".", ".", "#", "#"],
      ["-", "1", "2", "#", ".", ".", "#", "#"],
      ["-", "-", "5", "#", "#", "#", "#", "#"]]
r1 = correctNonogram(s1, n1)
print(r1)

s1 = 9
n1 = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
      ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
      ['-', '-', '-', '-', '-', '-', '-', '4', '3', '-', '-', '-', '-', '-'], 
      ['-', '-', '-', '-', '-', '2', '2', '2', '1', '9', '3', '4', '2', '2'], 
      ['-', '-', '-', '-', '1', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
      ['-', '-', '-', '-', '5', '.', '.', '#', '#', '#', '#', '#', '.', '.'], 
      ['-', '-', '-', '-', '7', '.', '#', '#', '#', '#', '#', '#', '#', '.'], 
      ['-', '-', '-', '-', '9', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
      ['1', '1', '1', '1', '1', '#', '.', '#', '.', '#', '.', '#', '.', '#'], 
      ['-', '-', '-', '-', '1', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
      ['-', '-', '-', '-', '1', '.', '.', '.', '.', '#', '.', '.', '.', '.'], 
      ['-', '-', '-', '1', '1', '.', '.', '#', '.', '#', '.', '.', '.', '.'], 
      ['-', '-', '-', '-', '3', '.', '.', '#', '#', '#', '.', '.', '.', '.']]
r1 = correctNonogram(s1, n1)
print(r1)


# %%
