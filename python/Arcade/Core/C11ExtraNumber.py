#
# * Core 11, Extra Number
# * Easy

# * You're given three integers, a, b and c. It is guaranteed that two of these 
# * integers are equal to each other. What is the value of the third integer?

# * Example

# For a = 2, b = 7, and c = 2, the output should be
# extraNumber(a, b, c) = 7.

# The two equal numbers are a and c. The third number (b) equals 7, which is the answer.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer a

#     Guaranteed constraints:
#     1 ≤ a ≤ 109.

#     [input] integer b

#     Guaranteed constraints:
#     1 ≤ b ≤ 109.

#     [input] integer c

#     Guaranteed constraints:
#     1 ≤ c ≤ 109.

#     [output] integer

#%%

# * Solution 1
def extraNumber1(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c: 
        return a


# * Solution 2
# ! XOR! 
def extraNumber2(a, b, c):
    return a^b^c

a1 = 2
b1 = 7
c1 = 2
r1 = extraNumber2(a1, b1, c1)
print(r1)

a1 = 0
b1 = 1
c1 = 1
r1 = extraNumber2(a1, b1, c1)
print(r1)
