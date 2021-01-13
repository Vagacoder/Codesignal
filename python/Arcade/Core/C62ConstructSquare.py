#
# * Core 62. Construct Square
# * Medium

# * Given a string consisting of lowercase English letters, find the largest square number which can be obtained by reordering the string's characters and replacing them with any digits you need (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.

# If there is no solution, return -1.

# * Example

#     For s = "ab", the output should be
#     constructSquare(s) = 81.
#     The largest 2-digit square number with different digits is 81.
#     For s = "zzz", the output should be
#     constructSquare(s) = -1.
#     There are no 3-digit square numbers with identical digits.
#     For s = "aba", the output should be
#     constructSquare(s) = 900.
#     It can be obtained after reordering the initial string into "baa" and replacing "a" with 0 and "b" with 9.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     Guaranteed constraints:
#     1 ≤ s.length < 10.

#     [output] integer

#%%

# * Solution 1
from itertools import permutations

def constructSquare(s):
    n = len(s)
    d_max = int((10**n)**.5)
    d_min = int((10**(n-1))**.5)
    for d in range(d_max, d_min-1, -1):
        num = str(d * d)
        if sorted(s.count(c) for c in set(s)) == sorted(num.count(c) for c in set(num)):
            return int(num)
    return -1    

    


a1 = 'ab'
r1 = constructSquare(a1)
print('ex: {}, an: {}'.format(a1, r1))
