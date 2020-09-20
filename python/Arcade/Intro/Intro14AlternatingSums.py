#
# * Intro 14. Alternating Sums
# * Easy

# * Several people are standing in a row and need to be divided into two teams. 
# * The first person goes into team 1, the second goes into team 2, the third goes 
# * into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. 
# Return an array of two integers, where the first element is the total weight 
# of team 1, and the second element is the total weight of team 2 after the 
# division is complete.

# * Example

# For a = [50, 60, 60, 45, 70], the output should be
# alternatingSums(a) = [180, 105].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 105,
#     45 ≤ a[i] ≤ 100.

#     [output] array.integer

#%%

# * Solution 1
def alternatingSum(a: list) -> list:
    w1 = sum(a[::2])
    w2 = sum(a[1::2])
    return [w1, w2]


# * Solution 2
def alternatingSum1(a: list) -> list:
    result = [0,0]
    for i, x in enumerate(a):
        result[i%2] += x
    
    return result


a1 = [50, 60, 60, 45, 70]
r1 = alternatingSum1(a1)
print('For {}, expected: {}, result: {}'.format(a1,  [180, 105], r1))

#%%