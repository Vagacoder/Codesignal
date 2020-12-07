#
# * Core 12, Is Infinite Process
# * Easy

# * Given integers a and b, determine whether the following pseudocode results 
# * in an infinite loop

# while a is not equal to b do
#   increase a by 1
#   decrease b by 1

# Assume that the program is executed on a virtual machine which can store arbitrary 
# long numbers and execute forever.

# * Example

#     For a = 2 and b = 6, the output should be
#     isInfiniteProcess(a, b) = false;
#     For a = 2 and b = 3, the output should be
#     isInfiniteProcess(a, b) = true.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer a

#     Guaranteed constraints:
#     0 ≤ a ≤ 20.

#     [input] integer b

#     Guaranteed constraints:
#     0 ≤ b ≤ 20.

#     [output] boolean

#     true if the pseudocode will never stop, false otherwise.

#%%

# * Solution 1
def isInfiniteProcess(a, b):
    if a > b:
        return True
    return (b-a)%2 != 0


a1 = 2
b1 = 6
r1 = isInfiniteProcess(a1, b1)
print(r1)

a1 = 2
b1 = 3
r1 = isInfiniteProcess(a1, b1)
print(r1)

# %%
