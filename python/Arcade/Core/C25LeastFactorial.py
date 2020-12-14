#
# * Core 25, Least Factorial
# * Easy

# * Given an integer n, find the minimal k such that

#     k = m! (where m! = 1 * 2 * ... * m) for some integer m;
#     k >= n.

# In other words, find the smallest factorial which is not less than n.

# * Example

# For n = 17, the output should be
# leastFactorial(n) = 24.

# 17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ n ≤ 120.

#     [output] integer

#%%

# * Solution 1
def leastFactorial(n: int)-> int:
    result = 1
    i = 2
    while result < n:
        result = result * i
        i+=1
    
    return result


n1 = 17
r1 = leastFactorial(n1)
print(r1)

n1 = 1
r1 = leastFactorial(n1)
print(r1)

n1 = 109
r1 = leastFactorial(n1)
print(r1)
