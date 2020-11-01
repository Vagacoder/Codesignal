#
# * Python 54, Cracking Password
# * Easy

# * You've been trying to crack the password from your friend's laptop (just to 
# * prank him, malicious intent!), but with no luck. However, looks like you're 
# * finally up to something: you checked the keyboard with the "little detective" 
# * game set and determined that the password consists of a limited set of digits.

# * You've seen your friend typing the password quite a few times, and are now 
# * sure that it consists of k digits. You also know that he is very superstitious 
# * and believes in the power of number d, so the password is apt to be divisible 
# * by it.

# * Given the digits that comprise the password, its length k and the number d by 
# * which it is divisible, return a sorted list of strings that should be tried 
# * as passwords.

# * Example

# For digits = [1, 5, 2], k = 2, and d = 3,
# the output should be
# crackingPassword(digits, k, d) = ["12", "15", "21", "51"].

# Here are all the numbers of length 2: 11, 15, 12, 51, 55, 52, 21, 25 and 22. 
# Only four of them are divisible by 3, and they comprise the answer.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer digits

#     Array of distinct digits.

#     Guaranteed constraints:
#     1 ≤ digits.length ≤ 10,
#     0 ≤ digits[i] ≤ 9.

#     [input] integer k

#     The number of digits in the password.

#     Guaranteed constraints:
#     1 ≤ k ≤ 9.

#     [input] integer d

#     The lucky number by which the password should be divisible.

#     Guaranteed constraints:
#     1 ≤ d ≤ 300.

#     [output] array.string

#     A sorted list of strings that should be tested as passwords.

#%%
from itertools import product

# ! itertools product
def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([createNumber(x) for x in list(product(digits, repeat=k)) if int(createNumber(x))%d==0])


a1 = [1, 5, 2]
a2 = 2
a3 = 3
r1 = crackingPassword(a1, a2, a3)
print(r1)


a1 = [4, 6, 0, 3]
a2 = 4
a3 = 13
r1 = crackingPassword(a1, a2, a3)
print(r1)
# %%
