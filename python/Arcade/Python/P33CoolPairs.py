#
# * Python 33, Cool Pairs
# * Easy

# * A pair of numbers is considered to be cool if their product is divisible by 
# * their sum. More formally, a pair (i, j) is cool if and only if (i * j) % (i + j) = 0.

# * Given two lists a and b, find cool pairs with the first number in the pair 
# * from a, and the second one from b. Return the number of different sums of 
# * elements in such pairs.

# * Example

# For a = [4, 5, 6, 7, 8] and b = [8, 9, 10, 11, 12],
# the output should be
# coolPairs(a, b) = 2.

# There are three cool pairs that can be formed from these arrays: (4, 12), (6, 12) and (8, 8). Their respective sums are 16, 18 and 16, which means that there are just 2 different sums: 16 and 18. Thus, the output should be equal to 2.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Array of distinct elements.

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 100,
#     1 ≤ a[i] ≤ 100.

#     [input] array.integer b

#     Array of distinct elements.

#     Guaranteed constraints:
#     1 ≤ b.length ≤ 100,
#     1 ≤ b[i] ≤ 100.

#     [output] integer

#     The number of different sums of elements in cool pairs formed by elements from a and b.

#%%

# * Solution 1
def coolPairs(a, b):
    uniqueSums = {(i+j):'' for i in a for j in b if (i*j)%(i+j) ==0 }
    print(uniqueSums)
    return len(uniqueSums)


a1 = [4, 5, 6, 7, 8]
b1 = [8, 9, 10, 11, 12]
r1 = coolPairs(a1, b1)
print(r1)


# %%
