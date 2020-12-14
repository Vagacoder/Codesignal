#
# * Core 26 Count Sum of Two Representations 2
# * Easy

# * Given integers n, l and r, find the number of ways to represent n as a sum of 
# * two integers A and B such that l ≤ A ≤ B ≤ r.

# * Example

# For n = 6, l = 2, and r = 4, the output should be
# countSumOfTwoRepresentations2(n, l, r) = 2.

# There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive integer.

#     Guaranteed constraints:
#     5 ≤ n ≤ 109.

#     [input] integer l

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ l ≤ r.

#     [input] integer r

#     A positive integer.

#     Guaranteed constraints:
#     l ≤ r ≤ 109,
#     r - l ≤ 106.

#     [output] integer

#%%

# * Solution 1, Two pointers
def countSumOfTwoRepresentations2(n, l, r):
    result = 0
    low = l
    high = r
    while low <= high:
        curSum = low + high
        if curSum == n:
            result+=1
            low += 1
            high -= 1
        elif curSum > n:
            high -= 1
        elif curSum < n:
            low += 1
    return result


# * Solution 2, 
def countSumOfTwoRepresentations3(n, l, r):
    return sum(1 for x in range(l, r+1) if l <= x <= n-x <= r)


# * Solution 3, Mathmetics
def countSumOfTwoRepresentations4(n, l, r):
    import math
    return max(min((n//2)-l, r-math.ceil(n/2))+1, 0)


n1 = 6
l1 = 2
r1 = 4
re1 = countSumOfTwoRepresentations4(n1, l1, r1)
print(re1)

n1 = 24
l1 = 12
r1 = 12
re1 = countSumOfTwoRepresentations4(n1, l1, r1)
print(re1)
