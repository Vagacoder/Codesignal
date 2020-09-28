#
# * Intro 28. Alphabetic Shift
# * Easy

# * Given a string, your task is to replace each of its characters by the next 
# * one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# * Example

# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     A non-empty string consisting of lowercase English characters.

#     Guaranteed constraints:
#     1 ≤ inputString.length ≤ 1000.

#     [output] string

#     The resulting string after replacing each of its characters.

#%%

# * Solution 1
def alphabeticShift1(inputString: str) -> str:
    ordA = ord('a')
    result = ''
    for c in inputString:
        result += chr((ord(c) - ordA + 1) % 26 + ordA)

    return result


# * Solution 2
# ! str.join()
def alphabeticShift2(inputString: str) -> str:
    return "".join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in inputString)



a1 = 'crazy'
e1 = 'dsbaz'
r1 = alphabeticShift2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))


# %%
