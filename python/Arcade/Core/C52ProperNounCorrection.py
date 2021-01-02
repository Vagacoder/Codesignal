#
# * Core 52, Proper Noun Correction
# * Easy

# * Proper nouns always begin with a capital letter, followed by small letters.

# Correct a given proper noun so that it fits this statement.

# * Example

#     For noun = "pARiS", the output should be
#     properNounCorrection(noun) = "Paris";
#     For noun = "John", the output should be
#     properNounCorrection(noun) = "John".

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string noun

#     A string representing a proper noun with a mix of capital and small English letters.

#     Guaranteed constraints:
#     1 ≤ noun.length ≤ 10.

#     [output] string

#     Corrected (if needed) noun.

#%%

# * Solution 1
def properNounCorrection(noun:str)-> str:
    return noun.capitalize()


a1 = 'pArIS'
r1 = properNounCorrection(a1)
print(r1)
