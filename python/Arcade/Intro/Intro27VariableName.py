#
# * Intro 27. Variable Name
# * Easy

# * Correct variable names consist only of English letters, digits and underscores 
# * and they can't start with a digit.

# Check if the given string is a correct variable name.

# Example

#     For name = "var_1__Int", the output should be
#     variableName(name) = true;
#     For name = "qq-q", the output should be
#     variableName(name) = false;
#     For name = "2w2", the output should be
#     variableName(name) = false.

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string name

#     Guaranteed constraints:
#     1 ≤ name.length ≤ 10.

#     [output] boolean

#     true if name is a correct variable name, false otherwise.

#%%

# * Solution 1
def variableName1(name:str)->bool:
    n = len(name)
    if n == 0 or name[0].isdigit():
        return False

    for c in name:
        if (not c.isalnum()) and  c != '_':
            return False

    return True


# * Solution 2
# ! Nice and short
def variableName2(name: str)->bool:
    return name.isidentifier();


# * Solution 3
# ! Regex
# ! re.match() checks only at the beginning of the string
# ! re.search() checks anywhere in the string
import re
def variableName3(name:str)->bool:
    if re.search('^[a-zA-Z_][a-zA-Z0-9_]*$', name):
        return True
    else:
        return False


a1 = 'var_1_Int3'
e1 = True
r1 = variableName3(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))


# %%
