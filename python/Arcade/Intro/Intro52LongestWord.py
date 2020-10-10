# 
# * Intro 52, Longest Word
# * Easy

# * Define a word as a sequence of consecutive English letters. Find the longest 
# * word from the given string.

# * Example

# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string text

#     Guaranteed constraints:
#     4 ≤ text.length ≤ 50.

#     [output] string

#     The longest word from text. It's guaranteed that there is a unique output.

#%%

# ! 2 errors
# * Solution 1
import re

def longestWord1(text:str)->str:
    tokens = text.split(" ")

    maxL = -1
    maxS = tokens[0]

    for i in range(len(tokens)):
        tokens[i]= re.sub('[^A-Za-z]+','', tokens[i])
        if len(tokens[i]) > maxL:
            maxL = len(tokens[i])
            maxS = tokens[i]
    
    return maxS
    

# * Solution 2
import re

def longestWord2(text:str) -> str:
    tokens = re.split('[^A-Za-z]+', text)

    maxL = -1
    maxS = tokens[0]

    for i, t in enumerate(tokens):
        if len(t) > maxL:
            maxL = len(t)
            maxS = t
    
    return maxS


# * Solution 3
# ! max(iterable, *iterable, key, default)
def longestWord3 (text:str) -> str:
    return max(re.split('[^a-zA-Z]', text), key=len)



a1 = 'You are the best!!!!!!!!!!!! CodeFighter ever!'
e1 = 'CodeFighter'
r1 = longestWord2(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

# %%
