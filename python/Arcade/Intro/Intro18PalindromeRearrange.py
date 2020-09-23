#
# * Intro 18. Palindrome Rearranging
# * Medium

# * Given a string, find out if its characters can be rearranged to form a palindrome.

# * Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     A string consisting of lowercase English letters.

#     Guaranteed constraints:
#     1 ≤ inputString.length ≤ 50.

#     [output] boolean

#     true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.

#%%

# * Solution 1
def palindromeRearranging1(inputString: str) -> bool:
    counts = {}
    for x in inputString:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] = 1

    count = 0
    for key, val in counts.items():
        if val%2 ==1:
            count+=1

    return count < 2


# * Solution 2
# ! set(iterable)
# ! str.count()
def palindromeRearranging2(inputString: str) -> bool:
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1


s1 = 'aabb'
r1 = palindromeRearranging2(s1)
e1 = True
print('For {}, expected: {}, result: {}'.format(s1, e1, r1))

# %%
