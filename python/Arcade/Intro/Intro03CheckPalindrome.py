#
#  * Intro 03, Check Palindrome
#  * Given the string, check if it is a palindrome.

#  * Example

#     For inputString = "aabaa", the output should be
#     checkPalindrome(inputString) = true;
#     For inputString = "abac", the output should be
#     checkPalindrome(inputString) = false;
#     For inputString = "a", the output should be
#     checkPalindrome(inputString) = true.

#  * Input/Output

#     [execution time limit] 3 seconds (java)

#     [input] string inputString

#     A non-empty string consisting of lowercase characters.

#     Guaranteed constraints:
#     1 ≤ inputString.length ≤ 105.

#     [output] boolean

#     true if inputString is a palindrome, false otherwise.

#%%
def checkPalindrome1(inputString:str)->bool:
    return inputString == inputString[::-1]


strs = ["aabaa", "abac", "a", "az", "abacaba", "z", "aaabaaaa", 
                                "zzzazzazz", "hlbeeykoqqqqokyeeblh", "hlbeeykoqqqokyeeblh"]
expected = [True, False, True, False, True, True, False, False, True, True]

for i, s in enumerate(strs):
    result = checkPalindrome1(s)
    if result == expected[i]:
        print('Test {} is passed\n'.format(i))
    else:
        print('Test {} is failed, expected: {}, result: {}\n'.format(i, expected[i], result))


# %%
