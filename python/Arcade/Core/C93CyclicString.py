#
# * Core 93, Cyclic String
# * Medium

# * You're given a substring s of some cyclic string. What's the length of the 
# * smallest possible string that can be concatenated to itself many times to 
# * obtain this cyclic string?

# * Example

# For s = "cabca", the output should be
# cyclicString(s) = 3.

# "cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained 
# by concatenating "abc" to itself. Thus, the answer is 3.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     Guaranteed constraints:
#     3 ≤ s.length ≤ 15.

#     [output] integer

#%%

# * Solution 1
def cyclicString(s: str) -> int:
    
    def removeExtra(s1: str) -> str:
        index = -1
        n = len(s1)
        for i in range(1, n):
            curStr = s1[:i]
            if s1.endswith(curStr):
                if i != n-1:
                    index = i
                else:
                    if index >= 0:
                        index = i
        if index >= 0:
            return s1[index:]
        else:
            return s1

    return len(removeExtra(s))


# * Solution 2
def cyclicString2(s: str) -> int:
    c = 1
    while (s[:c]*len(s))[:len(s)]!=s: c += 1
    return c    


a1 = 'cabca'
r1 = cyclicString(a1)
print(r1)

a1 = 'aba'
r1 = cyclicString(a1)
print(r1)

a1 = 'cccccc'
r1 = cyclicString(a1)
print(r1)

a1 = 'bcaba'
r1 = cyclicString(a1)
print(r1)

a1 = 'abacabaabacab'
r1 = cyclicString(a1)
print(r1)

# %%

