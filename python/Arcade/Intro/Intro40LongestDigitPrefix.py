#
# * Intro 40, Longest Digits Prefix

# * Given a string, output its longest prefix which contains only digits.

# * Example

# For inputString = "123aa1", the output should be
# longestDigitsPrefix(inputString) = "123".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Guaranteed constraints:
#     3 ≤ inputString.length ≤ 100.

#     [output] string


#%%

# * Solution 1
def longestDigitsPrefix1(inputString:str)->str:
    for i, c in enumerate(inputString):
        if not c.isdigit():
            return inputString[:i]

    return inputString


# * Solution 2
# ! use regex
import re

def longestDigitsPrefix2(inputString:str)->str:
    return re.findall('^\d*', inputString)[0]



a1 = '123aa1'
e1 = '123'
r1 = longestDigitsPrefix2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
