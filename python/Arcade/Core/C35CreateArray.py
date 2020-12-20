#
# * Core 35, Create Array
# * Easy

# * Given an integer size, return array of length size filled with 1s.

# * Example

# For size = 4, the output should be
# createArray(size) = [1, 1, 1, 1].

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer size

#     A positive integer.

#     Guaranteed constraints:
#     1 ≤ size ≤ 1000.

#     [output] array.integer

#%%

def createArray(size: int)-> list:
    return [1] * size


n1 = 4
r1 = createArray(n1)
print(r1)

# %%
