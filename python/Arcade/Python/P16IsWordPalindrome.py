#
# * Python 16, Is Word Palindrome
# * Easy

# * Given a word, check whether it is a palindrome or not. A string is considered 
# * to be a palindrome if it reads the same in both directions.

# * Example

#     For word = "aibohphobia", the output should be
#     isWordPalindrome(word) = true;

#     For word = "hehehehehe", the output should be
#     isWordPalindrome(word) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string word

#     A string containing lowercase English letters.

#     Guaranteed constraints:
#     1 ≤ word.length ≤ 20.

#     [output] boolean

#     true if the given word is a palindrome, false otherwise.

#%%

# * Solution 1
def isWordPalindrome(word:str)->bool:
    return word == word[::-1];


a1 = 'aibohphobia'
e1 = True
r1 = isWordPalindrome(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
