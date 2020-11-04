#
# * Python 60 Pref Sum
# * Easy

# * There is a great technique that allows finding sums of consecutive elements 
# * in the given array extremely fast. It is based on the usage of prefix sums. 
# * Given array a, your task is to calculate all its prefix sums.

# * Example

# For a = [1, 2, 3], the output should be
# prefSum(a) = [1, 3, 6].

# Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Guaranteed constraints:
#     2 ≤ a.length ≤ 3 · 104,
#     -1000 ≤ a[i] ≤ 1000.

#     [output] array.integer

#%%

# * Solution 1

def prefSum1(a:list)->list:
    return [sum(a[:i+1]) for i in range(len(a))]


# * Solution 2
from functools import reduce
def prefSum2(a:list)->list:
    return [reduce(lambda i, j: i+j, a[:i+1]) for i in range(len(a))]


# * Solution 3
from itertools import accumulate
def prefSum3(a:list)->list:
    return list(accumulate(a))


# * Solution 4
# ! Important
def prefSum4(a:list)->list:
    return [ [a,a.append(x+a.pop())][0][-1] for x in [a,a.append(0),a][0][:-1] ]


a1 = [1, 2, 3]
r1 = prefSum4(a1)
print(r1)

# %%
