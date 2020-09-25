#
# * Is IPv4 Address
# * Medium

# * An IP address is a numerical label assigned to each device (e.g., computer, 
# * printer) participating in a computer network that uses the Internet Protocol 
# * for communication. There are two versions of the Internet protocol, and thus 
# * two versions of addresses. One of them is the IPv4 address.

# * Given a string, find out if it satisfies the IPv4 address naming rules.

# * Example

#     For inputString = "172.16.254.1", the output should be
#     isIPv4Address(inputString) = true;

#     For inputString = "172.316.254.1", the output should be
#     isIPv4Address(inputString) = false.

#     316 is not in range [0, 255].

#     For inputString = ".254.255.0", the output should be
#     isIPv4Address(inputString) = false.

#     There is no first number.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string inputString

#     A string consisting of digits, full stops and lowercase English letters.

#     Guaranteed constraints:
#     1 ≤ inputString.length ≤ 30.

#     [output] boolean

#     true if inputString satisfies the IPv4 address naming rules, false otherwise.

#%%
# * Solution 1
def isIPv4Address1(inputString: str)->bool:
    tokens = inputString.split('.')

    if len(tokens) != 4:
        return False
    
    for token in tokens:
        if len(token) >1 and token.startswith('0'):
            return False
        try:
            intToken = int(token)
            if intToken < 0 or intToken > 255:
                return False
        except:
            return False

    return True


# * Solution 2
def isIPv4Address2(s):
    p = s.split('.')
    # ! str.isdigit()
    return len(p) == 4 and \
            all(n.isdigit() and 0 <= int(n) < 256 for n in p)


# * Solution 3
# ! ipaddress library
import ipaddress
def isIPv4Address3(inputString):
    try:
        ipaddress.ip_address(inputString)        
    except:
        return False
    return True


s1 = '172.16.254.1'
e1 = True
r1 = isIPv4Address1(s1)
print('For {}, expected: {}, result: {}'.format(s1, e1, r1))

s2 = '172.316.254.1'
e2 = False
r2 = isIPv4Address1(s2)
print('For {}, expected: {}, result: {}'.format(s2, e2, r2))

s3 = '01.233.161.131'
e3 = False
r3 = isIPv4Address1(s3)
print('For {}, expected: {}, result: {}'.format(s3, e3, r3))

s4 = '64.00.161.131'
e4 = False
r4 = isIPv4Address1(s4)
print('For {}, expected: {}, result: {}'.format(s4, e4, r4))

# %%
