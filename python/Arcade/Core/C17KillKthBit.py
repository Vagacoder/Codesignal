#
# * Core 17 Kill K-th Bit
# ! Hard

# * In order to stop the Mad Coder evil genius you need to decipher the encrypted 
# * message he sent to his minions. The message contains several numbers that, 
# * when typed into a supercomputer, will launch a missile into the sky blocking 
# * out the sun, and making all the people on Earth grumpy and sad.

# * You figured out that some numbers have a modified single digit in their 
# * binary representation. More specifically, in the given number n the kth bit 
# * from the right was initially set to 0, but its current value might be different. 
# * It's now up to you to write a function that will change the kth bit of n back to 0.

# * Example

#     For n = 37 and k = 3, the output should be
#     killKthBit(n, k) = 33.

#     3710 = 1001012 ~> 1000012 = 3310.

#     For n = 37 and k = 4, the output should be
#     killKthBit(n, k) = 37.

#     The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this 
#       number), so the answer is still 37.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     0 ≤ n ≤ 231 - 1.

#     [input] integer k

#     The 1-based index of the changed bit (counting from the right).

#     Guaranteed constraints:
#     1 ≤ k ≤ 31.

#     [output] integer

#%%

# * Solution 1
def killKthBit1(n:int, k:int)->int:
    # print(bin(n))
    # print(str(bin(n)))
    # print(str(bin(n))[-k])

    return n if n < 2**(k-1) or str(bin(n))[-k] == '0' else (n - 2**(k-1))


# * Solution 2, Bit operations
def killKthBit2(n:int, k:int)->int:
    return n&~(2**(k-1))


n1 = 37 
k1 = 4
r1 = killKthBit2(n1, k1)
print(r1)

n1 = 37 
k1 = 3
r1 = killKthBit2(n1, k1)
print(r1)
