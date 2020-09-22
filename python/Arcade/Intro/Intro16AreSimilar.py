#
# * Intro 16. Are Simialr?
# * Medium

# * Two arrays are called similar if one can be obtained from another by swapping 
# * at most one pair of elements in one of the arrays.

# * Given two arrays a and b, check whether they are similar.

# * Example

#     For a = [1, 2, 3] and b = [1, 2, 3], the output should be
#     areSimilar(a, b) = true.

#     The arrays are equal, no need to swap any elements.

#     For a = [1, 2, 3] and b = [2, 1, 3], the output should be
#     areSimilar(a, b) = true.

#     We can obtain b from a by swapping 2 and 1 in b.

#     For a = [1, 2, 2] and b = [2, 1, 1], the output should be
#     areSimilar(a, b) = false.

#     Any swap of any two elements either in a or in b won't make a and b equal.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     Array of integers.

#     Guaranteed constraints:
#     3 ≤ a.length ≤ 1e5,
#     1 ≤ a[i] ≤ 1000.

#     [input] array.integer b

#     Array of integers of the same length as a.

#     Guaranteed constraints:
#     b.length = a.length,
#     1 ≤ b[i] ≤ 1000.

#     [output] boolean

#     true if a and b are similar, false otherwise.

#%%

# * Solution 1, this one is faster, no step of sort, O(n), with sort it is O(nlogn)
def areSimilar1(a:list, b:list)->bool:
    count = 0
    s1 = -1
    s2 = -1
    for i, ai in enumerate(a):
        if ai != b[i]:
            if count == 2:
                return False
            else:
                count += 1

            if s1 > -1:
                s2 = i
            else:
                s1 = i

    return a[s1] == b[s2] and a[s2] == b[s1]



# * Solution 2
# ! Python collections, and Counter, zip()
from collections import Counter as C

def areSimilar2(a:list, b:list)->bool:
    return C(a) == C(b) and sum(a != b for a, b in zip(a, b)) < 3



# * Solution 3
# ! Python sorted(iterable), zip()
def areSimilar3(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2



a1 = [1, 2, 3] 
b1 = [1, 2, 3]
e1 = True
r1 = areSimilar1(a1, b1)
print('For {} and {}, expected: {}, result: {}'.format(a1, b1, e1, r1))

a2 = [1, 2, 3] 
b2 = [2, 1, 3]
e2 = True
r2 = areSimilar1(a2, b2)
print('For {} and {}, expected: {}, result: {}'.format(a2, b2, e2, r2))

a3 = [1, 2, 2] 
b3 = [2, 1, 1]
e3 = False
r3 = areSimilar1(a3, b3)
print('For {} and {}, expected: {}, result: {}'.format(a3, b3, e3, r3))
