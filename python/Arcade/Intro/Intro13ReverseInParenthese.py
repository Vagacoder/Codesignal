#
# * Intro 13. Reverse In Parentheses
# * Medium

# * Write a function that reverses characters in (possibly nested) parentheses in the input string.

# * Input strings will always be well-formed with matching ()s.

# * Example

#     For inputString = "(bar)", the output should be
#     reverseInParentheses(inputString) = "rab";
#     For inputString = "foo(bar)baz", the output should be
#     reverseInParentheses(inputString) = "foorabbaz";
#     For inputString = "foo(bar)baz(blim)", the output should be
#     reverseInParentheses(inputString) = "foorabbazmilb";
#     For inputString = "foo(bar(baz))blim", the output should be
#     reverseInParentheses(inputString) = "foobazrabblim".
#     Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

#     Guaranteed constraints:
#     0 ≤ inputString.length ≤ 50.

#     [output] string

#     Return inputString, with all the characters that were in parentheses reversed.

#%%

def reverseInParentheses(inputString: str)->str:
    while('(' in inputString):
        # ! str.find(substr, (start, (end)))
        leftP = inputString.rfind('(')
        rightP = inputString.find(')',leftP)

        # ! reverse string by [ end : start : -1 ]
        inputString = inputString[:leftP] + inputString[rightP-1:leftP:-1] + inputString[rightP+1:]

    return inputString



s1 = '(bar)'
r1 = reverseInParentheses(s1)
print('Expect: {}, result: {}'.format('rab', r1))

s2 = 'foo(bar)baz(blim)'
r2 = reverseInParentheses(s2)
print('Expect: {}, result: {}'.format('foorabbazmilb', r2))

s3 = 'foo(bar(baz))blim'
r3 = reverseInParentheses(s3)
print('Expect: {}, result: {}'.format('foobazrabblim', r3))
