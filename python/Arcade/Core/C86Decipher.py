#
# * Core 86, Decipher
# * Easy

# * Consider the following ciphering algorithm:

#     For each character replace it with its code.
#     Concatenate all of the obtained numbers.

# Given a ciphered string, return the initial one if it is known that it consists 
# only of lowercase letters.

# Note: here the character's code means its decimal ASCII code, the numerical 
# representation of a character used by most modern programming languages.

# Example

# For cipher = "10197115121", the output should be
# decipher(cipher) = "easy".

# Explanation: charCode('e') = 101, charCode('a') = 97, charCode('s') = 115 and 
# charCode('y') = 121.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string cipher

#     A non-empty string which is guaranteed to be a cipher for some other string 
# of lowercase letters.

#     Guaranteed constraints:
#     2 ≤ cipher.length ≤ 100.

#     [output] string

#%%

# * Solution 1
def decipher(cipher: str)-> str:
    n = len(cipher)
    i = 0
    minCode = 97
    maxCode = 122
    result = ''
    while i < n:
        curCode = cipher[i:i+2]
        step = 2
        if int(curCode) < 97:
            curCode = cipher[i:i+3]
            step = 3
        
        result += chr(int(curCode))
        i += step

    return result



a1 = '10197115121'
r1 = decipher(a1)
print(r1)

a1 = '10297115106108102108971061151041029897107106115981001029710711510010298'
r1 = decipher(a1)
print(r1)