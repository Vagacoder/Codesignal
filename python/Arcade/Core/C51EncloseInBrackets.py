#
# * Core 51, Enclose in Brackets
# * Easy

# * Given a string, enclose it in round brackets.

# * Example

# For inputString = "abacaba", the output should be
# encloseInBrackets(inputString) = "(abacaba)".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Guaranteed constraints:
#     0 ≤ inputString.length ≤ 10.

#     [output] string

#%%

# * Solution 1
def encloseInBrackets(inputString: str)-> str:
    return '(' + inputString + ')'


a1 = 'ababcaba'
r1 = encloseInBrackets(a1)
print(r1)
