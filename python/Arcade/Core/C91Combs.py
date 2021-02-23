#
# * Core 91 Combs
# * Medium

# * Miss X has only two combs in her possession, both of which are old and miss 
# * a tooth or two. She also has many purses of different length, in which she 
# * carries the combs. The only way they fit is horizontally and without overlapping. 
# * Given teeth' positions on both combs, find the minimum length of the purse 
# * she needs to take them with her.

# It is guaranteed that there is at least one tooth at each end of the comb.
# It is also guaranteed that the total length of two strings is smaller than 32.
# Note, that the combs can not be rotated/reversed.

# * Example

# For comb1 = "*..*" and comb2 = "*.*", the output should be
# combs(comb1, comb2) = 5.

# Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string comb1

#     A comb is represented as a string. If there is an asterisk ('*') in the ith position, there is a tooth there. Otherwise there is a dot ('.'), which means there is a missing tooth on the comb.

#     Guaranteed constraints:
#     3 ≤ comb1.length ≤ 8.

#     [input] string comb2

#     The second comb is represented in the same way as the first one.

#     Guaranteed constraints:
#     1 ≤ comb2.length ≤ 5.

#     [output] integer

#     The minimum length of a purse Miss X needs.

#%%

# * Solution 1
def combs(comb1:list, comb2:list)-> int:
    n1 = len(comb1)
    n2 = len(comb2)
    
    r1 = float('inf')
    i = 0
    while i < n1:
        j = 0
        while j < n2 and i+j < n1:
            if comb1[i+j] == '*' and comb2[j] == '*':
                break
            j += 1
        if j == n2 or i+j == n1:
            r1 = max(i+n2, n1)
            break
        i += 1

    r1 = min(r1, n1+n2)

    # print('r1',r1)

    r2 = float('inf')
    i = 0
    while i < n2:
        j = 0
        while j < n1 and i+j < n2:
            if comb2[i+j] == '*' and comb1[j] == '*':
                break
            j += 1
        if j == n1 or i+j == n2:
            r2 = max(i+n1, n2)
            break
        i += 1

    r2 = min(r2, n1+n2)

    # print('r2',r2)

    return min(r1, r2)

a1 = '*..*.*'
a2 = '*.***'
r1 = combs(a1, a2)
print(r1)

a1 = '*.**'
a2 = '*.*'
r1 = combs(a1, a2)
print(r1)

a1 = '*...*'
a2 = '*.*'
r1 = combs(a1, a2)
print(r1)