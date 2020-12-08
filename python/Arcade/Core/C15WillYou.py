#
# * Core 15, Will You?
# * Easy

# * Once Mary heard a famous song, and a line from it stuck in her head. That 
# * line was "Will you still love me when I'm no longer young and beautiful?". 
# * Mary believes that a person is loved if and only if he/she is both young and 
# * beautiful, but this is quite a depressing thought, so she wants to put her 
# * belief to the test.

# Knowing whether a person is young, beautiful and loved, find out if they 
# contradict Mary's belief.

# A person contradicts Mary's belief if one of the following statements is true:

#     they are young and beautiful but not loved;
#     they are loved but not young or not beautiful.

# * Example

#     For young = true, beautiful = true, and loved = true, the output should be
#     willYou(young, beautiful, loved) = false.

#     Young and beautiful people are loved according to Mary's belief.

#     For young = true, beautiful = false, and loved = true, the output should be
#     willYou(young, beautiful, loved) = true.

#     Mary doesn't believe that not beautiful people can be loved.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] boolean young

#     [input] boolean beautiful

#     [input] boolean loved

#     [output] boolean

#     true if the person contradicts Mary's belief, false otherwise.

#%%

# * Solution 1
def willYou1(young, beautiful, loved):
    return (young and beautiful and not loved) or (loved and (not young or not beautiful))


# * Solution 2
def willYou2(young, beautiful, loved):
    return loved != (young and beautiful)


y1 = True
b1 = True
l1 = True
r1 = willYou2(y1, b1, l1)
print(r1)

# %%
