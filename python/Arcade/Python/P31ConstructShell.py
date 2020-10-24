#
# * Python 31, Construct Shell
# * Easy

# * A 2D list lst of size 2 * n - 1 is called a shell if it is filled with zeros 
# * and has the following configuration:

#     lst[0] contains one element;
#     lst[1] contains two elements;
#     ...
#     lst[n - 2] contains n - 1 elements;
#     lst[n - 1] contains n elements;
#     lst[n] contains n - 1 elements;
#     ...
#     lst[2 * n - 3] contains two elements;
#     lst[2 * n - 2] contains one element.

# * Given an integer n, return a shell list.

# * Example

# For n = 3, the output should be

# constructShell(n) = [[0],
#                      [0, 0],
#                      [0, 0, 0],
#                      [0, 0],
#                      [0]]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer n

#     An integer defining the size of the shell.

#     Guaranteed constraints:
#     1 ≤ n ≤ 30.

#     [output] array.array.integer

#     A shell.

#%%

# * Solution 1
def constructShell1(n:int)-> list:
    return [[0]*(i+1) for i in range(n)]+[[0] * i for i in range(n-1, 0, -1)]


# * Solution 2
# ! Smart
def constructShell2(n):
    return [[0]*min(i,2*n-i) for i in range(1,2*n)]


a1 = 3
r1 = constructShell2(a1)
print(r1)


# %%
