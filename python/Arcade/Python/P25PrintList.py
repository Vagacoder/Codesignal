#
# * Python 25, Print List
# * Easy

# * You were supposed to prepare a presentation about lists in Python, but totally 
# * forgot about it. Now that you don't have enough time for it, you decide to 
# * show some usage examples instead and say with the poker face that this is how 
# * you understood the assignment.

# * Now you need to implement a function that will display a list in the console. 
# * Implement a function that, given a list lst, will return it as a string as 
# * follows: "This is your list: lst".

# * Example

# For lst = [1, 2, 3, 4, 5], the output should be
# printList(lst) = "This is your list: [1, 2, 3, 4, 5]".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer lst

#     A list containing integer values.

#     Guaranteed constraints:
#     0 ≤ lst.length ≤ 50,
#     -100 ≤ lst[i] ≤ 100.

#     [output] string

#     A string containing information about lst.

#%%
def printList(lst:list)->list:
    return 'This is your list: ' + str(lst)


a1 = [1, 2, 3, 4, 5]
r1 = printList(a1)
print(r1)

# %%
