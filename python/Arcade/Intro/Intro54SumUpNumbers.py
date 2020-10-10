#
# * Intro 54, Sum Up Numbers
# * Medium

# * CodeMaster has just returned from shopping. He scanned the check of the items 
# * he bought and gave the resulting string to Ratiorg to figure out the total 
# * number of purchased items. Since Ratiorg is a bot he is definitely going to 
# * automate it, so he needs a program that sums up all the numbers which appear 
# * in the given input.

# Help Ratiorg by writing a function that returns the sum of numbers that appear 
# in the given inputString.

# * Example

# For inputString = "2 apples, 12 oranges", the output should be
# sumUpNumbers(inputString) = 14.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Guaranteed constraints:
#     0 ≤ inputString.length ≤ 105.

#     [output] integer


#%%

# * Solution 1
import re
def sumUpNumbers(inputString: str)-> int:
    findings = re.findall('\d+', inputString)
    print(findings)
    return sum([int(x) for x in findings])



a1 = '2 apples, 12 oranges'
e1 = 12
r1 = sumUpNumbers(a1)
print('For {}, expected: {}, result:{}'.format(a1, e1, r1))


# %%
