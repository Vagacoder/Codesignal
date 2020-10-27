#
# * Python 41, Unique Characters
# * Easy

# * You need to compress a large document that consists of a small number of 
# * different characters. To choose the best encoding algorithm, you would like 
# * to look closely at the characters that comprise this document.

# * Given a document, return an array of all unique characters that appear in it 
# * sorted by their ASCII codes.

# * Example

# For document = "Todd told Tom to trot to the timber",
# the output should be
# uniqueCharacters(document) = [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't'].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string document

#     A string consisting of English letters, whitespace characters and punctuation marks.

#     Guaranteed constraints:
#     1 ≤ document.length ≤ 80.

#     [output] array.char

#     A sorted array of all the unique characters that appear in the document.


#%%

# * Solution 1
# ! Difference between sorted() and list.sort()
def uniqueCharacters(document):
    return sorted(set(a for a in document))


a1 = 'Todd told Tom to trot to the timber'
r1 = uniqueCharacters(a1)
print(r1)

# %%
