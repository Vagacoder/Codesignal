#
# * Python 12, Fix Message
# * Easy

# * One of your friends has an awful writing style: he almost never starts a message 
# * with a capital letter, but adds uppercase letters in random places throughout 
# * the message. It makes chatting with him very difficult for you, so you decided 
# * to write a plugin that will change each message received from your friend into 
# * a more readable form.

# * Implement a function that will change the very first symbol of the given message 
# * to uppercase, and make all the other letters lowercase.

# * Example

# For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1",
# the output should be
# fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string message

#     A string consisting of English letters, whitespace characters, digits and punctuation marks.

#     Guaranteed constraints:
#     1 ≤ message.length ≤ 65.

#     [output] string

#     Fixed message with its first letter capitalized, and all other letters converted to lowercase.

#%%
# * Solution 1
def fixMessage(message):
    return message.capitalize()


a1 = "you'll NEVER believe what that 'FrIeNd' of mine did!!1"
e1 = "You'll never believe what that 'friend' of mine did!!1"
r1 = fixMessage(a1)
print('For {}, \nexpected: {}, \nresult:{}'.format(a1, e1, r1))


# %%
