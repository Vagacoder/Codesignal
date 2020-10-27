#
# * Python 39, Least Common Denominator
# * Easy

# * You need to sum up a bunch of fractions that have different denominators. In 
# * order to do this, you need to find the least common denominator of all the 
# * fractions. As a professional programmer, you know that the least common 
# * denominator is in fact their LCM.

# For the given list of denominators, find the least common denominator by finding their LCM.

# * Example

# For denominators = [2, 3, 4, 5, 6], the output should be
# leastCommonDenominator(denominators) = 60.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer denominators

#     The list of denominators, where each denominator is a positive integer.

#     Guaranteed constraints:
#     1 ≤ denominators.length ≤ 10,
#     2 ≤ denominators[i] ≤ 50.

#     [output] integer

#     The least common denominator.




#%%
from fractions import gcd
import functools

# * Solution 1
# ! functools.reduce()
def leastCommonDenominator(denominators):
    return functools.reduce(lambda a, b: a*b/gcd(a,b), denominators)


a1 = [2, 3, 4, 5, 6]
r1 = leastCommonDenominator(a1)
print(r1)

# %%
