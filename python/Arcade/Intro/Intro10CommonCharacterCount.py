#
#  * Intro 10. Common Character Count
#  * 
#  * Given two strings, find the number of common characters between them.

#  * Example
 
#  For s1 = "aabcc" and s2 = "adcaa", the output should be
#  commonCharacterCount(s1, s2) = 3.
 
# Strings have 3 common characters - 2 "a"s and 1 "c".

# * Input/Output

# [execution time limit] 3 seconds (java)

# [input] string s1

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 1 ≤ s1.length < 15.

# [input] string s2

#     A string consisting of lowercase English letters.
    
#     Guaranteed constraints:
#     1 ≤ s2.length < 15.
    
#     [output] integer

#%%

# * Solution 1
def commonCharacterCount(s1:list, s2:list)-> int:
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))


# * Solution 2
def commonCharacterCount1(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)
    
s1 = 'aabcc'
s2 = 'adcaa'

print(commonCharacterCount(s1, s2))
print(commonCharacterCount1(s1, s2))
