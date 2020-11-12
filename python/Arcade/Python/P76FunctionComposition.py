#
# * Python 76. Function Composition
# * Easy

# * As a professional and respected database programmer, you implemented a low-
# * level API for your front-end colleagues to use. One of them, however, appeared 
# * to be quite an ungrateful exemplar, and had the nerve to criticize your work: 
# * it seems to him that the functionality your API provides is too basic, and he 
# * has to implement several additional functions on his end to make things work.

# You don't like to leave the users of your ingenious work disgruntled, so you 
# have to update your API. It can be done quite simple: most of the high-level 
# functionality can be added by combining several basic functions. Now you need 
# to implement a function that will compose an arbitrary number of functions, and 
# test it on some variable x.

# * Example

# For functions = ["abs", "math.sin", "lambda x: 3 * x / 2"]
# and x = 3.1415, the output should be
# functionsComposition(functions, x) = 1.

# abs(math.sin(3 * 3.1415 / 2)) = abs(sin(4.71225)) ≈ abs(-1) = 1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string functions

#     Array of functions. Each function is given as a string. It is guaranteed 
#       that the result of applying function eval to functions[i] produces a valid 
#       function for each i. It is also guaranteed that functions[0](functions[1]
#       (functions[2](...(functions[functions.length - 1])...))) is defined in point x.

#     Guaranteed constraints:
#     1 ≤ functions.length ≤ 10.

#     [input] float x

#     The value to which the functions should be applied. It is guaranteed that 
#       it contains at most 4 digits after the decimal point.

#     Guaranteed constraints:
#     -1000 ≤ x ≤ 1000.

#     [output] float

#     The value obtained by applying composition of functions to x. Your output 
#       will be considered correct if its absolute error does not exceed 10-5.

#%%

import math
from functools import reduce

# * Solution 1
# ! function composition and reduce
def compose(functions):
    return reduce(lambda f, g: lambda x : f(g(x)), functions)

def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)


functions = ["abs", "math.sin", "lambda x: 3 * x / 2"]
x = 3.1415
r1 = functionsComposition(functions, x)
print(r1)

# %%
