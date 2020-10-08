#
# * Intro 47, Is MAC48 Address
# * Medium

# * A media access control address (MAC address) is a unique identifier assigned 
# * to network interfaces for communications on the physical network segment.

# * The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly 
# * form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by 
# * hyphens (e.g. 01-23-45-67-89-AB).

# * Your task is to check by given string inputString whether it corresponds to 
# * MAC-48 address or not.

# * Example

#     For inputString = "00-1B-63-84-45-E6", the output should be
#     isMAC48Address(inputString) = true;
#     For inputString = "Z1-1B-63-84-45-E6", the output should be
#     isMAC48Address(inputString) = false;
#     For inputString = "not a MAC-48 address", the output should be
#     isMAC48Address(inputString) = false.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     Guaranteed constraints:
#     15 ≤ inputString.length ≤ 20.

#     [output] boolean

#     true if inputString corresponds to MAC-48 address naming rules, false otherwise.

#%%

# * Solution 1
def isMAC48Address1(inputString:str)-> bool:
    tokens = inputString.split('-')

    if len(tokens) != 6:
        return False

    for t in tokens:
        if len(t) != 2:
            return False
        else:
            try:
                hexN = int(t, 16)
                if hexN >255 or hexN < 0:
                    return False
            except:
                return False

    return True


# * Solution 2
import re
def isMAC48Address2(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))


a1 = "00-1B-63-84-45-E6"
e1 = True
r1 = isMAC48Address1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = "Z1-1B-63-84-45-E6"
e1 = False
r1 = isMAC48Address1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = "not a MAC-48 address"
e1 = False
r1 = isMAC48Address1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
