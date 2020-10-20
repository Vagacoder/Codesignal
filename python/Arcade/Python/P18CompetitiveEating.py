#
# * Python 18, Competitve Eating
# * Easy

# * The track of players' time will be kept by a float number. It will be displayed 
# * on the board with the set precision precision with center alignment, and it 
# * is guaranteed that it will fit in the screen. Your task is to test the billboard. 
# * Given the time t, the width of the screen and the precision with which the time 
# * should be displayed, return a string that should be shown on the billboard.

# * Example

# For t = 3.1415, width = 10, and precision = 2,
# the output should be

# competitiveEating(t, width, precision) = "   3.14   "

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] float t

#     The time to be displayed on the billboard. It is guaranteed that t has at most 5 digits after the decimal point.

#     Guaranteed constraints:
#     0 ≤ t < 1000.

#     [input] integer width

#     The width of the billboard. It is guaranteed that it's big enough to display the time t with the desired precision.

#     In case it's impossible to align the time perfectly in the center, left padding should be 1 whitespace character shorter than right padding.

#     Guaranteed constraints:
#     3 ≤ width ≤ 20.

#     [input] integer precision

#     Precision with which the number should be displayed.

#     Guaranteed constraints:
#     0 ≤ precision ≤ 10.

#     [output] string

#     A string of length width representing the time t as it will be displayed on the billboard.

#%%

# * Solution 1
# ! string.center()
def competitiveEating1(t:float, width:int, precision:int)-> str:
    return ('{' + ':0.{}f'.format(precision) + '}').format(t).center(width)


# * Solution 2
# ! string format with order number
def competitiveEating2(t:float, width:int, precision:int)-> str:
    return '{0:.{1}f}'.format(t, precision).center(width)


a1 = 3.1415
a2 = 10
a3 = 2
e1 = '   3.14   '
r1 = competitiveEating2(a1, a2, a3)
print('For {}, expected: {}, result: \'{}\''.format(a1, e1, r1))

a1 = 29.8245
a2 = 10
a3 = 0
e1 = '    30    '
r1 = competitiveEating2(a1, a2, a3)
print('For {}, expected: {}, result: \'{}\''.format(a1, e1, r1))

# %%
