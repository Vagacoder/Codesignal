#
# * Intro 33, Strings Rearrangement
# * Medium

# * Given an array of equal-length strings, you'd like to know if it's possible 
# * to rearrange the order of the elements in such a way that each consecutive 
# * pair of strings differ by exactly one character. Return true if it's possible, 
# * and false if not.

# * Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

# * Example

#     For inputArray = ["aba", "bbb", "bab"], the output should be
#     stringsRearrangement(inputArray) = false.

#     There are 6 possible arrangements for these strings:
#         ["aba", "bbb", "bab"]
#         ["aba", "bab", "bbb"]
#         ["bbb", "aba", "bab"]
#         ["bbb", "bab", "aba"]
#         ["bab", "bbb", "aba"]
#         ["bab", "aba", "bbb"]

#     None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

#     For inputArray = ["ab", "bb", "aa"], the output should be
#     stringsRearrangement(inputArray) = true.

#     It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string inputArray

#     A non-empty array of strings of lowercase letters.

#     Guaranteed constraints:
#     2 ≤ inputArray.length ≤ 10,
#     1 ≤ inputArray[i].length ≤ 15.

#     [output] boolean

#     Return true if the strings can be reordered in such a way that each neighbouring pair of strings differ by exactly one character (false otherwise).

#%%

# * Solution 1
# ! Bug: in sorted list, such as [aa, aa, aa, ab, ab], is still good
def stringsRearrangement1(inputArray: list)->bool:
    sortedArray = sorted(inputArray)
    print(sortedArray)
    for i, s in enumerate(sortedArray):
        if i != 0 :
            s1 =sortedArray[i-1]
            if not isOneCharDiff(s, s1):
                return False

    return True


# * Solution 2
# ! Idea
# ? Turn list to undirected graph, vertex is string, edge exsits between 2 vertices
# ? if they are 1 char different. The problem is ask whether there is a Hamilton
# ? circle (connecting all vertices) in this graph?

# ! Idea from leading board
# ! Check if this graph has Hamiltonian path
# ! based on theorem (1): A simple graph with n vertices (n >= 3) is Hamiltonian if every vertex has degree n / 2 or greater
# ! and theorem (2): A graph is Hamiltonian if and only if its closure is Hamiltonian

def stringsRearrangement2(inputArray: list)->bool:
    v = len(inputArray)
    degrees = [0]*v
    graph =[]

    for i in range(v):
        graph.append([])

    for i in range(v):
        for j in range(v):
            if i != j and isOneCharDiff(inputArray[i], inputArray[j]):
                graph[i].append(j)
                degrees[i]+=1

    # print(graph)
    # print(degrees)

    # ! My trial on Hamilton start ==================================
    # if 0 in degrees:
    #     return False
    
    # if degrees.count(1) > 2:
    #     return False
    # elif 0 < degrees.count(1) <=2:
    #     startIndex = degrees.index(1)

    #     #  TODO
    #     visited = [False]*v
    #     count = [0]
    #     dfs(startIndex, graph, visited, count)
    #     return count[0] == v
    # else:
    #     visited = [False]*v
    #     count = [0]
    #     dfs(0, graph, visited, count)
    #     return count[0] == v

    # ! My trial on Hamilton end ====================================



    
# * Helper for my
def dfs(v: int, graph:list, visited:list, count: list):
    visited[v] =True
    count[0] +=1
    for w in graph[v]:
        if not visited[w]:
            dfs(w, graph, visited, count)




# * Solution 3
# ! Brute force
# ? Generate all permutations and found correct one
def stringsRearrangement3(inputArray: list)->bool:
    allPermuList = getPermutation(inputArray)
    for p in allPermuList:
        if isGoodP(p):
            return True

    return False


# * Helper
# ! Permutation of list of string
def getPermutation(l: list)->list:
    if len(l) <= 1:
        return [l]

    permutation = []
    
    for i, string in enumerate(l):

        shortList = l[:i] + l[(i+1):]

        for p in getPermutation(shortList):
            tempList = [string]
            
            for stringInP in p:
                tempList.append(stringInP)

            permutation.append(tempList)
        
    return permutation

# * tester for permutation
# print(getPermutation(["aa", "bb"]))
# print(getPermutation(["aba", "bbb", "bab"]))


def isGoodP(p:list)->bool:
    n = len(p)
    for i in range(n-1):
        if not isOneCharDiff(p[i], p[i+1]):
            return False
    
    return True


def isOneCharDiff(s1:str, s2:str)->bool:
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    return count == 1


# * Solution 4
# ! Using permutatins library
from itertools import permutations

# ! zip()
def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1


# ! zip() again
def stringsRearrangement4(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False




a1 = ["aba", "bbb", "bab"]
e1 = False
r1 = stringsRearrangement3(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

a1 = ["ab", "bb", "aa"]
e1 = True
r1 = stringsRearrangement3(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

a1 = ["abc", "abx", "axx", "abx", "abc"]
e1 = True
r1 = stringsRearrangement3(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

# %%
