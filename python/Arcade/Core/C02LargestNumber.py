#
# * Core 02, Largest Number
# * Easy

# * Given an integer n, return the largest number that contains exactly n digits.

# * Example

# For n = 2, the output should be
# largestNumber(n) = 99.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     1 ≤ n ≤ 9.

#     [output] integer

#     The largest integer of length n.

#%%
# * Solution 1
def largestNumber1(n):
    return int('9'*n)


# * Solution 2
def largestNumber2(n):
    return 10**n - 1


n1 = 4
r1 = largestNumber2(n1)
print(r1)
r1 == 9999
