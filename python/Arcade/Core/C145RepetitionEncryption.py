#
# * Core 145. Repetition Encryption
#

# Implement the missing code, denoted by ellipses. You may not modify the pre-
# existing code.

# Jane just got a letter from her friend and realized that something's wrong: 
# some words in the letter are written twice in a row. The thing is, she and her 
# friend devised an ingenious cypher, the key to which is the number of pairs of 
# repeated words in the encoded text. The cases of the words don't matter.

# Formally, a word is a substring of letter consisting of English letters, such 
# that characters to the left of the leftmost letter and to the right of the 
# rightmost letter are not letters.

# For obvious reasons, Jane can't tell you how the encryption works, but she needs 
# your help with calculating the number of pairs of consecutive equal words. Write 
# a function that, given a letter, returns this number.

# * Example

# For letter = "Hi, hi Jane! I'm so. So glad to to finally be able to write - 
# WRITE!! - to you!", the output should be repetitionEncryption(letter) = 4.

# There are 4 pairs of consecutive identical words in the text. They are shown in 
# different colors below:
# "Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string letter

#     The letter Jane's friend wrote to her. It is guaranteed that there are no 
#       more than two consecutive equal words in a row. It is also guaranteed that 
#       between two such pairs there are at least two symbols.

#     Guaranteed constraints:
#     1 ≤ letter.length ≤ 250.

#     [output] integer

#     The number of pairs of consecutive equal words in the letter.

#%%

import re

# * Solution 1
# ! not working 2nd test case
def repetitionEncryption(letter):
    pattern = r'(\w+)(\W+)\1(?:$|[\W])'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    return len(re.findall(regex, letter))


# * Solution 2
def repetitionEncryption2(letter):
    pattern = '([a-z]+)[^a-z]+\\1(?:$|[^a-z])'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    return len(re.findall(regex, letter))



l1 = "Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"
r1 = repetitionEncryption(l1)
print(r1)

l1 = "let's s?,play%3with,1symbols88,/symbols"
r1 = repetitionEncryption(l1)
print(r1)

