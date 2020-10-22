#
# * Python 24, Remove Tasks
# * Easy

# * Today is a good day: it's the kth year since you started to work at the 
# * company, which means you have to have a party today. In order to get home 
# * earlier and prepare for the jamboree, you need to get home early. You decided 
# * to remove each kth tasks from your toDo list, since today is your day and 
# * you can do whatever you please.

# * Given the list of task ids in your toDo list, remove each kth task from it 
# * and return the list of remaining tasks.

# * Example

# For k = 3 and toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22],
# the output should be
# removeTasks(k, toDo) = [1237, 2847, 2947, 1, 374827, 22].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] integer k

#     Guaranteed constraints:
#     1 ≤ k ≤ 30.

#     [input] array.integer toDo

#     Ids of the tasks in your to-do list.

#     Guaranteed constraints:
#     1 ≤ toDo.length ≤ 100,
#     1 ≤ toDo[i] ≤ 4 · 105.

#     [output] array.integer

#%%

# * Solution 1
# ! del list using slice
def removeTasks(k:int, toDo:list)->list:
    del toDo[k-1::k]
    return toDo



a1 = [1, 2, 3, 4, 5, 6]
a2 = 3
r1 = removeTasks(a2, a1)
print(r1)


# %%
