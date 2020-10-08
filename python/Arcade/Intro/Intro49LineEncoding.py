#
# * Intro 49, Line Encoding
# * Medium

# * Given a string, return its encoding defined as follows:

#     First, the string is divided into the least possible number of disjoint 
#     substrings consisting of identical characters.
#         for example, "aabbbc" is divided into ["aa", "bbb", "c"]

#     Next, each substring with length greater than one is replaced with a 
#     concatenation of its length and the repeating character.
#         for example, substring "bbb" is replaced by "3b"

#     Finally, all the new strings are concatenated together in the same order 
#     and a new string is returned.

# * Example

# For s = "aabbbc", the output should be
# lineEncoding(s) = "2a3bc".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     String consisting of lowercase English letters.

#     Guaranteed constraints:
#     4 ≤ s.length ≤ 15.

#     [output] string

#     Encoded version of s.

#%%

# * Solution 1
def lineEncoding1(s:str)->str:
    n = len(s)
    j = 0
    coding = []
    for i in range(n):
        if s[i] == s[j]:
            pass
        else:
            coding.append((s[j], (i-j)))
            j = i

    if j < n:
        coding.append((s[j], (n-j)))

    result = ''

    for t in coding:
        if t[1] != 1:
            result += str(t[1]) + t[0]
        else:
            result += t[0]

    return result


# * Solution 2
# ! using itertools.groupby
from itertools import groupby

def lineEncoding2(s:str)-> str:
    result = ''
    for count, group in groupby(s):
        y = len(list(group))
        if y == 1:
            result += count
        else:
            result += str(y) + count

    return result


# * Solution 3
import re

# ! Great solution using regex
def lineEncoding3(s):
    return re.sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(1), s)



a1 = 'aabbbc'
e1 = '2a3bc'
r1 = lineEncoding3(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))


# %%
