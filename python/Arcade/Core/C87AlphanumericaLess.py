#
# * Core 87, Alphanumerica Less
# * Medium

# * An alphanumeric ordering of strings is defined as follows: each string is 
# * considered as a sequence of tokens, where each token is a letter or a number 
# * (as opposed to an isolated digit, as is the case in lexicographic ordering). 
# * For example, the tokens of the string "ab01c004" are [a, b, 01, c, 004]. In 
# * order to compare two strings, we'll first break them down into tokens and 
# * then compare the corresponding pairs of tokens with each other (i.e. compare 
# * the first token of the first string with the first token of the second string, 
# * etc).

# Here is how tokens are compared:

#     If a letter is compared with another letter, the usual alphabetical order 
#       applies.
#     A number is always considered less than a letter.
#     When two numbers are compared, their values are compared. Leading zeros, if 
#       any, are ignored.

# If at some point one string has no more tokens left while the other one still 
# does, the one with fewer tokens is considered smaller.

# If the two strings s1 and s2 appear to be equal, consider the smallest index i 
# such that tokens(s1)[i] and tokens(s2)[i] (where tokens(s)[i] is the ith token 
# of string s) differ only by the number of leading zeros. If no such i exists, 
# the strings are indeed equal. Otherwise, the string whose ith token has more 
# leading zeros is considered smaller.

# Here are some examples of comparing strings using alphanumeric ordering.

# "a" < "a1" < "ab"
# "ab42" < "ab000144" < "ab00144" < "ab144" < "ab000144x"
# "x11y012" < "x011y13"

# Your task is to return true if s1 is strictly less than s2, and false otherwise.

# Example

#     For s1 = "a" and s2 = "a1", the output should be alphanumericLess(s1, s2) 
#       = true;

#     These strings have equal first tokens, but since s1 has fewer tokens than 
#       s2, it's considered smaller.

#     For s1 = "ab" and s2 = "a1", the output should be alphanumericLess(s1, s2) 
#       = false;

#     These strings also have equal first tokens, but since numbers are considered 
#       less than letters, s1 is larger.

#     For s1 = "b" and s2 = "a1", the output should be alphanumericLess(s1, s2) 
#       = false.

#     Since b is greater than a, s1 is larger.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s1

#     A string consisting of English letters and digits.

#     Guaranteed constraints:
#     1 ≤ s1.length ≤ 20.

#     [input] string s2

#     A string consisting of English letters and digits.

#     Guaranteed constraints:
#     1 ≤ s2.length ≤ 20.

#     [output] boolean

#     true if s1 is alphanumerically strictly less than s2, false otherwise.

#%%

# * Solution 1
# ! Bad idea
def alphanumericLess(s1: str, s2: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    i1 = 0
    i2 = 0
    while i1 < n1 and i2 < n2:
        # * both are digit
        if s1[i1].isdigit() and s2[i2].isdigit():
            j1 = i1
            j2 = i2
            n1str = ''
            n2str = ''
            while i1 < n1 and s1[i1].isdigit():
                n1str += s1[i1]
                i1 += 1
            while i2 < n2 and s2[i2].isdigit():
                n2str += s2[i2]
                i2 += 1
            if int(n1str) > int(n2str):
                return False
            elif int(n1str) == int(n2str):
                if (i1 - j1) <= (i2 - j2):
                    return False
            
        else:
            if s1[i1] > s2[i2]:
                return False
            else:
                i1 += 1
                i2 += 1

    return n1 <= n2


a1 = 'a'
a2 = 'a1'
a3 = 'ab'
a4 = 'ab42'
a5 = 'ab000144'
a6 = 'ab00144'

r1 = alphanumericLess(a1, a2)
print('ex: {}, ar: {}'.format(True, r1))

r2 = alphanumericLess(a2, a3)
print('ex: {}, ar: {}'.format(True, r2))

r3 = alphanumericLess(a3, a4)
print('ex: {}, ar: {}'.format(True, r3))

r4 = alphanumericLess(a4, a5)
print('ex: {}, ar: {}'.format(True, r4))

r5 = alphanumericLess(a5, a6)
print('ex: {}, ar: {}'.format(True, r5))

a7 = 'x11y012'
a8 = 'x011y13'

r6 = alphanumericLess(a7, a8)
print('ex: {}, ar: {}'.format(True, r6))

a9 = '0000'
a10 = '000'
r7 = alphanumericLess(a9, a10)
print('ex: {}, ar: {}'.format(True, r7))
