#
# * Core 80, Character Parity
# * Easy

# * Given a character, check if it represents an odd digit, an even digit or not 
# * a digit at all.

# * Example

#     For symbol = '5', the output should be
#     characterParity(symbol) = "odd";
#     For symbol = '8', the output should be
#     characterParity(symbol) = "even";
#     For symbol = 'q', the output should be
#     characterParity(symbol) = "not a digit".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] char symbol

#     A symbol to check.

#     Guaranteed constraints:
#     symbol is guaranteed to be a UTF-8 symbol.

#     [output] string

#%%
# * Solution 1
def characterParity(symbol:str) -> str:
    return 'not a digit' if not symbol.isdigit() else 'even' if int(symbol)%2 == 0 else 'odd'


a1 = '5'
r1 = characterParity(a1)
print(r1)

a1 = '8'
r1 = characterParity(a1)
print(r1)

a1 = 'q'
r1 = characterParity(a1)
print(r1)