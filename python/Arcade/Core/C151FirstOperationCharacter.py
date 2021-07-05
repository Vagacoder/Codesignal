#
# * Core 151. First Operation Character

# Given a string which represents a valid arithmetic expression, find the index 
# of the character in the given expression corresponding to the arithmetic operation 
# which needs to be computed first.

# Note that several operations of the same type with equal priority are computed 
# from left to right.

# See the explanation of the third example for more details about the operations 
# priority in this problem.

# * Example

#     For expr = "(2 + 2) * 2", the output should be
#     firstOperationCharacter(expr) = 3.

#     There are two operations in the expression: + and *. The result of + should 
#       be computed first, since it is enclosed in parentheses. Thus, the output 
#       is the index of the '+' sign, which is 3.

#     For expr = "2 + 2 * 2", the output should be
#     firstOperationCharacter(expr) = 6.

#     There are two operations in the given expression: + and *. Since there are 
#       no parentheses, * should be computed first as it has higher priority. The 
#       answer is the position of '*', which is 6.

#     For expr = "((2 + 2) * 2) * 3 + (2 + (2 * 2))", the output should be first-
#       OperationCharacter(expr) = 28.

#     There are two operations which are enclosed in two parentheses: + at the 
#       position 4, and * at the position 28. Since * has higher priority than +, 
#       the answer is 28.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string expr

#     A string consisting of digits, parentheses, addition and multiplication 
#       signs (pluses and asterisks). It is guaranteed that there is at least one 
#       arithmetic sign in it.

#     Guaranteed constraints:
#     5 ≤ expr.length ≤ 45.

#     [output] integer


#%%

# * Solution 1
def firstOperationCharacter(expr: str)-> int:
    if '(' not in expr:
        if '*' in expr:
            return expr.index('*')
        else:
            return expr.index('+')
    stack = []
    parenthesis = []
    for i, c in enumerate(expr):
        if c == '(':
            stack.append(i)
        elif c== ')':
            parenthesis.append((stack.pop(), i, len(stack)+1))
    # print(stack)
    # print(parenthesis)

    highestNestedOrder = 0
    highestParen = []
    for i, p in enumerate(parenthesis):
        if p[2] > highestNestedOrder:
            highestNestedOrder = p[2]
            highestParen = [p]
        elif p[2] == highestNestedOrder:
            highestParen.append(p)
    # print(highestNestedOrder)
    # print(highestParen)

    hasMultiple = [False]*len(highestParen)
    for i, p in enumerate(highestParen):
        if '*' in expr[p[0]:p[1]]:
            hasMultiple[i] = True
    # print(hasMultiple)

    for i, h in enumerate(hasMultiple):
        if h:
            p = highestParen[i]
            # print(p)
            return expr.index('*', p[0], p[1])
    
    p = highestParen[0]
    return expr.index('+', p[0], p[1])


# * Solution 2
# ! Awesome !
def firstOperationCharacter2(expr):
    # * m is max parentheis level
    m=b=0
    for x in expr:
        b += x == '('
        b -= x == ')'
        m = max(m,b)
    print(m,b)

    # ! check * first, then check +
    for p in '*+':
        for i,x in enumerate(expr):
            b += x == '('
            b -= x == ')'
            if b == m and x == p: return i



e1 = '((2 + 2) * 2) * 3 + (2 + (2 * 2))'
r1 = firstOperationCharacter2(e1)
print(r1)

# e1 = '4 * 3 + 2'
# r1 = firstOperationCharacter2(e1)
# print(r1)
