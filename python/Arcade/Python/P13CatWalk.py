#
# * Python 13, Cat Walk
# * Easy

# * You've been working on a particularly difficult algorithm all day, and finally 
# * decided to take a break and drink some coffee. To your horror, when you returned 
# * you found out that your cat decided to take a walk on the keyboard in your 
# * absence, and pressed a key or two. Your computer doesn't react to letters 
# * being pressed when an unauthorized action appears, but allows typing whitespace 
# * characters and moving the arrow keys, so now your masterpiece contains way 
# * too many whitespace characters.

# * To repair the damage, you need to start with implementing a function that will 
# * replace all multiple space characters in the given line of your code with 
# * single ones. In addition, all leading and trailing whitespaces should be removed.

# * Example

# For

# line = "def      m   e  gaDifficu     ltFun        ction(x):"

# the output should be
# catWalk(line) = "def m e gaDifficu ltFun ction(x):".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string line

#     One line from your code containing way too many whitespace characters.

#     Guaranteed constraints:
#     5 ≤ line.length ≤ 125.

#     [output] string

#     line with unnecessary whitespace characters removed.

#%%

# * SOlution 1
# ! string.split(), default separator is ANY whitespace
def catWalk(code: str)-> str:
    return ' '.join(code.split())


a1 = 'def      m   e  gaDifficu     ltFun        ction(x):'
e1 = 'def m e gaDifficu ltFun ction(x):'
r1 = catWalk(a1)
print('Expected:')
print(e1)
print('Result:')
print(r1)

# %%
