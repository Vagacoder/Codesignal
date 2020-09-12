#
# * Intro 04 Adjacent Elements Product
# *  Given an array of integers, find the pair of adjacent elements that has the 
# * largest product and return that product.

# * Example

#     For inputArray = [3, 6, -2, -5, 7, 3], the output should be
#     adjacentElementsProduct(inputArray) = 21.

#     7 and 3 produce the largest product.

# * Input/Output

#     [execution time limit] 3 seconds (java)

#     [input] array.integer inputArray

#     An array of integers containing at least two elements.

#     Guaranteed constraints:
#     2 ≤ inputArray.length ≤ 10,
#     -1000 ≤ inputArray[i] ≤ 1000.

#     [output] integer

#     The largest product of adjacent elements.

#%%
from typing import List

def adjacentElementsProduct(input:List[int]) -> int:
    return max( [input[i] * input[i+1] for i in range(len(input)-1) ] )


a1 = [3, 6, -2, -5, 7, 3]
r1 = adjacentElementsProduct(a1)
print('Expected: {}, result: {}'.format(21, r1))

# %%
