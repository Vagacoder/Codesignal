#
# * Core 18, Array Packing
# * Medium

# * You are given an array of up to four non-negative integers, each less than 256.

# * Your task is to pack these integers into one number M in the following way:

#     The first element of the array occupies the first 8 bits of M;
#     The second element occupies next 8 bits, and so on.

# Return the obtained integer M.

# Note: the phrase "first bits of M" refers to the least significant bits of M - 
# the right-most bits of an integer. For further clarification see the following example.

# * Example

# For a = [24, 85, 0], the output should be
# arrayPacking(a) = 21784.

# An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
# After packing these into one number we get 00000000 01010101 00011000 (spaces 
#   are placed for convenience), which equals to 21784.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 4,
#     0 ≤ a[i] < 256.

#     [output] integer

#%%

# * Solution 1, Bit Operations
def arrayPacking(a:list)-> int:
    result = 0
    for i, val in enumerate(a):
        # print(i)
        # print(bin(val))
        # print(val<<(i*8))
        # print(bin(val<<(i*8)))
        # print()
        result += (val<<(i*8))

    return result


a1 = [24, 85, 0]
r1 = arrayPacking(a1)
print(r1)


# %%
