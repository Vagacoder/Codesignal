#
# * Python 17, Permutation Cipher
# * Easy

# * You found your very first laptop in the attic, and decided to give in to 
# * nostalgia and turn it on. The laptop turned out to be password protected, 
# * but you know how to crack it: you have always used the same password, but 
# * encrypt it using permutation ciphers with various keys. The key to the cipher 
# * used to protect your old laptop very conveniently happened to be written on 
# * the laptop lid.

# Here's how permutation cipher works: the key to it consists of all the letters 
# of the alphabet written up in some order. All occurrences of letter 'a' in the 
# encrypted text are substituted with the first letter of the key, all occurrences 
# of letter 'b' are replaced with the second letter from the key, and so on, up 
# to letter 'z' replaced with the last symbol of the key.

# Given the password you always use, your task is to encrypt it using the permutation 
# cipher with the given key.

# * Example

# For password = "iamthebest" and
# key = "zabcdefghijklmnopqrstuvwxy", the output should be
# permutationCipher(password, key) = "hzlsgdadrs".

# Here's a table that can be used to encrypt the text:

# abcdefghijklmnopqrstuvwxyz
# ||  |  ||   |     || 
# vv  v  vv   v     vv
# zabcdefghijklmnopqrstuvwxy

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string password

#     The password you always use. It is guaranteed to consist only of lowercase 
#       English letters.
#     If you're using Python 2, note that the string is given as a unicode.

#     Guaranteed constraints:
#     1 ≤ password.length ≤ 26.

#     [input] string key

#     The key to the permutation cipher. It is guaranteed to be a permutation of 
#       the plaintext alphabet.
#     If you're using Python 2, note that the string is given as a unicode.

#     Guaranteed constraints:
#     key.length = 26.

#     [output] string

#     Your password encrypted by the permutations cipher with the given key.

#%%

# * Solution 1
# ! string.translate(), string.maketrans()
def permutationCipher1(password:str, key:str)->str:
    table = {ord(c): key[ord(c)-ord('a')] for c in password} 
    print(table)
    return password.translate(table)


# * Solution 2
import string

def permutationCipher2(password:str, key:str)->str:
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)


# * Solution 3
# ! for python 2, nice table
def permutationCipher3(password:str, key:str)->str:
    table = ' '*97+key
    return str(password).translate(table)




a1 = 'iamthebest'
a2 = 'zabcdefghijklmnopqrstuvwxy'
e1 = 'hzlsgdadrs'
r1 = permutationCipher2(a1, a2)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
