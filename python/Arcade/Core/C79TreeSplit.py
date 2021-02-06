#
# * Core 79, Tree Split
# * Medium

# * You have a long strip of paper with integers written on it in a single line 
# * from left to right. You wish to cut the paper into exactly three pieces such 
# * that each piece contains at least one integer and the sum of the integers in 
# * each piece is the same. You cannot cut through a number, i.e. each initial 
# * number will unambiguously belong to one of the pieces after cutting. How many 
# * ways can you do it?

# It is guaranteed that the sum of all elements in the array is divisible by 3.

# Example

# For a = [0, -1, 0, -1, 0, -1], the output should be
# threeSplit(a) = 4.

# Here are all possible ways:

#     [0, -1] [0, -1] [0, -1]
#     [0, -1] [0, -1, 0] [-1]
#     [0, -1, 0] [-1, 0] [-1]
#     [0, -1, 0] [-1] [0, -1]

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Guaranteed constraints:
#     5 ≤ a.length ≤ 104,
#     -108 ≤ a[i] ≤ 108.

#     [output] integer

#     It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

#%%

# * Solution 1
def threeSplit(a: list)->int:
    n = len(a)
    count = 0
    for i in range(1, n):
        for j in range(i+1, n):
            if sum(a[0:i]) == sum(a[(i):j]) == sum(a[j:]):
                count +=1
                print(a[0:i])
                print(a[(i):j])
                print(a[j:])
                print()

    return count


a1 = [0, -1, 0, -1, 0, -1]
r1 = threeSplit(a1)
print(r1)
