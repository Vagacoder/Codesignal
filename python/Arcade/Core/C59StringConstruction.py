#
# * Core 59. String Construction
# * Medium

# * Given two strings a and b, both consisting only of lowercase English letters, 
# * your task is to calculate how many strings equal to a can be constructed using 
# * only letters from the string b? Each letter can be used only once and in one 
# * string only.

# * Example

#     For a = "abc" and b = "abccba", the output should be stringsConstruction(a, b) = 2.
#     We can construct 2 strings a = "abc" using only letters from the string b.
#     For a = "ab" and b = "abcbcb", the output should be stringsConstruction(a, b) = 1.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string a

#     String to construct, containing only lowercase English letters.

#     Guaranteed constraints:
#     1 ≤ a.length ≤ 105.

#     [input] string b

#     String containing needed letters, containing only lowercase English letters.

#     Guaranteed constraints:
#     1 ≤ b.length ≤ 105.

#     [output] integer

#     The number of strings a that can be constructed from the string b.

#%%

# * Solution 1
def stringsConstruction(a: str, b: str) -> int :
    dict1 = {}
    dict2 = {}

    for c in a:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1
    
    for c in b:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1
    
    # print(dict1)
    # print(dict2)

    result = float('INF')
    for k in dict1:
        if k in dict2:
            count = dict2[k]//dict1[k]
            result = min(result, count)
        else:
            return 0
    
    return result


# * Solution 2
def stringsConstruction(a: str, b: str) -> int:
    return min(b.count(c)//a.count(c) for c in a)


a1 = 'abc'
b1 = 'abccba'
r1 = stringsConstruction(a1, b1)
print(r1)

a1 = 'ab'
b1 = 'abcbcb'
r1 = stringsConstruction(a1, b1)
print(r1)

a1 = 'z'
b1 = 'y'
r1 = stringsConstruction(a1, b1)
print(r1)

a1 = 'za'
b1 = 'bzc'
r1 = stringsConstruction(a1, b1)
print(r1)