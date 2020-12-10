#
# * Core 20, Mirror Bits
# * Easy

# * Reverse the order of the bits in a given integer.

# * Example

#     For a = 97, the output should be
#     mirrorBits(a) = 67.

#     97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

#     For a = 8, the output should be
#     mirrorBits(a) = 1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer a

#     Guaranteed constraints:
#     5 ≤ a ≤ 105.

#     [output] integer

#%%

# * Solution 1
def mirrorBits(a:int)-> int:
    return int(bin(a)[-1:1:-1], 2)


# * Solution 2
# ! Bit Operation!
def mirrorBits2(a:int)-> int:
    result = 0
    while a:
        result = result << 1 | a & 1
        a >>= 1
    
    return result


a1 = 97
r1 = mirrorBits2(a1)
print(r1)
