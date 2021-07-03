#
# * Core 148. HTML Table

# HTML tables allow web developers to arrange data into rows and columns of cells. 
# They are created using the <table> tag. Its content consists of one or more rows 
# denoted by the <tr> tag. Further, the content of each row comprises one or more 
# cells denoted by the <td> tag, and content within the <td> tags is what site 
# visitors see in the table. For this task assume that tags have no attributes in 
# contrast to real world HTML.

# Some tables contain the <th> tag. This tag defines header cells, which shouldn't 
# be counted as regular cells.

# You are given a rectangular HTML table. Extract the content of the cell with 
# coordinates (row, column).

# If you are not familiar with HTML, check out this note.

# * Example

#     For table = "<table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td>
#       <td>FoUr4</td></tr></table>", row = 0, and column = 1, the output should be
#     htmlTable(table, row, column) = "TWO".

#     <table>
#      <tr>
#       <td>1</td>
#       <td>TWO</td>
#      </tr>
#      <tr>
#       <td>three</td>
#       <td>FoUr4</td>
#      </tr>
#     </table>

#     corresponds to:
#     1	TWO
#     three	FoUr4

#     For table = "<table><tr><td>1</td><td>TWO</td></tr></table>", row = 1, and 
#       column = 0, the output should be
#     htmlTable(table, row, column) = "No such cell".

#     <table>
#      <tr>
#       <td>1</td>
#       <td>TWO</td>
#      </tr>
#     </table>

#     corresponds to:
#     1	TWO

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string table

#     A syntactically correct representation of a rectangular HTML table with at 
#       least one cell. Each of its cells contains only letters and/or digits.

#     Guaranteed constraints:
#     35 ≤ table.length ≤ 1600.

#     [input] integer row

#     A non-negative integer representing 0-based index of the desired row (rows 
#       are numbered from top to bottom).

#     Guaranteed constraints:
#     0 ≤ row ≤ 10.

#     [input] integer column

#     A non-negative integer representing 0-based index of the desired column (
#       columns are numbered from left to right).

#     Guaranteed constraints:
#     0 ≤ column ≤ 10.

#     [output] string

#     The content of the cell with coordinates (row, column) or the string "No 
#       such cell" if there is no cell with those coordinates in the table.

#%%

# * Solution 1
def htmlTable(table: str, row: int, column: int):
    r = 0
    tokens = table.split('><')
    # print(tokens)
    for i, token in enumerate(tokens):
        if r == row and token == 'tr' and tokens[i+1][:2] == 'td':
            # * check if still inside same row
            for j in range(i+1, i+column+2):
                if tokens[j][:2] != 'td':
                    return 'No such cell'
            return tokens[i+column+1][3:-4]

        if token == 'tr':
            r += 1
        
    return 'No such cell'


# * Solution 2
def htmlTable2(t, r, c):
    
    try:
        t = t.split('<tr>')[r+1]
        t = t.split('<td>')[c+1]
        return t[:t.find('</')]
    except:
        return 'No such cell'
    

t1 = "<table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td><td>FoUr4</td></tr></table>"
r1 = 0
c1 = 1
re1 = htmlTable(t1, r1, c1)
print(re1)

t1 = "<table><tr><th>CIRCUMFERENCE</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr><tr><td>BITS</td><td>3</td><td>4</td><td>8</td><td>10</td><td>12</td><td>15</td></tr></table>"
r1 = 0
c1 = 6
re1 = htmlTable(t1, r1, c1)
print(re1)
