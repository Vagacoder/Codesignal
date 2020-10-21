#
# * Python 19, New Style Formatting
# * Easy

# * You came to work in a big company as a Senior Python Developer. Unfortunately 
# * your team members seem to be quite old-school: you can see old-style string 
# * formatting everywhere in the code, which is not too cool. You tried to force 
# * the team members to start using the new style formatting, but it looks like 
# * it will take some time to persuade them: old habits die hard, especially in 
# * old-school programmers.

# * To show your colleagues that the new style formatting is not that different 
# * from the old style, you decided to implement a function that will turn the 
# * old-style syntax into a new one. Implement a function that will turn the old
# * -style string formating s into a new one so that the following two strings 
# * have the same meaning:

#     s % (*args)
#     s.format(*args)

# * Example

# For s = "We expect the %f%% growth this week", the output should be
# newStyleFormatting(s) = "We expect the {}% growth this week".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     A correct old-style formatting string. It is guaranteed that each % sign 
#       in it is always followed either by a correct conversion type or by another 
#       '%' sign (see this for reference). It is also guaranteed that it doesn't 
#       contain curly brackets ('{' or '}').

#     Guaranteed constraints:
#     1 ≤ s.length ≤ 70.

#     [output] string

#     A new-style formatting string without positional indices.

#%%

# * Solution 1
import re

def newStyleFormatting1(s:str)-> str:
    tokens = s.split('%%')
    for i, token in enumerate(tokens):
        tokens[i] = re.sub('%[^%]', '{}', token)

    return '%'.join(tokens)



a1 = 'We expect the %f%% growth this week'
e1 = 'We expect the {}% growth this week'
r1 = newStyleFormatting1(a1)
print('Expected:', a1)
print('Result:', r1)

# %%
