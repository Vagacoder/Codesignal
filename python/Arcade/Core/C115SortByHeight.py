#
# * Core 115, Sort by Height
# * Easy

# * Some people are standing in a row in a park. There are trees between them 
# * which cannot be moved. Your task is to rearrange the people by their heights 
# * in a non-descending order without moving the trees. People can be very tall!

# * Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 1000,
#     -1 ≤ a[i] ≤ 1000.

#     [output] array.integer

#     Sorted array a with all the trees untouched.

#%%

# * Solution 1
def sortByHeight(a: list)-> list:
    p = [x for x in a if x != -1]
    p.sort()
    print(p)
    i = 0
    for j, x in enumerate(a):
        if x != -1:
            a[j] = p[i]
            i += 1
    return a
            


a1 = [-1, 150, 190, 170, -1, -1, 160, 180]
r1 = sortByHeight(a1)
print(r1)

