#
# * Core 57. Is MAC48 Address?
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
import re


# * Solution 1
def isMAC48Address(inputString:str)-> bool:
    sarr = inputString.split('-')
    if len(sarr) != 6:
        return False
    for s in sarr:
        if len(s) != 2:
            return False
        if not re.match('[0-9A-F][0-9A-F]', s):
            return False
    
    return True


# * Solution 2
def isMAC48Address2(inputString:str)-> bool:    
    return True if re.match('^[0-9A-F]{2}(-[0-9A-F]{2}){5}$', inputString) else False


a1 = '00-1B-63-84-45-E6'
r1 = isMAC48Address2(a1)
print(r1)

a1 = 'Z1-1B-63-84-45-E6'
r1 = isMAC48Address2(a1)
print(r1)

a1 = 'not a MAC-48 address'
r1 = isMAC48Address2(a1)
print(r1)

a1 = '00-1B-63-84-45-E6-'
r1 = isMAC48Address2(a1)
print(r1)

# %%
