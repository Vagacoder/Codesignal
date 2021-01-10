#
# * Core 60. Is Substitution Cipher
# * Medium

# * A ciphertext alphabet is obtained from the plaintext alphabet by means of 
# * rearranging some characters. For example "bacdef...xyz" will be a simple 
# * ciphertext alphabet where a and b are rearranged.

# * A substitution cipher is a method of encoding where each letter of the plaintext 
# * alphabet is replaced with the corresponding (i.e. having the same index) letter 
# * of some ciphertext alphabet.

# Given two strings, check whether it is possible to obtain them from each other 
# using some (possibly, different) substitution ciphers.

# * Example

#     For string1 = "aacb" and string2 = "aabc", the output should be
#     isSubstitutionCipher(string1, string2) = true.

#     Any ciphertext alphabet that starts with acb... would make this transformation possible.

#     For string1 = "aa" and string2 = "bc", the output should be
#     isSubstitutionCipher(string1, string2) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string string1

#     A string consisting of lowercase English characters.

#     Guaranteed constraints:
#     1 ≤ string1.length ≤ 10.

#     [input] string string2

#     A string consisting of lowercase English characters of the same length as string1.

#     Guaranteed constraints:
#     string2.length = string1.length.

#     [output] boolean

#%%

# * Solution 1
def isSubstitutionCipher(string1:str, string2: str)-> bool:
    n = len(string1)
    sub1to2 = {}
    sub2to1 = {}
    for i in range(n):
        c = string1[i]
        if c not in sub1to2:
            sub1to2[c] = string2[i]
        else:
            if sub1to2[c] != string2[i]:
                return False
        c = string2[i]
        if c not in sub2to1:
            sub2to1[c] = string1[i]
        else:
            if sub2to1[c] != string1[i]:
                return False

    return True
            

# * Solution 2
# ! Smart! 
def isSubstitutionCipher2(string1:str, string2: str)-> bool:
    print(set(zip(string1, string2)))
    print(set(string1))
    print(set(string2))
    return len(set(zip(string1, string2))) == len(set(string1)) == len(set(string2))


a1 = 'aacb'
a2 = 'aabc'
r1 = isSubstitutionCipher2(a1, a2)
print('Ex: {}, Actu: {}'.format(True, r1))

a1 = 'aa'
a2 = 'bc'
r1 = isSubstitutionCipher2(a1, a2)
print('Ex: {}, Actu: {}'.format(False, r1))

a1 = 'aaxyaa'
a2 = 'aazzaa'
r1 = isSubstitutionCipher2(a1, a2)
print('Ex: {}, Actu: {}'.format(False, r1))
