#
# * Python 63, Fibonacci List
# * Easy

# * No time to explain! The World Government made contact with intelligent alien 
# * life, and needs you to send a message to the outer space. The aliens only 
# * receive messages that are stored in a sequence of lists of sizes 0, 1, 1, 2, 
# * 3, 5, ..., in other words those whose length increase according to the Fibonacci 
# * sequence.

# The Government is too busy composing the message, and needs you to prepare the 
# list in which the message should be sent. Given an integer n, return a list of 
# n lists, where the first element consists is empty (consists of 0 zeros), the 
# second element consists of 1 zero, and so on.

# * Example

# For n = 6, the output should be

# fibonacciList(n) = [[], 
#                     [0], 
#                     [0], 
#                     [0, 0], 
#                     [0, 0, 0], 
#                     [0, 0, 0, 0, 0]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     The size of the list you should return.

#     Guaranteed constraints:
#     2 ≤ n ≤ 20.

#     [output] array.array.integer

#     A 2-dimensional list of zeros, where the list sizes form the Fibonacci sequence.

#%%

# * Solution 1
# ! Smart !
import functools

def fibonacciList(n:int)->list:
    return [[0] * x for x in functools.reduce(lambda a, b:a+[a[-1]+a[-2]], range(n-2), [0, 1])]
    # return functools.reduce(lambda a, b:a+[a[-1]+a[-2]], range(n), [0, 1])

a1 = 5
r1 = fibonacciList(a1)
print(r1)

# %%
