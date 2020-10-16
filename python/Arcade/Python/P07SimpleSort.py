#
# * Python 07, Simple Sort

# * To understand how efficient the built-in Python sorting function is, you 
# * decided to implement your own simple sorting algorithm and compare its speed 
# * to the speed of the Python sorting. Write a function that, given an array of 
# * integers arr, sorts its elements in ascending order.

# * Hint: with Python it's possible to swap several elements in a single line. 
# * To solve the task, use this knowledge to fill in both of the blanks (...).

# * Example

# For arr = [2, 4, 1, 5], the output should be
# simpleSort(arr) = [1, 2, 4, 5].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer arr

#     Guaranteed constraints:
#     1 ≤ arr.length ≤ 500,
#     -105 ≤ arr[i] ≤ 105.

#     [output] array.integer

#     The given array with elements sorted in ascending order.

#%%
# * Solution 1
def simpleSort(arr):

    n = len(arr)
    
    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

a1 = [2, 3, 1, 5, 4]
simpleSort(a1)
print(a1)

# %%
