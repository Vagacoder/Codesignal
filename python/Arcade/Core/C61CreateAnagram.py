#
# * Core 61. Create Anagram
# * Medium

# * You are given two strings s and t of the same length, consisting of uppercase 
# * English letters. Your task is to find the minimum number of "replacement 
# * operations" needed to get some anagram of the string t from the string s. A 
# * replacement operation is performed by picking exactly one character from the 
# * string s and replacing it by some other character.

# * Example

#     For s = "AABAA" and t = "BBAAA", the output should be
#     createAnagram(s, t) = 1;
#     For s = "OVGHK" and t = "RPGUC", the output should be
#     createAnagram(s, t) = 4.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string s
#     Guaranteed constraints:
#     5 ≤ s.length ≤ 35.

#     [input] string t
#     Guaranteed constraints:
#     t.length = s.length.

#     [output] integer
#     The minimum number of replacement operations needed to get an anagram of 
#       the string t from the string s.

#%%

# * Solution 1
def createAnagram(s: str, t: str)-> int:
    n = len(s)
    dic1 = {}
    dic2 = {}

    for i in range(n):
        c = s[i]
        if c in dic1:
            dic1[c] += 1
        else:
            dic1[c] = 1
        c = t[i]
        if c in dic2:
            dic2[c] += 1
        else:
            dic2[c] = 1

    # print(dic1)
    # print(dic2)

    keys = list(dic1.keys())
    for k in keys:
        if k in dic2:
            if dic1[k] > dic2[k]:
                dic1[k] -= dic2[k]
                del dic2[k]
            elif dic1[k] < dic2[k]:
                dic2[k] -= dic1[k]
                del dic1[k]
            else:
                del dic1[k]
                del dic2[k]
    
    # print(dic1)
    # print(dic2)

    count = 0
    for k in dic1:
        count+= dic1[k]
    
    return count


# * Solution 2
# ! Smart !
def createAnagram2(s: str, t: str)-> int:
    return sum(max(0, s.count(i)-t.count(i)) for i in set(s))


a1 = 'AABAA'
a2 = 'BBAAA'
r1 = createAnagram(a1, a2)
print('ex: {}, ac: {}'.format(1, r1))

a1 = 'OVGHK'
a2 = 'RPGUC'
r1 = createAnagram(a1, a2)
print('ex: {}, ac: {}'.format(4, r1))

a1 = 'KJDMDLEEKALIJB'
a2 = 'AFDJGDCGHMIGHB'
r1 = createAnagram(a1, a2)
print('ex: {}, ac: {}'.format(7, r1))
