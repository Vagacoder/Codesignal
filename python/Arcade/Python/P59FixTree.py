#
# * Python 59, Fix Tree
# * Easy

# * Not long ago a young Christmas elf asked you to implement a function that 
# * creates Christmas trees made of asterisks ('*') similar to the one below:

#     *    
#     *    
#    ***   
#   *****  
#  ******* 
# *********
#    ***   

# Unfortunately because of the extreme coldness the tree that you sent over was 
# corrupted: although its lines are given in the correct order, but are not aligned 
# properly. Now your task is to fix the given tree by centering the asterisks in 
# each line.

# * Example

# For

# tree = [
#   "      *  ", 
#   "    *    ", 
#   "***      ", 
#   "    *****", 
#   "  *******", 
#   "*********", 
#   " ***     "
# ]

# the output should be

# fixTree(tree) = [
#   "    *    ", 
#   "    *    ", 
#   "   ***   ", 
#   "  *****  ", 
#   " ******* ", 
#   "*********", 
#   "   ***   "
# ]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string tree

#     A list representing a tree, where all strings have the same odd length and 
#       have the format "< ><*>< >", where < > denotes some (possibly none) 
#       whitespace characters, and <*> denotes an odd number of asterisk.

#     Guaranteed constraints:
#     1 ≤ tree.length ≤ 31,
#     1 ≤ tree[0].length ≤ 21.

#     [output] array.string

#     A fixed tree, with asterisks centered in each line.

#%% 

# * Solution 1
def fixTree1(tree:list)->list:
    return [' '*((len(line)-len(line.strip()))//2) + line.strip() + ' '*((len(line)-len(line.strip()))//2) for line in tree]


# * Solution 2
def fixTree2(tree:list)->list:
    return [line.strip().center(len(line)) for line in tree]



a1 = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
r1 = fixTree1(a1)
print(r1)

# %%
