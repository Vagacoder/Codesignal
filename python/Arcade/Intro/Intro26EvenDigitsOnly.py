#
# * Intro 26. Even Digits Only
# * Easy

# * Check if all digits of the given integer are even.

# * Example

#     For n = 248622, the output should be
#     evenDigitsOnly(n) = true;
#     For n = 642386, the output should be
#     evenDigitsOnly(n) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     1 ≤ n ≤ 109.

#     [output] boolean

#     true if all digits of n are even, false otherwise.

#%%

# * Solution 1
def evenDigitsOnly1(n:int)-> bool:
    for c in str(n):
        if int(c)%2 != 0:
            return False

    return True


# * Solution 2
def evenDigitsOnly2(n:int)-> bool:
    # ! all(iterable) -> bool
    return all([int(i)%2 == 0 for i in str(n)])



a1 = 248622
e1 = True
r1 = evenDigitsOnly2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
