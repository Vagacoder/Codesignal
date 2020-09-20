#
# * Intro 12 Sort by Height
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

#     If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] 
#     is the height of a person standing in the ith position.

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 1000,
#     -1 ≤ a[i] ≤ 1000.

#     [output] array.integer

#     Sorted array a with all the trees untouched.


#%%

# * Solution 1
def sortByHeight(a):
    n = len(a)
    # ! filter() and map()
    temp = list(filter(lambda x : x >-1, a))
    temp.sort()

    i = 0
    j = 0
    while i < n:
        if a[i] == -1:
            i +=1
            continue
        else:
            a[i] = temp[j]
            i+=1
            j+=1

    return a


# * Solution 2
def sortByHeight2(a):
    temp = list(filter(lambda x : x > -1, a))
    temp.sort()

    # ! use enumerate(), no need use len()
    for i, h in enumerate(a):
        if h == -1:
            # ! insert into list
            temp.insert(i, -1)

    return temp


a1 = [-1, 150, 190, 170, -1, -1, 160, 180]
r1 = sortByHeight2(a1)
print(r1)

# %%
