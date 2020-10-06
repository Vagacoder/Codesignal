#
# * Intro 44, Find Email Domain
# * Medium

# * An email address such as "John.Smith@example.com" is made up of a local part 
# * ("John.Smith"), an "@" symbol, then a domain part ("example.com").

# * The domain name part of an email address may only consist of letters, digits, 
# * hyphens and dots. The local part, however, also allows a lot of different 
# * special characters. Here you can look at several examples of correct and 
# * incorrect email addresses.

# Given a valid email address, find its domain part.

# * Example

#     For address = "prettyandsimple@example.com", the output should be
#     findEmailDomain(address) = "example.com";
#     For address = "fully-qualified-domain@codesignal.com", the output should be
#     findEmailDomain(address) = "codesignal.com".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string address

#     Guaranteed constraints:
#     10 ≤ address.length ≤ 50.

#     [output] string

#%%

# * Solution 1
import re
def findEmailDomain1(address: str)-> str:
    return re.findall('.?@([^@]+\.[^@]+)', address)[-1]


# * Solution 2
def findEmailDomain2(address: str)-> str:
    i = address.rfind('@')
    return address[i+1:]


a1 = 'fully-qualified-domain@codesignal.com'
e1 = 'codesignal.com'
r1 = findEmailDomain1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = '\" \"@space.com'
e1 = 'space.com'
r1 = findEmailDomain1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = 'example-indeed@strange-example.com'
e1 = 'strange-example.com'
r1 = findEmailDomain1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

a1 = '\"very.unusual.@.unusual.com\"@usual.com'
e1 = 'usual.com'
r1 = findEmailDomain1(a1)
print('For {}, expected: {}, result: {}'.format(a1, e1, r1))

# %%
