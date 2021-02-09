#
# * Core 81, Reflect String
# * Easy

# * Define an alphabet reflection as follows: a turns into z, b turns into y, c 
# * turns into x, ..., n turns into m, m turns into n, ..., z turns into a.

# * Define a string reflection as the result of applying the alphabet reflection 
# * to each of its characters.

# Reflect the given string.

# * Example

# For inputString = "name", the output should be
# reflectString(inputString) = "mznv".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     A string of lowercase characters.

#     Guaranteed constraints:
#     3 ≤ inputString.length ≤ 1000.

#     [output] string

#%%

# * Solution 1
def reflectString(inputString: str)-> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([alphabet[26-alphabet.index(c)-1] for c in inputString])


a1 = 'name'
r1 = reflectString(a1)
print(r1)
