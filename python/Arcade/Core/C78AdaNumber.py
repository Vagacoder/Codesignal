#
# * Core 78, Ada Number
# * Medium

# * Consider two following representations of a non-negative integer:

#     A simple decimal integer, constructed of a non-empty sequence of digits 
#       from 0 to 9;
#     An integer with at least one digit in a base from 2 to 16 (inclusive), 
#       enclosed between # characters, and preceded by the base, which can only 
#       be a number between 2 and 16 in the first representation. For digits from 
#       10 to 15 characters a, b, ..., f and A, B, ..., F are used.

# Additionally, both representations may contain underscore (_) characters; they 
# are used only as separators for improving legibility of numbers and can be 
# ignored while processing a number.

# Your task is to determine whether the given string is a valid integer representation.

# Note: this is how integer numbers are represented in the programming language 
# Ada.

# * Example

#     For line = "123_456_789", the output should be
#     adaNumber(line) = true;
#     For line = "16#123abc#", the output should be
#     adaNumber(line) = true;
#     For line = "10#123abc#", the output should be
#     adaNumber(line) = false;
#     For line = "10#10#123ABC#", the output should be
#     adaNumber(line) = false;
#     For line = "10#0#", the output should be
#     adaNumber(line) = true;
#     For line = "10##", the output should be
#     adaNumber(line) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)
#     [input] string line
#     A non-empty string.
#     Guaranteed constraints:
#     2 ≤ line.length ≤ 30.
#     [output] boolean
#     true if line is a valid integer representation, false otherwise.

#%%
import re

# * Solution 1
def adaNumber(line:str)->bool:
    if '#' in line:
        if line.count('#') != 2:
            return False
        try:
            tokens = line.split('#')
            if int(tokens[0]) > 16 or int(tokens[0])<2:
                return False
            elif len(tokens[1])==0:
                return False
            else:    
                return str(int(tokens[1].replace('_', ''), base=int(tokens[0]))).isdigit()
        except:
            return False
    else:
        return line.replace('_', '').isdigit()


a1 = '123_456_789'
r1 = adaNumber(a1)
print(r1)

a1 = '16#123abc#'
r1 = adaNumber(a1)
print(r1)

