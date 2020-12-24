#
# * Core 43, Is Power
# * Easy

# * Determine if the given number is a power of some non-negative integer.

# * Example

#     For n = 125, the output should be
#     isPower(n) = true;
#     For n = 72, the output should be
#     isPower(n) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ n ≤ 400.

#     [output] boolean

#     true if n can be represented in the form ab (a to the power of b) where a 
#       and b are some non-negative integers and b ≥ 2, false otherwise.

#%%
import math

def isPower(n: int)-> bool:
    for a in range(21):
        for b in range(2, 10):
            if a**b == n:
                return True
            elif a**b > n:
                continue
        
    return False


n1 = 125
r1 = isPower(n1)
print(r1)

n1 = 72
r1 = isPower(n1)
print(r1)

n1 = 11
r1 = isPower(n1)
print(r1)

# %%
