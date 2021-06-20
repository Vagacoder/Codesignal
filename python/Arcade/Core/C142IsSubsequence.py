#
# * Core 142. Is Subsequence

# Given a string s, determine if it is a subsequence of a given string t.

# * Example

#     For t = "CodeSignal" and s = "CoSi", the output should be
#     isSubsequence(t, s) = true;

#     For t = "CodeSignal" and s = "cosi", the output should be
#     the output should be
#     isSubsequence(t, s) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string t

#     A string consisting of English letters, whitespace characters (' '), digits and punctuation marks (".,?!=*+-").

#     Guaranteed constraints:
#     0 ≤ t.length ≤ 500.

#     [input] string s

#     A string consisting of English letters, whitespace characters (' '), digits and punctuation marks (".,?!=*+-").

#     Guaranteed constraints:
#     0 ≤ s.length ≤ 50.

#     [output] boolean

#     true if the s is a subsequence of t, false otherwise.

#%%

import re

# * Solution 1
# ! Not working:
# ! 1: not starting with '.*'
# ! 2: need [] 
def isSubsequence(t:str, s:str) -> bool:
    pattern = ''
    for ch in s:
        pattern += r".*{}.*".format(ch)

    print(pattern)
    return re.search(pattern, t) is not None


# * Solution 2
def isSubsequence2(t:str, s:str) -> bool:
    pattern = ''
    for ch in s:
        pattern += '['+ch+'].*'

    print(pattern)
    return re.search(pattern, t) is not None

# t1 = 'Codesignal'
# s1 = 'Cosi'
# r1 = isSubsequence(t1, s1)
# print(r1)

# t1 = 'Codesignal'
# s1 = 'cosi'
# r1 = isSubsequence(t1, s1)
# print(r1)

t1 = 'he sd.f dsk e8.sd??l**23, 23,f.s++83+'
s1 = 'h  8.?*3+'
r1 = isSubsequence2(t1, s1)
print(r1)

t1 = 'abc'
s1 = 'd'
r1 = isSubsequence2(t1, s1)
print(r1)
