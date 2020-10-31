#
# * Python 50, Float Range
# * Easy

# * As you may know, the range function in Python allows coders to iterate over 
# * elements from start to stop with the given step. Unfortunately it works only 
# * for integer values, and additional libraries should be used if a programmer 
# * wants to use float values.

# * CodeSignal doesn't include third-party libraries, so you have to make do with 
# * the standard ones. Given float numbers start, stop and step, your task is to 
# * return a list of values from start to stop (including start and not including 
# * stop), evenly spaced by the step.

# * Values start, stop and step have at most 5 digits after the decimal point each.

# * Example

# For start = -0.9, stop = 0.45, and step = 0.2,
# the output should be
# floatRange(start, stop, step) = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] float start

#     Guaranteed constraints:
#     -1000 ≤ start ≤ stop ≤ 1000.

#     [input] float stop

#     Guaranteed constraints:
#     -1000 ≤ start ≤ stop ≤ 1000.

#     [input] float step

#     Guaranteed constraints:
#     0.05 ≤ step ≤ 1000.

#     [output] array.float

#     A list of values in range [start, stop), spaced by the step.

#%%

# * Solution 1
from itertools import accumulate

def floatRange1(start, stop, step):
    gen = accumulate([start]*(int)((stop-start)//step+1), lambda a, x: a+step)
    return list(gen)


# * Solution 2
from itertools import takewhile, count

def floatRange2(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)



a1 = -0.9
a2 = 0.45
a3 = 0.2
r1 = floatRange2(a1, a2, a3)
print(r1)
# %%
