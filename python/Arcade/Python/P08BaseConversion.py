#
# * Python 08, Base Conversion
# * Easy

# * Your university professor decided to have a little fun and asked the class to 
# * implement a function that, given a number n and a base x, converts the number 
# * from base x to base 16. To make things more interesting, he announced that 
# * the first student to write the solution will have to answer fewer question 
# * than the rest of the class during the final exam.

# * Laughing devilishly, you asked if it was okay to use a language of your choice, 
# * and the unsuspecting professor answered "yes". It's settled then: Python is 
# * your language of choice!

# Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

# * Example

# For n = "1302" and x = 5, the output should be
# baseConversion(n, x) = "ca".

# Here's why:
# 13025 = 20210 = ca16.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string n

#     A valid non-negative integer in base x. The string is guaranteed to consist of digits and lowercase English letters.

#     Guaranteed constraints:
#     1 < n.length ≤ 10.

#     [input] integer x

#     The base of n.

#     Guaranteed constraints:
#     2 ≤ x ≤ 36.

#     [output] string

#     The value of n in base 16. The string should contain only digits and lowercase English letters 'a' - 'f'.

#%%

# * Solution 1
def baseConversion1(n:str, x:int)->str:
    sumN = 0
    for i, c in enumerate(n[::-1]):
        sumN += int(c) * x**i
    
    return hex(sumN).replace('0x', '')



# * Solution 2
def baseConversion2(n:str, x:int)->str:
    return hex(int(n, x)).replace('0x', '')



# * Solution 3
# ! Old string format 
def baseConversion3(n, x):
    return "%x" % int(n, x)



# * Solution 4
# ! New string format
def baseConversion4(n:str, x:int)->str:
    return '{:x}'.format(int(n,x))



a1 = '1302'
a2 = 5
e1 = 'ca'
r1 = baseConversion4(a1, a2)
print('For {} and {}, expected: {}, result: {}'.format(a1, a2, e1, r1))

# %%
