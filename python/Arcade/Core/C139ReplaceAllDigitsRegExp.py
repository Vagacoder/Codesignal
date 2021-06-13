#
# * Core 139. Replace All Digits RegExp
# 

# * Implement the missing code, denoted by ellipses. You may not modify the pre-
# * existing code.

# Implement a function that replaces each digit in the given string with a '#' 
# character.

# * Example

# For input = "There are 12 points", the output should be
# replaceAllDigitsRegExp(input) = "There are ## points".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string input

#     Guaranteed constraints:
#     5 ≤ input.length ≤ 20.

#     [output] string

#%%

# * Solution 1
import re
def replaceAllDigitsRegExp(inputString: str)-> str:
    return re.sub('\d', '#', inputString)


a1 = 'There are 12 points' 
r1 = replaceAllDigitsRegExp(a1)
print(r1)


