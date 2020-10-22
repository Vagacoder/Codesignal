#
# * Python 21, Lists Concatenation
# * Easy

# * Given two lists lst1 and lst2, your task is to return a list formed by the 
# * elements of lst1 followed by the elements of lst2.

# * Note: this is a bugfix task, which means that the function is already implemented 
# * but there is a bug in one of its lines. Your task is to find and fix it.

# * Example

# For lst1 = [2, 2, 1] and lst2 = [10, 11], the output should be
# listsConcatenation(lst1, lst2) = [2, 2, 1, 10, 11].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer lst1

#     Guaranteed constraints:
#     0 ≤ lst1.length ≤ 20,
#     -106 ≤ lst1[i] ≤ 106.

#     [input] array.integer lst2

#     Guaranteed constraints:
#     0 ≤ lst2.length ≤ 20,
#     -106 ≤ lst2[i] ≤ 106.

#     [output] array.integer

#%%
# * Solution 1
def listsConcatenation1(lst1:list, lst2:list)->list:
    res = lst1
    res+=lst2
    return res


# * Solution 2
def listsConcatenation2(lst1:list, lst2:list)-> list:
    res = lst1
    res.extend(lst2)
    return res



a1 = [1,2,3]
a2 = [3,4,5]
r1 = listsConcatenation2(a1, a2)
print(r1)

# %%
