#
# * Interview Practice, Arrays 01, First Duplicate
# * Easy

# * Given an array a that contains only numbers in the range from 1 to a.length, 
# * find the first duplicate number for which the second occurrence has the minimal 
# * index. In other words, if there are more than 1 duplicated numbers, return 
# * the number for which the second occurrence has a smaller index than the second 
# * occurrence of the other number does. If there are no such elements, return -1.

# * Example

#     For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

#     There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a 
#       smaller index than the second occurrence of 2 does, so the answer is 3.

#     For a = [2, 2], the output should be firstDuplicate(a) = 2;

#     For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

# * Input/Output

#     [execution time limit] 3 seconds (java)

#     [input] array.integer a

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 105,
#     1 ≤ a[i] ≤ a.length.

#     [output] integer

#     The element in a that occurs in the array more than once and has the minimal 
#       index for its second occurrence. If there are no such elements, return -1.

#%%

# * Solution 1
def firstDuplicate1(a: list)-> int:
    n = len(a)
    for i in range(n):
        for j in range(i):
            if a[j] == a[i]:
                return a[i]
    
    return -1


# * Solution 2
# ! trade space for speed
def firstDuplicate2(a: list)-> int:
    mySet = set()
    for i in a:
        if i in mySet:
            return i;
        else:
            mySet.add(i)
    
    return -1

a1 = [2, 1, 3, 5, 3, 2]
e1 = 3
r1 = firstDuplicate2(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))



# %%
