#
# * Core 103 Draw Rectangle
# * Medium

# You are implementing a command-line version of the Paint app. Since the command 
# line doesn't support colors, you are using different characters to represent 
# pixels. Your current goal is to support rectangle x1 y1 x2 y2 operation, which 
# draws a rectangle that has an upper left corner at (x1, y1) and a lower right 
# corner at (x2, y2). Here the x-axis points from left to right, and the y-axis 
# points from top to bottom.

# Given the initial canvas state and the array that represents the coordinates of 
# the two corners, return the canvas state after the operation is applied. For 
# the details about how rectangles are painted, see the example.

# * Example

# For

# canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#           ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#           ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#           ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
#           ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

# and rectangle = [1, 1, 4, 3], the output should be

# drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
#                   					['a', '*', '-', '-', '*', 'a', 'a', 'a'],
#                   					['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
#                   					['b', '*', '-', '-', '*', 'b', 'b', 'b'],
#                   					['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

# Here is the rectangle, colored for illustration:


# [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
# ['a', '*', '-', '-', '*', 'a', 'a', 'a'],
# ['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
# ['b', '*', '-', '-', '*', 'b', 'b', 'b'],
# ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

# Note that rectangle sides are depicted as -s and |s, asterisks (*) stand for its corners and all of the other "pixels" remain the same.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.array.char canvas

#     A non-empty rectangular matrix of characters.

#     Guaranteed constraints:
#     2 ≤ canvas.length ≤ 10,
#     2 ≤ canvas[0].length ≤ 10.

#     [input] array.integer rectangle

#     Array of four integers - [x1, y1, x2, y2].

#     Guaranteed constraints:
#     0 ≤ x1 < x2 < canvas[i].length,
#     0 ≤ y1 < y2 < canvas.length.

#     [output] array.array.char

#%%

# * Solution 1
def drawRectangle(canvas: list, rectangle: list)-> list:
    x1, y1, x2, y2 = rectangle
    # print(x1, y1, x2, y2)

    # * Draw top and bottom lines
    for i in range(x1, x2+1):
        if i == x1 or i == x2:
            canvas[y1][i] = '*'
            canvas[y2][i] = '*'
        else:
            canvas[y1][i] = '-'
            canvas[y2][i] = '-'

    # * Draw left and right lines
    for i in range(y1+1, y2):
        canvas[i][x1] = '|'
        canvas[i][x2] = '|'

    return canvas


a1 = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
      ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
      ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
      ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
      ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
b1 = [1, 1, 4, 3]
r1 = drawRectangle(a1, b1)
print(r1)

