#
# * Core 47. Comfortabel Numbers
# * Easy

# * Let's say that number a feels comfortable with number b if a ≠ b and b lies 
# * in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

# * How many pairs (a, b) are there, such that a < b, both a and b lie on the 
# * segment [l, r], and each number feels comfortable with the other (so a feels 
# * comfortable with b and b feels comfortable with a)?

# * Example

# For l = 10 and r = 12, the output should be
# comfortableNumbers(l, r) = 2.

# Here are all values of s(x) to consider:

#     s(10) = 1, so 10 is comfortable with 9 and 11;
#     s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
#     s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.

# Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer l

#     Guaranteed constraints:
#     1 ≤ l ≤ r ≤ 1000.

#     [input] integer r

#     Guaranteed constraints:
#     1 ≤ l ≤ r ≤ 1000.

#     [output] integer

#     The number of pairs satisfying all the above conditions.


#%%

def comfortableNumbers(l:int, r:int)->int:
    
    def s(n:int)->int:
        result = 0
        while n > 0:
            result += n%10
            n //= 10
        
        return result

    # return s(219)

    def isComfortable(a:int, b:int)->bool:
        aRange = s(a)
        return b in range(a-aRange, a+aRange+1)

    # return isComfortable(10, 11)

    count = 0
    for i in range(l, r):
        for j in range(i+1, r+1):
            if isComfortable(i, j) and isComfortable(j, i):
                count+=1
                # print(i, j)
    
    return count


l1 = 10
r1 = 12
re1 = comfortableNumbers(l1, r1)
print(re1)

l1 = 1
r1 = 9
re1 = comfortableNumbers(l1, r1)
print(re1)


l1 = 239
r1 = 777
re1 = comfortableNumbers(l1, r1)
print(re1)
# %%
