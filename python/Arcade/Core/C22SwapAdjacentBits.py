#
# * Core 22, Swap Adjacent Bits
# * Easy

# * You're given an arbitrary 32-bit integer n. Take its binary representation, 
# * split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) 
# * and swap bits in each pair. Then return the result as a decimal number.

# * Example

#     For n = 13, the output should be
#     swapAdjacentBits(n) = 14.

#     1310 = 11012 ~> {11}{01}2 ~> 11102 = 1410.

#     For n = 74, the output should be
#     swapAdjacentBits(n) = 133.

#     7410 = 010010102 ~> {01}{00}{10}{10}2 ~> 100001012 = 13310.
#     Note the preceding zero written in front of the initial number: since both 
#       numbers are 32-bit integers, they have 32 bits in their binary representation. 
#       The preceding zeros in other cases don't matter, so they are omitted. 
#       Here, however, it does make a difference.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     0 ≤ n < 230.

#     [output] integer

#%%

# * Solution 1
def swapAdjacentBits(n:int)-> int:
    # print(bin(n)[2:])
    nStr = bin(n)[2:]
    n = len(nStr)
    if n%2 != 0:
        nStr = '0'+nStr
        n = len(nStr)
    # print(nStr)
    result = ''
    for i in range(0, n, 2):
        # print('i', i)
        if i == 0:
            result += nStr[1::-1]
        else:
            # print(nStr[i+1:i-1:-1])
            result += nStr[i+1:i-1:-1]

    # print('result', result)

    return int(result,2)


# * Solution 2
# ! Bit Operations
def swapAdjacentBits2(n:int)-> int:
    # a = int('aaaaaaaa', 16)
    # print(a)
    # b = int('55555555', 16)
    # print(b)
    return (n<<1 & int('aaaaaaaa', 16)) | (n >>1 & int('55555555', 16))



n1 = 14
r1 = swapAdjacentBits2(n1)
print(r1)
