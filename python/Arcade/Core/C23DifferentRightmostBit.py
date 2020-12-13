#
# * Core 23, Different Rightmost BIt
# * Medium

# * You're given two integers, n and m. Find position of the rightmost bit in 
# * which they differ in their binary representations (it is guaranteed that 
# * such a bit exists), counting from right to left.

# * Return the value of 2position_of_the_found_bit (0-based).

# * Example

#     For n = 11 and m = 13, the output should be
#     differentRightmostBit(n, m) = 2.

#     1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position 1 (0-based) from the right in the binary representations.
#     So the answer is 21 = 2.

#     For n = 7 and m = 23, the output should be
#     differentRightmostBit(n, m) = 16.

#     710 = 1112, 2310 = 101112, i.e.

#     00111
#     10111

#     So the answer is 24 = 16.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     0 ≤ n ≤ 230.

#     [input] integer m

#     Guaranteed constraints:
#     0 ≤ m ≤ 230,
#     n ≠ m.

#     [output] integer

#%%

# * Solution 1,
def differentRightmostBit1(n, m):
    nXorM = n^m
    # print(bin(n^m))
    mask = 1
    index = 1
    while index <= len(bin(n^m)[2:]):
        # print('mask', bin(mask))
        # print('nXorM & mask', (nXorM & mask))
        if nXorM & mask != 0:
            return mask
        mask <<= 1
        index+=1
        # print('index', index)
    
    return -1
    
# * Solution 2,
# ! for the right most set bit: n & -n
def differentRightmostBit2(n, m):
    return (n^m)&-(n^m)

n1 = 11
m1 = 13
r1 = differentRightmostBit2(n1, m1)
print(r1)

n1 = 7
m1 = 23
r1 = differentRightmostBit2(n1, m1)
print(r1)

n1 = 7
m1 = 7
r1 = differentRightmostBit2(n1, m1)
print(r1)
