#
# * Core 30, Apple Boxes
# * Easy

# * You have k apple boxes full of apples. Each square box of size m contains m 
# * × m apples. You just noticed two interesting properties about the boxes:

# *   The smallest box is size 1, the next one is size 2,..., all the way up to size k.
# *   Boxes that have an odd size contain only yellow apples. Boxes that have an 
#       even size contain only red apples.

# Your task is to calculate the difference between the number of red apples and 
# the number of yellow apples.

# * Example

# For k = 5, the output should be
# appleBoxes(k) = -15.

# There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, 
# making the answer 20 - 35 = -15.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer k

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ k ≤ 40.

#     [output] integer

#     The difference between the two types of apples.

#%%

# * Solution 1
def appleBoxes(k:int)->int:
    red = 0
    yellow = 0
    for i in range(1, k+1):
        if i%2== 0:
            red += i*i
        else:
            yellow += i*i
    
    return red - yellow


# * Solution 2
def appleBoxes2(k:int)->int:
    return sum(i*i if i%2==0 else -i*i for i in range(1, k+1))


# * Solution 3
def appleBoxes3(n):
    return ((-1)**n)*n*(n+1)/2



k1 = 5
r1 = appleBoxes2(k1)
print(r1)

# %%
