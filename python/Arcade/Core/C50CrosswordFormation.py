#
# * Core 50, Crossword Formation
# * Medium

# * ou're a crossword fanatic, and have finally decided to try and create your 
# * own. However, you also love symmetry and good design, so you come up with a 
# * set of rules they should follow:

#     the crossword must contain exactly four words;
#     these four words should form four pairwise intersections;
#     all words must be written either left-to-right or top-to-bottom;
#     the area of the rectangle formed by empty cells inside the intersections 
#       isn't equal to zero.

# Given 4 words, find the number of ways to make a crossword following the above-
# described rules. Note that two crosswords which differ by rotation are considered 
# different.

# * Example

# For words = ["crossword", "square", "formation", "something"], the output should be
# crosswordFormation(words) = 6.

# The six crosswords can be formed as shown below:

#   f                         f                             f
#   o                     c r o s s w o r d     c r o s s w o r d
# c r o s s w o r d           r   o                   q     r
#   m   q                     m   m                   u     m
#   a   u            ;  s q u a r e          ;        a     a
#   t   a                     t   t                   r     t
#   i   r                     i   h             s o m e t h i n g
# s o m e t h i n g           o   i                         o
#   n                         n   n                         n
#                                 g                               
                                                              
#     c         s               s                                      
# f o r m a t i o n       c     q               c         s          
#     o         m         r     u               r         o      
#     s q u a r e       f o r m a t i o n       o         m            
#     s         t    ;    s     r            ;  s q u a r e                  
#     w         h         s o m e t h i n g     s         t         
#     o         i         w                     w         h     
#     r         n         o                   f o r m a t i o n            
#     d         g         r                     r         n         
#                         d                     d         g             

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string words

#     An array of distinct strings, the words you need to use in your crossword.

#     Guaranteed constraints:
#     words.length = 4,
#     3 ≤ words[i].length < 15.

#     [output] integer

#     The number of ways to make a correct crossword of the desired formation.

#%%
from itertools import permutations as permus

# * Solution 1
# ! TLE for last test
def crosswordFormation(words:list) -> int:
    count = 0
    
    # * Get permutations from words
    for perm in permus(words):
    # if True:
    #     perm = words

        # print(perm)

        n0 = len(perm[0])
        n1 = len(perm[1])
        n2 = len(perm[2])
        n3 = len(perm[3])

        # print(n0, n1, n2, n3)

        # * Frist string perm[0], 2 pointers: i0, j0
        for i0 in range(n0-2):
            for j0 in range((i0+2), n0):
                p0c0 = perm[0][i0]
                p0c1 = perm[0][j0]

                # * Second string perm[1], 2 pointers: i1, j1
                # * Third string perm[2], 2 pointers: i2, j2
                for i1 in range(n1-2):
                    for i2 in range(n2-2):
                        p1c0 = perm[1][i1]
                        p2c0 = perm[2][i2]
                        if p0c0 == p1c0 and p0c1 == p2c0:
                            for j1 in range(i1+2, n1):
                                for j2 in range(i2+2, n2):
                                    # * skip for optimize
                                    if (j1-i1) != (j2-i2):
                                        continue
                                    p1c1 = perm[1][j1]
                                    p2c1 = perm[2][j2]

                                    # * Forth string perm[3], 2 pointers: i3, j3
                                    for i3 in range(n3-2):
                                        for j3 in range(i3+2, n3):
                                            # * skip for optimize
                                            if (j0-i0)!=(j3-i3):
                                                continue
                                            p3c0 = perm[3][i3]
                                            p3c1 = perm[3][j3]
                                            # * check on indeces is not necessary, since it is skipped
                                            if (j1-i1) == (j2-i2) and (j0-i0)==(j3-i3) and p1c1 == p3c0 and p2c1 == p3c1:
                                                # print(p0c0, p0c1)
                                                # print(p1c0, p1c1)
                                                # print(p2c0, p2c1)
                                                # print(p3c0, p3c1)
                                                # print()
                                                count += 1


    return count

# * Solution 2
# ! From solution 1, do some index checking for string 2 and string 3
def crosswordFormation2(words:list) -> int:
    count = 0
    
    # * Get permutations from words
    for perm in permus(words):
    # if True:
    #     perm = words

        # print(perm)

        n0 = len(perm[0])
        n1 = len(perm[1])
        n2 = len(perm[2])
        n3 = len(perm[3])

        # print(n0, n1, n2, n3)

        # * Frist string perm[0], 2 pointers: i0, j0
        for i0 in range(n0-2):
            for j0 in range((i0+2), n0):
                p0c0 = perm[0][i0]
                p0c1 = perm[0][j0]

                # * Second string perm[1], 2 pointers: i1, j1
                # * Third string perm[2], 2 pointers: i2, j2
                for i1 in range(n1-2):
                    for i2 in range(n2-2):
                        p1c0 = perm[1][i1]
                        p2c0 = perm[2][i2]
                        if p0c0 == p1c0 and p0c1 == p2c0:
                            for j1 in range(i1+2, n1):
                                # * (i1, j1) and (i2, j2) must have same distance
                                j2 = i2 + (j1 - i1)
                                # * prevent out of bound
                                if j2 >= n2:
                                    continue
                                p1c1 = perm[1][j1]
                                p2c1 = perm[2][j2]

                                # * Forth string perm[3], 2 pointers: i3, j3
                                for i3 in range(n3-2):
                                    # * (i0, j0) and (i3, j3) must have same distance
                                    j3 = i3 + (j0-i0)
                                    # * prevent out of bound
                                    if j3 >= n3:
                                        continue
                                    p3c0 = perm[3][i3]
                                    p3c1 = perm[3][j3]
                                    # * check 
                                    if p1c1 == p3c0 and p2c1 == p3c1:
                                        # print(p0c0, p0c1)
                                        # print(p1c0, p1c1)
                                        # print(p2c0, p2c1)
                                        # print(p3c0, p3c1)
                                        # print()
                                        count += 1


    return count




# * Solution 3
def crosswordFormation3(words:list) -> int:
    count = 0
    for l in permus(words):
        for d1 in range(len(l[0])-2):
            s1 = [i for i,j in enumerate(l[1]) if j == l[0][d1]]
            for d2 in range(d1+2, len(l[0])):
                s2 = [i for i,j in enumerate(l[2]) if j == l[0][d2]]
                for cw1 in s1:
                    for cw2 in s2:
                        for c1, c2 in zip(l[1][cw1+2:],l[2][cw2+2:]):
                            for c3, c4 in zip(l[3],l[3][d2-d1:]):
                                count += c1 == c3 and c2 == c4
    return count






w1 = ["crossword", "square", "formation", "something"]
r1 = crosswordFormation2(w1)
print(r1)

# print(list(permus(w1)))
