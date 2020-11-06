#
# * Python 64, Primes Sum
# * Easy

# * It is believed by some tribes of South Codelenica that only two events determine 
# * the person's destiny: the first time he picked a flower, and the first time 
# * he planted one. They also believe in the power of prime numbers and in the 
# * power of sums (and a bunch of other most probably unrelated stuff), so you 
# * are wondering if it has something to do with their belief in the destiny-determining 
# * events.

# You know that you first picked a flower in year a of the Codelenican calendar, 
# and planted it in year b. Now you're curious about the sum of all the prime 
# numbers in the range [a, b], to see if this number could possibly affect your life.

# * Example

# For a = 10 and b = 20, the output should be
# primesSum(a, b) = 60.

# There are 4 prime numbers in the range [10, 20]: 11, 13, 17 and 19. Their sum 
# is equal to 11 + 13 + 17 + 19 = 60. It's a round number, maybe it does mean 
# something?..

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer a

#     The year in which you picked a flower for the first time.

#     Guaranteed constraints:
#     1 ≤ a ≤ b ≤ 105.

#     [input] integer b

#     The year in which you planted a flower for the first time.

#     Guaranteed constraints:
#     1 ≤ a ≤ b ≤ 105.

#     [output] integer

#     The sum of prime numbers in the range [a, b].

#%%

# * Solution 1
def primesSum(a:int, b:int)->int:
    return sum([x for x in range(max(2, a), b+1) if all([x%y for y in range(2, int(x**0.5)+1)])])

a = 10
b = 20
r1 = primesSum(a, b)
print(r1)

a = 13
b = 13
r1 = primesSum(a, b)
print(r1)

a = 1
b = 7
r1 = primesSum(a, b)
print(r1)
# %%
