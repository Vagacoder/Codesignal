#
# * Core 88, Array Conversion
# * Medium

# * Given an array of 2k integers (for some integer k), perform the following 
# * operations until the array contains only one element:

#     On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of 
#       consecutive elements with their sum;
#     On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive 
#       elements with their product.

# After the algorithm has finished, there will be a single element left in the 
# array. Return that element.

# * Example

# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be
# arrayConversion(inputArray) = 186.

# We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so 
# the answer is 186.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer inputArray

#     Guaranteed constraints:
#     1 ≤ inputArray.length ≤ 27,
#     -100 ≤ inputArray[i] ≤ 100.

#     [output] integer

#%%

# * Solution 1
def arrayConversion(inputArray: list) -> int:
    result = inputArray.copy()
    while len(result) > 1:
        temp = []
        i = 0
        while i < len(result):
            temp.append(result[i] + result[i+1])
            i += 2
        result = temp
        if len(result) <= 1:
            break
        temp = []
        i = 0
        while i < len(result):
            temp.append(result[i] * result[i+1])
            i += 2
        result = temp
    
    return result[0]


a1 = [1, 2, 3, 4, 5, 6, 7, 8]
r1 = arrayConversion(a1)
print(r1)

# %%
