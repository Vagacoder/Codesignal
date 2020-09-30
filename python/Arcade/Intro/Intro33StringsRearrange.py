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

    print(graph)
    print(degrees)

    if 0 in degrees:
        return False
    
    if degrees.count(1) > 2:
        return False
    else:
        startIndex = degrees.index(1)
    
    #  TODO
    dfs(startIndex)
    



# * Helper
def isOneCharDiff(s1:str, s2:str)->bool:
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
        
    return count == 1


a1 = ["aba", "bbb", "bab"]
e1 = False
r1 = stringsRearrangement2(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

a1 = ["ab", "bb", "aa"]
e1 = True
r1 = stringsRearrangement2(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

a1 = ["abc", "abx", "axx", "abx", "abc"]
e1 = True
r1 = stringsRearrangement2(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))

# %%
