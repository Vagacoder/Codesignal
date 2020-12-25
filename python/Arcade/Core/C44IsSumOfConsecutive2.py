#
# * Core 44, Is Sum of Consecutive 2
# * Medium

# * Find the number of ways to express n as sum of some (at least two) consecutive 
# * positive integers.

# * Example

#     For n = 9, the output should be
#     isSumOfConsecutive2(n) = 2.

#     There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

#     For n = 8, the output should be
#     isSumOfConsecutive2(n) = 0.

#     There are no ways to represent n = 8.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ n ≤ 104.

#     [output] integer

#%%
# * Solution 1
def isSumOfConsecutive2(n:int)-> int:
    count = 0

    for i in range(1, n):
        tempSum = i
        j = i+1
        while j < n:
            tempSum += j
            if tempSum == n:
                count += 1
                break
            elif tempSum > n:
                break
            j += 1

    return count


n1 =  9
r1 = isSumOfConsecutive2(n1)
print(r1)

n1 =  99
r1 = isSumOfConsecutive2(n1)
print(r1)

n1 =  8
r1 = isSumOfConsecutive2(n1)
print(r1)

