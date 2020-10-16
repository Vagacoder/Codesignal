#
# * Python 05, Count Bits
# * Easy

# * Implement the missing code, denoted by ellipses. You may not modify the pre-
# * existing code.

# * Implement a function that, given an integer n, uses a specific method on it 
# * and returns the number of bits in its binary representation.

# * Note: in this task and most of the following tasks you will be given a code 
# * snippet with some part of it replaced by the ellipsis (...). Only this part 
# * is allowed to be changed.

# * Example

# For n = 50, the output should be
# countBits(n) = 6.

# 5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ n ≤ 109.

#     [output] integer

#     The number of bits in binary representation of n.

#%%
# * Solution 1
def countBits1(n:int) -> int:
    return  len(bin(n).replace('0b', ''))
    

# * Solution 2
def countBits2(n:int) -> int:
    return n.bit_length()




a1 = 50
e1 = 6
r1 = countBits2(50)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
