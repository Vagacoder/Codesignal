#
# * Intro 58, Message from Binary Code
# * Medium

# * You are taking part in an Escape Room challenge designed specifically for 
# * programmers. In your efforts to find a clue, you've found a binary code written 
# * on the wall behind a vase, and realized that it must be an encrypted message. 
# * After some thought, your first guess is that each consecutive 8 bits of the 
# * code stand for the character with the corresponding extended ASCII code.

# * Assuming that your hunch is correct, decode the message.

# * Example

# For code = "010010000110010101101100011011000110111100100001", the output should be
# messageFromBinaryCode(code) = "Hello!".

# The first 8 characters of the code are 01001000, which is 72 in the binary 
# numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
# Other letters can be obtained in the same manner.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string code

#     A string, the encrypted message consisting of characters '0' and '1'.

#     Guaranteed constraints:
#     0 < code.length < 800.

#     [output] string

#     The decrypted message.

#%%

# * Solution 1
def messageFromBinaryCode(code: str)-> str:
    # letters = [chr(int(code[x:x+8], 2)) for x in range(0, len(code), 8)]
    return ''.join([chr(int(code[x:x+8], 2)) for x in range(0, len(code), 8)])

a1 = '010010000110010101101100011011000110111100100001'
e1 = 'Hello!'
r1 = messageFromBinaryCode(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
