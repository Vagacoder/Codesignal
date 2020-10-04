#
# * Intro 41, Digit Degree
# * Medium

# * Let's define digit degree of some positive integer as the number of times we 
# * need to replace this number with the sum of its digits until we get to a one 
# * digit number.

# * Given an integer, find its digit degree.

# * Example

#     For n = 5, the output should be
#     digitDegree(n) = 0;
#     For n = 100, the output should be
#     digitDegree(n) = 1.
#     1 + 0 + 0 = 1.
#     For n = 91, the output should be
#     digitDegree(n) = 2.
#     9 + 1 = 10 -> 1 + 0 = 1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     Guaranteed constraints:
#     5 ≤ n ≤ 109.

#     [output] integer


#%%

# * Solution 1
def digitDegree1(n: int)-> int:
    count = 0
    while n > 9:
        strN = str(n)
        newN = 0
        for c in strN:
            newN += int(c)
        n = newN
        count +=1

    return count


# * Solution 2
# ! Recursive
def digitDegree2(n):
    if n < 10:
        return 0
    
    sumOfDigits = sum([int(i) for i in str(n)])
    
    return digitDegree2(sumOfDigits) + 1



a1 = 5
e1 = 0
r1 = digitDegree2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = 100
e1 = 1
r1 = digitDegree2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = 91
e1 = 2
r1 = digitDegree2(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
