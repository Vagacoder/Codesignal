#
# * Intro 35, First Digit

# * Find the leftmost digit that occurs in a given string.

# * Example

#     For inputString = "var_1__Int", the output should be
#     firstDigit(inputString) = '1';
#     For inputString = "q2q-q", the output should be
#     firstDigit(inputString) = '2';
#     For inputString = "0ss", the output should be
#     firstDigit(inputString) = '0'.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     A string containing at least one digit.

#     Guaranteed constraints:
#     3 ≤ inputString.length ≤ 10.

#     [output] char

#%%

# * Solution 1
def firstDigit1(inputString: str)-> str:
    for c in inputString:
        if c.isdigit():
            return c
    return ''


# * Solution 2
# ! Using regex
import re
def firstDigit2(inputString: str)-> str:
    return re.findall('\d', inputString)[0]



a1 = 'var_1__Int'
e1 = 1
r1 = firstDigit2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))



# %%
