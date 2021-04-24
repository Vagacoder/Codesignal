#
# * Core 114, Shuffled Array
# * Easy

# * A noob programmer was given two simple tasks: sum and sort the elements of 
# * the given array
# a = [a1, a2, ..., an]. He started with summing and did it easily, but decided 
# to store the sum he found in some random position of the original array which 
# was a bad idea. Now he needs to cope with the second task, sorting the original 
# array a, and it's giving him trouble since he modified it.

# Given the array shuffled, consisting of elements a1, a2, ..., an, a1 + a2 + ... 
# + an in random order, return the sorted array of original elements a1, a2, ..., an.

# Example

#     For shuffled = [1, 12, 3, 6, 2], the output should be
#     shuffledArray(shuffled) = [1, 2, 3, 6].

#     1 + 3 + 6 + 2 = 12, which means that 1, 3, 6 and 2 are original elements of 
#       the array.

#     For shuffled = [1, -3, -5, 7, 2], the output should be
#     shuffledArray(shuffled) = [-5, -3, 2, 7].

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer shuffled

#     Array of at least two integers. It is guaranteed that there is an index i 
#       such that shuffled[i] = shuffled[0] + ... + shuffled[i - 1] + shuffled[i + 1]
#        + ... + shuffled[n].

#     Guaranteed constraints:
#     2 ≤ shuffled.length ≤ 104,
#     -5 · 104 ≤ shuffled[i] ≤ 5 · 104.

#     [output] array.integer

#     A sorted array of shuffled.length - 1 elements.

#%%
# * Solution 1
def shuffledArray(shuffled: list)-> list:
    result = sorted(shuffled)
    # print(result)
    sumOfResult = sum(result)
    # print(sumOfResult)
    for i in range(len(result)):
        # print(i, result[i])
        if result[i] == sumOfResult - result[i]:
            return result[:i] + result[i+1:]
    

# * Solution 2
def shuffledArray2(shuffled: list)-> list:
    shuffled.remove(sum(shuffled) // 2)
    return sorted(shuffled)


a1 = [1, 12, 3, 6, 2]
r1 = shuffledArray(a1)
print(r1)

a1 = [1, -3, -5, 7, 2]
r1 = shuffledArray(a1)
print(r1)

