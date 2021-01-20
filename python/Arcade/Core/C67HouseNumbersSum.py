#
# * Core 67, House Numbers Sum
# * Easy

# * A boy is walking a long way from school to his home. To make the walk more 
# * fun he decides to add up all the numbers of the houses that he passes by during 
# * his walk. Unfortunately, not all of the houses have numbers written on them, 
# * and on top of that the boy is regularly taking turns to change streets, so 
# * the numbers don't appear to him in any particular order.

# At some point during the walk the boy encounters a house with number 0 written 
# on it, which surprises him so much that he stops adding numbers to his total 
# right after seeing that house.

# For the given sequence of houses determine the sum that the boy will get. It is 
# guaranteed that there will always be at least one 0 house on the path.

# * Example

# For inputArray = [5, 1, 2, 3, 0, 1, 5, 0, 2], the output should be
# houseNumbersSum(inputArray) = 11.

# The answer was obtained as 5 + 1 + 2 + 3 = 11.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     5 ≤ inputArray.length ≤ 10,
#     0 ≤ inputArray[i] ≤ 10.

#     [output] integer

#%%

# * Solution 1
def houseNumbersSum(inputArray):
    return sum(x for i,x in enumerate(inputArray) if i < inputArray.index(0))


# * Solution 2
def houseNumbersSum2(inputArray):
    return sum(inputArray[:inputArray.index(0)])


a1 = [5, 1, 2, 3, 0, 1, 5, 0, 2]
r1 = houseNumbersSum2(a1)
print(r1)
