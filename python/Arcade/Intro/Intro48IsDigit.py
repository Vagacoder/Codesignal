#
# * Intro 48, Is Digit
# * Easy

# * Determine if the given character is a digit or not.

# * Example

#     For symbol = '0', the output should be
#     isDigit(symbol) = true;
#     For symbol = '-', the output should be
#     isDigit(symbol) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] char symbol

#     A character which is either a digit or not.

#     Guaranteed constraints:
#     Given symbol is from ASCII table.

#     [output] boolean

#     true if symbol is a digit, false otherwise.

#%%

# * Solution 1
def isDigit(symbol: str)->bool:
    return symbol.isdigit()


a1 = '-'
e1 = False
r1 = isDigit(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
