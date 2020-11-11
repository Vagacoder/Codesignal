#
# * Python 72, Try Functions
# * Easy

# * You've been working on a numerical analysis when something went horribly wrong: 
# * your solution returned completely unexpected results. It looks like you apply 
# * a wrong function at some point of calculation. This part of the program was 
# * implemented by your colleague who didn't follow the PEP standards, so it's 
# * extremely difficult to comprehend.

# To understand what function is applied to x instead of the one that should have 
# been applied, you decided to go ahead and compare the result with results of 
# all the functions you could come up with. Given the variable x and a list of 
# functions, return a list of values f(x) for each x in functions.

# * Example

# For x = 1 and
# functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"],
# the output should be
# tryFunctions(x, functions) = [0.84147, 0.5403, 2, 1].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] float x

#     The value to which the functions should be applied. It is guaranteed to have 
#       at most 1 digit after the decimal point.

#     Guaranteed constraints:
#     -1000 ≤ x ≤ 1000.

#     [input] array.string functions

#     Array of functions. Each function is given as a string. It is guaranteed 
#       that the result of applying function eval to functions[i] produces a valid 
#       function for each i. It is also guaranteed that eval(functions[i]) is 
#       defined in point x for each i.

#     Guaranteed constraints:
#     1 ≤ functions.length ≤ 10.

#     [output] array.float

#     A list of the same length as functions, where the ith element is the result 
#       of applying the ith function to x. Your output will be considered correct 
#       if its absolute error does not exceed 10-5.

#%%

import math

# * Solution 1
# ! eval(func)(arguments)
def tryFunctions1(x, functions):
    return [eval(func)(x) for func in functions]


functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]
x = 1
r1 = tryFunctions1(x, functions)
print(r1)

# %%
