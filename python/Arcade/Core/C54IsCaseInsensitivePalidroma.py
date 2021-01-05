#
# * Core 54, Is Case Insensitive Palindrome
# * Easy

# * Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.

# * Example

#     For inputString = "AaBaa", the output should be
#     isCaseInsensitivePalindrome(inputString) = true.

#     "aabaa" is a palindrome as well as "AABAA", "aaBaa", etc.

#     For inputString = "abac", the output should be
#     isCaseInsensitivePalindrome(inputString) = false.

#     All the strings which can be obtained via changing case of some group of letters, i.e. "abac", "Abac", "aBAc" and 13 more, are not palindromes.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Non-empty string consisting of English letters.

#     Guaranteed constraints:
#     4 ≤ inputString.length ≤ 10.

#     [output] boolean

#%%

# * Solution 1
def isCaseInsensitivePalindrome(inputString:str)-> bool:
    return inputString.lower() == inputString.lower()[::-1]

a1 = 'AaBaa'
r1 = isCaseInsensitivePalindrome(a1)
print(r1)

a1 = 'abac'
r1 = isCaseInsensitivePalindrome(a1)
print(r1)
