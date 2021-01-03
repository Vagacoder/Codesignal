#
# * Core 53. Is Tandem Repeat
# * East

# * Determine whether the given string can be obtained by one concatenation of some string to itself.

# * Example

#     For inputString = "tandemtandem", the output should be
#     isTandemRepeat(inputString) = true;
#     For inputString = "qqq", the output should be
#     isTandemRepeat(inputString) = false;
#     For inputString = "2w2ww", the output should be
#     isTandemRepeat(inputString) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Guaranteed constraints:
#     2 ≤ inputString.length ≤ 20.

#     [output] boolean

#     true if inputString represents a string concatenated to itself, false otherwise.

#%%

# * Solution 1
def isTandemRepeat(inputString:str)-> bool:
    n = len(inputString)
    print(inputString[:n//2])
    print(inputString[n//2:])
    return inputString[:n//2] == inputString[n//2:]


a1 = 'tandemtandem'
r1 = isTandemRepeat(a1)
print(r1)

a1 = 'qqq'
r1 = isTandemRepeat(a1)
print(r1)