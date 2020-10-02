#
# * Intro 36. Different Symbol Naive
# * Easy

# * Given a string, find the number of different characters in it.

# * Example

# For s = "cabca", the output should be
# differentSymbolsNaive(s) = 3.

# There are 3 different characters a, b and c.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     A string of lowercase English letters.

#     Guaranteed constraints:
#     3 ≤ s.length ≤ 1000.

#     [output] integer

#%%

# * Solution 1
def differentSymbolNaive1(s: str)->int:
    return len(set(x for x in s))


# * Solution 2
# ! Shortcut
def differentSymbolNaive2(s: str)->int:
    return len(set(s))


a1 ='cabca'
e1 = 3
r1 = differentSymbolNaive2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
