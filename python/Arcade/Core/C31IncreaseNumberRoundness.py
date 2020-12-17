#
# * Core 31, Increase Number Roundness
# * Easy

# * Define an integer's roundness as the number of trailing zeroes in it.

# * Given an integer n, check if it's possible to increase n's roundness by swapping 
# * some pair of its digits.

# * Example

#     For n = 902200100, the output should be
#     increaseNumberRoundness(n) = true.

#     One of the possible ways to increase roundness of n is to swap digit 1 with 
#       digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

#     For instance, one may swap the leftmost 0 with 1.

#     For n = 11000, the output should be
#     increaseNumberRoundness(n) = false.

#     Roundness of n is 3, and there is no way to increase it.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive integer.

#     Guaranteed constraints:
#     100 ≤ n ≤ 109.

#     [output] boolean

#     true if it's possible to increase n's roundness, false otherwise.

#%%
# * Solution 1
def increaseNumberRoundness(n: int) -> bool:
    return str(n).rstrip('0').count('0') > 0


# * Solution 2
def increaseNumberRoundness2(n: int) -> bool:
    return '0' in str(n).rstrip('0')


n1 = 902200100
r1 = increaseNumberRoundness2(n1)
print(r1)

n1 = 1100
r1 = increaseNumberRoundness2(n1)
print(r1)
