#
# * Core 118. Maximum Sum
# * You are given an array of integers a. A range sum query is defined by a pair 
# * of non-negative integers l and r (l <= r). The output to a range sum query on 
# * the given array a is the sum of all the elements of a that have indices from 
# * l to r, inclusive.

# You have the array a and a list of range sum queries q. Find an algorithm that 
# can rearrange the array a in such a way that the total sum of all of the query 
# outputs is maximized, and return this total sum.

# * Example

# For a = [9, 7, 2, 4, 4] and q = [[1, 3], [1, 4], [0, 2]], the output should be
# maximumSum(a, q) = 62.

# You can get this sum if the array a is rearranged to be [2, 9, 7, 4, 4]. In that 
# case, the first range sum query [1, 3] returns the sum 9 + 7 + 4 = 20, the 
# second query [1, 4] returns the sum 9 + 7 + 4 + 4 = 24, and the third query 
# [0, 2] returns the sum 2 + 9 + 7 = 18. The total sum will be 20 + 24 + 18 = 62.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer a

#     An initial array.

#     Guaranteed constraints:
#     2 ≤ a.length ≤ 10,
#     1 ≤ a[i] ≤ 10.

#     [input] array.array.integer q

#     An array of range sum queries, where each query is an array of two non-negative integers.

#     Guaranteed constraints:
#     1 ≤ q.length ≤ 10,
#     0 ≤ q[i][0] ≤ q[i][1] < a.length.

#     [output] integer

#     Return the maximum possible total sum of the given range sum query outputs.

#%%

# * Solution 1
# ! TLE
import itertools

def maximumSum(a:list, q:list)-> int:
    perA = itertools.permutations(a)
    results = []
    for pA in perA:
        # print(pA)
        sums = 0
        for r in q:
            # print(sums)
            sums += sum(pA[r[0]:r[1]+1])
        results.append(sums)
        # print(results)
    return max(results)


# * Solution 2
# ! compare to #3 , this one does more work to find best arrangement
def maximumSum2(a:list, q:list)-> int:
    n = len(a)
    sortedA = sorted(a)
    # print(sortedA)
    
    counts = [0]*n
    for r in q:
        for i in range(r[0], r[1]+1):
            counts[i] += 1
    # print(counts)

    countsWithIndex = [(x, i) for i, x in enumerate(counts)]
    # print(countsWithIndex)
    countsWithIndex.sort(key=lambda x: x[0])
    # print(countsWithIndex)
    
    bestArrange = [0] * n
    for i in range(n):
        bestArrange[countsWithIndex[i][1]] = sortedA[i]
    
    result = 0
    for r in q:
        result += sum(bestArrange[r[0]:r[1]+1])
    return result


# * Solution 3
# ! Compare to #2, this one does directly calculate the sum
def maximumSum3(A, Q):
    c = [0]*len(A)
    for l, r in Q:
        for i in range(l, r+1):
            c[i] += 1
    return sum(a*b for a, b in zip(sorted(A), sorted(c)))


a1 = [9, 7, 2, 4, 4]
q1 = [[1, 3], [1, 4], [0, 2]]
r1 = maximumSum2(a1, q1)
print(r1)
