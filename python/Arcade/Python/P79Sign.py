#
# * Python 79, Sign
# * Easy

# * Although Python does provide a bunch of useful built-in functions, some of 
# * them are simply missing for no apparent reason. One example of such function 
# * is a sign function implemented in many other languages. sign(x) returns 1 if 
# * x is positive, -1 if x is negative, and 0 if x is equal to zero.

# You decided to build your own package of useful functions, and would like to 
# start with the sign function. Given the value of x, return the result of applying 
# the sign function to it.

# * Example

# For x = -34, the output should be
# sign(x) = -1.

# -34 is a negative number, thus the output should be -1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer x

#     The argument of the sign function.

#     Guaranteed constraints:
#     -50 ≤ x ≤ 50.

#     [output] integer

#     The value of sign(x).

#%%

class Functions(object):

    # * Solution 1
    # ! Static Method of Python Class
    @staticmethod
    def sign1(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    
    # * Solution 2
    # ! Class Method of Python Class
    @classmethod
    def sign2(cls, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0



def sign1(x):
    return Functions.sign1(x)


def sign2(x):
    return Functions.sign2(x)


x = -34
r1 = sign1(x)
print(r1)

r1 = sign2(x)
print(r1)

# %%
