#
# * Core 21, Second Rightmost Zero Bit
# * Easy

# * Presented with the integer n, find the 0-based position of the second rightmost 
# * zero bit in its binary representation (it is guaranteed that such a bit exists), 
# * counting from right to left.

# Return the value of 2position_of_the_found_bit.

# * Example

# For n = 37, the output should be
# secondRightmostZeroBit(n) = 8.

# 3710 = 100101 (2). The second rightmost zero bit is at position 3 (0-based) from 
# the right in the binary representation of n. Thus, the answer is 23 = 8.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     4 ≤ n ≤ 230.

#     [output] integer

#%%

# * Solution 1
def secondRightmostZeroBit1(n):
    count = 0
    for i in range(len(bin(n))):
        if not n & 1:
            count+=1
            if count == 2:
                return 2**(i+1)

        n <<= 1

    return -1


# * Solution 2
# ! for the right most unset bit: ~n & (n+1)
def secondRightmostZeroBit2(n):
    return ~(n|(~n & (n+1))) & ((n|(~n & (n+1)))+1)


# * Solution 3
# ! Smart!
def secondRightmostZeroBit3(n):
    return (((((n + 1) | n) + 1) | n) - n)



n1 = 37
r1 = secondRightmostZeroBit3(n1)
print(r1)

# n1 = 728782938
# r1 = secondRightmostZeroBit2(n1)
# print(r1)
