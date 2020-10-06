#
# * Intro 45, Build Palindrome

# * Given a string, find the shortest possible string which can be achieved by 
# * adding characters to the end of initial string to make it a palindrome.

# * Example

# For st = "abcdc", the output should be
# buildPalindrome(st) = "abcdcba".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string st

#     A string consisting of lowercase English letters.

#     Guaranteed constraints:
#     3 ≤ st.length ≤ 10.

#     [output] string

#%%

# * Solution 1
def buildPalidrome(st: str)->str:
    for l in range(len(st)):
        addon = st[:l]
        newSt = st + addon[::-1]
        if newSt == newSt[::-1]:
            return newSt



a1 = 'abcdc'
e1 = 'abcdcba'
r1 = buildPalidrome(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))



# %%
