#
# * Intro 51, Delete Digit
# * Medium

# * Given some integer, find the maximal number you can obtain by deleting exactly 
# * one digit of the given number.

# * Example

#     For n = 152, the output should be
#     deleteDigit(n) = 52;
#     For n = 1001, the output should be
#     deleteDigit(n) = 101.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     10 ≤ n ≤ 106.

#     [output] integer


#%%

# * Solution 1
def deleteDigit(n:int) -> int:
    nStr = str(n)

    # all = []
    # for i in range(len(nStr)):
    #     all.append(int(nStr[:i] + nStr[i+1:]))
    
    # return max(all)

    return max([int(nStr[:i] + nStr[i+1:]) for i in range(len(nStr))])

a1 = 152
e1 = 52
r1 = deleteDigit(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
