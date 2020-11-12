#
# * Python 75. Simple Composition
# * Easy

# * In computer science, function composition is a mechanism of combining simple 
# * functions to build more complicated ones. Here's the deal: your colleague 
# * working on the databases implemented a low-level API that you have to deal 
# * with, and there's no way for you to update it and make it more sophisticated 
# * (or simply useful). Now you need to make a function that will be able to 
# * combine low-level functions into a single one using the function composition.

# Given two functions f and g that you need to combine and a variable x, return 
# the result of the applying the function to x, i.e. f(g(x)).

# * Example

# For f = "math.log10", g = "abs", and x = -100,
# the output should be
# simpleComposition(f, g, x) = 2.

# math.log10(abs(x)) = log10(abs(-100)) = log10(100) = 2.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string f

#     A function given as a string. It is guaranteed that the result of applying 
#       function eval to f produces a valid function. It is also guaranteed that 
#       eval(f) is defined in point x.

#     [input] string g

#     A function in the same format as f.

#     [input] float x

#     The argument of the functions. It is guaranteed to have at most 1 digit 
#       after the decimal point.

#     Guaranteed constraints:
#     -1000 ≤ x ≤ 1000.

#     [output] float

#     The result of applying composition of functions f and g to x. Your output 
#       will be considered correct if its absolute error does not exceed 10-5.

#%%
import math

# * Solution 1

# ! eval() and function compostion
def compose(f, g):
    return lambda x: f(g(x))

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)


f = 'math.log10'
g = 'abs'
x = -100
r1 = simpleComposition(f, g, x)
print(r1)


# %%
