#
# * Core 150. Cells Joining

# You are writing a spreadsheet application for an ancient operating system. The 
# system runs on a computer so old that it can only display ASCII graphics. 
# Currently you are stuck with implementing the cells joining algorithm.

# You are given a table in ASCII graphics, where the following characters are used 
# for borders: +, -, |. The rows can have different heights and the columns can 
# have different widths. Each cell has an area greater than 1 (excluding the 
# borders) and can contain any ASCII characters excluding +, - and |.

# The algorithm you want to implement should merge the cells within a given 
# rectangular part of the table into a single cell by removing the borders between 
# them (i.e. replace them with space characters (' ') and replace redundant +s 
# with correct border symbols). The cells to join are represented by the coordinates 
# of the cells at the extreme bottom-left and top-right of the area.

# * Example
# For

# table = ["+----+--+-----+----+",
#          "|abcd|56|!@#$%|qwer|",
#          "|1234|78|^&=()|tyui|",
#          "+----+--+-----+----+",
#          "|zxcv|90|77777|stop|",
#          "+----+--+-----+----+",
#          "|asdf|~~|ghjkl|100$|",
#          "+----+--+-----+----+"]

# and coords = [[2, 0], [1, 1]], the output should be

# cellsJoining(table, coords) = ["+----+--+-----+----+",
#                                "|abcd|56|!@#$%|qwer|",
#                                "|1234|78|^&=()|tyui|",
#                                "+----+--+-----+----+",
#                                "|zxcv 90|77777|stop|",
#                                "|       +-----+----+",
#                                "|asdf ~~|ghjkl|100$|",
#                                "+-------+-----+----+"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string table

#     A table in ASCII graphics. '|' and '-' characters represent borders, and '+' characters represent their intersection. It is guaranteed that there are no joined cells in the table. It's also guaranteed that the table occupies the entire rectangular array, i.e. its outer borders occupy the leftmost and the rightmost columns of the array as well as its topmost and bottommost rows.

#     Guaranteed constraints:
#     3 ≤ table.length ≤ 25,
#     3 ≤ table[i].length ≤ 80,
#     table[i].length = table[j].length.

#     [input] array.array.integer coords

#     coords[0] contains 0-based row and column indices (given in that exact order) of the extreme bottom left cell in the area to join, and coords[1] contains indices of the extreme top right cell of that region.

#     It's guaranteed that there are at least two cells to be joined, and that cells with the given indices do exist in the table.

#     The rows are numbered from top to bottom while the columns are numbered from left to right.

#     Guaranteed constraints:
#     coords.length = 2,
#     coords[i].length = 2,
#     0 ≤ coords[1][0] ≤ coords[0][0] < 10,
#     0 ≤ coords[0][1] ≤ coords[1][1] ≤ 25.

#     [output] array.string

#     Table with cells in given region joined into one.

#%%

# * Solution 1
def cellsJoining(table: list, coords: list)-> list:
    row1 = coords[1][0]
    row2 = coords[0][0]
    col1 = coords[0][1]
    col2 = coords[1][1]
    # print(row1, row2, col1, col2)

    n = len(table)
    m = len(table[0])
    # print(n, m)

    rowIndex = [0]*n
    rowCount = -1
    for i, row in enumerate(table):
        rowIndex[i] = rowCount
        if row.startswith('+'):
            rowCount += 1
    # print(rowIndex)

    colIndex = [0]*m
    colCount = -1
    for i, col in enumerate(table[0]):
        colIndex[i] = colCount
        if col == '+':
            colCount += 1
    # print(colIndex)

    startCol = -1
    endCol = -1
    for i, colI in enumerate(colIndex):
        if startCol == -1 and colI == col1:
            startCol = i
        if colI == col2:
            endCol = i
    # print(startCol, endCol)

    for i, row in enumerate(table):
        if row.startswith('|') and rowIndex[i] >= row1 and rowIndex[i] <= row2:
            for j, col in enumerate(row):
                if colIndex[j] >= col1 and colIndex[j] < col2 and col == '|':
                    table[i] = table[i][:j] + ' ' + table[i][j+1:]
        if row.startswith('+'):
            if rowIndex[i] == row1-1 and i == 0:
                table[i] = row[:startCol] + '-'*(endCol-startCol) + row[endCol:]
            elif rowIndex[i] >= row1 and rowIndex[i] < row2:
                table[i] = row[:startCol] + ' '*(endCol-startCol) + row[endCol:]
                if col1 == 0:
                    table[i] = '|' + table[i][1:]
                if col2 == colIndex[-1]:
                    table[i] = table[i][:-1] +'|'
            elif rowIndex[i] == row2 and i == n-1:
                table[i] = row[:startCol] + '-'*(endCol-startCol) + row[endCol:]

    return table

# * Solution 2
def cellsJoining2(table, coords):
    table = list(map(list, table))
    rdivs = [i for i, row in enumerate(table) if row[0] == "+"]
    cdivs = [i for i, col in enumerate(table[0]) if col == "+"]
    x1, y1, x2, y2 = rdivs[coords[1][0]], cdivs[coords[0][1]], rdivs[coords[0][0] + 1], cdivs[coords[1][1] + 1]
    for x in range(x1 + 1, x2):
        if y1 == 0:
            table[x][y1] = "|"
        if y2 == len(table[0]) - 1:
            table[x][y2] = "|"
            
        for y in range(y1 + 1, y2):
            if table[x][y] in "|-+":
                table[x][y] = " "
    
    for y in range(y1 + 1, y2):
        if x1 == 0:
            table[x1][y] = "-"
        if x2 == len(table) - 1:
            table[x2][y] = "-"
    return list(map(lambda x: "".join(x), table))
        


# t1 = ["+----+--+-----+----+",
#          "|abcd|56|!@#$%|qwer|",
#          "|1234|78|^&=()|tyui|",
#          "+----+--+-----+----+",
#          "|zxcv|90|77777|stop|",
#          "+----+--+-----+----+",
#          "|asdf|~~|ghjkl|100$|",
#          "+----+--+-----+----+"]
# c1 = [[2,0], [1,1]]
# r1 = cellsJoining(t1, c1)
# print(r1)

t1 = ["+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+", 
      "|1|1|  |  |  |3|     |4|   |    |5|ggg                                        |", 
      "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+", 
      "| | |11|23|44| |55555| |abc|defg| |                                           |", 
      "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+", 
      "| | |  |  |  | |     | |   |    | |#$%#                                       |", 
      "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+", 
      "| | |  |  |  | |     | |   |    | |!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|", 
      "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+", 
      "|*|*|42|  |  | |     |0|=) |    | |                                           |", 
      "+-+-+--+--+--+-+-----+-+---+----+-+-------------------------------------------+"]
c1 = [[4,0], [0,11]]
r1 = cellsJoining(t1, c1)
print(r1)