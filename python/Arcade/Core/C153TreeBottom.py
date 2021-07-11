#
# * Core 153. Tree Bottom

# 

# You are given a recursive notation of a binary tree: each node of a tree is 
# represented as a set of three elements:

#     value of the node;
#     left subtree;
#     right subtree.

# So, a tree can be written as (value left_subtree right_subtree). It is guaranteed 
# that 1 ≤ value ≤ 109. If a node doesn't exist then it is represented as an empty 
# set: (). For example, here is a representation of a tree in the given picture:

# (2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))

# Your task is to obtain a list of nodes, that are the most distant from the tree 
# root, in the order from left to right.

# In the notation of a node its value and subtrees are separated by exactly one 
# space character.

# * Example

# For

# tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"

# the output should be
# treeBottom(tree) = [5, 11, 4].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string tree

#     Guaranteed constraints:
#     9 ≤ tree.length ≤ 1000.

#     [output] array.integer

#     The values of the nodes that are the most distant from the tree root.

#%%

# * Solution 1
def treeBottom(tree: str) -> list:
    result = []
    maxLevel = 0
    curLevel = 0
    n = len(tree)
    i = 0
    while i < n: 
        c = tree[i]
        if c == '(':
            curLevel += 1
            i += 1
        elif c == ')':
            curLevel -= 1
            i += 1
        elif c.isdigit():
            number = c
            i += 1
            while i < n:
                if tree[i].isdigit():
                    number += tree[i]
                    i += 1
                else:
                    break
            if curLevel == maxLevel:
                result.append(int(number))
            elif curLevel > maxLevel:
                maxLevel = curLevel
                result = [int(number)]
        else:
            i += 1

    return result



t1 = '(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))'
r1 = treeBottom(t1)
print(r1)
