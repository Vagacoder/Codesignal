#
# * Core 141. N-th Number

# You are given a string s of characters that contains at least n numbers (here, 
# a number is defined as a consecutive series of digits, where any character 
# immediately to the left and right of the series are not digits). The numbers 
# may contain leading zeros, but it is guaranteed that each number has at least 
# one non-zero digit in it.

# Your task is to find the nth number and return it as a string without leading 
# zeros.

# * Example

# For s = "8one 003number 201numbers li-000233le number444" and n = 4,
# the output should be
# nthNumber(s, n) = "233".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     A string containing at least n numbers.

#     Guaranteed constraints:
#     20 ≤ s.length ≤ 650.

#     [input] integer n

#     1-based index of the number to find.

#     Guaranteed constraints:
#     1 ≤ n ≤ 15.

#     [output] string

#     The nth number without leading zeros.

#%%

import re

# * Solution 1
# ! ?: Non-capture version of parenthesis
def nthNumber(s: str, n: int)-> str:
    pattern = r"(?:[^1-9]*([0-9]+)){"+str(n)+"}"
    return re.match(pattern, s).group(1)


# * Solution 2
def nthNumber2(s: str, n: int)-> str:
    pattern = r"([^1-9]*([0-9]+)){"+str(n)+"}"
    return re.match(pattern, s).group(2)


s1 = '8one 003number 201numbers li-000233le number444'
n1 = 4
r1 = nthNumber(s1, n1)
print(r1)
